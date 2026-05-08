"""Moolabs SDK exception hierarchy.

Ported from moolabs-app_legacy/sdks/python/moolabs_cls/exceptions.py and
rewired for the unified `moolabs` package. Renamed `CLS*` → `Moolabs*` to
match the unified customer-facing brand.

The wrapper layer (see _dx_client.py) maps openapi-generator's
`ApiException` to these types based on HTTP status. Application code can
catch the specific subclass it cares about without inspecting status codes
manually:

    from moolabs import Moolabs, AuthenticationError, RateLimitError

    client = Moolabs(api_key="...")
    try:
        client.billing.list_invoices()
    except AuthenticationError:
        ...  # 401
    except RateLimitError as e:
        time.sleep(e.retry_after or 5)
        ...
"""

from __future__ import annotations


class MoolabsError(Exception):
    """Base exception for all Moolabs SDK errors."""


class MoolabsAPIError(MoolabsError):
    """Error returned by the Moolabs API."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_body: dict | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class AuthenticationError(MoolabsAPIError):
    """Authentication failed (401)."""


class AuthorizationError(MoolabsAPIError):
    """Authorization denied for an authenticated request (403)."""


class NotFoundError(MoolabsAPIError):
    """Resource not found (404)."""


class ValidationError(MoolabsAPIError):
    """Request validation failed (400/422)."""

    def __init__(
        self,
        message: str,
        errors: dict | None = None,
        **kwargs: object,
    ) -> None:
        super().__init__(message, **kwargs)
        self.errors = errors or {}


class RateLimitError(MoolabsAPIError):
    """Rate limit exceeded (429)."""

    def __init__(
        self,
        message: str,
        retry_after: int | None = None,
        **kwargs: object,
    ) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class RetryableError(MoolabsAPIError):
    """Transient error that may succeed on retry (5xx, network errors)."""
