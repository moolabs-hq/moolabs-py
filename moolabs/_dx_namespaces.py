"""Capability namespace classes for the normalized Moolabs SDK.

The customer writes ``client.<capability>.<method>(...)``. Each capability
namespace wraps one or more generated API classes; this module provides
the dispatch.

Two namespace types:
  - ``_Namespace`` — generic; builds a {method_name → bound_method} index
    from all backing classes for the capability, dispatches via __getattr__.
    O4 verified zero method-name collisions across all multi-class
    capabilities so a single flat index works without sub-accessors today.
  - ``_UsageNamespace`` — subclass that special-cases ``ingest_events`` to
    route through the F2 fallback chain (``IngestUrlResolver``) and the G5
    in-memory buffer (``IngestBuffer``) per contracts §3.5 / §3.5a.

The module is import-cycle-safe: it does NOT import ``moolabs.api.*``
modules directly. The caller (``_dx_client.py``) injects an
``import_api_class`` callable that resolves a class-name string to the
actual generated class. This keeps the namespace logic testable with fake
API classes and avoids forcing every test to depend on the generated tree.
"""

from __future__ import annotations

import json
import math
import uuid
import warnings
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Literal, Optional

from ._dx_buffer import IngestBuffer
from ._dx_routing import CAPABILITY_MAP, BackingClass
from ._dx_urls import IngestUrlResolver


# Default CloudEvent ``source`` when the caller doesn't supply one. Per the
# PRD's wire-shape contract (Section 4 / FR-1), the SDK identifies itself as
# the producer if the customer hasn't pinned their own app-level source.
_DEFAULT_SDK_SOURCE = "moolabs-sdk"


@dataclass(frozen=True)
class IngestResult:
    """Customer-facing return type for the three new ergonomic ingest methods.

    Frozen so callers can stash it in a dict / log line without mutation
    accidentally changing the recorded outcome.

    Fields:
      - ``event_id``: the id that was sent (auto-generated when the caller
        didn't pass ``event_id=``). Useful for sibling-join with a future
        cost event sharing the same ``entity_id``.
      - ``transport``: ``"buffered"`` when enqueued to the in-memory G5
        buffer (non-blocking; HTTP happens later via the drain worker).
        ``"sync"`` when posted on the caller's thread (strict-sync mode,
        constructed via ``Moolabs(buffer=False)``).
      - ``accepted_at``: client-side timestamp the SDK recorded when the
        envelope was built / enqueued. NOT the server's receipt time.
    """

    event_id: str
    transport: Literal["buffered", "sync"]
    accepted_at: datetime


def _check_value_is_finite(value: Any, *, name: str = "value") -> None:
    """Reject NaN / Inf / non-numeric for the usage-lane ``value`` field.

    Bool is technically a numeric in Python (``isinstance(True, int) ==
    True``), but a True/False slipping in here would silently coerce to
    1/0 on the wire — almost always a customer bug. We reject explicitly
    to surface the type confusion at the call site.
    """
    if isinstance(value, bool):
        raise ValueError(
            f"{name} must be a finite number, not bool; got {value!r}"
        )
    if not isinstance(value, (int, float)):
        raise ValueError(
            f"{name} must be a finite number; got {type(value).__name__} {value!r}"
        )
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError(f"{name} must be a finite number; got {value!r}")


def _check_spans_have_span_ids(spans: list[dict]) -> None:
    """Every span MUST carry a non-empty ``span_id``.

    Acute's per-span dedup grain is ``sdk:{span_id}``; an empty / missing
    span_id collides every cost span into the same dedup key, silently
    dropping legitimate spans. Reject up front so the bug surfaces at the
    call site rather than as a downstream "where did my cost data go?"
    investigation.
    """
    for i, span in enumerate(spans):
        if not isinstance(span, dict):
            raise ValueError(
                f"spans[{i}] must be a dict; got {type(span).__name__}"
            )
        if not span.get("span_id"):
            raise ValueError(
                f"spans[{i}].span_id must be a non-empty string"
            )


def _check_cost_spans_have_provider_and_model(spans: list[dict]) -> None:
    """Every cost-lane span MUST carry a non-empty ``provider`` and ``model``.

    Acute's cost-enricher rejects spans without both via a silent ``continue``
    at ``services/moo-acute/app/workers/cost_enricher.py``; events with all-
    invalid spans produce NO log line at acute, making the drop invisible to
    operators. Reject up front so the failure surfaces at the call site rather
    than as a downstream "cost event silently disappeared" investigation.

    The validator accepts a per-span ``provider``/``model`` OR a span_id-only
    span when the top-level ``provider``/``model`` kwargs on ``cost.ingest_event``
    are set (the canonical wire shape supports both). The call site decides
    which form to accept; this function checks the per-span form.
    """
    for i, span in enumerate(spans):
        if not isinstance(span, dict):
            # Caught by _check_spans_have_span_ids already; defensive only.
            continue
        if not span.get("provider"):
            raise ValueError(
                f"spans[{i}].provider must be a non-empty string — spans without "
                "provider are silently dropped during downstream cost processing, "
                "resulting in missing cost-attribution data"
            )
        if not span.get("model"):
            raise ValueError(
                f"spans[{i}].model must be a non-empty string — spans without "
                "model are silently dropped during downstream cost processing, "
                "resulting in missing cost-attribution data"
            )


def _check_meta_is_json_serializable(meta: dict) -> None:
    """Verify ``meta`` round-trips through JSON BEFORE buffer enqueue.

    If meta carries a non-serializable value (e.g. a ``set`` or a
    ``Decimal``), the failure would otherwise happen in the drain worker
    AFTER the customer's call already returned — an async failure mode
    the customer can't catch. Surface it synchronously here.
    """
    try:
        json.dumps(meta)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"meta must be JSON-serializable: {exc}") from exc


# Well-known top-level data keys per the canonical wire contract.
# These are first-class kwargs on every ingest method; they land at
# ``data.<key>`` directly on the wire (NOT under ``data.meta``).
# Kept here as a single source of truth — the parity gate's normalizer
# checks for them, and the LOCKED_INGEST_EVENT_SURFACE continuity gate
# uses this set to enforce surface consistency across languages.
_CANONICAL_WELL_KNOWN_KEYS = (
    "provider",
    "model",
    "total_input_tokens",
    "total_output_tokens",
    "total_tokens",
    "latency_ms",
    "status",
)


def _build_envelope(
    *,
    event_type: str,
    customer_id: str,
    entity_id: str,
    meter_slug: Optional[str] = None,
    value: Optional[float] = None,
    spans: Optional[list[dict]] = None,
    # Well-known top-level data.* keys (canonical wire shape).
    # Optional everywhere — present at data.<key> when non-None.
    provider: Optional[str] = None,
    model: Optional[str] = None,
    total_input_tokens: Optional[int] = None,
    total_output_tokens: Optional[int] = None,
    total_tokens: Optional[int] = None,
    latency_ms: Optional[int] = None,
    status: Optional[str] = None,
    event_id: Optional[str] = None,
    source: Optional[str] = None,
    time: Optional[datetime] = None,
    meta: Optional[dict] = None,
) -> Any:
    """Build a CloudEvent envelope from ergonomic kwargs (US-002).

    Wire contract: docs/prd/2026-06-02-sdk-unified-ingest-methods-prd.md
    Section 4 canonical envelope. ``entity_id`` maps to ``data.request_id``
    on the wire (the threading key preserved for moo-meter's request_id
    column and acute's cross-lane join).

    Well-known top-level data.* keys (provider, model, total_input_tokens,
    total_output_tokens, total_tokens, latency_ms, status) land at
    ``data.<key>`` directly. Arbitrary customer-defined fields go through
    ``meta=`` and land nested at ``data.meta.<key>``.

    Boundary checks (per FR-6) fire synchronously BEFORE buffer enqueue, so
    customers see the rejection at their call site:

      - empty ``event_type`` / ``customer_id`` / ``entity_id``
      - non-finite ``value`` (NaN / Inf / bool / non-numeric)
      - missing or empty ``span_id`` on any span
      - non-JSON-serializable ``meta``

    Returns a Pydantic-validated ``Event`` instance. The caller passes it
    via ``EventsApi.ingest_events(event=...)``. Customer never instantiates
    ``Event(...)`` directly.

    NOTE: ``tenant_id`` is NOT a kwarg here and NOT in the wire envelope —
    the server derives tenant identity from the API key.
    """
    if not event_type:
        raise ValueError("event_type must be a non-empty string")
    if not customer_id:
        raise ValueError("customer_id must be a non-empty string")
    if not entity_id:
        raise ValueError("entity_id must be a non-empty string")
    if value is not None:
        _check_value_is_finite(value)
    if spans is not None:
        _check_spans_have_span_ids(spans)
        # Lane discriminator: USAGE envelopes carry meter_slug+value and may
        # optionally include spans as supplemental context (e.g. event lineage
        # or per-span breakdown attached to a usage emit). Those spans don't
        # flow through the downstream cost-enrichment pipeline and don't need
        # provider/model. COST envelopes carry ONLY spans (no meter_slug, no
        # value) and DO flow to the cost-enrichment pipeline, which silently
        # drops spans without provider+model. The provider+model check fires
        # only on the cost lane.
        #
        # Empty string is treated as equivalent to None for meter_slug —
        # matches the Go SDK's ``args.MeterSlug == ""`` semantics where empty
        # string is the natural zero value. Without this, a caller passing
        # ``meter_slug=""`` (explicit empty, not None) would silently bypass
        # the cost-span check.
        is_cost_lane = (meter_slug is None or meter_slug == "") and value is None
        if is_cost_lane and (not provider or not model):
            _check_cost_spans_have_provider_and_model(spans)
    if meta is not None:
        _check_meta_is_json_serializable(meta)

    # Assemble ``data``. Order on the wire is JSON-irrelevant (parity gate
    # sorts keys); we keep the assembly order readable here for humans
    # diffing the envelope shape.
    data: dict[str, Any] = {"request_id": entity_id}
    if meter_slug is not None:
        data["meter_slug"] = meter_slug
    if value is not None:
        data["value"] = value
    # Well-known top-level keys (canonical wire shape).
    if provider is not None:
        data["provider"] = provider
    if model is not None:
        data["model"] = model
    if total_input_tokens is not None:
        data["total_input_tokens"] = total_input_tokens
    if total_output_tokens is not None:
        data["total_output_tokens"] = total_output_tokens
    if total_tokens is not None:
        data["total_tokens"] = total_tokens
    if latency_ms is not None:
        data["latency_ms"] = latency_ms
    if status is not None:
        data["status"] = status
    if spans is not None:
        data["spans"] = spans
    # Arbitrary customer fields stay nested at data.meta per Decision 4 of
    # the PRD's HOW section — provides a clean namespace separation between
    # well-known keys (above) and free-form metadata.
    if meta is not None:
        data["meta"] = meta

    # ``Event`` lives in the generated layer; import lazily to keep
    # ``_dx_namespaces`` import-cycle-safe (the module-level comment at the
    # top of this file documents the no-direct-generated-imports rule).
    from moolabs.models.event import Event  # type: ignore[import-not-found]

    return Event(
        id=event_id or uuid.uuid4().hex,
        specversion="1.0",
        source=source or _DEFAULT_SDK_SOURCE,
        type=event_type,
        subject=customer_id,
        time=time or datetime.now(timezone.utc),
        datacontenttype="application/json",
        data=data,
    )


# HTTP status codes that mean "this request will NEVER succeed on retry."
# Auth (401/403): the API key is wrong, missing scope, or revoked. Retrying
# burns the same key; buffering hides the error from the caller. Validation
# (400/422): the request body is malformed; retrying with the same body fails
# identically. 404 on an ingest URL would mean the route was removed — also
# terminal at the SDK layer (a redeploy is required, not a retry).
_TERMINAL_STATUSES = frozenset({400, 401, 403, 404, 422})


def _is_terminal_error(exc: BaseException) -> bool:
    """True if `exc` represents a non-retryable HTTP failure.

    Inspects the openapi-generator-cli generated ApiException, which exposes
    `.status` as an int when the request reached a response. Network errors
    and other Exception subclasses without a `.status` attribute are treated
    as transient (retryable / bufferable).
    """
    status = getattr(exc, "status", None)
    if isinstance(status, int) and status in _TERMINAL_STATUSES:
        return True
    return False


# Callable that resolves an API class name to the actual class.
# Real impl: importlib.import_module("moolabs.api.<snake>_api") then getattr.
# Test impl: dict lookup against fake classes.
ImportApiClass = Callable[[str], type]

# Callable that wraps a backend name → ApiClient instance. The
# Moolabs client owns the per-backend ApiClient lifecycle; namespaces
# just look them up.
GetClient = Callable[[str], Any]


class _Namespace:
    """Method-index-based dispatch over one or more backing API classes.

    For each ``BackingClass(api_class, backend)`` in the capability's
    routing entry, the namespace instantiates the API class against the
    backend's shared ApiClient, then walks ``dir()`` for public callables
    and registers them in the dispatch index.

    Method lookups go through ``__getattr__`` so the customer can call
    any method on any backing class as if it lived directly on the
    namespace. If two backing classes within the same capability would
    expose the same method name, **first one wins** — O4 verified this
    doesn't happen today, but the rule keeps behavior deterministic
    if it ever does.
    """

    def __init__(
        self,
        capability: str,
        get_client: GetClient,
        import_api_class: ImportApiClass,
    ) -> None:
        if capability not in CAPABILITY_MAP:
            raise ValueError(
                f"unknown capability {capability!r}; valid: "
                f"{sorted(CAPABILITY_MAP)}"
            )
        self._capability = capability
        self._get_client = get_client
        self._import_api_class = import_api_class
        self._method_index: dict[str, Any] = {}
        self._backing_instances: list[tuple[BackingClass, Any]] = []
        self._build_index()

    def _build_index(self) -> None:
        """Walk every backing class, instantiate it, and register its
        public methods in the dispatch index."""
        for bc in CAPABILITY_MAP[self._capability]:
            api_class = self._import_api_class(bc.api_class)
            client = self._get_client(bc.backend)
            instance = api_class(client)
            self._backing_instances.append((bc, instance))
            for attr in dir(instance):
                if attr.startswith("_"):
                    continue
                value = getattr(instance, attr, None)
                if not callable(value):
                    continue
                # First-class-wins on method-name collision (O4 says today
                # this never fires; defensive for future Arc additions).
                # No log line — library never writes to stderr. If this
                # ever fires in practice, surface it via the parity check
                # or an explicit assertion at namespace construction.
                if attr in self._method_index:
                    continue
                self._method_index[attr] = value

    # ── Pythonic protocols ──

    def __getattr__(self, name: str) -> Any:
        # __getattr__ is only invoked when normal lookup fails — instance
        # attributes (_capability, _method_index, etc.) hit __getattribute__
        # first. So we only see method names here.
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            return self._method_index[name]
        except KeyError:
            sample = ", ".join(sorted(self._method_index)[:5])
            raise AttributeError(
                f"capability {self._capability!r} has no method {name!r}; "
                f"available include: {sample}..."
            )

    def __dir__(self) -> list[str]:
        # Help IDE autocomplete and dir() inspection. Includes both private
        # attrs (__class__, etc.) and the method-index keys.
        return list(self._method_index.keys()) + ["_capability"]

    def __repr__(self) -> str:
        n = len(self._method_index)
        return f"<{self._capability} namespace: {n} methods>"


class _UsageNamespace(_Namespace):
    """Special-cased usage namespace.

    Every method routes through ``_Namespace``'s normal dispatch (so
    ``list_events``, ``list_meters``, ``query_meter``, etc. all work
    unchanged) EXCEPT for ``ingest_events``, which:

      1. Resolves a per-call URL via the F2 fallback chain.
      2. Calls the underlying ``EventsApi.ingest_events`` against an
         ``ApiClient`` pointed at the resolved URL.
      3. Reports the outcome to the resolver (so POST failures eventually
         invalidate the cached URL per contracts §3.5).
      4. If the F2 chain exhausts (every URL failed) AND the buffer is
         enabled, enqueues the events to the G5 buffer and returns a
         "queued" sentinel instead of raising.
      5. If buffer is disabled, raises the underlying exception.
    """

    # Sentinel returned by ingest_events when events were buffered rather
    # than delivered synchronously. Customers who want strict-sync should
    # construct with ``buffer=False``.
    _BUFFERED_SENTINEL_KEY = "buffered"

    def __init__(
        self,
        get_client: GetClient,
        import_api_class: ImportApiClass,
        ingest_resolver: IngestUrlResolver,
        ingest_buffer: Optional[IngestBuffer],
        make_client_at_url: Callable[[str], Any],
    ) -> None:
        super().__init__("usage", get_client, import_api_class)
        self._ingest_resolver = ingest_resolver
        self._ingest_buffer = ingest_buffer
        self._make_client_at_url = make_client_at_url
        # Cache the generated EventsApi class lookup; we re-instantiate per
        # call with different clients but the class itself doesn't change.
        self._events_api_class = import_api_class("EventsApi")

        # Producer-channel pattern (post-PR #395 round-5): the customer's
        # ingest_events call does a non-blocking queue.put (~1 µs Python
        # overhead due to GIL), then a dedicated producer thread moves
        # events from the queue to the buffer. Customer's thread never
        # touches the buffer's threading.Lock.
        #
        # Python doesn't have channels; queue.Queue is the equivalent.
        # put_nowait() raises queue.Full instead of blocking — we catch
        # it and increment _ingest_queue_dropped.
        #
        # Queue capacity scales with the buffer's max_size: max(1024,
        # buffer_max/8). Round-4 I-NEW-5: a customer with buffer_max=100k
        # otherwise gets a 1024-deep queue, sees ingest_queue_dropped
        # rising while buffer stats stay clean — confusing duplicate
        # failure mode.
        import queue as _queue
        import threading as _threading
        queue_cap = 1024
        if ingest_buffer is not None:
            queue_cap = max(1024, ingest_buffer._config.max_size // 8)
        self._event_queue: "_queue.Queue[list[Any]]" = _queue.Queue(maxsize=queue_cap)
        self._producer_stop = _threading.Event()
        self._producer_thread: Optional[_threading.Thread] = None
        self._producer_lock = _threading.Lock()   # guards lazy start
        self._ingest_queue_dropped: int = 0
        self._producer_recoveries: int = 0   # round-4 C-NEW-1 (Python sibling)

    def __getattr__(self, name: str) -> Any:
        if name == "ingest_events":
            return self._ingest_events
        return super().__getattr__(name)

    def __dir__(self) -> list[str]:
        return list(set(super().__dir__()) | {"ingest_events"})

    def _ingest_events(self, events: list[Any], **kwargs: Any) -> Any:
        """F2-routed, G5-buffered event ingest (legacy list-shaped surface).

        .. deprecated::
           Use ``client.usage.ingest_event(...)`` instead — the singular,
           kwargs-based surface. The list-shaped method is retained for one
           minor version after the unified ingest methods ship so existing
           call sites don't break during migration.

        **Default mode (buffer enabled):** non-blocking. Events are
        enqueued to the in-memory buffer and returned immediately;
        the background worker delivers them via the F2 chain. The
        customer's call returns in microseconds regardless of network
        conditions. Auth/network failures are surfaced via
        ``stats()['terminal_drops']`` and the customer-supplied logger,
        NOT raised at the call site.

        **Strict-sync mode (buffer=False at construction):** blocking.
        Events are POSTed inline on the caller's thread; HTTP errors
        propagate up. Auth/validation errors (401/403/400/422/404) raise
        immediately. Transient errors raise; the URL is penalized in
        the F2 resolver so the next call re-walks the chain. Use this
        mode only when the caller specifically needs delivery
        confirmation per call.

        Pre-PR #395 round-4 design: buffer was failure-only path; every
        ingest call blocked the caller for the HTTP round-trip. New
        design: buffer is the primary path; caller never blocks unless
        explicitly opted in.

        US-001 fix (2026-06-02): the strict-sync path previously passed
        ``events`` (a list) as the positional arg to
        ``EventsApi.ingest_events(event: Event)`` which Pydantic rejects.
        The fix unwraps single-element lists and iterates multi-element
        lists, calling the singular underlying method per event.
        """
        if not events:
            return self._empty_ingest_response()

        # Deprecation warning fires on every non-empty call; Python's default
        # ``warnings`` filter dedupes by location, so customers see one
        # warning per call site rather than per invocation.
        warnings.warn(
            "client.usage.ingest_events(list) is deprecated; use "
            "client.usage.ingest_event(...) (singular, kwargs-based) instead.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self._ingest_buffer is not None:
            # Producer-channel: non-blocking queue put (~1 µs). Producer
            # thread moves events to the buffer; drain worker POSTs.
            # Customer's thread never touches the buffer's lock.
            self._ensure_producer()
            import queue as _queue
            try:
                self._event_queue.put_nowait(events)
                return {
                    self._BUFFERED_SENTINEL_KEY: True,
                    "count": len(events),
                }
            except _queue.Full:
                # Producer can't keep up; drop here (observable via
                # ingest_queue_dropped()).
                with self._producer_lock:
                    self._ingest_queue_dropped += len(events)
                return {
                    self._BUFFERED_SENTINEL_KEY: False,
                    "count": 0,
                    "ingest_queue_dropped": len(events),
                }

        # Strict-sync mode: caller wants delivery confirmation per call.
        url = self._ingest_resolver.get_ingest_url()
        client_at_url = self._make_client_at_url(url)
        events_api = self._events_api_class(client_at_url)

        # US-001: the generated ``EventsApi.ingest_events`` is typed for a
        # single ``event: Event``. Passing the list as a positional arg
        # makes Pydantic reject with ``ValidationError`` (the bug we hit on
        # the dev demo 2026-06-01). Fix: unwrap single-element lists,
        # iterate multi-element lists.
        try:
            if len(events) == 1:
                result = events_api.ingest_events(event=events[0], **kwargs)
            else:
                # Multi-event batch: underlying spec only supports singular
                # ingestion today. Iterate; if any single call raises, the
                # exception surfaces immediately (consistent with strict-sync
                # contract — partial-batch semantics aren't promised here).
                for ev in events:
                    events_api.ingest_events(event=ev, **kwargs)
                result = {"count": len(events)}
            self._ingest_resolver.report_post_outcome(url, success=True)
            return result
        except Exception as exc:
            if _is_terminal_error(exc):
                # Don't penalize the URL — a 401 means our key is wrong,
                # not that the host is down. Re-raise so caller sees it.
                raise
            self._ingest_resolver.report_post_outcome(url, success=False)
            raise

    @staticmethod
    def _empty_ingest_response() -> dict:
        """The response shape for an empty-events ingest call — short-circuit
        without doing any URL resolution or HTTP work."""
        return {"_dx_pagination_empty_ingest": True, "count": 0}

    # ── US-002: ergonomic-kwarg singular ingest ──────────────────────────────

    def ingest_event(
        self,
        *,
        event_type: str,
        customer_id: str,
        entity_id: str,
        meter_slug: str,
        value: float,
        # Well-known top-level data.* keys (canonical wire shape).
        provider: Optional[str] = None,
        model: Optional[str] = None,
        total_input_tokens: Optional[int] = None,
        total_output_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        latency_ms: Optional[int] = None,
        status: Optional[str] = None,
        event_id: Optional[str] = None,
        source: Optional[str] = None,
        time: Optional[datetime] = None,
        meta: Optional[dict] = None,
    ) -> IngestResult:
        """Emit a usage-lane CloudEvent to the unified meter endpoint.

        See docs/prd/2026-06-02-sdk-unified-ingest-methods-prd.md US-002.

        Required kwargs:
          - ``event_type``: CloudEvents ``type`` field (e.g. ``"ai.chat"``)
          - ``customer_id``: end-customer identifier (becomes CloudEvents
            ``subject``); the billable entity
          - ``entity_id``: threading key; same value on the sibling cost
            event lets downstream join the two without a transaction (on
            the wire as ``data.request_id``)
          - ``meter_slug``: which per-tenant meter aggregates this event
          - ``value``: the aggregation unit — sum/count/avg key

        Well-known top-level data.* kwargs (canonical wire shape — all
        optional, present at ``data.<key>`` when non-None):
          - ``provider``: third-party origin of the request (e.g. ``"openai"``)
          - ``model``: model/grade actually invoked (e.g. ``"gpt-4o"``)
          - ``total_input_tokens`` / ``total_output_tokens`` / ``total_tokens``:
            aggregate token counts (LLM-specific)
          - ``latency_ms``: end-to-end latency
          - ``status``: outcome string (e.g. ``"success"``, ``"failed"``)

        Other optional kwargs:
          - ``event_id``: stable id for idempotency; auto-generated UUID4
            hex if omitted (every retry mints a new id, so retry safety
            is opt-in)
          - ``source``: CloudEvents ``source`` (defaults to
            ``"moolabs-sdk"``); customers usually pass their app/service
            slug
          - ``time``: CloudEvents ``time`` (defaults to ``now(UTC)``)
          - ``meta``: free-form attribution dict — ANY non-canonical fields.
            Lands NESTED at ``data.meta.<key>`` per Decision 4 in the PRD.
            Use this for custom fields that aren't well-known canonical keys.

        Routing: built envelope flows through the existing G5 buffer (when
        present) or directly via ``EventsApi.ingest_events(event=...)``
        against an F2-resolved URL — same transport the legacy
        ``ingest_events(list)`` method uses post-US-001.

        ``tenant_id`` is NOT a kwarg. The server derives tenant identity
        from the API key sent in the ``Authorization`` header.

        Returns:
          - ``IngestResult`` carrying the (possibly auto-generated)
            ``event_id``, the ``transport`` ("buffered" or "sync"), and a
            client-side ``accepted_at`` timestamp.

        Raises:
          - ``ValueError`` — synchronously, before buffer enqueue —
            for any boundary-check failure (see ``_build_envelope``).
          - The underlying generated SDK's ``ApiException`` (or subclass)
            on strict-sync HTTP failures. In buffered mode HTTP failures
            are async; they surface via ``client.stats()['terminal_drops']``.
        """
        accepted_at = datetime.now(timezone.utc)
        envelope = _build_envelope(
            event_type=event_type,
            customer_id=customer_id,
            entity_id=entity_id,
            meter_slug=meter_slug,
            value=value,
            provider=provider,
            model=model,
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_tokens=total_tokens,
            latency_ms=latency_ms,
            status=status,
            event_id=event_id,
            source=source,
            time=time,
            meta=meta,
        )

        if self._ingest_buffer is not None:
            # Non-blocking enqueue. Producer thread moves [envelope] from
            # the queue to the buffer; drain worker POSTs asynchronously.
            self._ensure_producer()
            import queue as _queue
            try:
                self._event_queue.put_nowait([envelope])
            except _queue.Full:
                # Producer can't keep up; drop counter surfaces via
                # ingest_queue_dropped() / client.stats()[]. The caller's
                # IngestResult still reports transport="buffered" because
                # the customer's intent was buffered; the drop is async
                # observability.
                with self._producer_lock:
                    self._ingest_queue_dropped += 1
            return IngestResult(
                event_id=envelope.id,
                transport="buffered",
                accepted_at=accepted_at,
            )

        # Strict-sync mode: caller wants delivery confirmation per call.
        url = self._ingest_resolver.get_ingest_url()
        client_at_url = self._make_client_at_url(url)
        events_api = self._events_api_class(client_at_url)
        try:
            events_api.ingest_events(event=envelope)
            self._ingest_resolver.report_post_outcome(url, success=True)
            return IngestResult(
                event_id=envelope.id,
                transport="sync",
                accepted_at=accepted_at,
            )
        except Exception as exc:
            if _is_terminal_error(exc):
                # 401/403/400/422/404 — don't penalize the URL; the key /
                # body is wrong, not the host.
                raise
            self._ingest_resolver.report_post_outcome(url, success=False)
            raise

    # ── Producer-channel: customer thread → queue → producer thread → buffer ──

    def _ensure_producer(self) -> None:
        """Start the producer thread on first ingest. Idempotent + thread-safe."""
        if self._producer_thread is not None and self._producer_thread.is_alive():
            return
        with self._producer_lock:
            if self._producer_thread is not None and self._producer_thread.is_alive():
                return
            import threading as _threading
            self._producer_thread = _threading.Thread(
                target=self._producer_loop,
                name="moolabs-ingest-producer",
                daemon=True,
            )
            self._producer_thread.start()

    def _producer_loop(self) -> None:
        """Drain `_event_queue` and forward to the buffer. Exits when
        `_producer_stop` is set AND the queue is empty.

        **Drain-on-shutdown invariant (Codex review HIGH-1, round 6).**
        Events accepted by ``ingest_events`` with ``buffered: True`` MUST
        reach ``IngestBuffer`` before the producer exits, even if
        ``_stop_producer`` is called immediately afterwards. Prior
        implementation exited at the top of the loop on the stop flag,
        abandoning everything still queued (invisible in buffer stats —
        silent data loss on shutdown / short-lived processes). The fix is
        to exit ONLY when both: stop has been signaled AND the queue is
        empty. Matches the Go ``ProducerChannel.loop`` drain semantics.

        The outer loop body is wrapped in a broad BaseException catch
        (round-4 I-NEW-6 — the prior narrow `Exception` left
        KeyboardInterrupt/SystemExit/MemoryError as silent thread-killers).
        On any non-stop exception, log if a logger was injected via the
        buffer config, increment _producer_recoveries, and continue
        looping. The producer thread itself is unkillable except via
        _producer_stop.
        """
        import queue as _queue
        while True:
            # Exit ONLY when both conditions hold. Checking queue.empty()
            # is racy with concurrent put_nowait calls, but that's
            # acceptable here: ``_stop_producer`` is the ONLY caller that
            # sets the stop flag, and the documented contract is that
            # ``ingest_events`` is undefined after ``Moolabs.close()``.
            # Pre-close events are guaranteed to drain because they
            # entered the queue before the flag was set.
            if self._producer_stop.is_set() and self._event_queue.empty():
                return
            try:
                self._producer_loop_one_iteration()
            except BaseException as exc:  # noqa: BLE001 — never let producer die
                self._producer_recoveries += 1
                # If buffer has a logger, surface the panic event. Else
                # silently recover — the recovery counter is the signal.
                try:
                    if self._ingest_buffer is not None:
                        self._ingest_buffer._logger(
                            "moolabs.producer.recovered_from_exception",
                            {"exception_type": type(exc).__name__, "exception": str(exc)},
                        )
                except BaseException:  # noqa: BLE001 — defensive: don't let logger panic kill us
                    pass

    def _producer_loop_one_iteration(self) -> None:
        """One drain pass — pulled out so the BaseException catch in the
        outer loop wraps it cleanly."""
        import queue as _queue
        try:
            # Short timeout so we can check the stop flag periodically.
            events = self._event_queue.get(timeout=0.5)
        except _queue.Empty:
            return
        if events is None:
            # Sentinel poison-pill for fast shutdown.
            self._producer_stop.set()
            return
        if self._ingest_buffer is not None:
            try:
                self._ingest_buffer.enqueue(events)
            except Exception:  # noqa: BLE001
                # Worst case: overflow=raise + buffer full. Customer
                # already returned success; drop silently here.
                pass

    def _stop_producer(self, timeout: Optional[float] = None) -> None:
        """Signal producer to exit and wait for it. Called by Moolabs.close()."""
        if self._producer_thread is None or not self._producer_thread.is_alive():
            return
        self._producer_stop.set()
        # Wake the producer if it's blocked on queue.get
        try:
            self._event_queue.put_nowait(None)
        except Exception:  # noqa: BLE001
            pass
        self._producer_thread.join(timeout=timeout)

    def ingest_queue_dropped(self) -> int:
        """Count of events dropped because the producer queue was full.
        Surfaced separately from buffer.stats()['dropped'] which counts
        events dropped by the buffer's overflow_drop_oldest AFTER they
        made it through the producer queue."""
        with self._producer_lock:
            return self._ingest_queue_dropped


class _CostNamespace(_Namespace):
    """Cost capability — special-cased to add ``ingest_event`` routed
    through the unified meter endpoint (NOT the legacy acute direct path).

    Per docs/prd/2026-06-02-sdk-unified-ingest-methods-prd.md US-003 +
    Decision 2: the meter-endpoint is the SDK's only ingest target. Acute
    consumes the events from the ``om_default_events`` Kafka topic as a
    downstream consumer; customer SDK no longer talks to acute directly.

    Legacy methods on the cost capability — ``ingest_events_batch``
    (CostEventsApi batch endpoint), ``submit_adjustment``,
    ``ingest_sdk_spans`` (SdkIngestApi) — continue to dispatch via the
    generic ``_Namespace.__getattr__`` to their CostEventsApi/SdkIngestApi
    classes. The two ingestion-flavored ones emit a one-time
    ``DeprecationWarning`` per instance per method name on first access,
    pointing customers at ``client.cost.ingest_event(...)`` (the new
    meter-routed method).

    NOTE: ``submit_adjustment`` is NOT deprecated here — the unified
    adjustment surface (``client.events.adjust(...)``) is a separate
    slice tracked outside this PRD; customers who use the legacy method
    should keep using it until that surface ships.
    """

    # Methods on the cost capability that emit DeprecationWarning when
    # accessed via __getattr__ dispatch. Single-shot per (instance, name)
    # via ``_warned_methods`` so a tight loop doesn't spam.
    _DEPRECATED_LEGACY_METHODS = frozenset({
        "ingest_events_batch",  # CostEventsApi batch ingest (acute direct)
        "ingest_sdk_spans",     # SdkIngestApi (acute direct)
    })

    def __init__(
        self,
        get_client: GetClient,
        import_api_class: ImportApiClass,
        ingest_resolver: IngestUrlResolver,
        ingest_buffer: Optional[IngestBuffer],
        make_client_at_url: Callable[[str], Any],
    ) -> None:
        super().__init__("cost", get_client, import_api_class)
        self._ingest_resolver = ingest_resolver
        self._ingest_buffer = ingest_buffer
        self._make_client_at_url = make_client_at_url
        # Cache the meter EventsApi class for routing. The legacy
        # CostEventsApi / SdkIngestApi classes are still discovered by
        # ``_Namespace._build_index`` and remain accessible via the standard
        # ``__getattr__`` dispatch — but ``ingest_event`` (the new method)
        # always goes through ``EventsApi`` for the meter unified path.
        self._events_api_class = import_api_class("EventsApi")
        # Per-instance once-fire tracking for deprecation warnings. A class-
        # level shared set would silently swallow warnings across multiple
        # Moolabs instances in the same process (test isolation issue + the
        # surprise factor of "I created a new client but didn't see the
        # warning"). Per-instance is the right semantic.
        self._warned_methods: set[str] = set()

    def __getattr__(self, name: str) -> Any:
        """Same as ``_Namespace.__getattr__`` for unknown attributes, but
        emits a one-shot ``DeprecationWarning`` for the legacy ingest
        methods so customers see the migration hint in their logs without
        a hard break."""
        if name in self._DEPRECATED_LEGACY_METHODS:
            if name not in self._warned_methods:
                self._warned_methods.add(name)
                warnings.warn(
                    f"client.cost.{name}(...) is deprecated — it routes to the "
                    f"acute direct path which is being retired. Use "
                    f"client.cost.ingest_event(*, event_type, customer_id, "
                    f"entity_id, spans, ...) instead — it routes through the "
                    f"unified meter endpoint at meter.{{base}}/api/v1/events.",
                    DeprecationWarning,
                    stacklevel=2,
                )
        return super().__getattr__(name)

    # ── US-003: ergonomic-kwarg singular cost ingest ─────────────────────

    def ingest_event(
        self,
        *,
        event_type: str,
        customer_id: str,
        entity_id: str,
        spans: list[dict],
        # Well-known top-level data.* keys (canonical wire shape).
        provider: Optional[str] = None,
        model: Optional[str] = None,
        total_input_tokens: Optional[int] = None,
        total_output_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        latency_ms: Optional[int] = None,
        status: Optional[str] = None,
        event_id: Optional[str] = None,
        source: Optional[str] = None,
        time: Optional[datetime] = None,
        meta: Optional[dict] = None,
    ) -> IngestResult:
        """Emit a cost-lane CloudEvent to the unified meter endpoint.

        See docs/prd/2026-06-02-sdk-unified-ingest-methods-prd.md US-003.

        Required kwargs:
          - ``event_type``: CloudEvents ``type`` (e.g. ``"ai.completion"``)
          - ``customer_id``: end-customer identifier (becomes
            CloudEvents ``subject``)
          - ``entity_id``: threading key; same value on the sibling usage
            event lets downstream join the two without a transaction (on
            the wire as ``data.request_id``)
          - ``spans``: list of cost-side per-span breakdowns. Each span
            MUST carry a non-empty ``span_id``; acute's per-span dedup
            grain is ``sdk:{span_id}`` and an empty / missing id collides
            every span into the same dedup key (silent data loss). Other
            span fields are open-shape per acute's mapping engine.

        Well-known top-level data.* kwargs (canonical wire shape):
          - ``provider`` / ``model``: aggregate origin of the request.
            Use this when ALL spans share the same provider/model; use
            per-span ``provider``/``model`` (inside each span dict) when
            spans differ.
          - ``total_input_tokens`` / ``total_output_tokens`` / ``total_tokens``:
            aggregate LLM token counts across all spans.
          - ``latency_ms``: end-to-end latency for the whole event.
          - ``status``: outcome string for the whole event.

        Other optional kwargs are identical to ``usage.ingest_event``.

        Routing: the envelope flows through the existing G5 buffer (when
        present) or strict-sync via ``EventsApi.ingest_events(event=...)``
        — same transport ``usage.ingest_event`` uses. The cost lane is
        identified by the presence of ``data.spans``; absence of
        ``data.meter_slug`` / ``data.value`` distinguishes it from the
        usage lane.

        Why meter and not acute: per PRD Decision 2, the unified meter
        endpoint already publishes to the ``om_default_events`` Kafka
        topic, and acute's ``cost_enricher`` consumes from the same topic
        — so events emitted via the meter path arrive at acute through
        the Kafka stream automatically, with the additional benefit that
        moo-meter's sink lands them in ClickHouse (the events stream tab)
        and the BFF ingest_consumer (post US-001 fix) lands them in BFF
        Postgres for the usage stream tab.

        ``tenant_id`` is NOT a kwarg — server derives from the API key.

        Returns ``IngestResult`` (same shape as
        ``usage.ingest_event``).
        Raises ``ValueError`` synchronously on boundary check failures
        (see ``_build_envelope``).
        """
        accepted_at = datetime.now(timezone.utc)
        envelope = _build_envelope(
            event_type=event_type,
            customer_id=customer_id,
            entity_id=entity_id,
            spans=spans,
            provider=provider,
            model=model,
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_tokens=total_tokens,
            latency_ms=latency_ms,
            status=status,
            event_id=event_id,
            source=source,
            time=time,
            meta=meta,
        )

        if self._ingest_buffer is not None:
            # Direct enqueue to the shared buffer. Unlike _UsageNamespace
            # (which uses an intermediate producer-channel queue to avoid
            # lock contention on hot-path usage emissions), cost emission
            # is expected to be lower-frequency — direct enqueue's
            # simplicity wins. If cost volume justifies it later, the
            # producer-channel pattern can be added without a customer-
            # facing API change.
            self._ingest_buffer.enqueue([envelope])
            return IngestResult(
                event_id=envelope.id,
                transport="buffered",
                accepted_at=accepted_at,
            )

        url = self._ingest_resolver.get_ingest_url()
        client_at_url = self._make_client_at_url(url)
        events_api = self._events_api_class(client_at_url)
        try:
            events_api.ingest_events(event=envelope)
            self._ingest_resolver.report_post_outcome(url, success=True)
            return IngestResult(
                event_id=envelope.id,
                transport="sync",
                accepted_at=accepted_at,
            )
        except Exception as exc:
            if _is_terminal_error(exc):
                raise
            self._ingest_resolver.report_post_outcome(url, success=False)
            raise


class _EventsNamespace:
    """Events capability — special-cased ``ingest`` method that emits a
    single envelope carrying BOTH lanes (usage + cost) in one call.

    See docs/prd/2026-06-02-sdk-unified-ingest-methods-prd.md US-004.

    Does NOT extend ``_Namespace`` because there are no backing API
    classes to dispatch to — ``events`` is not in ``CAPABILITY_MAP``.
    This namespace is a focused wrapper over the unified meter endpoint
    (``EventsApi.ingest_events``) that lets a customer with both a
    billable usage dimension AND cost-side per-span breakdown at the
    same call site emit one envelope instead of two siblings.

    Customers reach this via ``client.events.ingest(...)`` — the
    ``Moolabs.events`` property (in ``_dx_client.py``) constructs this
    namespace lazily on first access.

    Single-lane callers can still use this method (passing only meter
    or only spans), but they're typically better served by
    ``client.usage.ingest_event`` or ``client.cost.ingest_event``
    which have stricter signatures (required kwargs make the intent
    clear at the call site).
    """

    def __init__(
        self,
        ingest_resolver: IngestUrlResolver,
        ingest_buffer: Optional[IngestBuffer],
        make_client_at_url: Callable[[str], Any],
        import_api_class: ImportApiClass,
    ) -> None:
        self._ingest_resolver = ingest_resolver
        self._ingest_buffer = ingest_buffer
        self._make_client_at_url = make_client_at_url
        # Same routing target as _UsageNamespace and _CostNamespace —
        # EventsApi against the F2-resolved meter URL.
        self._events_api_class = import_api_class("EventsApi")

    def ingest(
        self,
        *,
        event_type: str,
        customer_id: str,
        entity_id: str,
        meter_slug: Optional[str] = None,
        value: Optional[float] = None,
        spans: Optional[list[dict]] = None,
        # Well-known top-level data.* keys (canonical wire shape).
        provider: Optional[str] = None,
        model: Optional[str] = None,
        total_input_tokens: Optional[int] = None,
        total_output_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        latency_ms: Optional[int] = None,
        status: Optional[str] = None,
        event_id: Optional[str] = None,
        source: Optional[str] = None,
        time: Optional[datetime] = None,
        meta: Optional[dict] = None,
    ) -> IngestResult:
        """Emit a CloudEvent carrying both lanes (if both provided).

        Required kwargs:
          - ``event_type``: CloudEvents ``type``
          - ``customer_id``: end-customer identifier (becomes ``subject``)
          - ``entity_id``: threading key (becomes ``data.request_id``)

        At least ONE of the two lanes MUST be present:
          - Usage lane: BOTH ``meter_slug`` AND ``value`` must be set
          - Cost lane: ``spans`` must be set (a list — empty is allowed)

        If neither lane is complete (both lane-specific groups missing
        or partial), ``ValueError`` is raised synchronously before any
        envelope construction or HTTP work — the customer's call site
        gets immediate feedback.

        ``tenant_id`` is NOT a kwarg (FR-3) — server derives from key.

        Routing: same as ``usage.ingest_event`` and
        ``cost.ingest_event`` — ``EventsApi.ingest_events(event=...)``
        against the F2-resolved meter URL, with buffer + drain when
        a buffer was supplied at Moolabs construction.

        Returns ``IngestResult`` with the (possibly auto-generated)
        ``event_id``, the ``transport`` label, and a tz-aware client
        timestamp.

        Raises ``ValueError`` for:
          - empty-lane envelope (this method's responsibility)
          - any ``_build_envelope`` boundary check failure (empty
            event_type / customer_id / entity_id, non-finite value,
            empty span_id, non-JSON-serializable meta)
        """
        # Empty-envelope guard: at least one lane must be complete.
        # Usage lane is complete when BOTH meter_slug and value are
        # supplied. Cost lane is complete when spans is supplied (a
        # list — an empty list still represents an intentional cost-
        # lane envelope, distinct from omitting the field).
        usage_lane_complete = (meter_slug is not None and value is not None)
        cost_lane_complete = (spans is not None)
        if not usage_lane_complete and not cost_lane_complete:
            raise ValueError(
                "events.ingest requires at least one lane to be present. "
                "Provide meter_slug + value (usage lane), or spans (cost "
                "lane), or both. Got: "
                f"meter_slug={meter_slug!r}, value={value!r}, spans={spans!r}."
            )

        accepted_at = datetime.now(timezone.utc)
        envelope = _build_envelope(
            event_type=event_type,
            customer_id=customer_id,
            entity_id=entity_id,
            meter_slug=meter_slug,
            value=value,
            spans=spans,
            provider=provider,
            model=model,
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_tokens=total_tokens,
            latency_ms=latency_ms,
            status=status,
            event_id=event_id,
            source=source,
            time=time,
            meta=meta,
        )

        if self._ingest_buffer is not None:
            # Direct enqueue — same simplicity tradeoff as _CostNamespace.
            # The producer-channel pattern in _UsageNamespace is a hot-
            # path optimization for high-frequency usage emissions; this
            # method targets the rarer both-lanes-at-once case.
            self._ingest_buffer.enqueue([envelope])
            return IngestResult(
                event_id=envelope.id,
                transport="buffered",
                accepted_at=accepted_at,
            )

        url = self._ingest_resolver.get_ingest_url()
        client_at_url = self._make_client_at_url(url)
        events_api = self._events_api_class(client_at_url)
        try:
            events_api.ingest_events(event=envelope)
            self._ingest_resolver.report_post_outcome(url, success=True)
            return IngestResult(
                event_id=envelope.id,
                transport="sync",
                accepted_at=accepted_at,
            )
        except Exception as exc:
            if _is_terminal_error(exc):
                raise
            self._ingest_resolver.report_post_outcome(url, success=False)
            raise


# ── Factory ───────────────────────────────────────────────────────────────


def make_namespace(
    capability: str,
    get_client: GetClient,
    import_api_class: ImportApiClass,
    *,
    ingest_resolver: Optional[IngestUrlResolver] = None,
    ingest_buffer: Optional[IngestBuffer] = None,
    make_client_at_url: Optional[Callable[[str], Any]] = None,
) -> _Namespace:
    """Return the right namespace subclass for the given capability.

    For ``usage``, returns ``_UsageNamespace`` (requires ``ingest_resolver``
    and ``make_client_at_url`` — buffer is optional but typically provided
    by ``_dx_client.py`` when ``buffer=True``).

    For every other capability, returns ``_Namespace``.
    """
    if capability == "usage":
        if ingest_resolver is None or make_client_at_url is None:
            raise ValueError(
                "usage namespace requires ingest_resolver and make_client_at_url "
                "(needed for the F2 ingest path)"
            )
        return _UsageNamespace(
            get_client=get_client,
            import_api_class=import_api_class,
            ingest_resolver=ingest_resolver,
            ingest_buffer=ingest_buffer,
            make_client_at_url=make_client_at_url,
        )
    if capability == "cost":
        # US-003: cost capability gets ergonomic ingest_event that routes
        # via the unified meter endpoint (EventsApi). Same F2 + G5
        # plumbing as usage; the routing target is meter, not acute.
        if ingest_resolver is None or make_client_at_url is None:
            raise ValueError(
                "cost namespace requires ingest_resolver and make_client_at_url "
                "(needed for the unified-meter F2 ingest path; same as usage)"
            )
        return _CostNamespace(
            get_client=get_client,
            import_api_class=import_api_class,
            ingest_resolver=ingest_resolver,
            ingest_buffer=ingest_buffer,
            make_client_at_url=make_client_at_url,
        )
    return _Namespace(
        capability=capability,
        get_client=get_client,
        import_api_class=import_api_class,
    )
