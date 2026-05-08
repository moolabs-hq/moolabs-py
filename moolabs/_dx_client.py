"""Unified Moolabs SDK facade — `Moolabs(api_key=..., cls_base_url=..., meter_base_url=...)`.

This file is hand-written DX layer that sits ON TOP of the openapi-generator
output. It is copied into the generated tree by `generate.sh` post-codegen
when the tuple config sets `dx_dir: sdks/dx/python`.

Two top-level namespaces customers see:
  - `client.cls.*`   → routes to api.moolabs.com (BFF, direct)
  - `client.meter.*` → routes to meter.moolabs.com (Meter, direct)

Token: ONE `api_key`, generated in the customer UI, valid against both
backends (each backend validates the same token independently — no
proxying through BFF).

Usage:

    from moolabs import Moolabs

    client = Moolabs(api_key="moo_live_xxx")

    # CLS (BFF-routed) — wallets, grants, ledger, billing, etc.
    wallet = client.cls.wallets.create_wallet(...)
    grants = client.cls.grants.list_grants(...)
    ledger = client.cls.ledger.create_transfer(...)

    # Meter (Meter-routed) — events, meters, entitlements, etc.
    client.meter.events.ingest_events([...])
    meters = client.meter.meters.list_meters()
    sub = client.meter.subscriptions.create_subscription(...)

Customer never sees the BFF / Meter split as separate clients or URLs in
day-to-day code. They just pick which namespace matches the operation
they want.

NOTE on collisions: BFF and Meter both have `portal` and `subscriptions`
tags. The OpenAPI generator emits the *first* one as `portal_api.py` /
`subscriptions_api.py` (currently the Meter side, due to stitch order)
and the *second* with a `0` suffix on the FILENAME — `portal0_api.py`
contains the BFF version. The CLASS names inside both files are the
same (`PortalApi`, `SubscriptionsApi`); routing is determined by which
ApiClient instance we instantiate them with, not by class identity.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    # Avoid runtime imports of the generated layer until first use, so that
    # `import moolabs` is fast and so that test fixtures that mock the
    # generated layer don't need the real classes at import time.
    from moolabs.api_client import ApiClient


# Default base URLs — production hostnames. Customers behind a private
# deployment can override per-instance.
_DEFAULT_CLS_BASE_URL = "https://api.moolabs.com"
_DEFAULT_METER_BASE_URL = "https://meter.moolabs.com"


class Moolabs:
    """Unified Moolabs SDK client.

    Args:
        api_key: Moolabs-issued API key (generated in the customer UI).
            The same key authenticates against both the CLS (BFF) and
            Meter backends; each backend validates it independently.
        cls_base_url: Base URL for CLS / billing operations. Defaults
            to ``https://api.moolabs.com``.
        meter_base_url: Base URL for usage / metering operations.
            Defaults to ``https://meter.moolabs.com``.
    """

    def __init__(
        self,
        api_key: str,
        cls_base_url: str = _DEFAULT_CLS_BASE_URL,
        meter_base_url: str = _DEFAULT_METER_BASE_URL,
    ) -> None:
        if not api_key:
            raise ValueError("Moolabs(api_key=...) is required")

        self._api_key = api_key
        self._cls_base_url = cls_base_url.rstrip("/")
        self._meter_base_url = meter_base_url.rstrip("/")
        self._cls_client: ApiClient | None = None
        self._meter_client: ApiClient | None = None

    def _make_client(self, base_url: str) -> "ApiClient":
        # Local import — see TYPE_CHECKING note above.
        from moolabs.api_client import ApiClient
        from moolabs.configuration import Configuration

        return ApiClient(
            Configuration(host=base_url, access_token=self._api_key)
        )

    def _get_cls_client(self) -> "ApiClient":
        if self._cls_client is None:
            self._cls_client = self._make_client(self._cls_base_url)
        return self._cls_client

    def _get_meter_client(self) -> "ApiClient":
        if self._meter_client is None:
            self._meter_client = self._make_client(self._meter_base_url)
        return self._meter_client

    @property
    def cls(self) -> "_ClsNamespace":
        """All operations that route to the CLS / BFF backend (api.moolabs.com)."""
        return _ClsNamespace(self._get_cls_client())

    @property
    def meter(self) -> "_MeterNamespace":
        """All operations that route to the Meter backend (meter.moolabs.com)."""
        return _MeterNamespace(self._get_meter_client())

    # ── Lifecycle ─────────────────────────────────────────────────────────

    def close(self) -> None:
        """Release any open HTTP connections held by the underlying ApiClients.

        Safe to call multiple times. Subsequent namespace access reconstructs
        clients on demand.
        """
        if self._cls_client is not None:
            self._cls_client.close()
            self._cls_client = None
        if self._meter_client is not None:
            self._meter_client.close()
            self._meter_client = None

    def __enter__(self) -> "Moolabs":
        return self

    def __exit__(self, *_exc_info: object) -> None:
        self.close()


class _ClsNamespace:
    """All operations that route to the CLS / BFF backend (api.moolabs.com).

    Sub-namespaces correspond to the BFF's per-resource OpenAPI tags
    (wallets, grants, ledger, billing, alerts, auto_topup, rate_cards,
    rating, fx_rates, portal, subscriptions, etc.). New tags added to
    BFF will need a new property here.
    """

    def __init__(self, client: "ApiClient") -> None:
        self._client = client

    @property
    def wallets(self) -> Any:
        from moolabs.api.wallets_api import WalletsApi
        return WalletsApi(self._client)

    @property
    def grants(self) -> Any:
        from moolabs.api.grants_api import GrantsApi
        return GrantsApi(self._client)

    @property
    def ledger(self) -> Any:
        from moolabs.api.ledger_api import LedgerApi
        return LedgerApi(self._client)

    @property
    def alerts(self) -> Any:
        from moolabs.api.alerts_api import AlertsApi
        return AlertsApi(self._client)

    @property
    def auto_topup(self) -> Any:
        from moolabs.api.auto_topup_api import AutoTopupApi
        return AutoTopupApi(self._client)

    # NOTE: client.cls.billing is intentionally absent. The BFF spec
    # (`services/moolabs-app/bff/openapi.json`) does not currently emit any
    # operations under the `billing` tag — the router code declares one but
    # the OpenAPI dump shows zero billing-tagged ops. When BFF starts
    # exposing them, add a `billing` property here mirroring `wallets`/etc.
    # For Meter-side billing, use `client.meter.billing`.

    @property
    def rate_cards(self) -> Any:
        from moolabs.api.rate_cards_api import RateCardsApi
        return RateCardsApi(self._client)

    @property
    def rating(self) -> Any:
        from moolabs.api.rating_api import RatingApi
        return RatingApi(self._client)

    @property
    def fx_rates(self) -> Any:
        from moolabs.api.fx_rates_api import FxRatesApi
        return FxRatesApi(self._client)

    @property
    def portal(self) -> Any:
        # BFF portal tokens — `portal` tag (Meter's was renamed to MeterPortal
        # at stitch time, so PortalApi contains only BFF /v1/portal/* paths).
        from moolabs.api.portal_api import PortalApi
        return PortalApi(self._client)

    @property
    def subscriptions(self) -> Any:
        # BFF subscriptions (paths /v1/subscriptions/*). Meter's Subscriptions
        # tag is renamed to MeterSubscriptions at stitch time.
        from moolabs.api.subscriptions_api import SubscriptionsApi
        return SubscriptionsApi(self._client)


class _MeterNamespace:
    """All operations that route to the Meter backend (meter.moolabs.com).

    Sub-namespaces correspond to Meter's per-resource OpenAPI tags
    (events, meters, customers, subscriptions, entitlements, apps,
    portal, product_catalog, subjects, notifications, etc.).
    """

    def __init__(self, client: "ApiClient") -> None:
        self._client = client

    @property
    def events(self) -> Any:
        from moolabs.api.events_api import EventsApi
        return EventsApi(self._client)

    @property
    def meters(self) -> Any:
        from moolabs.api.meters_api import MetersApi
        return MetersApi(self._client)

    @property
    def customers(self) -> Any:
        from moolabs.api.customers_api import CustomersApi
        return CustomersApi(self._client)

    @property
    def subscriptions(self) -> Any:
        # Meter subscriptions tagged MeterSubscriptions (renamed at stitch).
        from moolabs.api.meter_subscriptions_api import MeterSubscriptionsApi
        return MeterSubscriptionsApi(self._client)

    @property
    def billing(self) -> Any:
        # Meter billing tagged MeterBilling (renamed at stitch).
        from moolabs.api.meter_billing_api import MeterBillingApi
        return MeterBillingApi(self._client)

    @property
    def entitlements(self) -> Any:
        from moolabs.api.entitlements_api import EntitlementsApi
        return EntitlementsApi(self._client)

    @property
    def notifications(self) -> Any:
        from moolabs.api.notifications_api import NotificationsApi
        return NotificationsApi(self._client)

    @property
    def apps(self) -> Any:
        from moolabs.api.apps_api import AppsApi
        return AppsApi(self._client)

    @property
    def portal(self) -> Any:
        # Meter portal tokens tagged MeterPortal (renamed at stitch).
        from moolabs.api.meter_portal_api import MeterPortalApi
        return MeterPortalApi(self._client)

    @property
    def product_catalog(self) -> Any:
        from moolabs.api.product_catalog_api import ProductCatalogApi
        return ProductCatalogApi(self._client)

    @property
    def subjects(self) -> Any:
        from moolabs.api.subjects_api import SubjectsApi
        return SubjectsApi(self._client)
