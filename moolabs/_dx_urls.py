"""URL derivation + F2 ingest fallback chain.

Three responsibilities:

1. ``resolve_effective_base_url(base_url, api_key)`` — init-time rewrite of
   the customer-supplied ``base_url`` into the effective env-rooted host
   the rest of the SDK uses. Apex (``moolabs.com``) gets an env prefix
   injected from the key; explicit env roots (``dev.moolabs.com``) and
   self-hosted bases pass through unchanged. Pure function, no state.
   **Called exactly once at SDK construction** — see Moolabs.__init__.

2. ``derive_host(backend, base_url)`` — convention-based subdomain rewriting
   used for every non-ingest capability call. Pure function, no state.

3. ``IngestUrlResolver`` — stateful F2 fallback chain for the event-ingest
   hot path (contracts §3.5). Resolves the URL to POST events to via a 4-step
   chain, tracking discovery failures and recently-failed cached URLs.

The resolver is intentionally HTTP-agnostic — discovery is performed via a
caller-supplied callback (``discovery_fn``) so this module has no dependency
on the generated ``ApiClient``. The DX layer's ``_dx_client`` wires the
callback to an actual HTTP call.

Thread-safe: all state mutations are guarded by an internal lock. Multiple
ingest calls from different threads on the same ``Moolabs`` instance share
the same resolver and won't race the cache.
"""

from __future__ import annotations

import os
import threading
import time
from dataclasses import dataclass
from typing import Callable, Optional
from urllib.parse import urlparse

from ._dx_routing import (
    DEFAULT_REGION,
    REGION_INGEST_MAP,
    SUBDOMAIN_MAP,
)


# Path appended to ``meter.{base_url}`` for the F2 step-4 last-resort fallback
# (the always-derivable non-regional event endpoint). Used when discovery has
# failed AND the region-map fallback URL is unreachable / unknown.
_METER_INGEST_PATH = "/api/v1/events"

# Path on the BFF for SDK auto-discovery of the regional ingest URL.
_DISCOVERY_PATH = "/v1/tenant/config"


def normalize_base_url(base_url: str) -> str:
    """Strip scheme/path from a caller-provided base_url and return the bare host.

    The customer constructor accepts a root domain (``"moolabs.com"``) or a
    URL form (``"https://moolabs.com"``); both must work. The SDK prepends
    ``https://{subdomain}.`` so we need just the host part.

    >>> normalize_base_url("moolabs.com")
    'moolabs.com'
    >>> normalize_base_url("https://moolabs.com/")
    'moolabs.com'
    >>> normalize_base_url("https://moolabs.com")
    'moolabs.com'

    Empty or syntactically invalid input raises ``ValueError`` — caught at
    construction time so the customer sees the failure immediately.
    """
    if not base_url or not isinstance(base_url, str):
        raise ValueError(f"base_url must be a non-empty string, got {base_url!r}")
    stripped = base_url.strip().rstrip("/")
    if not stripped:
        raise ValueError(f"base_url is empty after stripping, got {base_url!r}")
    # Parse as URL — if no scheme, urlparse puts the whole thing in `path`.
    parsed = urlparse(stripped if "://" in stripped else f"https://{stripped}")
    host = parsed.hostname
    if not host:
        raise ValueError(f"base_url has no parseable host: {base_url!r}")
    return host


# ── Effective base_url resolution (init-time only) ────────────────────────
#
# Customer-facing apex domains where the SDK injects an env prefix derived
# from the API key. Bare apex like ``moolabs.com`` is a marketing/branding
# host, not an env root — the ALB cert is ``*.prod.moolabs.com`` (no SAN
# for ``*.moolabs.com``), so the SDK must compose subdomains under an env
# root like ``prod.moolabs.com``.
#
# Add new entries here when Moolabs adds new customer-facing apex TLDs
# (e.g. ``moolabs.io``). Self-hosted customers passing their own root
# (``tenant.example.com``) match no entry and pass through unchanged.
_INJECT_ENV_APEXES: frozenset[str] = frozenset({"moolabs.com"})

# Env prefixes the SDK recognizes in the API key. Customer keys minted
# by the future region-aware issuer have the form ``{env}-{region}-{rand}``,
# e.g. ``prod-us-d0b7403...``. Legacy raw-hex keys have no prefix and
# fall back to ``prod`` (rule 3 in resolve_effective_base_url).
_KNOWN_ENV_TOKENS: frozenset[str] = frozenset({"prod", "dev", "staging"})

# Fallback env root used for legacy unprefixed keys when ``base_url`` is
# an apex. Today this is the only deployed env root with a valid wildcard
# ALB cert; multi-region rollout adds ``prod-us``, ``prod-eu``, etc.
_LEGACY_KEY_FALLBACK_ENV: str = "prod"


def extract_env_prefix(api_key: str) -> Optional[str]:
    """Extract the ``{env}-{region}`` prefix from a region-aware API key.

    The future key format is ``{env}-{region}-{random}`` where ``env`` is
    one of ``prod`` / ``dev`` / ``staging`` and ``region`` is a short
    code like ``us``, ``eu``, ``au``. Legacy raw-hex keys returned None.

    >>> extract_env_prefix("prod-us-d0b740abc")
    'prod-us'
    >>> extract_env_prefix("dev-eu-xyz")
    'dev-eu'
    >>> extract_env_prefix("staging-au-1234")
    'staging-au'
    >>> extract_env_prefix("d0b7403c508b360ca637") is None
    True
    >>> extract_env_prefix("just-two-tokens-but-bad-env") is None
    True
    >>> extract_env_prefix("") is None
    True
    """
    if not api_key or not isinstance(api_key, str):
        return None
    parts = api_key.split("-", 2)
    if len(parts) < 3:
        return None
    env, region, _rest = parts
    if env not in _KNOWN_ENV_TOKENS or not region:
        return None
    return f"{env}-{region}"


def resolve_effective_base_url(base_url: str, api_key: str) -> str:
    """Resolve the effective base_url used for SDK subdomain composition.

    Called exactly ONCE at ``Moolabs.__init__`` — never per-call. The
    result becomes ``self._base_url`` for the rest of the instance's
    lifetime; ``derive_host`` and ``IngestUrlResolver`` all consume the
    already-resolved value.

    Three rules:

    1. ``base_url`` is NOT a known customer-facing apex (e.g.
       ``dev.moolabs.com``, ``prod.moolabs.com``, ``tenant.example.com``):
       use as-is. The customer has already chosen their env root or is
       self-hosted; injecting anything would be wrong.

    2. ``base_url`` IS an apex AND the API key has an env-region prefix
       (``prod-us-xxx``): inject the prefix → ``prod-us.moolabs.com``.
       This is the multi-region future; today no keys have this format
       so rule 2 is dormant pending issuer rollout.

    3. ``base_url`` IS an apex AND the key is legacy (no prefix): fall
       back to ``prod.{apex}``. Today's only working env root.

    >>> resolve_effective_base_url("dev.moolabs.com", "anything")
    'dev.moolabs.com'
    >>> resolve_effective_base_url("prod.moolabs.com", "d0b7403c")
    'prod.moolabs.com'
    >>> resolve_effective_base_url("tenant.example.com", "anything")
    'tenant.example.com'
    >>> resolve_effective_base_url("moolabs.com", "prod-us-d0b740")
    'prod-us.moolabs.com'
    >>> resolve_effective_base_url("moolabs.com", "dev-eu-xyz")
    'dev-eu.moolabs.com'
    >>> resolve_effective_base_url("moolabs.com", "d0b7403c")
    'prod.moolabs.com'
    >>> resolve_effective_base_url("https://moolabs.com/", "d0b7403c")
    'prod.moolabs.com'
    """
    normalized = normalize_base_url(base_url)
    if normalized not in _INJECT_ENV_APEXES:
        return normalized
    env_prefix = extract_env_prefix(api_key) or _LEGACY_KEY_FALLBACK_ENV
    return f"{env_prefix}.{normalized}"


def derive_host(backend: str, base_url: str) -> str:
    """Return the full ``https://{subdomain}.{base_url}`` for a backend.

    >>> derive_host("bff", "moolabs.com")
    'https://api.moolabs.com'
    >>> derive_host("meter", "moolabs.com")
    'https://meter.moolabs.com'
    >>> derive_host("arc", "tenant.example.com")
    'https://arc.tenant.example.com'

    Raises ``ValueError`` if ``backend`` is not in ``SUBDOMAIN_MAP``.
    """
    if backend not in SUBDOMAIN_MAP:
        raise ValueError(
            f"unknown backend {backend!r}; known: {sorted(SUBDOMAIN_MAP)}"
        )
    subdomain = SUBDOMAIN_MAP[backend]
    return f"https://{subdomain}.{normalize_base_url(base_url)}"


def _host_matches_base_url(url: str, base_url: str) -> bool:
    """True iff `url`'s hostname is `base_url` itself or a subdomain of it.

    Used by the F2 chain's discovery step as defense-in-depth: a compromised
    BFF could otherwise return an attacker-controlled host in
    ``endpoints.ingest`` and the SDK would happily POST customer events +
    the customer's API key to it. By rejecting any host outside the
    customer's configured ``base_url``, we keep the blast radius of a BFF
    compromise contained to BFF's own domain.

    >>> _host_matches_base_url("https://meter.moolabs.com/api/v1/events", "moolabs.com")
    True
    >>> _host_matches_base_url("https://moolabs.com/x", "moolabs.com")
    True
    >>> _host_matches_base_url("https://attacker.com/x", "moolabs.com")
    False
    >>> _host_matches_base_url("https://moolabs.com.attacker.com/x", "moolabs.com")
    False
    """
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    base = base_url.lower().lstrip(".")
    if not host or not base:
        return False
    # Exact match OR proper subdomain (host ends with ".base"). The leading
    # "." in the suffix check rejects "moolabs.com.attacker.com" — without
    # the dot, endswith("moolabs.com") would erroneously accept it.
    return host == base or host.endswith("." + base)


# ── F2 ingest fallback chain ──────────────────────────────────────────────


@dataclass
class IngestResolverConfig:
    """Tunables for ``IngestUrlResolver``.

    All defaults are the illustrative values pinned by contracts §3.5 / O6;
    the implementer should sanity-check against typical Moolabs incident
    recovery times before shipping production defaults.
    """

    # Bounded TTL on a failed ``/tenant/config`` discovery attempt. Within
    # this window the SDK skips re-trying discovery and goes straight to
    # the region-map fallback.
    discovery_retry_ttl_sec: float = 60.0

    # How many consecutive POST failures to a cached ingest URL before the
    # SDK invalidates the cache.
    post_failure_threshold: int = 3

    # How long the SDK remembers a URL as "recently failed". A subsequent
    # discovery that returns the same URL is skipped during this window;
    # the SDK falls through to the next chain step.
    recently_failed_ttl_sec: float = 300.0  # 5 minutes


class IngestUrlResolver:
    """F2 fallback chain resolver — pure URL-routing logic, thread-safe.

    Usage:
        resolver = IngestUrlResolver(
            base_url="moolabs.com",
            discovery_fn=lambda: _http_get_tenant_config(api_key, base_url),
        )

        url = resolver.get_ingest_url()
        try:
            _http_post_events(url, events)
            resolver.report_post_outcome(url, success=True)
        except (TimeoutError, ServerError):
            resolver.report_post_outcome(url, success=False)

    The resolver does NOT perform HTTP itself — ``discovery_fn`` is a caller-
    supplied callback that returns the parsed ``/tenant/config`` response
    (a dict like ``{"endpoints": {"ingest": "...", ...}}``). On exception,
    discovery is marked failed and step 3 is used.
    """

    def __init__(
        self,
        base_url: str,
        discovery_fn: Optional[Callable[[], dict]] = None,
        region: str = DEFAULT_REGION,
        config: Optional[IngestResolverConfig] = None,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._base_url = normalize_base_url(base_url)
        self._discovery_fn = discovery_fn
        self._region = region
        self._config = config or IngestResolverConfig()
        self._clock = clock

        # MOOLABS_INGEST_HOST env var override — short-circuits the F2 chain.
        # Customers running in single-region self-hosted or non-standard
        # cloud deployments (e.g., a regional ingest subdomain that hasn't
        # been provisioned yet) can pin the ingest host explicitly. Set
        # this BEFORE the resolver runs through steps 2-4; the value
        # populates _cached_url so step-1 returns it verbatim.
        #
        # Accepts either a bare host (``meter.dev.moolabs.com``,
        # ``https://meter.dev.moolabs.com``) or a full URL — the path-
        # doubling guard in _make_client_at_url normalizes either form.
        _ingest_host_env = os.environ.get("MOOLABS_INGEST_HOST")
        if _ingest_host_env:
            # Ensure scheme prefix; bare hostnames are accepted for ergonomics
            # but get an https:// prefix.
            if not _ingest_host_env.startswith(("http://", "https://")):
                _ingest_host_env = "https://" + _ingest_host_env
        # Use RLock to allow nested acquire from helpers (and to interoperate
        # with the Condition variable for singleflight discovery below).
        self._lock = threading.RLock()
        # Singleflight discovery: when one thread is running discoveryFn (out
        # of lock for the HTTP call), other threads wait on this CV instead
        # of duplicating the call. Notified after the discoverer commits its
        # result back to the cache.
        self._discovery_cv = threading.Condition(self._lock)
        self._discovery_in_flight: bool = False

        # Cached regional ingest URL from a successful discovery (None until
        # the first successful step-2 call). MOOLABS_INGEST_HOST populates
        # this at construction time so get_ingest_url short-circuits to a
        # step-1 cache hit on every call.
        self._cached_url: Optional[str] = _ingest_host_env if _ingest_host_env else None

        # Stickiness for the env-var pin (Phase 2 review 2026-06-03 Finding 3):
        # report_post_outcome clears _cached_url when post_failure_threshold
        # is breached. Without tracking the env-pinned URL separately, the
        # explicit pin becomes a one-shot init value that silently degrades
        # after N transient failures. Store the env pin so report_post_outcome
        # can restore it instead of falling through to the F2 chain
        # (which would derive a possibly-dead regional host).
        self._env_pinned_url: Optional[str] = _ingest_host_env if _ingest_host_env else None

        # Timestamp until which discovery should be skipped after a failure.
        self._discovery_blocked_until: float = 0.0

        # URL → timestamp the "recently failed" mark expires at.
        # Discovery returning a URL in this set causes the resolver to skip
        # the discovered URL and fall through to step 3.
        self._recently_failed: dict[str, float] = {}

        # Consecutive POST-failure counter per URL — when this reaches the
        # threshold, the URL is marked recently-failed AND the cache cleared.
        self._post_failures: dict[str, int] = {}

    # ── Public API ──

    def get_ingest_url(self) -> str:
        """Run the F2 chain and return a URL to POST events to.

        Always returns a URL. Discovery failures fall through to step 3/4
        rather than raising — the customer's ingest call should keep working
        through transient backend outages.

        **Singleflight discovery** (post-PR #395 review I3): the 10s HTTP
        discovery call is made WITHOUT holding the resolver lock so other
        operations on the resolver (cache check, recently-failed marking)
        don't serialize behind it. Concurrent threads arriving while
        discovery is in flight wait on a Condition variable for the
        discoverer to commit its result, then re-check the cache. So a
        burst of N concurrent ingest threads triggers AT MOST one
        discovery, while no thread blocks for cache reads against
        unrelated URLs.
        """
        # First pass: see if we're a cache hit, can fall through without
        # discovery, OR need to coordinate discovery.
        with self._discovery_cv:
            self._expire_recently_failed_locked()

            # Step 1 — cache hit.
            if self._cached_url is not None:
                return self._cached_url

            # Decide if we should discover (under lock).
            should_discover = (
                self._discovery_fn is not None
                and self._discovery_blocked_until <= self._clock()
            )
            if not should_discover:
                # Step 3 — region-map fallback (no discovery this call).
                return self._region_fallback_url_locked()

            if self._discovery_in_flight:
                # Another thread is already discovering. Wait for its
                # commit (or for it to give up), then re-check cache.
                # Timeout matches the discovery_retry_ttl as a backstop —
                # we never wait indefinitely.
                self._discovery_cv.wait(timeout=self._config.discovery_retry_ttl_sec)
                if self._cached_url is not None:
                    return self._cached_url
                # Discoverer gave up; we fall through to step 3 ourselves.
                return self._region_fallback_url_locked()

            # We own this discovery. Set the in-flight flag and release
            # the lock so other ops aren't blocked on our HTTP call.
            self._discovery_in_flight = True

        # ── Out of lock: HTTP call may take seconds.
        discovered: Optional[str] = None
        try:
            discovered = self._try_discovery_unlocked()
        finally:
            with self._discovery_cv:
                self._discovery_in_flight = False
                if discovered is not None:
                    self._cached_url = discovered
                # Wake every waiter (each re-checks the cache).
                self._discovery_cv.notify_all()

        with self._discovery_cv:
            if self._cached_url is not None:
                return self._cached_url
            return self._region_fallback_url_locked()

    def report_post_outcome(self, url: str, success: bool) -> None:
        """Update state based on the outcome of POSTing to ``url``.

        On success: reset the per-URL failure counter.
        On failure: increment; if it reaches the threshold AND the URL is
        the cached one, invalidate the cache and record the URL as recently
        failed (so a subsequent discovery returning the same URL falls
        through to step 3).
        """
        with self._lock:
            if success:
                self._post_failures.pop(url, None)
                return

            count = self._post_failures.get(url, 0) + 1
            self._post_failures[url] = count
            if count >= self._config.post_failure_threshold:
                # Invalidate cache + mark URL as recently failed.
                if self._cached_url == url:
                    # Env-pinned URL is sticky (Phase 2 review Finding 3):
                    # if the operator explicitly set MOOLABS_INGEST_HOST,
                    # don't fall through to the F2 chain (which would
                    # derive a possibly-dead regional host). Restore the
                    # pin so the next call uses it again. The downstream
                    # _recently_failed mark below still applies so we
                    # don't HAMMER the host immediately — but at least
                    # subsequent calls AFTER the TTL hit the pinned host,
                    # not a different one.
                    if self._env_pinned_url and url == self._env_pinned_url:
                        # Keep _cached_url == env_pinned_url; don't clear.
                        pass
                    else:
                        self._cached_url = None
                self._recently_failed[url] = (
                    self._clock() + self._config.recently_failed_ttl_sec
                )
                self._post_failures.pop(url, None)
                # Bound the set: theoretical attack / buggy BFF could
                # accumulate many distinct dead URLs before the TTL
                # expires. Cap at 64 entries (~256 bytes each) — drop
                # the oldest entries by expiry time.
                self._cap_recently_failed_locked(64)
                self._cap_post_failures_locked(64)

    # ── Step 3/4 composition (callable for tests) ──

    def step4_last_resort_url(self) -> str:
        """The always-derivable last-resort URL: ``meter.{base}/api/v1/events``.

        Independent of region, discovery, or cache state. For single-region
        self-hosted deployments this is the *expected* steady-state route
        (not a fallback) per contracts §3.5a.
        """
        return f"{derive_host('meter', self._base_url)}{_METER_INGEST_PATH}"

    # ── Internal helpers ──

    def _try_discovery_unlocked(self) -> Optional[str]:
        """Call ``discovery_fn`` and extract the regional ingest URL.

        **Called WITHOUT holding ``self._lock``** (post-PR #395 review I3).
        Returns the full POST URL on success or None on failure. State
        mutations that depend on the resolver lock (setting
        ``_discovery_blocked_until``, checking ``_recently_failed``) are
        deferred to a separate locked update at the caller's site so this
        function can do its 10s HTTP call without serializing every other
        ingest thread on the resolver mutex.

        On failure, returns None — the caller will see this, re-acquire the
        lock, and update ``_discovery_blocked_until`` to set the cool-off
        window. This is functionally equivalent to the previous in-lock
        behavior with one observable difference: the cool-off window
        starts ~10s later (when the failed HTTP returns, not when it began).
        That is a feature, not a bug — the failure timestamp should reflect
        when the failure was confirmed, not when discovery started.
        """
        assert self._discovery_fn is not None
        block_after = False
        try:
            response = self._discovery_fn()
        except Exception:  # noqa: BLE001 — any failure → fallback
            block_after = True
            response = None

        try:
            if block_after:
                return None
            if not isinstance(response, dict):
                block_after = True
                return None
            endpoints = response.get("endpoints", {})
            ingest_host = endpoints.get("ingest") if isinstance(endpoints, dict) else None
            if not isinstance(ingest_host, str) or not ingest_host:
                block_after = True
                return None

            # Normalize: append the meter ingest path if discovered URL is
            # host-only (current BFF contract).
            ingest_host = ingest_host.rstrip("/")
            if "://" in ingest_host and "/" not in ingest_host.split("://", 1)[1]:
                full_url = ingest_host + _METER_INGEST_PATH
            else:
                full_url = ingest_host

            # Defense-in-depth: discovered URL must be under base_url.
            if not _host_matches_base_url(full_url, self._base_url):
                block_after = True
                return None

            # Recently-failed check needs the lock; do it briefly.
            with self._lock:
                if full_url in self._recently_failed:
                    return None
            return full_url
        finally:
            if block_after:
                with self._lock:
                    self._discovery_blocked_until = (
                        self._clock() + self._config.discovery_retry_ttl_sec
                    )

    def _region_fallback_url_locked(self) -> str:
        """Compose ``https://ingest.{region_code}.{base_url}{path}`` from the
        SDK's region map; if the region resolves to no entry, fall through
        to step 4 (``meter.{base}/api/v1/events``)."""
        region_code = REGION_INGEST_MAP.get(self._region)
        if region_code is None:
            # Unknown region marker — final fallback to the always-derivable
            # meter host. Per contracts §3.5a this is also the steady-state
            # route for single-region self-hosted customers.
            return self.step4_last_resort_url()

        candidate = (
            f"https://ingest.{region_code}.{self._base_url}{_METER_INGEST_PATH}"
        )
        # If the regional URL itself is recently-failed (rare but possible
        # if a previous discovery returned the same regional host), fall
        # through to step 4.
        if candidate in self._recently_failed:
            return self.step4_last_resort_url()
        return candidate

    def _expire_recently_failed_locked(self) -> None:
        """Drop any "recently failed" entries whose TTL has passed."""
        now = self._clock()
        expired = [url for url, until in self._recently_failed.items() if until <= now]
        for url in expired:
            del self._recently_failed[url]

    def _cap_recently_failed_locked(self, max_entries: int) -> None:
        """Bound the recently_failed dict size by evicting entries with the
        EARLIEST expiry (i.e. those nearest to natural eviction anyway).

        Post-PR #395 review M2: under a buggy BFF or attacker scenario the
        dict could accumulate many distinct dead URLs faster than the
        300s TTL expires them. Bounded eviction keeps memory predictable.
        """
        if len(self._recently_failed) <= max_entries:
            return
        # Sort by expiry ascending; drop the oldest (first to expire).
        ordered = sorted(self._recently_failed.items(), key=lambda kv: kv[1])
        drop_count = len(self._recently_failed) - max_entries
        for url, _ in ordered[:drop_count]:
            del self._recently_failed[url]

    def _cap_post_failures_locked(self, max_entries: int) -> None:
        """Bound the post_failures dict. Entries that hit the threshold
        are normally popped immediately (see report_post_outcome), but a
        flood of distinct URLs each failing only N-1 times could grow
        unbounded. Cap by dropping the highest-count entries (closest
        to natural pop) when over budget."""
        if len(self._post_failures) <= max_entries:
            return
        ordered = sorted(self._post_failures.items(), key=lambda kv: -kv[1])
        drop_count = len(self._post_failures) - max_entries
        for url, _ in ordered[:drop_count]:
            del self._post_failures[url]

    # ── Introspection helpers (for tests + observability) ──

    @property
    def cached_url(self) -> Optional[str]:
        with self._lock:
            return self._cached_url

    def get_state_snapshot(self) -> dict:
        """Return a debug-friendly view of internal state. Useful for tests
        and (later) for structured logging when an ingest call falls back."""
        with self._lock:
            now = self._clock()
            return {
                "cached_url": self._cached_url,
                "discovery_blocked_for_sec": max(
                    0.0, self._discovery_blocked_until - now
                ),
                "recently_failed_count": len(self._recently_failed),
                "post_failures_tracked": len(self._post_failures),
            }
