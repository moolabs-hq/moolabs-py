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

from typing import Any, Callable, Optional

from ._dx_buffer import IngestBuffer
from ._dx_routing import CAPABILITY_MAP, BackingClass
from ._dx_urls import IngestUrlResolver


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
        """F2-routed, G5-buffered event ingest.

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
        """
        if not events:
            return self._empty_ingest_response()

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

        try:
            result = events_api.ingest_events(events, **kwargs)
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
    return _Namespace(
        capability=capability,
        get_client=get_client,
        import_api_class=import_api_class,
    )
