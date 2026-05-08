"""Webhook signature verification.

Ported from moolabs-app_legacy/sdks/python/moolabs_cls/webhooks.py without
behavior changes. Used by customer integrations that receive Moolabs webhooks
to verify the payload was sent by Moolabs (not a forgery).

Customer code:

    from moolabs._dx_webhooks import WebhookVerifier

    verifier = WebhookVerifier(secret="whsec_xxx")

    # In your HTTP handler:
    raw_body = request.get_data()
    sig = request.headers.get("X-Moolabs-Signature")  # e.g. "sha256=abc123..."
    if not verifier.verify_header(raw_body, sig):
        return 401, "invalid signature"
"""

from __future__ import annotations

import hashlib
import hmac

_HASH_ALGORITHMS = {
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


class WebhookVerifier:
    """Verify HMAC-signed webhook payloads using a shared secret.

    Constant-time comparison to prevent timing attacks.
    """

    def __init__(self, secret: str) -> None:
        if not secret:
            raise ValueError("WebhookVerifier secret cannot be empty")
        self._secret = secret.encode("utf-8")

    def verify(
        self, payload: bytes, signature: str, algorithm: str = "sha256"
    ) -> bool:
        """Verify a payload's signature against the secret.

        Args:
            payload: Raw webhook payload bytes (NOT decoded JSON).
            signature: Hex-encoded signature from the webhook header.
            algorithm: Hash algorithm — one of `sha256` or `sha512`.

        Returns:
            True if the signature is valid; False otherwise.

        Raises:
            ValueError: If `algorithm` is not supported.
        """
        hash_func = _HASH_ALGORITHMS.get(algorithm)
        if hash_func is None:
            raise ValueError(
                f"unsupported algorithm: {algorithm} (expected one of {sorted(_HASH_ALGORITHMS)})"
            )

        expected = hmac.new(self._secret, payload, hash_func).hexdigest()
        return hmac.compare_digest(expected, signature)

    def verify_header(self, payload: bytes, header_value: str) -> bool:
        """Verify a payload using a signature header.

        Header format: ``"sha256=<hex>"`` or just ``"<hex>"`` (sha256 default).

        Args:
            payload: Raw webhook payload bytes.
            header_value: Value of the signature header (e.g. ``X-Moolabs-Signature``).

        Returns:
            True if the signature is valid; False otherwise.
        """
        if "=" in header_value:
            algorithm, signature = header_value.split("=", 1)
            return self.verify(payload, signature, algorithm)
        return self.verify(payload, header_value, "sha256")
