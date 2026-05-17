"""Page<T> pagination iterator — C-SDK-3 / contracts §3.4.

The customer-facing contract for list methods:

  - The return value IS a page (``Page[Invoice]``, ``Page[Event]``, ...).
  - ``page.items`` is the current page only (no auto-fetch).
  - ``page.next_cursor`` is opaque; ``None`` means no more pages.
  - ``page.total`` is the total across all pages if the API provides it, else ``None``.
  - Iterating over the page (``for item in page``) yields items across ALL
    pages, lazily, with one HTTP call per page fetch.

This module provides the ``Page`` class. Wiring it onto specific generator-
emitted list methods is the DX layer's job (Task E.2 / E.3); the Page class
itself is generic over the item type and the fetch mechanism.

Design notes:
  - The Page is constructed with both the current page's data AND a
    ``fetch_next`` callable that returns the next Page (or ``None``).
    Calling ``fetch_next`` releases a reference to ``self`` so old pages
    can be GC'd as iteration advances — important for long lists.
  - Iteration that errors mid-stream raises the mapped Moolabs exception
    and stops. Items already yielded remain consumed.
  - The iterator is not re-entrant: ``iter(page)`` returns a fresh iterator
    each time, but the underlying ``fetch_next`` callable is single-use.
    Customers who want to re-iterate should call the list method again.
"""

from __future__ import annotations

from typing import Callable, Generic, Iterator, Optional, TypeVar

T = TypeVar("T")

# Type alias for the fetch callable. Returns the next Page in the sequence,
# or None when there are no more pages. Called at most once.
FetchNext = Callable[[], Optional["Page[T]"]]  # type: ignore[misc]


class Page(Generic[T]):
    """One page of items plus a lazy iterator across all subsequent pages.

    Attributes:
        items: The items on THIS page only. ``list[T]``.
        next_cursor: Opaque cursor for the next page; ``None`` if last page.
        total: Total items across all pages if the API returned it, else None.

    Iteration behaviour:
        >>> for item in page:           # yields items across all pages
        ...     ...
        >>> page.items                   # current page items only
        >>> page.next_cursor             # for manual paging
    """

    __slots__ = ("items", "next_cursor", "total", "_fetch_next", "_fetched")

    def __init__(
        self,
        items: list[T],
        next_cursor: Optional[str] = None,
        total: Optional[int] = None,
        fetch_next: Optional[FetchNext] = None,
    ) -> None:
        self.items: list[T] = list(items)
        self.next_cursor: Optional[str] = next_cursor
        self.total: Optional[int] = total
        self._fetch_next: Optional[FetchNext] = fetch_next
        self._fetched: bool = False

    # ── Pythonic protocols ──

    def __len__(self) -> int:
        """``len(page)`` == ``len(page.items)`` (current page only).

        NOT the total across all pages — use ``page.total`` for that, or
        fully iterate and count. This avoids accidentally triggering a
        full fetch via ``if len(page) > 0``-style idioms.
        """
        return len(self.items)

    def __iter__(self) -> Iterator[T]:
        """Iterate items across all pages, fetching subsequent pages lazily.

        Yields items from the current page first, then calls ``fetch_next``
        (if set and next_cursor is non-None) and yields from the next page,
        recursively until ``next_cursor is None`` OR ``fetch_next`` returns
        None OR no fetch_next was provided.

        An exception from ``fetch_next`` propagates out of iteration after
        the items from the current page have been yielded.
        """
        # Yield this page's items first
        for item in self.items:
            yield item

        # Advance through subsequent pages
        current = self
        while True:
            if current.next_cursor is None:
                return
            if current._fetch_next is None:
                # No way to fetch more — treat as end of stream
                return
            if current._fetched:
                # Single-use fetch_next; bail if already called (defensive)
                return
            current._fetched = True
            next_page = current._fetch_next()
            current._fetch_next = None  # release reference for GC
            if next_page is None:
                return
            for item in next_page.items:
                yield item
            current = next_page

    def __repr__(self) -> str:
        return (
            f"Page(items=<{len(self.items)}>, "
            f"next_cursor={self.next_cursor!r}, total={self.total!r})"
        )

    def __bool__(self) -> bool:
        """Truthiness == "has items on the current page". Matches ``__len__``
        semantics; never triggers a fetch."""
        return bool(self.items)

    # ── Factory for tests / wiring layer ──

    @classmethod
    def empty(cls) -> "Page[T]":
        """A terminal empty page. Useful for "no results" responses."""
        return cls(items=[], next_cursor=None, total=0, fetch_next=None)
