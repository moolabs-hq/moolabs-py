"""Capability → backing-class routing map for the normalized Moolabs SDK.

This module is the **single source of truth** for which generated API classes
back each customer-facing capability namespace. The DX layer reads it to:

  1. Construct capability namespace objects with the right backing classes.
  2. Derive the per-class backend (bff / meter / arc) so each call goes to
     the right host via the SUBDOMAIN_MAP.
  3. Resolve the regional ingest URL in the F2 fallback chain via the
     REGION_INGEST_MAP.

Adding a new capability or new backing class:
  - Append to ``CAPABILITY_MAP`` with the correct ``BackingClass(name, backend)``.
  - The class name must match an existing module under ``moolabs.api``; the
    routing-map unit test asserts this.
  - For the Go generator, ensure the tag is in ``stitch-specs.py``'s
    ``KNOWN_TAG_RENAMES_{SOURCE}`` if it collides with another source's tag.

Adding a new backend:
  - Register in ``SUBDOMAIN_MAP`` with the subdomain prefix.
  - Update ``stitch-specs.py``'s ``SOURCE_RENAMES`` registry to declare which
    schemas/tags need renaming when stitched after BFF.
  - Per-language ``_dx_routing`` modules must stay in sync (cross-language
    parity check, BE Task H).

This file is mirrored manually across Python / TypeScript / Go DX layers.
The automated cross-language parity job (BE Task H) fails the build on drift.
"""

from __future__ import annotations

from typing import NamedTuple


class BackingClass(NamedTuple):
    """One generated API class backing a capability namespace.

    Attributes:
        api_class: The class name as emitted by openapi-generator-cli's
            Python generator (e.g. ``"EventsApi"``). Must match an actual
            module path ``moolabs.api.<snake_case>_api.<api_class>``.
        backend: Which Moolabs service hosts these endpoints — used to look
            up the host via ``SUBDOMAIN_MAP``. Must be one of the keys in
            that map.
    """

    api_class: str
    backend: str


# ── Backend → subdomain ───────────────────────────────────────────────────
#
# Customer's ``base_url`` is the root domain (default ``"moolabs.com"``).
# Each backend gets a fixed subdomain prefix; the SDK derives the full host
# as ``https://{subdomain}.{base_url}`` per call. Customer code never types
# any of these subdomain strings — the entire point of the normalization.
SUBDOMAIN_MAP: dict[str, str] = {
    "bff":   "api",
    "meter": "meter",
    "arc":   "arc",
    # ACUTE — per sdk-cost-capability-acute-backing US-008 (T-11).
    # Drives the cost capability direct to ``acute.{base_url}`` instead of
    # going through BFF's cost-ingest-proxy router. Customer code never
    # types this string; ``derive_host`` reads SUBDOMAIN_MAP to compose
    # ``https://acute.{base_url}`` per call.
    "acute": "acute",
}


# ── Region → ingest-host subdomain ────────────────────────────────────────
#
# F2 fallback chain (contracts §3.5) step 3: if ``/tenant/config`` discovery
# fails for the event-ingest hot path, the SDK uses this map plus a region
# source (today: hardcoded ``"us"``; future: extracted from the API key) to
# compose ``https://ingest.{region_code}.{base_url}``.
#
# Mirrors BFF's ``REGION_INGEST_MAP`` in
# ``services/moolabs-app/bff/app/api/v1/tenant_config.py``. Drift between
# the two would surface as wrong-region ingest during a BFF outage; the
# values are kept identical by convention. Update both sides together.
REGION_INGEST_MAP: dict[str, str] = {
    "us-east-1":      "us",
    "us-west-2":      "us",
    "ap-southeast-1": "ap",
    "eu-west-1":      "eu",
}

# Fallback region when the SDK has no other signal (no key-derived region
# marker available today; future Task can swap this for key-payload parsing).
DEFAULT_REGION: str = "us-east-1"


# ── Capability → backing classes ──────────────────────────────────────────
#
# The 11 customer-facing capability namespaces frozen by contracts §3.2.
# ``portal`` is intentionally excluded (UI-only per requirements §8 Q-A
# closure 2026-05-15).
#
# Verified zero method-name collisions across all multi-class capabilities
# (O4 / 2026-05-15, enumerated against moolabs-py@main). Sub-accessor
# fallback (BE §3.2 / G4 bend) stays as a documented contingency for Arc
# when its generated classes land — not needed today.
CAPABILITY_MAP: dict[str, list[BackingClass]] = {
    # Event ingest + meter / usage querying.
    # `ingest_events` follows the F2 fallback chain (contracts §3.5) +
    # G5 in-memory buffer; other methods on these classes are plain meter
    # control-plane calls routed to ``meter.{base_url}``.
    "usage": [
        BackingClass("EventsApi", "meter"),
        BackingClass("MetersApi", "meter"),
    ],

    # Billed entities + the subjects (users / teams / instances) those
    # customers own.
    "customers": [
        BackingClass("CustomersApi", "meter"),
        BackingClass("SubjectsApi",  "meter"),
    ],

    # Sellable products — plans, features, addons (Meter) + rate cards (BFF).
    "catalog": [
        BackingClass("ProductCatalogApi", "meter"),
        BackingClass("RateCardsApi",      "bff"),
    ],

    # Subscriptions + addons. Single-class capability (stitcher renamed
    # Meter's ``Subscriptions`` tag to ``MeterSubscriptions`` to keep
    # the Go generator from merging with any future BFF subscriptions class).
    "subscriptions": [
        BackingClass("MeterSubscriptionsApi", "meter"),
    ],

    # Feature-access checks + entitlement grants.
    "entitlements": [
        BackingClass("EntitlementsApi", "meter"),
    ],

    # Prepaid-credit containers — wallet lifecycle, members, thresholds.
    # Pools sub-tag has zero ops in the current BFF spec; if/when populated,
    # add ``BackingClass("PoolsApi", "bff")`` here.
    "wallets": [
        BackingClass("WalletsApi", "bff"),
    ],

    # Credit balance movements — grants, ledger, auto-topup. Topup sub-tag
    # has zero ops in the current BFF spec; if populated, add
    # ``BackingClass("TopupApi", "bff")`` here.
    "credits": [
        BackingClass("GrantsApi",    "bff"),
        BackingClass("LedgerApi",    "bff"),
        BackingClass("AutoTopupApi", "bff"),
    ],

    # Issue invoices + rate raw usage. Meter's ``Billing`` tag is renamed
    # to ``MeterBilling`` at stitch time (Go generator class-merge guard).
    "billing": [
        BackingClass("MeterBillingApi", "meter"),
        BackingClass("RatingApi",       "bff"),
        BackingClass("FxRatesApi",      "bff"),
    ],

    # AR / dunning / collections. Arc backing classes — many because Arc
    # has fine-grained tag groups per resource type. Internal Arc tags
    # (admin, admin-email, admin-escalation-config, batch, governance,
    # health, steering, webhooks) and the renamed ``ArcPortal`` (UI-only,
    # excluded per O3) are intentionally NOT here.
    "collections": [
        BackingClass("AccountsApi",            "arc"),
        BackingClass("AccountTeamApi",         "arc"),
        BackingClass("AnalyticsApi",           "arc"),
        BackingClass("CasesApi",               "arc"),
        BackingClass("CashCreditsApi",         "arc"),
        BackingClass("ArcCommunicationsApi",   "arc"),  # tag renamed by stitcher
        BackingClass("CreditMemosApi",         "arc"),
        BackingClass("DisputesApi",            "arc"),
        BackingClass("EscalationsApi",         "arc"),
        BackingClass("HandoffsApi",            "arc"),
        BackingClass("NotesApi",               "arc"),
        BackingClass("PaymentsApi",            "arc"),
        BackingClass("PlansApi",               "arc"),
        BackingClass("PromisesApi",            "arc"),
        BackingClass("RemittancesApi",         "arc"),
        BackingClass("ReportsApi",             "arc"),
        BackingClass("TasksApi",               "arc"),
    ],

    # AI cost-intelligence ingestion — DIRECT to acute.{base_url}.
    #
    # Per sdk-cost-capability-acute-backing US-008 (T-11), client.cost.*
    # routes to ACUTE's real handlers instead of the BFF cost-ingest-proxy
    # forwarder. The stitcher (US-007) drops BFF's proxy paths when ACUTE
    # is contributing so the unified spec contains ACUTE's operations.
    #
    # Two backing classes:
    #   - CostEventsApi (acute) — POSTs at /api/v1/cost/ingest,
    #     /api/v1/cost/ingest/batch, /api/v1/cost/adjustments. The two
    #     GET endpoints under the same tag are dropped by the stitcher's
    #     EXCLUDE_PATHS_ACUTE so customers only see the 3 in-scope POSTs.
    #   - SdkIngestApi (acute) — POST at /api/v1/ingest/batch (the
    #     SDK-internal span batch ingest endpoint, separate tag because
    #     it's a different protocol shape).
    #
    # The BFF cost-ingest-proxy still SERVES these URLs in production
    # (requirements D8 rev 3 — indefinite dual-path coexistence as
    # fallback), but the customer SDK now talks to ACUTE directly. If
    # the SDK's ACUTE call fails, customer code can still pin to a
    # specific subdomain or use base_url overrides to fall back to BFF.
    "cost": [
        BackingClass("CostEventsApi", "acute"),
        BackingClass("SdkIngestApi",  "acute"),
    ],

    # Notification channels/rules (Meter) + usage alert thresholds (BFF).
    "notifications": [
        BackingClass("NotificationsApi", "meter"),
        BackingClass("AlertsApi",        "bff"),
    ],
}


# Ordered list of capabilities for stable iteration (e.g. cross-language
# parity diffs). The 11 namespaces in the order they appear in
# contracts §3.2 and the customer-facing docs.
CAPABILITY_ORDER: list[str] = [
    "usage",
    "customers",
    "catalog",
    "subscriptions",
    "entitlements",
    "wallets",
    "credits",
    "billing",
    "collections",
    "cost",
    "notifications",
]


# ── Self-consistency invariants (cheap runtime check) ─────────────────────
#
# Run as soon as the module is imported — if a backend referenced by a
# BackingClass is not in SUBDOMAIN_MAP, we fail fast with a clear message
# rather than emit a mysterious AttributeError on a downstream call.
def _validate_routing() -> None:
    valid_backends = set(SUBDOMAIN_MAP.keys())
    cap_set = set(CAPABILITY_MAP.keys())
    order_set = set(CAPABILITY_ORDER)
    if cap_set != order_set:
        missing = cap_set - order_set
        extra = order_set - cap_set
        raise RuntimeError(
            f"CAPABILITY_MAP keys vs CAPABILITY_ORDER drift: "
            f"in_map_not_ordered={sorted(missing)}, "
            f"in_order_not_mapped={sorted(extra)}"
        )
    for capability, classes in CAPABILITY_MAP.items():
        if not classes:
            raise RuntimeError(
                f"capability {capability!r} has no backing classes — every "
                f"namespace must back at least one class"
            )
        for bc in classes:
            if bc.backend not in valid_backends:
                raise RuntimeError(
                    f"capability {capability!r} backing class "
                    f"{bc.api_class!r} declares backend {bc.backend!r} "
                    f"which is not in SUBDOMAIN_MAP (known: "
                    f"{sorted(valid_backends)})"
                )


_validate_routing()
