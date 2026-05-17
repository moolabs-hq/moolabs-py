"""G5 in-memory ingest buffer.

Bounded, in-process queue that absorbs event-ingest failures so customer
code does not see exceptions when the F2 fallback chain exhausts. A
background worker periodically retries delivery via a caller-supplied
callback.

Contract: contracts §3.5a.

Properties:
- Memory-only; process crash loses pending events (documented in the
  customer-facing README; opt-out via ``Moolabs(api_key, buffer=False)``).
- Bounded queue (default 1000 events); overflow policy is configurable
  (``drop_oldest`` default; ``raise`` for customers who prefer hard
  backpressure).
- Single background worker per ``IngestBuffer`` instance — no thread pool,
  no contention for high-volume customers (per-instance, not per-process).
- Graceful shutdown: ``close(timeout=...)`` blocks while the worker
  attempts one last drain. ``__enter__`` / ``__exit__`` for context-manager
  use.

Decoupled from HTTP / F2 chain: the buffer takes a ``drain_callback`` that
receives a list of events and returns the count it successfully delivered.
Re-queued events (those the callback couldn't deliver) sit at the front of
the queue for the next drain attempt.
"""

from __future__ import annotations

import atexit
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Any, Callable, Optional


# Overflow policies. Strings (not enums) so the customer-facing API is
# friendly: ``Moolabs(api_key, buffer_overflow="raise")``.
OVERFLOW_DROP_OLDEST = "drop_oldest"
OVERFLOW_RAISE = "raise"
_VALID_OVERFLOW = {OVERFLOW_DROP_OLDEST, OVERFLOW_RAISE}


class IngestBufferFull(Exception):
    """Raised by ``enqueue()`` when ``overflow="raise"`` and the queue is full.

    Customers who want strict backpressure (no silent dropping) can catch
    this and apply their own retry / dead-letter logic.
    """


@dataclass
class IngestBufferConfig:
    """Tunables for ``IngestBuffer``. Defaults optimized for per-customer
    HTTP request rate (3 req/min at 20s flush) over per-event latency.

    Throughput ceiling = ``max_size / flush_interval_sec`` = 50 evt/s;
    customers sustaining >25 evt/s should raise ``max_size`` via
    ``Moolabs(buffer_max=...)`` to keep a 2× safety margin, otherwise
    ``stats()["dropped"]`` will increment continuously under normal
    operation.

    Peak memory: ~500 KB worst case (1000 events × ~500 bytes typical).
    Per-event latency to backend: up to ``flush_interval_sec`` (20s).
    Process-exit hang: up to ``shutdown_flush_timeout_sec`` (60s)
    when the backend is unreachable at close() time."""

    # Max events the queue holds before the overflow policy kicks in.
    max_size: int = 1000

    # Background worker poll interval. The worker sleeps this long between
    # drain attempts; the actual time-to-drain after an outage is at most
    # (flush_interval + drain_callback latency).
    flush_interval_sec: float = 20.0

    # close() blocks at most this long flushing pending events. After the
    # timeout, any remaining events are abandoned (counted in
    # stats()["abandoned_on_shutdown"], optionally logged via the
    # customer-supplied logger).
    shutdown_flush_timeout_sec: float = 60.0

    # What to do when enqueue() is called and the queue is at max_size:
    #   - "drop_oldest": pop the oldest events from the front, append the new
    #     ones. Bumps stats()["dropped"]; optionally logged via the
    #     customer-supplied logger.
    #   - "raise": IngestBufferFull is raised, no events are enqueued.
    overflow: str = OVERFLOW_DROP_OLDEST

    def __post_init__(self) -> None:
        if self.max_size <= 0:
            raise ValueError(f"max_size must be positive, got {self.max_size}")
        if self.flush_interval_sec <= 0:
            raise ValueError(
                f"flush_interval_sec must be positive, got {self.flush_interval_sec}"
            )
        if self.shutdown_flush_timeout_sec < 0:
            raise ValueError(
                f"shutdown_flush_timeout_sec must be non-negative, "
                f"got {self.shutdown_flush_timeout_sec}"
            )
        if self.overflow not in _VALID_OVERFLOW:
            raise ValueError(
                f"overflow must be one of {sorted(_VALID_OVERFLOW)}, "
                f"got {self.overflow!r}"
            )


# A drain_callback takes a list of events and returns the integer count of
# events it successfully delivered (from the front of the list). Returning
# a count less than ``len(events)`` keeps the unsent tail in the queue for
# the next attempt; raising leaves all events queued.
DrainCallback = Callable[[list[Any]], int]


class IngestBuffer:
    """Bounded in-memory queue + background drain worker.

    Usage:
        buffer = IngestBuffer(drain_callback=lambda evs: _try_post_events(evs))
        buffer.start()
        try:
            buffer.enqueue([event1, event2])
            ...
        finally:
            buffer.close()   # blocks up to shutdown_flush_timeout_sec

    Or as context manager (preferred):
        with IngestBuffer(drain_callback=...) as buffer:
            buffer.enqueue([event1, event2])
        # close() called on exit
    """

    def __init__(
        self,
        drain_callback: DrainCallback,
        config: Optional[IngestBufferConfig] = None,
        clock: Callable[[], float] = time.monotonic,
        logger: Optional[Callable[[str, dict], None]] = None,
    ) -> None:
        self._drain = drain_callback
        self._config = config or IngestBufferConfig()
        self._clock = clock
        # Optional per-event diagnostic logger. None = no output (NoopLogger
        # equivalent). When provided, the buffer invokes it on overflow,
        # abandoned-on-shutdown, and drain-failure events.
        self._logger: Callable[[str, dict], None] = logger or (lambda _m, _f: None)

        self._queue: deque[Any] = deque()
        self._lock = threading.Lock()
        self._not_empty = threading.Event()  # set when queue has items
        self._stop = threading.Event()       # signals worker to exit

        self._worker: Optional[threading.Thread] = None

        # Counters for observability + tests. Surface signals via stats()
        # AND optionally via the customer-supplied logger. Customers who
        # want per-event detail provide a logger; those who want only
        # aggregate monitoring poll stats() periodically.
        self._stats = {
            "enqueued": 0,                # events accepted into queue
            "dropped": 0,                 # events dropped on overflow
            "delivered": 0,               # events the drain callback consumed
            "drain_failures": 0,          # drain_callback raised (events stay queued)
            "terminal_drops": 0,          # events dropped: non-retryable upstream status
            "abandoned_on_shutdown": 0,   # events lost: close() timed out before final drain
        }

    # ── Public API ──

    def start(self) -> None:
        """Start the background drain worker. Idempotent.

        Also registers an atexit handler for best-effort final drain on
        process exit, mitigating the silent-event-loss risk of the
        daemon=True thread (without atexit, a customer who forgets
        client.close() loses every queued event when the process exits).
        """
        if self._worker is not None and self._worker.is_alive():
            return
        self._stop.clear()
        self._worker = threading.Thread(
            target=self._worker_loop,
            name="moolabs-ingest-buffer",
            daemon=True,  # don't block process exit if close() is skipped
        )
        self._worker.start()
        # Best-effort final drain at process exit. Idempotent: if the
        # customer DID call close() before exit, this is a no-op (close
        # is itself idempotent and the second call drains an empty queue).
        # We register self.close (bound method); atexit holds a strong
        # ref to it, which transitively pins this IngestBuffer for the
        # process lifetime — accepted: customers who construct one
        # IngestBuffer per Moolabs instance keep that instance alive
        # anyway, so the ref is logically held already.
        atexit.register(self.close)

    def enqueue(self, events: list[Any]) -> None:
        """Add events to the queue. Honors the overflow policy.

        Raises ``IngestBufferFull`` if ``overflow="raise"`` and the queue
        would exceed ``max_size``.

        Note: the customer-supplied logger is called AFTER releasing the
        lock. A logger that takes its own lock (or re-enters the buffer
        via qsize/stats) would otherwise deadlock the worker thread
        (round 3 review).
        """
        if not events:
            return
        overflowed = False
        with self._lock:
            new_size = len(self._queue) + len(events)
            overflow = max(0, new_size - self._config.max_size)
            if overflow:
                if self._config.overflow == OVERFLOW_RAISE:
                    raise IngestBufferFull(
                        f"ingest buffer full at {len(self._queue)} events "
                        f"(max_size={self._config.max_size}); "
                        f"{len(events)} event(s) rejected"
                    )
                # drop_oldest: pop from front to make room
                for _ in range(min(overflow, len(self._queue))):
                    self._queue.popleft()
                    self._stats["dropped"] += 1
                # If the new batch itself is larger than max_size, only the
                # last max_size events fit.
                if len(events) > self._config.max_size:
                    excess = len(events) - self._config.max_size
                    self._stats["dropped"] += excess
                    events = events[excess:]
                overflowed = True
            self._queue.extend(events)
            self._stats["enqueued"] += len(events)
            self._not_empty.set()

        # Logger called OUTSIDE the lock — see function-level comment.
        if overflowed:
            self._logger(
                "moolabs.ingest_buffer.overflow_drop_oldest",
                {"max_size": self._config.max_size},
            )

    def close(self, timeout: Optional[float] = None) -> None:
        """Stop the worker and attempt one final drain. Idempotent.

        If ``timeout`` is None, uses ``shutdown_flush_timeout_sec`` from
        config. After the timeout, any unsent events are abandoned with a
        warning log line.
        """
        if timeout is None:
            timeout = self._config.shutdown_flush_timeout_sec

        # Signal worker to stop after its current sleep cycle, then nudge it
        # with not_empty so it wakes immediately.
        self._stop.set()
        self._not_empty.set()
        if self._worker is not None and self._worker.is_alive():
            self._worker.join(timeout=timeout)

        # Final synchronous drain on whatever thread called close(), bounded
        # by remaining time. Best-effort: a single drain attempt. Failures
        # bump drain_failures (set inside _drain_once); we silently swallow
        # the exception here because stats() / customer-supplied Logger
        # have already captured the failure inside _drain_once.
        try:
            self._drain_once()
        except Exception:  # noqa: BLE001 — counter already bumped in _drain_once
            pass

        leftover = self.qsize()
        if leftover:
            # Counter + per-event log. Logger is noop unless customer
            # provided one; counter is always available via stats().
            with self._lock:
                self._stats["abandoned_on_shutdown"] += leftover
            self._logger(
                "moolabs.ingest_buffer.events_abandoned_on_shutdown",
                {"count": leftover, "timeout_sec": timeout},
            )

    def qsize(self) -> int:
        with self._lock:
            return len(self._queue)

    def record_terminal_drop(self, count: int) -> None:
        """Bump the terminal-drop counter. Called by the SDK's buffer drain
        callback when a non-retryable HTTP status (auth/validation/removed-
        route) was returned for a batch — the events are removed from the
        queue (retrying with the same key/body fails identically), and this
        counter is the SOLE customer-visible signal that data was lost.

        Library does not write to stderr by default. Pass a logger via
        MoolabsOptions.logger to receive the same event as a structured
        log line ('moolabs.ingest_buffer.terminal_drop'); otherwise poll
        stats() periodically and diff to detect a bad API key / removed-
        route scenario."""
        with self._lock:
            self._stats["terminal_drops"] += count

    def stats(self) -> dict[str, int]:
        """Snapshot of counters. Useful for tests + observability.

        Includes silent-failure counters so customers can detect dropped
        events even without an opt-in Logger (the SDK defaults to no
        log output; pass MoolabsOptions.logger to receive the same events
        as structured log lines):
          - terminal_drops: events dropped because the server returned a
            non-retryable status (401/403/400/422/404)
          - abandoned_on_shutdown: events lost because close() timed out
        """
        with self._lock:
            return dict(self._stats)

    # ── Context manager ──

    def __enter__(self) -> "IngestBuffer":
        self.start()
        return self

    def __exit__(self, *_exc: Any) -> None:
        self.close()

    # ── Internal ──

    def _worker_loop(self) -> None:
        """Background drain loop.

        Sleeps ``flush_interval_sec`` between attempts. Wakes early when
        events are enqueued (via ``_not_empty``). On stop, exits without
        another drain — final drain is performed by ``close()``.

        After a FAILED drain we deliberately clear ``_not_empty`` even if
        the queue is still non-empty, so the next iteration sleeps the full
        ``flush_interval_sec`` instead of immediately re-firing. Without
        this, a persistent failure cause (e.g. backend 5xx loop) turns the
        worker into a tight CPU loop hitting the same dead URL hundreds of
        times per second.
        """
        while not self._stop.is_set():
            # Wait up to flush_interval. If queue becomes non-empty earlier,
            # the not_empty event lets us wake up to drain sooner.
            self._not_empty.wait(timeout=self._config.flush_interval_sec)
            if self._stop.is_set():
                return
            drain_failed = False
            try:
                self._drain_once()
            except Exception as e:  # noqa: BLE001
                # Worker must never die. The drain_failures counter is
                # bumped inside _drain_once; we also emit a per-event log
                # (noop unless customer provided one). SDK never writes
                # to stderr by default.
                drain_failed = True
                self._logger(
                    "moolabs.ingest_buffer.drain_iteration_failed",
                    {"error": str(e)},
                )
            finally:
                # Reset the wake signal so the loop sleeps the full
                # flush_interval next iteration. Two cases:
                #   - queue empty: nothing to drain anyway
                #   - drain failed: backoff before retrying the same failure
                # If queue is non-empty AND drain succeeded partially, the
                # successful path will re-set _not_empty via enqueue() OR
                # the next flush tick (already short) will pick it up.
                if drain_failed:
                    self._not_empty.clear()
                else:
                    with self._lock:
                        if not self._queue:
                            self._not_empty.clear()

    def _drain_once(self) -> None:
        """Pop the current queue into an in-flight batch, deliver it, then
        re-enqueue any undelivered tail at the front.

        Pre-2026-05-16 design: snapshot-then-popleft-after. That had a race
        where concurrent `enqueue()` with `drop_oldest` could pop events from
        the queue front during the drain, then post-drain `popleft(delivered)`
        would remove newly-enqueued events instead of the snapshot's. Silent
        data loss.

        New design: pop everything under the lock BEFORE the drain (events
        are now "in flight" and invisible to overflow logic), call the
        drain callback, then under lock re-enqueue the undelivered tail at
        the FRONT (preserving order). Failed delivery → all events re-front.
        Concurrent enqueue during drain sees an empty (or smaller) queue,
        so `drop_oldest` can't touch in-flight events.

        Side effect: re-enqueueing at the front may briefly exceed max_size
        if concurrent enqueue filled the queue while the drain was in flight.
        Accepted: the next enqueue's overflow check fires and the now-oldest
        (which is the post-drain tail) is the first to be dropped — the
        same semantics as if the failed delivery had never happened.
        """
        with self._lock:
            if not self._queue:
                return
            # Pop ALL events into the in-flight batch under the lock.
            batch = list(self._queue)
            self._queue.clear()

        # Call out without holding the lock (HTTP can be slow).
        delivered = 0
        drain_exc: Optional[BaseException] = None
        try:
            delivered = self._drain(batch)
        except Exception as exc:  # noqa: BLE001 — re-raised after re-enqueue
            drain_exc = exc

        # Clamp + decide what to re-enqueue.
        delivered = max(0, min(delivered, len(batch)))
        undelivered = batch[delivered:]
        with self._lock:
            # Re-enqueue undelivered tail at the FRONT (preserving order).
            # extendleft reverses input, so reverse first to keep order.
            if undelivered:
                self._queue.extendleft(reversed(undelivered))
            if drain_exc is not None:
                self._stats["drain_failures"] += 1
            if delivered:
                self._stats["delivered"] += delivered

        if drain_exc is not None:
            # Bubble up to worker_loop preserving original exception context.
            # Events are already safely re-fronted before we raise.
            raise drain_exc

