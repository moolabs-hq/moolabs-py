# Moolabs Python SDK

Unified Python SDK for the Moolabs platform. One package, one client, one auth flow — covers both billing (CLS) and usage (Meter) operations.

```python
from moolabs import Moolabs

client = Moolabs(api_key="moo_live_...")

# Billing / wallets / grants — routed to api.moolabs.com (CLS)
wallet = client.cls.wallets.create_wallet(...)
grants = client.cls.grants.list_grants(...)

# Usage events / meters / subscriptions — routed to meter.moolabs.com
client.meter.events.ingest_events([...])
meters = client.meter.meters.list_meters()
```

## Install

```bash
pip install moolabs
```

Requires Python 3.8+.

## Authentication

Generate an API key in your Moolabs dashboard. The same key authenticates against both backends; the SDK handles routing internally.

```python
from moolabs import Moolabs

client = Moolabs(api_key="moo_live_...")
```

For staging or private deployments, override the base URLs:

```python
client = Moolabs(
    api_key="moo_test_...",
    cls_base_url="https://staging-api.moolabs.com",
    meter_base_url="https://staging-meter.moolabs.com",
)
```

## Two namespaces

The SDK exposes exactly two top-level namespaces. Pick whichever matches the operation you want.

### `client.cls.*` — CLS / billing operations

Routes all calls to `https://api.moolabs.com`. Sub-namespaces correspond to per-resource API groups:

| Namespace | Purpose |
|---|---|
| `client.cls.wallets` | Wallet lifecycle, balances, transfers |
| `client.cls.grants` | Credit grants and grant policies |
| `client.cls.ledger` | Ledger entries, transfers, audit |
| `client.cls.alerts` | Balance / threshold alert subscriptions |
| `client.cls.auto_topup` | Auto-topup rules |
| `client.cls.rate_cards` | Rate card definitions |
| `client.cls.rating` | Rate-event scoring |
| `client.cls.fx_rates` | FX rate lookups for multi-currency |
| `client.cls.portal` | Portal token issuance (BFF flavor) |
| `client.cls.subscriptions` | Subscription bindings (BFF flavor) |

### `client.meter.*` — Usage / metering operations

Routes all calls to `https://meter.moolabs.com`. Sub-namespaces:

| Namespace | Purpose |
|---|---|
| `client.meter.events` | Ingest usage events |
| `client.meter.meters` | Define and query meters |
| `client.meter.customers` | Customer entity management |
| `client.meter.subscriptions` | Meter-side subscriptions |
| `client.meter.billing` | Meter-side billing primitives |
| `client.meter.entitlements` | Entitlement checks |
| `client.meter.notifications` | Webhook + notification channels |
| `client.meter.apps` | App registrations |
| `client.meter.portal` | Portal tokens (Meter flavor) |
| `client.meter.product_catalog` | Product catalog |
| `client.meter.subjects` | Subjects (e.g., users, accounts) |

## Quickstart — typical usage flows

### Ingest usage events

```python
client.meter.events.ingest_events([
    {
        "id": "evt_unique_id",
        "type": "api.request",
        "subject": "user_42",
        "time": "2026-01-15T10:30:00Z",
        "data": {"endpoint": "/v1/predict", "tokens": 1500},
    }
])
```

### Unified ergonomic ingest (recommended)

The unified surface added in PR #439 lets you emit events with named
kwargs instead of hand-rolling CloudEvent envelopes. The SDK builds the
envelope, validates required fields synchronously (FR-6), and routes
through the same buffer + retry path. Three methods cover the three
shapes of event the platform accepts:

```python
# Usage-lane event — meter_slug + value required.
client.usage.ingest_event(
    event_type="ai.chat",
    customer_id="cust_42",
    entity_id="req_abc",           # threads to data.request_id on the wire
    meter_slug="llm_tokens",
    value=724,
    source="my-app/v2.3.1",        # optional; defaults to "moolabs-sdk"
    meta={"feature": "ai_chat"},   # optional; lands at data.meta nested
)

# Cost-lane event — per-span breakdown for AI cost intelligence.
client.cost.ingest_event(
    event_type="ai.chat.cost",
    customer_id="cust_42",
    entity_id="req_abc",           # same entity_id correlates the two
    spans=[
        {"span_id": "sp_chat", "model": "gpt-4o-mini", "tokens": 724,
         "cost": 0.000724},
    ],
)

# Dual-lane event — usage + cost emitted in one call.
client.events.ingest(
    event_type="ai.chat",
    customer_id="cust_42",
    entity_id="req_abc",
    meter_slug="llm_tokens",
    value=844,
    spans=[{"span_id": "sp_embed", "model": "text-embedding-3-small",
            "tokens": 120, "cost": 0.00000018}],
)
```

Each returns an `IngestResult` with `event_id`, `transport` (`"buffered"`
when the G5 buffer enqueued the call non-blocking, `"sync"` when strict-
sync mode posted inline), and a client-side `accepted_at` timestamp.

`tenant_id` is intentionally NOT a kwarg — the server derives tenant
identity from the API key.

#### Canonical well-known data fields

These seven AI-event fields are first-class kwargs and land at
`data.<key>` directly on the wire (snake_case). Use them — don't bury
them in `meta=`. Free-form fields keep going through `meta=` and nest
at `data.meta.<key>`.

| kwarg | wire | example |
|---|---|---|
| `provider` | `data.provider` | `"openai"` |
| `model` | `data.model` | `"gpt-4o"` |
| `total_input_tokens` | `data.total_input_tokens` | `1250` |
| `total_output_tokens` | `data.total_output_tokens` | `3800` |
| `total_tokens` | `data.total_tokens` | `5050` |
| `latency_ms` | `data.latency_ms` | `2340` |
| `status` | `data.status` | `"success"` |

```python
client.usage.ingest_event(
    event_type="ai.completion",
    customer_id="cust_acme_42",
    entity_id="req_a1b2c3d4",
    meter_slug="ai_tokens",
    value=1,
    provider="openai",
    model="gpt-4o",
    total_input_tokens=1250,
    total_output_tokens=3800,
    total_tokens=5050,
    latency_ms=2340,
    status="success",
    meta={"feature_key": "ai_chat"},   # customer-defined → data.meta.feature_key
)
```

Spans on the cost lane use `span_id` (snake_case) as the dedup grain
moo-acute reads. Always emit `span_id` — not `spanId`.

### Pointing the SDK at a non-default ingest host

For self-hosted deployments, preview environments, or hybrid setups
where the ingest endpoint differs from the canonical apex, set
`MOOLABS_INGEST_HOST` and the SDK will use it instead of the F2 region
fallback:

```bash
export MOOLABS_INGEST_HOST=meter.dev.moolabs.com     # bare host (https:// added)
# OR
export MOOLABS_INGEST_HOST=https://my-relay.example.com
```

Accepts a bare hostname (https:// auto-prefixed) or a full URL. Mirrored
on TypeScript (`process.env.MOOLABS_INGEST_HOST`) and Go (`os.Getenv`).
Empty string is treated as unset and the F2 chain runs normally.

### Check entitlement

```python
result = client.meter.entitlements.check_entitlement(
    subject="user_42",
    feature="ai-credits",
)
if result.granted:
    # serve the request
    ...
```

### Create a wallet + grant credits

```python
wallet = client.cls.wallets.create_wallet(
    tenant_id="tenant_xyz",
    pool_id="pool_abc",
    owner_type="USER",
    owner_id="user_42",
)

client.cls.grants.create_grant(
    wallet_id=wallet.id,
    amount="100.00",
    expires_at="2026-12-31T23:59:59Z",
)
```

## Error handling

All errors inherit from `MoolabsError`. Specific subclasses for HTTP status families:

```python
from moolabs import (
    Moolabs,
    MoolabsError,
    AuthenticationError,
    AuthorizationError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    RetryableError,
)

client = Moolabs(api_key="moo_live_...")

try:
    wallet = client.cls.wallets.create_wallet(...)
except AuthenticationError:
    # 401 — key invalid/expired
    ...
except ValidationError as e:
    # 422 — field-level validation
    print(e.errors)
except RateLimitError:
    # 429 — back off and retry
    ...
except RetryableError:
    # 5xx that's safe to retry
    ...
except MoolabsError as e:
    # any other API error
    ...
```

## Webhook signature verification

If you're consuming Moolabs webhooks (notifications, subscription state changes), verify the signature on each delivery:

```python
from moolabs import WebhookVerifier

verifier = WebhookVerifier(signing_secret="whsec_...")

# Raise on tampering; returns parsed body on success.
event = verifier.verify(
    body=request.body,
    signature=request.headers["X-Moolabs-Signature"],
)
```

## Resource cleanup

Use the client as a context manager to release HTTP connections cleanly:

```python
with Moolabs(api_key="moo_live_...") as client:
    client.meter.events.ingest_events([...])
# Connections closed on exit.
```

Or call `client.close()` manually.

## Source + issues

- Source mirror: https://github.com/moolabs-hq/moolabs-py
- Issues + feature requests: https://github.com/moolabs-hq/moolabs-py/issues

This package is auto-generated from the Moolabs OpenAPI specs on every release. Direct edits to the mirror repo will be overwritten on next publish — file an issue or PR against the source if you spot a generation bug.
