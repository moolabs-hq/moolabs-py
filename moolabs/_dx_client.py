"""Unified Moolabs SDK facade — capability-based public surface.

Customer entry point:

    from moolabs import Moolabs

    client = Moolabs(api_key="moo_live_xxx")  # default base_url = "moolabs.com"

    # 11 capability namespaces — convention-based subdomain derivation per call
    client.usage.list_events()
    client.billing.list_invoices()
    client.collections.list_cases()
    client.usage.ingest_events([...])    # F2 fallback chain + G5 buffer

    # Self-hosted / staging override
    other = Moolabs(api_key="...", base_url="moolabs.example.com")

    # Strict-sync mode (raise on F2 chain exhaustion instead of buffering)
    sync = Moolabs(api_key="...", buffer=False)

This file is the post-2026-05-15 rewrite (BE Task E.3) that replaces the
prior ``client.cls.*`` / ``client.meter.*`` namespaces with capability
namespaces (contracts §3.2). Key shape changes from rc7:

  - ``base_url`` is now the **root domain** (not a service URL)
  - ``cls_base_url`` / ``meter_base_url`` REMOVED — convention-based subdomain
    derivation in the SDK (contracts §3.3)
  - 11 capability namespaces replace the 2 service namespaces
  - New: ``buffer`` and ``buffer_max`` constructor params (G5 — contracts §3.5a)
  - F2 fallback chain on ``usage.ingest_events()`` (contracts §3.5)
  - All non-ingest capability calls go straight to ``{subdomain}.{base_url}``
    — no /tenant/config round-trip
  - ``CapabilityUnavailableError`` was considered, but the rev-2 pivot to
    convention-based routing means an unreachable backend just surfaces as
    ``RetryableError`` from the actual HTTP attempt. Error hierarchy unchanged.
"""

from __future__ import annotations

import importlib
import re
from typing import TYPE_CHECKING, Any, Callable, Optional

# LoggerFn is the optional per-event diagnostic callback. Customer passes
# this to Moolabs(... logger=...); the SDK invokes it on terminal_drop,
# overflow, abandoned-on-shutdown, etc. with a stable msg id + a structured
# fields dict. Default is _noop_logger (no output).
#
# Why a callable, not a class: Python idiom; matches how customers wire
# `logging.getLogger("myapp").warning` or a structlog binder. No interface
# definition required.
LoggerFn = Callable[[str, dict], None]


def _noop_logger(_msg: str, _fields: dict) -> None:
    """Default logger — discards every call. Library never writes to stderr
    unless the customer explicitly passes a logger to Moolabs(...).
    """

from ._dx_buffer import IngestBuffer, IngestBufferConfig
from ._dx_namespaces import _Namespace, make_namespace
from ._dx_routing import CAPABILITY_ORDER, SUBDOMAIN_MAP
from ._dx_urls import (
    IngestResolverConfig,
    IngestUrlResolver,
    derive_host,
    resolve_effective_base_url,
)

if TYPE_CHECKING:
    # Avoid runtime imports of the generated layer until first use, so
    # `import moolabs` is fast and so that test fixtures don't need the
    # real classes at import time.
    from moolabs.api_client import ApiClient  # noqa: F401


# Bundled default — non-US customers should override via base_url. Future
# direction (per requirements §C2): derive region from API key payload,
# fall back to this hostname.
_DEFAULT_BASE_URL = "moolabs.com"


def _pascal_to_snake(name: str) -> str:
    """Convert ``"MeterBillingApi"`` → ``"meter_billing_api"``.

    Used to map a capability map's class-name string to the actual module
    file the openapi-generator emits. The Python generator names files
    by the snake_case form of the tag name plus ``_api``.
    """
    s = re.sub(r"(?<!^)(?=[A-Z])", "_", name)
    return s.lower()


def _import_api_class(class_name: str) -> type:
    """Resolve ``"WalletsApi"`` to the actual class in ``moolabs.api.wallets_api``.

    Raises ``ImportError`` with a clear message if the module or class is
    missing — typically means the routing map (BE §3.2) references a class
    the current generated tree doesn't have. The routing-map unit test
    in tests/test_dx_routing.py catches most drift; this guard is the
    runtime backstop.
    """
    module_name = f"moolabs.api.{_pascal_to_snake(class_name)}"
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        raise ImportError(
            f"could not import {module_name} (backing class {class_name!r} for "
            "the SDK's capability routing map). Re-run codegen or check "
            "_dx_routing.CAPABILITY_MAP."
        ) from e
    try:
        return getattr(module, class_name)
    except AttributeError as e:
        raise ImportError(
            f"module {module_name} exists but doesn't define class {class_name!r}. "
            "Re-run codegen or check _dx_routing.CAPABILITY_MAP."
        ) from e


class Moolabs:
    """Unified capability-organized Moolabs SDK client.

    Args:
        api_key: Moolabs-issued API key from the dashboard (Access and
            Security → API keys). Validates against every Moolabs backend
            via the shared key store (C1 / Shape A, 2026-05-09).
        base_url: Root domain (host only). Defaults to ``"moolabs.com"``.
            Self-hosted customers pass their own root (e.g.
            ``"moolabs.example.com"``); the SDK derives api./meter./arc.
            subdomains internally.
        buffer: When True (default), event-ingest failures (F2 chain
            exhaustion) enqueue events to an in-memory buffer rather than
            raising. The background worker retries delivery via the F2 chain.
            Pass ``False`` for strict-sync semantics — failures raise
            ``RetryableError`` directly.
        buffer_max: Maximum events the in-memory buffer holds before the
            drop-oldest overflow policy kicks in. Default 10,000.

    No I/O at construction. Per-backend HTTP clients are constructed
    lazily on first capability access; the ingest buffer's worker thread
    is started lazily on the first ``usage.ingest_events()`` call.
    """

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        buffer: bool = True,
        buffer_max: int = 1000,
        logger: Optional[LoggerFn] = None,
        enable_ingest_discovery: bool = False,
    ) -> None:
        """Construct a Moolabs client.

        Args:
            api_key: Customer API key minted in the moolabs dashboard.
                This is the only identity input — the SDK never asks the
                customer to provide a separate tenant_id / namespace /
                org_id. Each backend resolves the tenant from this key
                via the shared `billing.api_keys` table (Shape A) and
                injects the relevant context server-side. If a backend
                fails to derive the tenant from a valid key, the bug is
                server-side, not SDK-side — the SDK intentionally does
                NOT compensate by sending OM-Namespace etc.
            base_url: Apex or env-rooted host. Defaults to ``moolabs.com``.
            buffer: When True (default) usage.ingest_events buffers and
                flushes in a background thread. When False, ingest calls
                are synchronous.
            buffer_max: Max events held in the buffer before backpressure
                kicks in.
            logger: Optional per-event diagnostic callback.
            enable_ingest_discovery: When True, ``usage.ingest_events``
                preflights ``GET /v1/tenant/config`` on the BFF to
                discover the regional ingest URL. **Default is False**
                because (a) the simple ``base_url`` case can route
                directly via the region/last-resort fallback without a
                preflight round-trip, and (b) BFF currently rejects
                customer-key Bearer auth (a separate gap), causing
                discovery to throw — even though the F2 resolver IS
                designed to fall through to the region fallback on
                discovery failure, the failure exception class isn't
                always caught and bubbles up as a ValidationError that
                aborts the ingest call. Multi-region or shard-aware
                deployments that need tenant-specific ingest routing
                can opt in via this flag.
        """
        if not api_key or not isinstance(api_key, str):
            raise ValueError("api_key must be a non-empty string")
        self._api_key = api_key
        # Apex (``moolabs.com``) is a marketing/branding host, not an env
        # root — the ALB cert is ``*.prod.moolabs.com`` only. Rewrite the
        # customer-supplied base_url ONCE at construction so all downstream
        # subdomain composition (derive_host, IngestUrlResolver) sees the
        # effective env-rooted host. Explicit env roots and self-hosted
        # bases pass through unchanged. See _dx_urls.resolve_effective_base_url.
        self._base_url = resolve_effective_base_url(
            base_url or _DEFAULT_BASE_URL, self._api_key
        )
        # Optional per-event diagnostic logger. NONE = no output. When
        # provided, the SDK invokes it on terminal_drop / overflow /
        # abandoned-on-shutdown / drain-failure events with a stable msg
        # id and a structured fields dict — wire it to
        # logging.getLogger("yourapp").warning, structlog, etc.
        self._logger: LoggerFn = logger or _noop_logger

        # Validate base_url early so a typo crashes at construction, not on
        # first capability call.
        for backend in SUBDOMAIN_MAP:
            # derive_host raises ValueError on malformed base_url; we don't
            # use the result, just exercise the validator.
            derive_host(backend, self._base_url)

        # F2 ingest resolver. The discovery step (`GET /v1/tenant/config`
        # on BFF) is OPT-IN — by default the resolver short-circuits to
        # the region/last-resort fallback URL without a preflight HTTP
        # call. See `enable_ingest_discovery` in the constructor docstring
        # for the rationale; the resolver itself handles
        # `discovery_fn=None` by skipping step 2 of the F2 chain.
        self._ingest_resolver = IngestUrlResolver(
            base_url=self._base_url,
            discovery_fn=(
                self._discover_tenant_config if enable_ingest_discovery else None
            ),
            config=IngestResolverConfig(),
        )

        # G5 buffer. Lazy worker start happens in _ingest_buffer property
        # the first time it's accessed.
        self._buffer_enabled = bool(buffer)
        self._buffer_max = buffer_max
        self._ingest_buffer: Optional[IngestBuffer] = None

        # Per-backend ApiClient cache. Lazy construction in _get_client.
        self._clients: dict[str, Any] = {}

        # Per-capability namespace cache. Lazy construction in capability
        # property accessors.
        self._namespaces: dict[str, _Namespace] = {}

    # ── Public capability properties ────────────────────────────────────

    # Eleven capability namespaces (contracts §3.2). Each lazily constructs
    # its namespace + backing API client instances on first access. The
    # property pattern preserves IDE autocomplete; the actual method
    # dispatch is in _Namespace.__getattr__.

    @property
    def usage(self) -> "_Namespace":
        return self._ns("usage")

    @property
    def customers(self) -> "_Namespace":
        return self._ns("customers")

    @property
    def catalog(self) -> "_Namespace":
        return self._ns("catalog")

    @property
    def subscriptions(self) -> "_Namespace":
        return self._ns("subscriptions")

    @property
    def entitlements(self) -> "_Namespace":
        return self._ns("entitlements")

    @property
    def wallets(self) -> "_Namespace":
        return self._ns("wallets")

    @property
    def credits(self) -> "_Namespace":
        return self._ns("credits")

    @property
    def billing(self) -> "_Namespace":
        return self._ns("billing")

    @property
    def collections(self) -> "_Namespace":
        return self._ns("collections")

    @property
    def cost(self) -> "_Namespace":
        return self._ns("cost")

    @property
    def notifications(self) -> "_Namespace":
        return self._ns("notifications")

    # ── Lifecycle ────────────────────────────────────────────────────────

    def close(self) -> None:
        """Release HTTP clients + drain the ingest buffer (graceful).

        Safe to call multiple times. After close(), subsequent capability
        access reconstructs the per-backend clients on demand — but the
        buffer is closed and cannot be re-started; new ingest calls will
        raise on F2 exhaustion.
        """
        # Stop the producer thread first (if usage namespace exists) so
        # it drains pending queue events into the buffer before the buffer
        # closes. Look it up by capability name to avoid coupling to the
        # lazy-namespace dict's internal state.
        usage_ns = self._namespaces.get("usage")
        if usage_ns is not None:
            try:
                usage_ns._stop_producer(timeout=2.0)
            except Exception:  # noqa: BLE001
                pass

        # Drain the ingest buffer (synchronously blocks up to
        # shutdown_flush_timeout_sec from IngestBufferConfig).
        if self._ingest_buffer is not None:
            self._ingest_buffer.close()

        # Release each backend's ApiClient. The generated ApiClient has
        # a .close() in current openapi-generator-python output but it's
        # idempotent if absent.
        for client in self._clients.values():
            try:
                client.close()
            except (AttributeError, Exception):  # noqa: BLE001
                pass
        self._clients.clear()
        self._namespaces.clear()

    def __enter__(self) -> "Moolabs":
        return self

    def __exit__(self, *_exc_info: object) -> None:
        self.close()

    # ── Internals ────────────────────────────────────────────────────────

    def _ns(self, capability: str) -> "_Namespace":
        """Lazy namespace construction. Cached per capability for the
        instance's lifetime so re-accessing ``client.billing`` doesn't
        rebuild the method index every time."""
        cached = self._namespaces.get(capability)
        if cached is not None:
            return cached

        kwargs: dict[str, Any] = {}
        if capability == "usage":
            # Wire F2 + G5 hooks
            kwargs["ingest_resolver"] = self._ingest_resolver
            kwargs["ingest_buffer"] = self._lazy_ingest_buffer()
            kwargs["make_client_at_url"] = self._make_client_at_url

        ns = make_namespace(
            capability=capability,
            get_client=self._get_client,
            import_api_class=_import_api_class,
            **kwargs,
        )
        self._namespaces[capability] = ns
        return ns

    def _get_client(self, backend: str) -> Any:
        """Per-backend ApiClient — lazy + cached. Each backend gets one
        client pointed at the convention-derived host (``api.{base}``,
        ``meter.{base}``, ``arc.{base}``)."""
        if backend in self._clients:
            return self._clients[backend]
        host = derive_host(backend, self._base_url)
        client = self._make_client_at_url(host)
        self._clients[backend] = client
        return client

    def _make_client_at_url(self, host: str) -> Any:
        """Create a fresh ApiClient against ``host`` with this instance's
        API key. Used both for the per-backend cached clients AND for the
        F2 ingest path's per-call resolved client.

        The SDK sends ONLY the api_key (via Authorization: Bearer on
        Configuration.access_token). The server resolves tenant identity
        from the key — the SDK never sends OM-Namespace or any other
        tenant-discriminating header. If a backend fails to derive
        tenant from a valid key, the fix is server-side.
        """
        # Import the generated layer lazily so `import moolabs` is fast.
        from moolabs.api_client import ApiClient
        from moolabs.configuration import Configuration

        return ApiClient(
            Configuration(host=host, access_token=self._api_key)
        )

    def _lazy_ingest_buffer(self) -> Optional[IngestBuffer]:
        """Construct and start the G5 buffer on first request; return None
        if buffering is disabled."""
        if not self._buffer_enabled:
            return None
        if self._ingest_buffer is None:
            self._ingest_buffer = IngestBuffer(
                drain_callback=self._buffer_drain_callback,
                config=IngestBufferConfig(max_size=self._buffer_max),
                logger=self._logger,   # propagate (noop if customer didn't supply one)
            )
            self._ingest_buffer.start()
        return self._ingest_buffer

    def _buffer_drain_callback(self, events: list[Any]) -> int:
        """Worker-thread callback: try to deliver buffered events via the
        F2 chain. Returns the count successfully delivered (events leave
        the queue from the front).

        Terminal failures (auth 401/403, validation 400/422, removed-route
        404) DISCARD the batch — retrying with the same key/body fails
        identically; keeping these in the buffer forever is the silent-
        data-loss bug. Logs at WARN so the operator sees the drop.
        """
        url = self._ingest_resolver.get_ingest_url()
        try:
            client = self._make_client_at_url(url)
            EventsApi = _import_api_class("EventsApi")
            EventsApi(client).ingest_events(events)
            self._ingest_resolver.report_post_outcome(url, success=True)
            return len(events)
        except Exception as exc:
            # Lazy import to avoid namespace cycle at module load
            from ._dx_namespaces import _is_terminal_error
            if _is_terminal_error(exc):
                # Drop the batch — retry will fail identically. Bump the
                # terminal-drop counter (always; cheap, polling-friendly)
                # AND emit a per-event log (only if customer provided
                # a logger). Counter alone tells you HOW MUCH; logger
                # gives you WHICH status + WHICH error per event.
                if self._ingest_buffer is not None:
                    self._ingest_buffer.record_terminal_drop(len(events))
                self._logger(
                    "moolabs.ingest_buffer.terminal_drop",
                    {
                        "status": getattr(exc, "status", None),
                        "count": len(events),
                        "error": str(exc),
                    },
                )
                return len(events)
            self._ingest_resolver.report_post_outcome(url, success=False)
            return 0   # transient; events stay queued for next tick

    def _discover_tenant_config(self) -> dict:
        """Call ``GET /tenant/config`` on the BFF for the F2 resolver.

        Returns the parsed dict. Raises on any HTTP / parse failure — the
        IngestUrlResolver catches the exception and applies its discovery-
        retry TTL.
        """
        # Lazy import — we may never call this if the customer doesn't ingest.
        from moolabs.api_client import ApiClient
        from moolabs.configuration import Configuration

        host = derive_host("bff", self._base_url)
        cfg = Configuration(host=host, access_token=self._api_key)
        client = ApiClient(cfg)
        try:
            # The generated TenantConfigApi (or similar) class exposes the
            # GET /tenant/config endpoint after the BFF spec refresh from
            # Task A.2 lands in the regenerated SDK. Fall back to raw HTTP
            # if the class isn't present yet.
            try:
                TenantConfigApi = _import_api_class("TenantConfigApi")
                resp = TenantConfigApi(client).get_tenant_config()
                # The generated method returns a model instance — convert to dict.
                if hasattr(resp, "to_dict"):
                    return resp.to_dict()
                if isinstance(resp, dict):
                    return resp
            except ImportError:
                # TenantConfigApi not yet generated — fall back to raw HTTP via
                # the underlying urllib3 pool the ApiClient holds.
                pass

            # Raw fallback. ApiClient.call_api is the generated client's HTTP
            # entry point; signatures vary across generator versions, so we
            # bail to a low-level rest call if needed.
            return self._raw_get_tenant_config(host)
        finally:
            try:
                client.close()
            except Exception:  # noqa: BLE001
                pass

    def _raw_get_tenant_config(self, host: str) -> dict:
        """Fallback raw HTTP call for /tenant/config when no generated
        class is available. Returns the parsed JSON dict."""
        # Use urllib3 / Python stdlib so we don't add a hard requests/httpx
        # dependency on the SDK.
        import json
        from urllib.request import Request, urlopen

        req = Request(
            url=f"{host}/v1/tenant/config",
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "Accept": "application/json",
            },
        )
        with urlopen(req, timeout=10) as resp:  # noqa: S310 (URL is internal)
            data = resp.read()
        return json.loads(data.decode("utf-8"))

    # ── Introspection ────────────────────────────────────────────────────

    def __repr__(self) -> str:
        return (
            f"<Moolabs(base_url={self._base_url!r}, "
            f"buffer={self._buffer_enabled}, "
            f"capabilities={len(CAPABILITY_ORDER)})>"
        )
