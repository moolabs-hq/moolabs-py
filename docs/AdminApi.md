# moolabs.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnose_subscription**](AdminApi.md#diagnose_subscription) | **GET** /v1/admin/diagnostics/subscription/{subscription_id} | Diagnose Subscription
[**get_ingest_dead_letter_endpoint_v1**](AdminApi.md#get_ingest_dead_letter_endpoint_v1) | **GET** /v1/admin/ingest/dead-letters/{dead_letter_id} | Get Ingest Dead Letter Endpoint
[**get_ingest_dead_letters_v1**](AdminApi.md#get_ingest_dead_letters_v1) | **GET** /v1/admin/ingest/dead-letters | Get Ingest Dead Letters
[**get_ledger_audit_get**](AdminApi.md#get_ledger_audit_get) | **GET** /v1/admin/ledger/audit | Get Ledger Audit
[**get_ledger_balance_get**](AdminApi.md#get_ledger_balance_get) | **GET** /v1/admin/ledger/balance | Get Ledger Balance
[**override_first_ingress_endpoint_v1**](AdminApi.md#override_first_ingress_endpoint_v1) | **POST** /v1/admin/usage/first-ingress/override | Override First Ingress Endpoint
[**process_lifecycle_event_manually_v1_admin**](AdminApi.md#process_lifecycle_event_manually_v1_admin) | **POST** /v1/admin/subscriptions/{subscription_id}/process-lifecycle-event | Process Lifecycle Event Manually
[**replay_ingest_dead_letter_endpoint_v1**](AdminApi.md#replay_ingest_dead_letter_endpoint_v1) | **POST** /v1/admin/ingest/dead-letters/{dead_letter_id}/replay | Replay Ingest Dead Letter Endpoint
[**retry_unpriced**](AdminApi.md#retry_unpriced) | **POST** /v1/admin/usage/unpriced/retry | Retry Unpriced
[**review_quarantined**](AdminApi.md#review_quarantined) | **POST** /v1/admin/usage/quarantined/review | Review Quarantined
[**trigger_subscription_sync**](AdminApi.md#trigger_subscription_sync) | **POST** /v1/admin/subscriptions/{subscription_id}/sync | Trigger Subscription Sync


# **diagnose_subscription**
> object diagnose_subscription(subscription_id, tenant_id)

Diagnose Subscription

Diagnose subscription sync and grant creation status.  Returns:     Dictionary with diagnostic information about:     - Subscription sync status     - Lifecycle events     - Grants created     - Pools created     - Wallets created

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Diagnose Subscription
        api_response = api_instance.diagnose_subscription(subscription_id, tenant_id)
        print("The response of AdminApi->diagnose_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->diagnose_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingest_dead_letter_endpoint_v1**
> object get_ingest_dead_letter_endpoint_v1(dead_letter_id)

Get Ingest Dead Letter Endpoint

Return one ingest dead-letter record including raw payload and stack trace.  Authentication is enforced subtree-wide by `dependencies=[Depends(try_portal_or_apikey)]` on the `/admin` mount in `app/api/v1/router.py`. This handler additionally takes the resolved `auth` context as a parameter so we can derive the caller's `tenant_id` SERVER-SIDE -- it is *not* read from a client-supplied header (an earlier iteration of this PR used `X-Org-Id`; round-3 adversarial review proved that input was unverified user-input and could be spoofed by harvesting `tenant_id` from the list endpoint).  Cross-tenant guard: the row's ``tenant_id`` must match ``auth.tenant_id`` OR be NULL (untenanted poison-pill events). Mismatch returns 404 -- not 403 -- so the endpoint never leaks the existence of a row in another tenant.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    dead_letter_id = 'dead_letter_id_example' # str | Dead-letter row identifier

    try:
        # Get Ingest Dead Letter Endpoint
        api_response = api_instance.get_ingest_dead_letter_endpoint_v1(dead_letter_id)
        print("The response of AdminApi->get_ingest_dead_letter_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_ingest_dead_letter_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dead_letter_id** | **str**| Dead-letter row identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingest_dead_letters_v1**
> object get_ingest_dead_letters_v1(tenant_id=tenant_id, pool_id=pool_id, replay_status=replay_status, reason_code=reason_code, limit=limit)

Get Ingest Dead Letters

List durable ingest dead-letter records.  Cross-tenant enumeration guard (PR #632 round-6 HIGH):  `try_portal_or_apikey` accepts per-tenant customer API keys (the same keys SDK customers use to submit events). Without forcing the tenant scope server-side, a customer of tenant A could omit the `tenant_id` query parameter -- or supply tenant B's id -- and enumerate all dead letters across all tenants (cloud_event_id, reason_detail, source_topic, kafka coords). The round-6 review correctly escalated this from MEDIUM residue to HIGH because the auth dep IS reachable by customer keys.  Fix mirrors the detail endpoint: the caller's auth-derived tenant scope is forced as the filter, overriding any client-supplied ``tenant_id`` query parameter. In production all three AuthContext subclasses (`ApiKeyContext`, `PortalTokenContext`, `OIDCJWTContext`) require ``tenant_id`` at construction, so the fall-through branch where ``auth.tenant_id is None`` honors the client-supplied filter is unreachable today -- it remains as defensive code in case a future staff-key path produces an untenanted context.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (ignored for per-tenant auth) (optional)
    pool_id = 'pool_id_example' # str | Optional pool filter (optional)
    replay_status = 'replay_status_example' # str | Optional replay status filter: PENDING/REPLAYED/FAILED (optional)
    reason_code = 'reason_code_example' # str | Optional reason code filter (optional)
    limit = 100 # int | Maximum rows (optional) (default to 100)

    try:
        # Get Ingest Dead Letters
        api_response = api_instance.get_ingest_dead_letters_v1(tenant_id=tenant_id, pool_id=pool_id, replay_status=replay_status, reason_code=reason_code, limit=limit)
        print("The response of AdminApi->get_ingest_dead_letters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_ingest_dead_letters_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter (ignored for per-tenant auth) | [optional] 
 **pool_id** | **str**| Optional pool filter | [optional] 
 **replay_status** | **str**| Optional replay status filter: PENDING/REPLAYED/FAILED | [optional] 
 **reason_code** | **str**| Optional reason code filter | [optional] 
 **limit** | **int**| Maximum rows | [optional] [default to 100]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_audit_get**
> object get_ledger_audit_get(tenant_id, pool_id, wallet_id=wallet_id, journal_entry_id=journal_entry_id, usage_event_id=usage_event_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, limit=limit)

Get Ledger Audit

Explain ledger audit trace.  This provides a detailed audit trail of journal entries, postings, and burn allocations.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Optional wallet filter (optional)
    journal_entry_id = 'journal_entry_id_example' # str | Optional journal entry filter (optional)
    usage_event_id = 'usage_event_id_example' # str | Optional usage event filter (optional)
    from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional start time filter (optional)
    to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Optional end time filter (optional)
    limit = 100 # int | Maximum number of entries (optional) (default to 100)

    try:
        # Get Ledger Audit
        api_response = api_instance.get_ledger_audit_get(tenant_id, pool_id, wallet_id=wallet_id, journal_entry_id=journal_entry_id, usage_event_id=usage_event_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, limit=limit)
        print("The response of AdminApi->get_ledger_audit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_ledger_audit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_id** | **str**| Optional wallet filter | [optional] 
 **journal_entry_id** | **str**| Optional journal entry filter | [optional] 
 **usage_event_id** | **str**| Optional usage event filter | [optional] 
 **from_effective_at** | **datetime**| Optional start time filter | [optional] 
 **to_effective_at** | **datetime**| Optional end time filter | [optional] 
 **limit** | **int**| Maximum number of entries | [optional] [default to 100]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_balance_get**
> object get_ledger_balance_get(tenant_id, pool_id, wallet_id, as_of_effective_at, as_of_recorded_at=as_of_recorded_at)

Get Ledger Balance

Get ledger balance at a specific point in time (time travel query).  This calculates the balance as of a specific effective_at and recorded_at timestamp.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    as_of_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Effective timestamp (for time travel)
    as_of_recorded_at = '2013-10-20T19:20:30+01:00' # datetime | Recorded timestamp (for time travel) (optional)

    try:
        # Get Ledger Balance
        api_response = api_instance.get_ledger_balance_get(tenant_id, pool_id, wallet_id, as_of_effective_at, as_of_recorded_at=as_of_recorded_at)
        print("The response of AdminApi->get_ledger_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_ledger_balance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_id** | **str**| Wallet identifier | 
 **as_of_effective_at** | **datetime**| Effective timestamp (for time travel) | 
 **as_of_recorded_at** | **datetime**| Recorded timestamp (for time travel) | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_first_ingress_endpoint_v1**
> object override_first_ingress_endpoint_v1(override_first_ingress_request)

Override First Ingress Endpoint

Break-glass first_ingress_at override.  This endpoint requires DB role/session policy enforcement by billing.override_first_ingress_at() and writes audit rows.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.override_first_ingress_request import OverrideFirstIngressRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    override_first_ingress_request = moolabs.OverrideFirstIngressRequest() # OverrideFirstIngressRequest | 

    try:
        # Override First Ingress Endpoint
        api_response = api_instance.override_first_ingress_endpoint_v1(override_first_ingress_request)
        print("The response of AdminApi->override_first_ingress_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->override_first_ingress_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **override_first_ingress_request** | [**OverrideFirstIngressRequest**](OverrideFirstIngressRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_lifecycle_event_manually_v1_admin**
> object process_lifecycle_event_manually_v1_admin(subscription_id, tenant_id)

Process Lifecycle Event Manually

Manually process an existing lifecycle event.  This directly calls the worker's process function to create grants and wallets without requiring Kafka. Useful for testing or reprocessing events.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Process Lifecycle Event Manually
        api_response = api_instance.process_lifecycle_event_manually_v1_admin(subscription_id, tenant_id)
        print("The response of AdminApi->process_lifecycle_event_manually_v1_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->process_lifecycle_event_manually_v1_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_ingest_dead_letter_endpoint_v1**
> object replay_ingest_dead_letter_endpoint_v1(dead_letter_id, replay_dead_letter_request=replay_dead_letter_request)

Replay Ingest Dead Letter Endpoint

Replay a dead-letter event back through normalization + usage ingest.  Cross-tenant guard (PR #632 round-7 review): the replay is state-changing (rolls forward usage events, marks the row REPLAYED, can assign a tenant via ``tenant_id_override``). Without this guard, a per-tenant customer key holder who passes the subtree auth gate could replay any tenant's poison-pill rows or assign their replay to another tenant. Round 7 surfaced this sibling-to-detail-endpoint hole that earlier rounds missed.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.replay_dead_letter_request import ReplayDeadLetterRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    dead_letter_id = 'dead_letter_id_example' # str | Dead-letter row identifier
    replay_dead_letter_request = moolabs.ReplayDeadLetterRequest() # ReplayDeadLetterRequest |  (optional)

    try:
        # Replay Ingest Dead Letter Endpoint
        api_response = api_instance.replay_ingest_dead_letter_endpoint_v1(dead_letter_id, replay_dead_letter_request=replay_dead_letter_request)
        print("The response of AdminApi->replay_ingest_dead_letter_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->replay_ingest_dead_letter_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dead_letter_id** | **str**| Dead-letter row identifier | 
 **replay_dead_letter_request** | [**ReplayDeadLetterRequest**](ReplayDeadLetterRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_unpriced**
> RetryUnpricedResponse retry_unpriced(retry_unpriced_request)

Retry Unpriced

Retry an UNPRICED usage event.  This resets the event to PENDING status so it can be re-rated.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.retry_unpriced_request import RetryUnpricedRequest
from moolabs.models.retry_unpriced_response import RetryUnpricedResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    retry_unpriced_request = moolabs.RetryUnpricedRequest() # RetryUnpricedRequest | 

    try:
        # Retry Unpriced
        api_response = api_instance.retry_unpriced(retry_unpriced_request)
        print("The response of AdminApi->retry_unpriced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->retry_unpriced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retry_unpriced_request** | [**RetryUnpricedRequest**](RetryUnpricedRequest.md)|  | 

### Return type

[**RetryUnpricedResponse**](RetryUnpricedResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **review_quarantined**
> ReviewQuarantinedResponse review_quarantined(review_quarantined_request)

Review Quarantined

Review a QUARANTINED usage event.  Actions: - \"retry\": Reset to PENDING for retry - \"manual_rate\": Mark for manual rating - \"ignore\": Keep in QUARANTINED state

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.review_quarantined_request import ReviewQuarantinedRequest
from moolabs.models.review_quarantined_response import ReviewQuarantinedResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    review_quarantined_request = moolabs.ReviewQuarantinedRequest() # ReviewQuarantinedRequest | 

    try:
        # Review Quarantined
        api_response = api_instance.review_quarantined(review_quarantined_request)
        print("The response of AdminApi->review_quarantined:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->review_quarantined: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_quarantined_request** | [**ReviewQuarantinedRequest**](ReviewQuarantinedRequest.md)|  | 

### Return type

[**ReviewQuarantinedResponse**](ReviewQuarantinedResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_subscription_sync**
> object trigger_subscription_sync(subscription_id)

Trigger Subscription Sync

Manually trigger subscription sync and lifecycle event publishing.  This endpoint: 1. Fetches subscription from OpenMeter 2. Gets tenant_id from environment variable (shared across all customers) 3. Syncs the subscription from OpenMeter 4. Publishes an ACTIVATED lifecycle event if the subscription is active and no event exists 5. Returns the sync result

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AdminApi(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID to sync

    try:
        # Trigger Subscription Sync
        api_response = api_instance.trigger_subscription_sync(subscription_id)
        print("The response of AdminApi->trigger_subscription_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->trigger_subscription_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID to sync | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

