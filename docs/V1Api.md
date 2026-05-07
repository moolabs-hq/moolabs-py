# moolabs.V1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_credits**](V1Api.md#allocate_credits) | **POST** /v1/wallets/allocate | Allocate Credits
[**bind_subject_to_wallet**](V1Api.md#bind_subject_to_wallet) | **POST** /v1/wallets/members | Bind Subject To Wallet
[**check_trigger_v1**](V1Api.md#check_trigger_v1) | **POST** /v1/auto-topup/rules/{rule_id}/check | Check Trigger
[**create_fx_rate_endpoint_v1**](V1Api.md#create_fx_rate_endpoint_v1) | **POST** /v1/fx-rates/rates | Create Fx Rate Endpoint
[**create_mapping**](V1Api.md#create_mapping) | **POST** /v1/mappings | Create Mapping
[**create_rate_card**](V1Api.md#create_rate_card) | **POST** /v1/rate_cards | Create Rate Card
[**create_reconstruction_run**](V1Api.md#create_reconstruction_run) | **POST** /v1/reconstruction/runs | Create Reconstruction Run
[**create_rule_v1**](V1Api.md#create_rule_v1) | **POST** /v1/auto-topup/rules | Create Rule
[**create_snapshot**](V1Api.md#create_snapshot) | **POST** /v1/snapshots | Create Snapshot
[**create_threshold_endpoint**](V1Api.md#create_threshold_endpoint) | **POST** /v1/alerts/thresholds | Create Threshold Endpoint
[**create_token_endpoint**](V1Api.md#create_token_endpoint) | **POST** /v1/portal/tokens | Create Token Endpoint
[**create_value_recognition_entry_endpoint_v1_fx**](V1Api.md#create_value_recognition_entry_endpoint_v1_fx) | **POST** /v1/fx-rates/value-recognition/entry | Create Value Recognition Entry Endpoint
[**create_wallet**](V1Api.md#create_wallet) | **POST** /v1/wallets | Create Wallet
[**delete_rule_v1**](V1Api.md#delete_rule_v1) | **DELETE** /v1/auto-topup/rules/{rule_id} | Delete Rule
[**delete_threshold_endpoint**](V1Api.md#delete_threshold_endpoint) | **DELETE** /v1/alerts/thresholds/{threshold_id} | Delete Threshold Endpoint
[**diagnose_subscription**](V1Api.md#diagnose_subscription) | **GET** /v1/admin/diagnostics/subscription/{subscription_id} | Diagnose Subscription
[**explain_query**](V1Api.md#explain_query) | **POST** /v1/performance/queries/explain | Explain Query
[**get_activity_v1**](V1Api.md#get_activity_v1) | **GET** /v1/auto-topup/activity | Get Activity
[**get_affected_events_endpoint_v1**](V1Api.md#get_affected_events_endpoint_v1) | **GET** /v1/reconstruction/affected-events | Get Affected Events Endpoint
[**get_alerts_state_endpoint**](V1Api.md#get_alerts_state_endpoint) | **GET** /v1/alerts/state | Get Alerts State Endpoint
[**get_connection_pool_info_v1**](V1Api.md#get_connection_pool_info_v1) | **GET** /v1/performance/connection-pool | Get Connection Pool Info
[**get_fx_rate_at_endpoint_v1**](V1Api.md#get_fx_rate_at_endpoint_v1) | **POST** /v1/fx-rates/rates/at | Get Fx Rate At Endpoint
[**get_grant**](V1Api.md#get_grant) | **GET** /v1/grants/{grant_id} | Get Grant
[**get_index_usage**](V1Api.md#get_index_usage) | **GET** /v1/performance/indexes/usage | Get Index Usage
[**get_late_events_v1**](V1Api.md#get_late_events_v1) | **GET** /v1/reconstruction/late-events | Get Late Events
[**get_ledger_audit**](V1Api.md#get_ledger_audit) | **GET** /v1/ledger/audit | Get Ledger Audit
[**get_ledger_audit_get**](V1Api.md#get_ledger_audit_get) | **GET** /v1/admin/ledger/audit | Get Ledger Audit
[**get_ledger_balance**](V1Api.md#get_ledger_balance) | **GET** /v1/ledger/balance | Get Ledger Balance
[**get_ledger_balance_get**](V1Api.md#get_ledger_balance_get) | **GET** /v1/admin/ledger/balance | Get Ledger Balance
[**get_missing_index_recommendations**](V1Api.md#get_missing_index_recommendations) | **GET** /v1/performance/indexes/missing | Get Missing Index Recommendations
[**get_performance_report_endpoint**](V1Api.md#get_performance_report_endpoint) | **GET** /v1/performance/report | Get Performance Report Endpoint
[**get_portal_context**](V1Api.md#get_portal_context) | **GET** /v1/portal/context | Get Portal Context
[**get_rate_card**](V1Api.md#get_rate_card) | **GET** /v1/rate_cards/{rate_card_id} | Get Rate Card
[**get_rule_v1**](V1Api.md#get_rule_v1) | **GET** /v1/auto-topup/rules/{rule_id} | Get Rule
[**get_slow_queries**](V1Api.md#get_slow_queries) | **GET** /v1/performance/queries/slow | Get Slow Queries
[**get_snapshot_at_endpoint**](V1Api.md#get_snapshot_at_endpoint) | **GET** /v1/snapshots/wallet/{wallet_id}/at | Get Snapshot At Endpoint
[**get_subscription**](V1Api.md#get_subscription) | **GET** /v1/subscriptions/{subscription_id} | Get Subscription
[**get_table_size_analysis**](V1Api.md#get_table_size_analysis) | **GET** /v1/performance/tables/sizes | Get Table Size Analysis
[**get_usage_event**](V1Api.md#get_usage_event) | **GET** /v1/usage/{event_id} | Get Usage Event
[**get_wallet**](V1Api.md#get_wallet) | **GET** /v1/wallets/{wallet_id} | Get Wallet
[**get_wallet_activity**](V1Api.md#get_wallet_activity) | **GET** /v1/wallets/{wallet_id}/activity | Get Wallet Activity
[**get_wallet_members**](V1Api.md#get_wallet_members) | **GET** /v1/wallets/{wallet_id}/members | Get Wallet Members
[**get_wallet_state**](V1Api.md#get_wallet_state) | **GET** /v1/ledger/state | Get Wallet State
[**get_wallet_state_projection_endpoint_v1**](V1Api.md#get_wallet_state_projection_endpoint_v1) | **GET** /v1/state-projection/wallet/{wallet_id} | Get Wallet State Projection Endpoint
[**get_wallet_subtree**](V1Api.md#get_wallet_subtree) | **GET** /v1/reconstruction/wallets/{wallet_id}/subtree | Get Wallet Subtree
[**handle_lifecycle_event**](V1Api.md#handle_lifecycle_event) | **POST** /v1/subscriptions/lifecycle | Handle Lifecycle Event
[**invalidate_tokens_endpoint**](V1Api.md#invalidate_tokens_endpoint) | **POST** /v1/portal/tokens/invalidate | Invalidate Tokens Endpoint
[**list_grants**](V1Api.md#list_grants) | **GET** /v1/grants | List Grants
[**list_mappings**](V1Api.md#list_mappings) | **GET** /v1/mappings | List Mappings
[**list_outbox_events_endpoint**](V1Api.md#list_outbox_events_endpoint) | **GET** /v1/outbox/events | List Outbox Events Endpoint
[**list_rules_v1**](V1Api.md#list_rules_v1) | **GET** /v1/auto-topup/rules | List Rules
[**list_snapshots_endpoint**](V1Api.md#list_snapshots_endpoint) | **GET** /v1/snapshots/wallet/{wallet_id} | List Snapshots Endpoint
[**list_thresholds_endpoint**](V1Api.md#list_thresholds_endpoint) | **GET** /v1/alerts/thresholds | List Thresholds Endpoint
[**list_tokens_endpoint**](V1Api.md#list_tokens_endpoint) | **GET** /v1/portal/tokens | List Tokens Endpoint
[**list_unpriced_events**](V1Api.md#list_unpriced_events) | **GET** /v1/unpriced/events | List Unpriced Events
[**list_usage_events**](V1Api.md#list_usage_events) | **GET** /v1/usage/ | List Usage Events
[**list_wallet_members**](V1Api.md#list_wallet_members) | **GET** /v1/wallet_members | List Wallet Members
[**list_wallets**](V1Api.md#list_wallets) | **GET** /v1/wallets | List Wallets
[**mint_grant**](V1Api.md#mint_grant) | **POST** /v1/grants/mint | Mint Grant
[**openmeter_webhook**](V1Api.md#openmeter_webhook) | **POST** /v1/integrations/openmeter/webhooks/openmeter | Openmeter Webhook
[**openmeter_webhook_batch**](V1Api.md#openmeter_webhook_batch) | **POST** /v1/integrations/openmeter/webhooks/openmeter/batch | Openmeter Webhook Batch
[**patch_rule_v1**](V1Api.md#patch_rule_v1) | **PATCH** /v1/auto-topup/rules/{rule_id} | Patch Rule
[**payment_succeeded_v1**](V1Api.md#payment_succeeded_v1) | **POST** /v1/auto-topup/payments/succeeded | Payment Succeeded
[**process_events**](V1Api.md#process_events) | **POST** /v1/unpriced/process | Process Events
[**process_lifecycle_event_manually_v1_admin**](V1Api.md#process_lifecycle_event_manually_v1_admin) | **POST** /v1/admin/subscriptions/{subscription_id}/process-lifecycle-event | Process Lifecycle Event Manually
[**process_outbox_endpoint**](V1Api.md#process_outbox_endpoint) | **POST** /v1/outbox/process | Process Outbox Endpoint
[**process_pending_events_v1**](V1Api.md#process_pending_events_v1) | **POST** /v1/rating/process-pending | Process Pending Events
[**process_pending_projections_endpoint_v1**](V1Api.md#process_pending_projections_endpoint_v1) | **POST** /v1/state-projection/process | Process Pending Projections Endpoint
[**process_rollover**](V1Api.md#process_rollover) | **POST** /v1/rollover/process | Process Rollover
[**process_value_recognition_v1_fx**](V1Api.md#process_value_recognition_v1_fx) | **POST** /v1/fx-rates/value-recognition/process | Process Value Recognition
[**project_wallet_state_endpoint_v1**](V1Api.md#project_wallet_state_endpoint_v1) | **POST** /v1/state-projection/project/{wallet_id} | Project Wallet State Endpoint
[**rate_event**](V1Api.md#rate_event) | **POST** /v1/rating/rate/{usage_event_id} | Rate Event
[**record_usage**](V1Api.md#record_usage) | **POST** /v1/usage/record | Record Usage
[**resolve_event**](V1Api.md#resolve_event) | **POST** /v1/unpriced/resolve/{usage_event_id} | Resolve Event
[**resolve_tenant_and_pool**](V1Api.md#resolve_tenant_and_pool) | **GET** /v1/wallets/resolve | Resolve Tenant And Pool
[**retry_unpriced**](V1Api.md#retry_unpriced) | **POST** /v1/admin/usage/unpriced/retry | Retry Unpriced
[**review_quarantined**](V1Api.md#review_quarantined) | **POST** /v1/admin/usage/quarantined/review | Review Quarantined
[**sync_subscription**](V1Api.md#sync_subscription) | **POST** /v1/subscriptions/sync | Sync Subscription
[**trigger_subscription_sync**](V1Api.md#trigger_subscription_sync) | **POST** /v1/admin/subscriptions/{subscription_id}/sync | Trigger Subscription Sync
[**update_rule_v1**](V1Api.md#update_rule_v1) | **PUT** /v1/auto-topup/rules/{rule_id} | Update Rule
[**update_threshold_endpoint**](V1Api.md#update_threshold_endpoint) | **PUT** /v1/alerts/thresholds/{threshold_id} | Update Threshold Endpoint
[**update_wallet_settings**](V1Api.md#update_wallet_settings) | **PATCH** /v1/wallets/{wallet_id}/settings | Update Wallet Settings
[**update_wallet_thresholds**](V1Api.md#update_wallet_thresholds) | **PATCH** /v1/wallets/{wallet_id}/thresholds | Update Wallet Thresholds
[**validate_snapshot_endpoint**](V1Api.md#validate_snapshot_endpoint) | **POST** /v1/snapshots/{snapshot_id}/validate | Validate Snapshot Endpoint
[**void_grant**](V1Api.md#void_grant) | **POST** /v1/grants/{grant_id}/void | Void Grant
[**warm_rate_card_cache_v1**](V1Api.md#warm_rate_card_cache_v1) | **POST** /v1/performance/cache/warm/rate-cards | Warm Rate Card Cache
[**warm_wallet_cache**](V1Api.md#warm_wallet_cache) | **POST** /v1/performance/cache/warm/wallets | Warm Wallet Cache


# **allocate_credits**
> object allocate_credits(allocate_credits_request)

Allocate Credits

Allocate credits from source wallet to target wallet.  Server-side validation: - Both wallets must belong to the same tenant and pool. - Source must have sufficient transferable balance. - Creates double-entry journal entries (JournalEntry header + JournalPosting lines).

### Example

* Bearer Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.allocate_credits_request import AllocateCreditsRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    allocate_credits_request = moolabs.AllocateCreditsRequest() # AllocateCreditsRequest | 

    try:
        # Allocate Credits
        api_response = api_instance.allocate_credits(allocate_credits_request)
        print("The response of V1Api->allocate_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->allocate_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocate_credits_request** | [**AllocateCreditsRequest**](AllocateCreditsRequest.md)|  | 

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

# **bind_subject_to_wallet**
> object bind_subject_to_wallet(tenant_id, pool_id, subject_id, wallet_id)

Bind Subject To Wallet

Bind a subject to a wallet.  Creates or updates wallet_members entry.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pool_id = 'pool_id_example' # str | 
    subject_id = 'subject_id_example' # str | 
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Bind Subject To Wallet
        api_response = api_instance.bind_subject_to_wallet(tenant_id, pool_id, subject_id, wallet_id)
        print("The response of V1Api->bind_subject_to_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->bind_subject_to_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pool_id** | **str**|  | 
 **subject_id** | **str**|  | 
 **wallet_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_trigger_v1**
> TriggerResponse check_trigger_v1(rule_id, check_trigger_request=check_trigger_request)

Check Trigger

Check trigger condition and trigger auto top-up if needed.  This endpoint: - Checks if trigger condition is met - Checks cooldown atomicity - Acquires trigger lock - Emits AUTO_TOPUP_REQUESTED outbox event

### Example


```python
import moolabs
from moolabs.models.check_trigger_request import CheckTriggerRequest
from moolabs.models.trigger_response import TriggerResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    check_trigger_request = moolabs.CheckTriggerRequest() # CheckTriggerRequest |  (optional)

    try:
        # Check Trigger
        api_response = api_instance.check_trigger_v1(rule_id, check_trigger_request=check_trigger_request)
        print("The response of V1Api->check_trigger_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->check_trigger_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **check_trigger_request** | [**CheckTriggerRequest**](CheckTriggerRequest.md)|  | [optional] 

### Return type

[**TriggerResponse**](TriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fx_rate_endpoint_v1**
> FxRateResponse create_fx_rate_endpoint_v1(create_fx_rate_request)

Create Fx Rate Endpoint

Create a new FX rate version.  This endpoint creates a versioned FX rate for converting credits to USD. FX rates are effective at a specific timestamp and can be locked to grants.

### Example


```python
import moolabs
from moolabs.models.create_fx_rate_request import CreateFxRateRequest
from moolabs.models.fx_rate_response import FxRateResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_fx_rate_request = moolabs.CreateFxRateRequest() # CreateFxRateRequest | 

    try:
        # Create Fx Rate Endpoint
        api_response = api_instance.create_fx_rate_endpoint_v1(create_fx_rate_request)
        print("The response of V1Api->create_fx_rate_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_fx_rate_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_fx_rate_request** | [**CreateFxRateRequest**](CreateFxRateRequest.md)|  | 

### Return type

[**FxRateResponse**](FxRateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mapping**
> MappingResponse create_mapping(tenant_id, create_mapping_request)

Create Mapping

Create or update a feature key mapping.  Maps a meter_slug to a feature_key for usage event rating. This is a bitemporal update - closes any existing active mapping and creates a new one.

### Example


```python
import moolabs
from moolabs.models.create_mapping_request import CreateMappingRequest
from moolabs.models.mapping_response import MappingResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    create_mapping_request = moolabs.CreateMappingRequest() # CreateMappingRequest | 

    try:
        # Create Mapping
        api_response = api_instance.create_mapping(tenant_id, create_mapping_request)
        print("The response of V1Api->create_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **create_mapping_request** | [**CreateMappingRequest**](CreateMappingRequest.md)|  | 

### Return type

[**MappingResponse**](MappingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rate_card**
> RateCardResponse create_rate_card(create_rate_card_request)

Create Rate Card

Create a new rate card.  Features: - Non-overlap constraint enforcement (no overlapping time ranges) - Rate card versioning - Pricing model fingerprinting  Returns:     Created rate card

### Example


```python
import moolabs
from moolabs.models.create_rate_card_request import CreateRateCardRequest
from moolabs.models.rate_card_response import RateCardResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_rate_card_request = moolabs.CreateRateCardRequest() # CreateRateCardRequest | 

    try:
        # Create Rate Card
        api_response = api_instance.create_rate_card(create_rate_card_request)
        print("The response of V1Api->create_rate_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_rate_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rate_card_request** | [**CreateRateCardRequest**](CreateRateCardRequest.md)|  | 

### Return type

[**RateCardResponse**](RateCardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reconstruction_run**
> ReconstructionRunResponse create_reconstruction_run(create_reconstruction_run_request)

Create Reconstruction Run

Create and process a reconstruction run.  This endpoint: - Materializes wallet subtree from root wallet - Gets affected events in the time window - Re-rates affected events - Creates CORRECTION journal entries linked to originals  Triggered on LATE events (policy-based).

### Example


```python
import moolabs
from moolabs.models.create_reconstruction_run_request import CreateReconstructionRunRequest
from moolabs.models.reconstruction_run_response import ReconstructionRunResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_reconstruction_run_request = moolabs.CreateReconstructionRunRequest() # CreateReconstructionRunRequest | 

    try:
        # Create Reconstruction Run
        api_response = api_instance.create_reconstruction_run(create_reconstruction_run_request)
        print("The response of V1Api->create_reconstruction_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_reconstruction_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_reconstruction_run_request** | [**CreateReconstructionRunRequest**](CreateReconstructionRunRequest.md)|  | 

### Return type

[**ReconstructionRunResponse**](ReconstructionRunResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule_v1**
> AutoTopupRuleResponse create_rule_v1(create_auto_topup_rule_request)

Create Rule

Create an auto top-up rule.  This endpoint creates a rule that triggers automatic wallet top-up when certain conditions are met (e.g., LOW state, threshold crossed).

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.models.create_auto_topup_rule_request import CreateAutoTopupRuleRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_auto_topup_rule_request = moolabs.CreateAutoTopupRuleRequest() # CreateAutoTopupRuleRequest | 

    try:
        # Create Rule
        api_response = api_instance.create_rule_v1(create_auto_topup_rule_request)
        print("The response of V1Api->create_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auto_topup_rule_request** | [**CreateAutoTopupRuleRequest**](CreateAutoTopupRuleRequest.md)|  | 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot**
> SnapshotResponse create_snapshot(create_snapshot_request)

Create Snapshot

Create a balance snapshot using REPEATABLE READ transaction isolation.  This endpoint creates a snapshot of the wallet balance at a specific point in time. The snapshot uses REPEATABLE READ isolation to ensure a consistent view of the data.

### Example


```python
import moolabs
from moolabs.models.create_snapshot_request import CreateSnapshotRequest
from moolabs.models.snapshot_response import SnapshotResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_snapshot_request = moolabs.CreateSnapshotRequest() # CreateSnapshotRequest | 

    try:
        # Create Snapshot
        api_response = api_instance.create_snapshot(create_snapshot_request)
        print("The response of V1Api->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_snapshot_request** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_threshold_endpoint**
> object create_threshold_endpoint(wallet_id, tenant_id, pool_id, create_threshold_request)

Create Threshold Endpoint

Create a wallet threshold.  Thresholds trigger alerts when wallet state crosses the threshold. - PERCENT: 0-100, triggers when spent_percent >= threshold - ABSOLUTE: micros, triggers when effective_available_micros <= threshold

### Example


```python
import moolabs
from moolabs.models.create_threshold_request import CreateThresholdRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    create_threshold_request = moolabs.CreateThresholdRequest() # CreateThresholdRequest | 

    try:
        # Create Threshold Endpoint
        api_response = api_instance.create_threshold_endpoint(wallet_id, tenant_id, pool_id, create_threshold_request)
        print("The response of V1Api->create_threshold_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_threshold_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **create_threshold_request** | [**CreateThresholdRequest**](CreateThresholdRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token_endpoint**
> object create_token_endpoint(create_portal_token_request)

Create Token Endpoint

Create a portal token for a subject.  The token is scoped to the subject's tenant and pool (resolved server-side). Plaintext is returned only once — only the SHA-256 hash is stored. tenant_id is derived from server config (never a query param).

### Example


```python
import moolabs
from moolabs.models.create_portal_token_request import CreatePortalTokenRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_portal_token_request = moolabs.CreatePortalTokenRequest() # CreatePortalTokenRequest | 

    try:
        # Create Token Endpoint
        api_response = api_instance.create_token_endpoint(create_portal_token_request)
        print("The response of V1Api->create_token_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_token_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_portal_token_request** | [**CreatePortalTokenRequest**](CreatePortalTokenRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_value_recognition_entry_endpoint_v1_fx**
> object create_value_recognition_entry_endpoint_v1_fx(create_value_recognition_request)

Create Value Recognition Entry Endpoint

Create a VALUE_RECOGNITION journal entry.  This endpoint creates a journal entry for revenue recognition in USD.

### Example


```python
import moolabs
from moolabs.models.create_value_recognition_request import CreateValueRecognitionRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_value_recognition_request = moolabs.CreateValueRecognitionRequest() # CreateValueRecognitionRequest | 

    try:
        # Create Value Recognition Entry Endpoint
        api_response = api_instance.create_value_recognition_entry_endpoint_v1_fx(create_value_recognition_request)
        print("The response of V1Api->create_value_recognition_entry_endpoint_v1_fx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_value_recognition_entry_endpoint_v1_fx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_value_recognition_request** | [**CreateValueRecognitionRequest**](CreateValueRecognitionRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet**
> WalletResponse create_wallet(create_wallet_request)

Create Wallet

Create or upsert a wallet.  - Validates hierarchy (depth, cycles) - Auto-creates SYSTEM wallet if needed - Returns wallet details

### Example


```python
import moolabs
from moolabs.models.create_wallet_request import CreateWalletRequest
from moolabs.models.wallet_response import WalletResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_wallet_request = moolabs.CreateWalletRequest() # CreateWalletRequest | 

    try:
        # Create Wallet
        api_response = api_instance.create_wallet(create_wallet_request)
        print("The response of V1Api->create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_wallet_request** | [**CreateWalletRequest**](CreateWalletRequest.md)|  | 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule_v1**
> object delete_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id)

Delete Rule

Delete an auto top-up rule.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier for validation (optional)

    try:
        # Delete Rule
        api_response = api_instance.delete_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id)
        print("The response of V1Api->delete_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->delete_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 
 **wallet_id** | **str**| Optional wallet identifier for validation | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_threshold_endpoint**
> object delete_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id)

Delete Threshold Endpoint

Delete a wallet threshold.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    threshold_id = 'threshold_id_example' # str | 
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier

    try:
        # Delete Threshold Endpoint
        api_response = api_instance.delete_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id)
        print("The response of V1Api->delete_threshold_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->delete_threshold_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threshold_id** | **str**|  | 
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **diagnose_subscription**
> object diagnose_subscription(subscription_id, tenant_id)

Diagnose Subscription

Diagnose subscription sync and grant creation status.  Returns:     Dictionary with diagnostic information about:     - Subscription sync status     - Lifecycle events     - Grants created     - Pools created     - Wallets created

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    subscription_id = 'subscription_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Diagnose Subscription
        api_response = api_instance.diagnose_subscription(subscription_id, tenant_id)
        print("The response of V1Api->diagnose_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->diagnose_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **explain_query**
> object explain_query(query_sql)

Explain Query

Explain query execution plan.  Uses PostgreSQL EXPLAIN to analyze query performance.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    query_sql = 'query_sql_example' # str | 

    try:
        # Explain Query
        api_response = api_instance.explain_query(query_sql)
        print("The response of V1Api->explain_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->explain_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_sql** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_v1**
> AutoTopupActivityResponse get_activity_v1(tenant_id, pool_id, wallet_id, limit=limit, offset=offset)

Get Activity

Get auto-topup activity/history for a wallet.  Returns history of auto-topup executions (both requested and completed).

### Example


```python
import moolabs
from moolabs.models.auto_topup_activity_response import AutoTopupActivityResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    limit = 50 # int | Maximum number of items to return (optional) (default to 50)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # Get Activity
        api_response = api_instance.get_activity_v1(tenant_id, pool_id, wallet_id, limit=limit, offset=offset)
        print("The response of V1Api->get_activity_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_activity_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_id** | **str**| Wallet identifier | 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 50]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

[**AutoTopupActivityResponse**](AutoTopupActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_affected_events_endpoint_v1**
> object get_affected_events_endpoint_v1(tenant_id, pool_id, wallet_ids, from_effective_at, to_effective_at)

Get Affected Events Endpoint

Get affected usage events in the time window for wallet subtree.  Returns events that were rated in the time window for the specified wallets.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_ids = 'wallet_ids_example' # str | Comma-separated wallet IDs
    from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Start of effective time window
    to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | End of effective time window

    try:
        # Get Affected Events Endpoint
        api_response = api_instance.get_affected_events_endpoint_v1(tenant_id, pool_id, wallet_ids, from_effective_at, to_effective_at)
        print("The response of V1Api->get_affected_events_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_affected_events_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_ids** | **str**| Comma-separated wallet IDs | 
 **from_effective_at** | **datetime**| Start of effective time window | 
 **to_effective_at** | **datetime**| End of effective time window | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alerts_state_endpoint**
> object get_alerts_state_endpoint(wallet_id, tenant_id, pool_id)

Get Alerts State Endpoint

Get alert state for a wallet.  Returns the current state of all alerts (ACTIVE/CLEARED) for the wallet.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier

    try:
        # Get Alerts State Endpoint
        api_response = api_instance.get_alerts_state_endpoint(wallet_id, tenant_id, pool_id)
        print("The response of V1Api->get_alerts_state_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_alerts_state_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_pool_info_v1**
> object get_connection_pool_info_v1()

Get Connection Pool Info

Get connection pool statistics.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)

    try:
        # Get Connection Pool Info
        api_response = api_instance.get_connection_pool_info_v1()
        print("The response of V1Api->get_connection_pool_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_connection_pool_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fx_rate_at_endpoint_v1**
> object get_fx_rate_at_endpoint_v1(get_fx_rate_request)

Get Fx Rate At Endpoint

Get FX rate effective at a specific timestamp.  Returns the FX rate that was effective at the given timestamp.

### Example


```python
import moolabs
from moolabs.models.get_fx_rate_request import GetFxRateRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    get_fx_rate_request = moolabs.GetFxRateRequest() # GetFxRateRequest | 

    try:
        # Get Fx Rate At Endpoint
        api_response = api_instance.get_fx_rate_at_endpoint_v1(get_fx_rate_request)
        print("The response of V1Api->get_fx_rate_at_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_fx_rate_at_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_fx_rate_request** | [**GetFxRateRequest**](GetFxRateRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_grant**
> GrantResponse get_grant(grant_id)

Get Grant

Get grant details by ID.

### Example


```python
import moolabs
from moolabs.models.grant_response import GrantResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    grant_id = 'grant_id_example' # str | 

    try:
        # Get Grant
        api_response = api_instance.get_grant(grant_id)
        print("The response of V1Api->get_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  | 

### Return type

[**GrantResponse**](GrantResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index_usage**
> object get_index_usage(var_schema=var_schema)

Get Index Usage

Get index usage statistics.  Analyzes which indexes are being used and which are unused.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Index Usage
        api_response = api_instance.get_index_usage(var_schema=var_schema)
        print("The response of V1Api->get_index_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_index_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_late_events_v1**
> object get_late_events_v1(tenant_id, pool_id, late_threshold_seconds=late_threshold_seconds)

Get Late Events

Detect LATE events (events recorded significantly after effective_at).  Returns events where recorded_at is much later than effective_at.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    late_threshold_seconds = 3600 # int | LATE event threshold (seconds) (optional) (default to 3600)

    try:
        # Get Late Events
        api_response = api_instance.get_late_events_v1(tenant_id, pool_id, late_threshold_seconds=late_threshold_seconds)
        print("The response of V1Api->get_late_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_late_events_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **late_threshold_seconds** | **int**| LATE event threshold (seconds) | [optional] [default to 3600]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_audit**
> object get_ledger_audit(tenant_id, pool_id, wallet_id=wallet_id, journal_entry_id=journal_entry_id, usage_event_id=usage_event_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, limit=limit)

Get Ledger Audit

Explain ledger audit trace.  This provides a detailed audit trail of journal entries, postings, and burn allocations.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
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
        api_response = api_instance.get_ledger_audit(tenant_id, pool_id, wallet_id=wallet_id, journal_entry_id=journal_entry_id, usage_event_id=usage_event_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, limit=limit)
        print("The response of V1Api->get_ledger_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_ledger_audit: %s\n" % e)
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

No authorization required

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


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
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
        print("The response of V1Api->get_ledger_audit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_ledger_audit_get: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_balance**
> object get_ledger_balance(tenant_id, pool_id, wallet_id, as_of_effective_at, as_of_recorded_at=as_of_recorded_at)

Get Ledger Balance

Get ledger balance at a specific point in time (time travel query).  This calculates the balance as of a specific effective_at and recorded_at timestamp.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    as_of_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Effective timestamp (for time travel)
    as_of_recorded_at = '2013-10-20T19:20:30+01:00' # datetime | Recorded timestamp (for time travel) (optional)

    try:
        # Get Ledger Balance
        api_response = api_instance.get_ledger_balance(tenant_id, pool_id, wallet_id, as_of_effective_at, as_of_recorded_at=as_of_recorded_at)
        print("The response of V1Api->get_ledger_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_ledger_balance: %s\n" % e)
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

No authorization required

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


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    as_of_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Effective timestamp (for time travel)
    as_of_recorded_at = '2013-10-20T19:20:30+01:00' # datetime | Recorded timestamp (for time travel) (optional)

    try:
        # Get Ledger Balance
        api_response = api_instance.get_ledger_balance_get(tenant_id, pool_id, wallet_id, as_of_effective_at, as_of_recorded_at=as_of_recorded_at)
        print("The response of V1Api->get_ledger_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_ledger_balance_get: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_missing_index_recommendations**
> object get_missing_index_recommendations(var_schema=var_schema)

Get Missing Index Recommendations

Identify potentially missing indexes.  Uses pg_stat_statements to identify sequential scans that might benefit from indexes.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Missing Index Recommendations
        api_response = api_instance.get_missing_index_recommendations(var_schema=var_schema)
        print("The response of V1Api->get_missing_index_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_missing_index_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_report_endpoint**
> object get_performance_report_endpoint(var_schema=var_schema)

Get Performance Report Endpoint

Generate comprehensive performance report.  Combines query analysis, index stats, connection pool stats, and table sizes.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Performance Report Endpoint
        api_response = api_instance.get_performance_report_endpoint(var_schema=var_schema)
        print("The response of V1Api->get_performance_report_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_performance_report_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_context**
> object get_portal_context()

Get Portal Context

Return resolved tenant/pool/subject for the authenticated portal token.  Called by MoolabsProvider on mount to resolve CLS queryParams (tenant_id, pool_id) without exposing them in browser code.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)

    try:
        # Get Portal Context
        api_response = api_instance.get_portal_context()
        print("The response of V1Api->get_portal_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_portal_context: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_card**
> RateCardResponse get_rate_card(rate_card_id)

Get Rate Card

Get rate card details by ID.

### Example


```python
import moolabs
from moolabs.models.rate_card_response import RateCardResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rate_card_id = 'rate_card_id_example' # str | 

    try:
        # Get Rate Card
        api_response = api_instance.get_rate_card(rate_card_id)
        print("The response of V1Api->get_rate_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_rate_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **str**|  | 

### Return type

[**RateCardResponse**](RateCardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule_v1**
> AutoTopupRuleResponse get_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id)

Get Rule

Get a specific auto top-up rule by ID.

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)

    try:
        # Get Rule
        api_response = api_instance.get_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of V1Api->get_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_slow_queries**
> object get_slow_queries(min_duration_ms=min_duration_ms, limit=limit)

Get Slow Queries

Analyze slow queries from PostgreSQL.  Uses pg_stat_statements to identify slow queries. Requires pg_stat_statements extension to be enabled.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    min_duration_ms = 100.0 # float | Minimum query duration in milliseconds (optional) (default to 100.0)
    limit = 20 # int | Maximum number of results (optional) (default to 20)

    try:
        # Get Slow Queries
        api_response = api_instance.get_slow_queries(min_duration_ms=min_duration_ms, limit=limit)
        print("The response of V1Api->get_slow_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_slow_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_duration_ms** | **float**| Minimum query duration in milliseconds | [optional] [default to 100.0]
 **limit** | **int**| Maximum number of results | [optional] [default to 20]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_at_endpoint**
> object get_snapshot_at_endpoint(wallet_id, tenant_id, pool_id, as_of_recorded_at)

Get Snapshot At Endpoint

Get the most recent snapshot at or before a recorded timestamp.  Returns the snapshot with as_of_recorded_at <= provided timestamp.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    as_of_recorded_at = '2013-10-20T19:20:30+01:00' # datetime | Recorded timestamp

    try:
        # Get Snapshot At Endpoint
        api_response = api_instance.get_snapshot_at_endpoint(wallet_id, tenant_id, pool_id, as_of_recorded_at)
        print("The response of V1Api->get_snapshot_at_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_snapshot_at_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **as_of_recorded_at** | **datetime**| Recorded timestamp | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> object get_subscription(subscription_id, tenant_id, as_of=as_of)

Get Subscription

Get subscription mirror as-of a specific time (bitemporal query).  Args:     subscription_id: Subscription ID     tenant_id: Tenant ID (query parameter)     as_of: Optional ISO 8601 datetime (defaults to now)

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    subscription_id = 'subscription_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    as_of = 'as_of_example' # str |  (optional)

    try:
        # Get Subscription
        api_response = api_instance.get_subscription(subscription_id, tenant_id, as_of=as_of)
        print("The response of V1Api->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **as_of** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_size_analysis**
> object get_table_size_analysis(var_schema=var_schema)

Get Table Size Analysis

Analyze table sizes for partitioning consideration.  Identifies large tables that might benefit from partitioning.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Table Size Analysis
        api_response = api_instance.get_table_size_analysis(var_schema=var_schema)
        print("The response of V1Api->get_table_size_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_table_size_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_event**
> object get_usage_event(event_id)

Get Usage Event

Get usage event details by ID.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get Usage Event
        api_response = api_instance.get_usage_event(event_id)
        print("The response of V1Api->get_usage_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_usage_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet**
> WalletResponse get_wallet(wallet_id)

Get Wallet

Get wallet details by ID.

### Example


```python
import moolabs
from moolabs.models.wallet_response import WalletResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Get Wallet
        api_response = api_instance.get_wallet(wallet_id)
        print("The response of V1Api->get_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_activity**
> object get_wallet_activity(wallet_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, cursor=cursor)

Get Wallet Activity

Get wallet activity (journal entries) for a specific wallet.  Returns ALL journal entry types (burns, mints, adjustments, expiry, topup, transfer, system). For entries with burn allocations, shows the burn amount as negative delta. For grant mints, shows the grant amount as positive delta. For other entry types, calculates delta based on entry type.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 
    from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Start time for activity range (optional)
    to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | End time for activity range (optional)
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency for reads (optional)
    limit = 50 # int | Maximum number of items to return (optional) (default to 50)
    cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        # Get Wallet Activity
        api_response = api_instance.get_wallet_activity(wallet_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, cursor=cursor)
        print("The response of V1Api->get_wallet_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_wallet_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **from_effective_at** | **datetime**| Start time for activity range | [optional] 
 **to_effective_at** | **datetime**| End time for activity range | [optional] 
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency for reads | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 50]
 **cursor** | **str**| Pagination cursor | [optional] 

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

# **get_wallet_members**
> object get_wallet_members(wallet_id)

Get Wallet Members

Get wallet members (subjects bound to a wallet).  Returns list of subjects that are bound to the specified wallet.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Get Wallet Members
        api_response = api_instance.get_wallet_members(wallet_id)
        print("The response of V1Api->get_wallet_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_wallet_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_state**
> object get_wallet_state(tenant_id, pool_id, wallet_id, as_of=as_of, consistency=consistency, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)

Get Wallet State

Get wallet state (balance and credit state).  - Eventually consistent by default (fast, uses denormalized remaining_micros) - STRONG consistency available for admin/debug (slower, uses state projection) - Returns balance, state (OK/LOW/OVERDRAFT/OVER_CAP), and metadata - Includes last_projected_at and projected_from_recorded_cut for STRONG consistency - Sets cache headers for eventual consistency reads

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Credit pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp (for time travel, legacy, use effective_as_of instead) (optional)
    consistency = 'eventual' # str | Consistency level: 'eventual' or 'STRONG' (optional) (default to 'eventual')
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency (overrides consistency param if True) (optional)

    try:
        # Get Wallet State
        api_response = api_instance.get_wallet_state(tenant_id, pool_id, wallet_id, as_of=as_of, consistency=consistency, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)
        print("The response of V1Api->get_wallet_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_wallet_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Credit pool identifier | 
 **wallet_id** | **str**| Wallet identifier | 
 **as_of** | **datetime**| As-of timestamp (for time travel, legacy, use effective_as_of instead) | [optional] 
 **consistency** | **str**| Consistency level: &#39;eventual&#39; or &#39;STRONG&#39; | [optional] [default to &#39;eventual&#39;]
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency (overrides consistency param if True) | [optional] 

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

# **get_wallet_state_projection_endpoint_v1**
> object get_wallet_state_projection_endpoint_v1(wallet_id, tenant_id, pool_id, as_of=as_of)

Get Wallet State Projection Endpoint

Get wallet state projection (same as POST /project but idempotent).

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp (for time travel) (optional)

    try:
        # Get Wallet State Projection Endpoint
        api_response = api_instance.get_wallet_state_projection_endpoint_v1(wallet_id, tenant_id, pool_id, as_of=as_of)
        print("The response of V1Api->get_wallet_state_projection_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_wallet_state_projection_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **as_of** | **datetime**| As-of timestamp (for time travel) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_subtree**
> object get_wallet_subtree(wallet_id, tenant_id, pool_id, max_depth=max_depth)

Get Wallet Subtree

Materialize wallet subtree starting from root wallet.  Returns all wallets in the hierarchy under the root wallet.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    max_depth = 3 # int | Maximum depth to traverse (optional) (default to 3)

    try:
        # Get Wallet Subtree
        api_response = api_instance.get_wallet_subtree(wallet_id, tenant_id, pool_id, max_depth=max_depth)
        print("The response of V1Api->get_wallet_subtree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->get_wallet_subtree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **max_depth** | **int**| Maximum depth to traverse | [optional] [default to 3]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_lifecycle_event**
> object handle_lifecycle_event(tenant_id, lifecycle_event_request)

Handle Lifecycle Event

Handle a subscription lifecycle event (write-through).  This endpoint: 1. Records the lifecycle event (idempotent) 2. Updates subscriptions_mirror (bitemporal) 3. For CANCELLED events, voids allowance grants (transactional)

### Example


```python
import moolabs
from moolabs.models.lifecycle_event_request import LifecycleEventRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | 
    lifecycle_event_request = moolabs.LifecycleEventRequest() # LifecycleEventRequest | 

    try:
        # Handle Lifecycle Event
        api_response = api_instance.handle_lifecycle_event(tenant_id, lifecycle_event_request)
        print("The response of V1Api->handle_lifecycle_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->handle_lifecycle_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **lifecycle_event_request** | [**LifecycleEventRequest**](LifecycleEventRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_tokens_endpoint**
> object invalidate_tokens_endpoint(invalidate_portal_token_request)

Invalidate Tokens Endpoint

Invalidate portal token(s) by token value or subject.  At least one of token or subject must be provided. Revocation is soft — sets revoked_at, never deletes.

### Example


```python
import moolabs
from moolabs.models.invalidate_portal_token_request import InvalidatePortalTokenRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    invalidate_portal_token_request = moolabs.InvalidatePortalTokenRequest() # InvalidatePortalTokenRequest | 

    try:
        # Invalidate Tokens Endpoint
        api_response = api_instance.invalidate_tokens_endpoint(invalidate_portal_token_request)
        print("The response of V1Api->invalidate_tokens_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->invalidate_tokens_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invalidate_portal_token_request** | [**InvalidatePortalTokenRequest**](InvalidatePortalTokenRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_grants**
> GrantsListResponse list_grants(tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, subject_id=subject_id, subscription_id=subscription_id, feature_key=feature_key, meter_slug=meter_slug, as_of=as_of, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, offset=offset)

List Grants

List grants.  Returns grants for a tenant/pool, optionally filtered by wallet_id, subject_id, subscription_id, feature_key, meter_slug, or as_of timestamp.  If subject_id or subscription_id is provided but tenant_id/pool_id are not, they will be auto-resolved.

### Example


```python
import moolabs
from moolabs.models.grants_list_response import GrantsListResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier (optional if subject_id or subscription_id provided) (optional)
    pool_id = 'pool_id_example' # str | Pool identifier (optional if subject_id or subscription_id provided) (optional)
    wallet_id = 'wallet_id_example' # str | Wallet identifier to filter by (optional)
    subject_id = 'subject_id_example' # str | Subject identifier (for finding wallet, auto-resolves tenant_id/pool_id) (optional)
    subscription_id = 'subscription_id_example' # str | Subscription identifier (filters grants by subscription, auto-resolves tenant_id/pool_id) (optional)
    feature_key = 'feature_key_example' # str | Feature key for scope filtering (optional)
    meter_slug = 'meter_slug_example' # str | Meter slug for scope filtering (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp for time travel (legacy, use effective_as_of instead) (optional)
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency for reads (optional)
    limit = 100 # int | Maximum number of grants to return (optional) (default to 100)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # List Grants
        api_response = api_instance.list_grants(tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, subject_id=subject_id, subscription_id=subscription_id, feature_key=feature_key, meter_slug=meter_slug, as_of=as_of, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, offset=offset)
        print("The response of V1Api->list_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier (optional if subject_id or subscription_id provided) | [optional] 
 **pool_id** | **str**| Pool identifier (optional if subject_id or subscription_id provided) | [optional] 
 **wallet_id** | **str**| Wallet identifier to filter by | [optional] 
 **subject_id** | **str**| Subject identifier (for finding wallet, auto-resolves tenant_id/pool_id) | [optional] 
 **subscription_id** | **str**| Subscription identifier (filters grants by subscription, auto-resolves tenant_id/pool_id) | [optional] 
 **feature_key** | **str**| Feature key for scope filtering | [optional] 
 **meter_slug** | **str**| Meter slug for scope filtering | [optional] 
 **as_of** | **datetime**| As-of timestamp for time travel (legacy, use effective_as_of instead) | [optional] 
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency for reads | [optional] 
 **limit** | **int**| Maximum number of grants to return | [optional] [default to 100]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

[**GrantsListResponse**](GrantsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mappings**
> List[MappingResponse] list_mappings(tenant_id, meter_slug=meter_slug, feature_key=feature_key)

List Mappings

List feature key mappings.  Returns all mappings for the tenant, optionally filtered by meter_slug or feature_key.

### Example


```python
import moolabs
from moolabs.models.mapping_response import MappingResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    meter_slug = 'meter_slug_example' # str | Filter by meter slug (optional)
    feature_key = 'feature_key_example' # str | Filter by feature key (optional)

    try:
        # List Mappings
        api_response = api_instance.list_mappings(tenant_id, meter_slug=meter_slug, feature_key=feature_key)
        print("The response of V1Api->list_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **meter_slug** | **str**| Filter by meter slug | [optional] 
 **feature_key** | **str**| Filter by feature key | [optional] 

### Return type

[**List[MappingResponse]**](MappingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outbox_events_endpoint**
> object list_outbox_events_endpoint(tenant_id=tenant_id, event_type=event_type, status=status, limit=limit)

List Outbox Events Endpoint

List outbox events.  Returns a list of events in the outbox, optionally filtered by tenant, event type, or status.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID (optional)
    event_type = 'event_type_example' # str | Filter by event type (optional)
    status = 'status_example' # str | Filter by status: pending, delivered, failed (optional)
    limit = 100 # int | Maximum events to return (optional) (default to 100)

    try:
        # List Outbox Events Endpoint
        api_response = api_instance.list_outbox_events_endpoint(tenant_id=tenant_id, event_type=event_type, status=status, limit=limit)
        print("The response of V1Api->list_outbox_events_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_outbox_events_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter by tenant ID | [optional] 
 **event_type** | **str**| Filter by event type | [optional] 
 **status** | **str**| Filter by status: pending, delivered, failed | [optional] 
 **limit** | **int**| Maximum events to return | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rules_v1**
> ListAutoTopupRulesResponse list_rules_v1(tenant_id, pool_id, wallet_id=wallet_id)

List Rules

List auto top-up rules.  Returns all rules for a tenant/pool, optionally filtered by wallet_id.

### Example


```python
import moolabs
from moolabs.models.list_auto_topup_rules_response import ListAutoTopupRulesResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier to filter by (optional)

    try:
        # List Rules
        api_response = api_instance.list_rules_v1(tenant_id, pool_id, wallet_id=wallet_id)
        print("The response of V1Api->list_rules_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_rules_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_id** | **str**| Optional wallet identifier to filter by | [optional] 

### Return type

[**ListAutoTopupRulesResponse**](ListAutoTopupRulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots_endpoint**
> object list_snapshots_endpoint(wallet_id, tenant_id, pool_id, limit=limit)

List Snapshots Endpoint

List snapshots for a wallet.  Returns the most recent snapshots first.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    limit = 100 # int | Maximum number of snapshots (optional) (default to 100)

    try:
        # List Snapshots Endpoint
        api_response = api_instance.list_snapshots_endpoint(wallet_id, tenant_id, pool_id, limit=limit)
        print("The response of V1Api->list_snapshots_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_snapshots_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **limit** | **int**| Maximum number of snapshots | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_thresholds_endpoint**
> object list_thresholds_endpoint(wallet_id, tenant_id, pool_id)

List Thresholds Endpoint

List all thresholds for a wallet.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier

    try:
        # List Thresholds Endpoint
        api_response = api_instance.list_thresholds_endpoint(wallet_id, tenant_id, pool_id)
        print("The response of V1Api->list_thresholds_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_thresholds_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokens_endpoint**
> object list_tokens_endpoint(subject=subject)

List Tokens Endpoint

List active portal tokens for tenant (optionally filtered by subject).

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    subject = 'subject_example' # str | Filter by subject (optional)

    try:
        # List Tokens Endpoint
        api_response = api_instance.list_tokens_endpoint(subject=subject)
        print("The response of V1Api->list_tokens_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_tokens_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Filter by subject | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unpriced_events**
> object list_unpriced_events(tenant_id=tenant_id, pool_id=pool_id, limit=limit)

List Unpriced Events

List UNPRICED events.  Returns a list of usage events that are currently UNPRICED.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID (optional)
    pool_id = 'pool_id_example' # str | Filter by pool ID (optional)
    limit = 100 # int | Maximum events to return (optional) (default to 100)

    try:
        # List Unpriced Events
        api_response = api_instance.list_unpriced_events(tenant_id=tenant_id, pool_id=pool_id, limit=limit)
        print("The response of V1Api->list_unpriced_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_unpriced_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter by tenant ID | [optional] 
 **pool_id** | **str**| Filter by pool ID | [optional] 
 **limit** | **int**| Maximum events to return | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_usage_events**
> object list_usage_events(tenant_id=tenant_id, pool_id=pool_id, rating_status=rating_status, feature_key=feature_key, meter_slug=meter_slug, subject_id=subject_id, from_time=from_time, to_time=to_time, limit=limit, offset=offset)

List Usage Events

List usage events with optional filters.  If subject_id is provided but tenant_id/pool_id are not, they will be auto-resolved.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier (optional if subject_id provided) (optional)
    pool_id = 'pool_id_example' # str | Pool identifier (optional if subject_id provided) (optional)
    rating_status = 'rating_status_example' # str | Filter by rating status (optional)
    feature_key = 'feature_key_example' # str | Filter by feature key (optional)
    meter_slug = 'meter_slug_example' # str | Filter by meter slug (optional)
    subject_id = 'subject_id_example' # str | Filter by subject ID (auto-resolves tenant_id/pool_id if not provided) (optional)
    from_time = 'from_time_example' # str | Filter events from this time (ISO 8601, e.g., 2026-02-09T00:48:00Z) (optional)
    to_time = 'to_time_example' # str | Filter events to this time (ISO 8601, e.g., 2026-02-09T00:50:00Z) (optional)
    limit = 100 # int | Maximum number of events to return (optional) (default to 100)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # List Usage Events
        api_response = api_instance.list_usage_events(tenant_id=tenant_id, pool_id=pool_id, rating_status=rating_status, feature_key=feature_key, meter_slug=meter_slug, subject_id=subject_id, from_time=from_time, to_time=to_time, limit=limit, offset=offset)
        print("The response of V1Api->list_usage_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_usage_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier (optional if subject_id provided) | [optional] 
 **pool_id** | **str**| Pool identifier (optional if subject_id provided) | [optional] 
 **rating_status** | **str**| Filter by rating status | [optional] 
 **feature_key** | **str**| Filter by feature key | [optional] 
 **meter_slug** | **str**| Filter by meter slug | [optional] 
 **subject_id** | **str**| Filter by subject ID (auto-resolves tenant_id/pool_id if not provided) | [optional] 
 **from_time** | **str**| Filter events from this time (ISO 8601, e.g., 2026-02-09T00:48:00Z) | [optional] 
 **to_time** | **str**| Filter events to this time (ISO 8601, e.g., 2026-02-09T00:50:00Z) | [optional] 
 **limit** | **int**| Maximum number of events to return | [optional] [default to 100]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wallet_members**
> object list_wallet_members(tenant_id, pool_id, subject_id=subject_id, wallet_id=wallet_id)

List Wallet Members

List wallet members with optional filters.  - Filters by tenant_id and pool_id (required) - Optionally filters by subject_id or wallet_id - Returns list of wallet members matching the filters - Includes resolved tenant_id and pool_id in response headers

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Credit pool identifier
    subject_id = 'subject_id_example' # str | Optional subject_id filter (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet_id filter (optional)

    try:
        # List Wallet Members
        api_response = api_instance.list_wallet_members(tenant_id, pool_id, subject_id=subject_id, wallet_id=wallet_id)
        print("The response of V1Api->list_wallet_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_wallet_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Credit pool identifier | 
 **subject_id** | **str**| Optional subject_id filter | [optional] 
 **wallet_id** | **str**| Optional wallet_id filter | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wallets**
> object list_wallets(tenant_id=tenant_id, pool_id=pool_id, subject_id=subject_id, subscription_id=subscription_id, owner_type=owner_type, owner_id=owner_id, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)

List Wallets

List wallets with optional filters.  - If subscription_id is provided, finds wallets via grants (most direct, no hardcoded resolution) - If subject_id is provided, tenant_id and pool_id are automatically resolved - If neither is provided, tenant_id and pool_id are required - Optionally filters by owner_type and owner_id - Returns list of wallets matching the filters

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier (optional if subject_id or subscription_id provided) (optional)
    pool_id = 'pool_id_example' # str | Credit pool identifier (optional if subject_id or subscription_id provided) (optional)
    subject_id = 'subject_id_example' # str | Subject identifier (if provided, tenant_id and pool_id are auto-resolved) (optional)
    subscription_id = 'subscription_id_example' # str | Subscription identifier (finds wallets via grants with this subscription_id) (optional)
    owner_type = 'owner_type_example' # str | Optional owner_type filter (optional)
    owner_id = 'owner_id_example' # str | Optional owner_id filter (optional)
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency for reads (optional)

    try:
        # List Wallets
        api_response = api_instance.list_wallets(tenant_id=tenant_id, pool_id=pool_id, subject_id=subject_id, subscription_id=subscription_id, owner_type=owner_type, owner_id=owner_id, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)
        print("The response of V1Api->list_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->list_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier (optional if subject_id or subscription_id provided) | [optional] 
 **pool_id** | **str**| Credit pool identifier (optional if subject_id or subscription_id provided) | [optional] 
 **subject_id** | **str**| Subject identifier (if provided, tenant_id and pool_id are auto-resolved) | [optional] 
 **subscription_id** | **str**| Subscription identifier (finds wallets via grants with this subscription_id) | [optional] 
 **owner_type** | **str**| Optional owner_type filter | [optional] 
 **owner_id** | **str**| Optional owner_id filter | [optional] 
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency for reads | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_grant**
> GrantResponse mint_grant(create_grant_request)

Mint Grant

Mint a new credit grant.  Features: - Idempotent minting (UNIQUE constraint on tenant_id, source_id, shard_index) - Scope support (ALL, FEATURE_LIST, METER_LIST) - Rollover configuration - Cost basis (FX locking for paid grants) - Sharding support (for large TOPUP grants)  Returns:     Created or existing grant

### Example


```python
import moolabs
from moolabs.models.create_grant_request import CreateGrantRequest
from moolabs.models.grant_response import GrantResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    create_grant_request = moolabs.CreateGrantRequest() # CreateGrantRequest | 

    try:
        # Mint Grant
        api_response = api_instance.mint_grant(create_grant_request)
        print("The response of V1Api->mint_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->mint_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_grant_request** | [**CreateGrantRequest**](CreateGrantRequest.md)|  | 

### Return type

[**GrantResponse**](GrantResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openmeter_webhook**
> object openmeter_webhook(tenant_id=tenant_id, pool_id=pool_id)

Openmeter Webhook

Handle OpenMeter webhook CloudEvent.  This endpoint receives CloudEvents from OpenMeter and normalizes them into CLS usage events.  **CloudEvent Format:** OpenMeter sends CloudEvents in CloudEvents v1.0 format: ```json {   \"specversion\": \"1.0\",   \"type\": \"usage\",   \"id\": \"event-id-123\",   \"time\": \"2026-01-13T21:00:00Z\",   \"source\": \"https://api.openmeter.io/v1/meters/meter-slug\",   \"subject\": \"customer-id-123\",   \"data\": {     \"value\": 100,     \"meter\": \"meter-slug\",     ...   } } ```  Or wrapped format (API v2): ```json {   \"event\": {     \"specversion\": \"1.0\",     \"type\": \"usage\",     ...   },   \"ingestedAt\": \"...\",   \"storedAt\": \"...\" } ```  **Request Headers:** - `X-OpenMeter-Signature` (optional): Webhook signature for verification  **Query Parameters:** - `tenant_id` (required): Tenant identifier - `pool_id` (required): Credit pool identifier  **Response:** - 201: Event processed successfully - 400: Invalid event format or missing required fields - 500: Processing error  **Idempotency:** - Uses CloudEvent `id` field as idempotency key - Duplicate events are safely ignored (UNIQUE constraint)

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    pool_id = 'pool_id_example' # str |  (optional)

    try:
        # Openmeter Webhook
        api_response = api_instance.openmeter_webhook(tenant_id=tenant_id, pool_id=pool_id)
        print("The response of V1Api->openmeter_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->openmeter_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **pool_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openmeter_webhook_batch**
> object openmeter_webhook_batch(tenant_id=tenant_id, pool_id=pool_id)

Openmeter Webhook Batch

Handle batch of OpenMeter webhook CloudEvents.  Processes multiple CloudEvents in a single request. Each event is processed independently (idempotent).  **Request Body:** ```json {   \"events\": [     { \"specversion\": \"1.0\", \"type\": \"usage\", ... },     { \"specversion\": \"1.0\", \"type\": \"usage\", ... }   ] } ```  **Response:** - 201: All events processed (some may have failed individually) - Results include per-event status  **Query Parameters:** - `tenant_id` (required): Tenant identifier - `pool_id` (required): Credit pool identifier

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    pool_id = 'pool_id_example' # str |  (optional)

    try:
        # Openmeter Webhook Batch
        api_response = api_instance.openmeter_webhook_batch(tenant_id=tenant_id, pool_id=pool_id)
        print("The response of V1Api->openmeter_webhook_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->openmeter_webhook_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **pool_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_rule_v1**
> AutoTopupRuleResponse patch_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)

Patch Rule

Partially update an auto top-up rule (e.g., enable/disable).  This is an alias for PUT - updates the specified fields.

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.models.update_auto_topup_rule_request import UpdateAutoTopupRuleRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier for validation (optional)
    update_auto_topup_rule_request = moolabs.UpdateAutoTopupRuleRequest() # UpdateAutoTopupRuleRequest |  (optional)

    try:
        # Patch Rule
        api_response = api_instance.patch_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)
        print("The response of V1Api->patch_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->patch_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 
 **wallet_id** | **str**| Optional wallet identifier for validation | [optional] 
 **update_auto_topup_rule_request** | [**UpdateAutoTopupRuleRequest**](UpdateAutoTopupRuleRequest.md)|  | [optional] 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_succeeded_v1**
> PaymentSucceededResponse payment_succeeded_v1(payment_succeeded_request)

Payment Succeeded

Handle payment succeeded callback.  This endpoint: - Mints grant with FX locking (idempotent) - Creates CREDIT_MINT journal entry - Emits AUTO_TOPUP_SUCCEEDED outbox event

### Example


```python
import moolabs
from moolabs.models.payment_succeeded_request import PaymentSucceededRequest
from moolabs.models.payment_succeeded_response import PaymentSucceededResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    payment_succeeded_request = moolabs.PaymentSucceededRequest() # PaymentSucceededRequest | 

    try:
        # Payment Succeeded
        api_response = api_instance.payment_succeeded_v1(payment_succeeded_request)
        print("The response of V1Api->payment_succeeded_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->payment_succeeded_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_succeeded_request** | [**PaymentSucceededRequest**](PaymentSucceededRequest.md)|  | 

### Return type

[**PaymentSucceededResponse**](PaymentSucceededResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_events**
> object process_events(tenant_id=tenant_id, pool_id=pool_id, limit=limit, max_attempts=max_attempts)

Process Events

Process multiple UNPRICED events.  This endpoint processes UNPRICED events that are ready for retry, attempting to resolve missing information and re-rate them.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID (optional)
    pool_id = 'pool_id_example' # str | Filter by pool ID (optional)
    limit = 100 # int | Maximum events to process (optional) (default to 100)
    max_attempts = 5 # int | Maximum retry attempts (optional) (default to 5)

    try:
        # Process Events
        api_response = api_instance.process_events(tenant_id=tenant_id, pool_id=pool_id, limit=limit, max_attempts=max_attempts)
        print("The response of V1Api->process_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter by tenant ID | [optional] 
 **pool_id** | **str**| Filter by pool ID | [optional] 
 **limit** | **int**| Maximum events to process | [optional] [default to 100]
 **max_attempts** | **int**| Maximum retry attempts | [optional] [default to 5]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Process Lifecycle Event Manually
        api_response = api_instance.process_lifecycle_event_manually_v1_admin(subscription_id, tenant_id)
        print("The response of V1Api->process_lifecycle_event_manually_v1_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_lifecycle_event_manually_v1_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_outbox_endpoint**
> object process_outbox_endpoint(tenant_id=tenant_id, batch_size=batch_size, max_attempts=max_attempts)

Process Outbox Endpoint

Process outbox events that are ready for delivery.  This endpoint should be called periodically (e.g., by a worker) to deliver notifications and webhooks from the outbox.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    batch_size = 100 # int | Maximum events to process (optional) (default to 100)
    max_attempts = 10 # int | Maximum retry attempts (optional) (default to 10)

    try:
        # Process Outbox Endpoint
        api_response = api_instance.process_outbox_endpoint(tenant_id=tenant_id, batch_size=batch_size, max_attempts=max_attempts)
        print("The response of V1Api->process_outbox_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_outbox_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter | [optional] 
 **batch_size** | **int**| Maximum events to process | [optional] [default to 100]
 **max_attempts** | **int**| Maximum retry attempts | [optional] [default to 10]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_pending_events_v1**
> object process_pending_events_v1(limit=limit, shard_attempt_offset=shard_attempt_offset, tenant_id=tenant_id, pool_id=pool_id)

Process Pending Events

Process pending usage events.  This is a batch processing endpoint that: - Fetches PENDING events - Rates each event - Returns summary  In production, this would be a background worker.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    limit = 10 # int | Number of events to process (optional) (default to 10)
    shard_attempt_offset = 0 # int | Shard attempt offset (optional) (default to 0)
    tenant_id = 'tenant_id_example' # str | Filter by tenant_id (for testing) (optional)
    pool_id = 'pool_id_example' # str | Filter by pool_id (for testing) (optional)

    try:
        # Process Pending Events
        api_response = api_instance.process_pending_events_v1(limit=limit, shard_attempt_offset=shard_attempt_offset, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of V1Api->process_pending_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_pending_events_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of events to process | [optional] [default to 10]
 **shard_attempt_offset** | **int**| Shard attempt offset | [optional] [default to 0]
 **tenant_id** | **str**| Filter by tenant_id (for testing) | [optional] 
 **pool_id** | **str**| Filter by pool_id (for testing) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_pending_projections_endpoint_v1**
> object process_pending_projections_endpoint_v1(tenant_id=tenant_id, pool_id=pool_id, batch_size=batch_size)

Process Pending Projections Endpoint

Process wallets that need state projection.  This endpoint should be called periodically (e.g., by a worker) to project state for wallets impacted by newly sealed journal entries.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    pool_id = 'pool_id_example' # str | Optional pool filter (optional)
    batch_size = 100 # int | Maximum number of wallets to process (optional) (default to 100)

    try:
        # Process Pending Projections Endpoint
        api_response = api_instance.process_pending_projections_endpoint_v1(tenant_id=tenant_id, pool_id=pool_id, batch_size=batch_size)
        print("The response of V1Api->process_pending_projections_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_pending_projections_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter | [optional] 
 **pool_id** | **str**| Optional pool filter | [optional] 
 **batch_size** | **int**| Maximum number of wallets to process | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_rollover**
> RolloverResponse process_rollover(rollover_request)

Process Rollover

Process period-close rollover for a subscription.  This endpoint: - Computes period boundaries based on subscription anchor_at and cadence - Identifies eligible grants with rollover enabled - Calculates rollover amounts (FULL or PARTIAL) - Creates rollover grants - Creates ROLLOVER journal entries - Emits BILLING_CYCLE_CLOSED outbox events  Uses advisory locks to prevent concurrent closes.

### Example


```python
import moolabs
from moolabs.models.rollover_request import RolloverRequest
from moolabs.models.rollover_response import RolloverResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rollover_request = moolabs.RolloverRequest() # RolloverRequest | 

    try:
        # Process Rollover
        api_response = api_instance.process_rollover(rollover_request)
        print("The response of V1Api->process_rollover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_rollover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollover_request** | [**RolloverRequest**](RolloverRequest.md)|  | 

### Return type

[**RolloverResponse**](RolloverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_value_recognition_v1_fx**
> ValueRecognitionResponse process_value_recognition_v1_fx(process_value_recognition_request)

Process Value Recognition

Process burn allocations for a journal entry and create VALUE_RECOGNITION postings.  This endpoint: - Gets all burn allocations for a journal entry - Computes USD value for each allocation (using locked FX rates or effective_at rate) - Creates VALUE_RECOGNITION postings in USD

### Example


```python
import moolabs
from moolabs.models.process_value_recognition_request import ProcessValueRecognitionRequest
from moolabs.models.value_recognition_response import ValueRecognitionResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    process_value_recognition_request = moolabs.ProcessValueRecognitionRequest() # ProcessValueRecognitionRequest | 

    try:
        # Process Value Recognition
        api_response = api_instance.process_value_recognition_v1_fx(process_value_recognition_request)
        print("The response of V1Api->process_value_recognition_v1_fx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->process_value_recognition_v1_fx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_value_recognition_request** | [**ProcessValueRecognitionRequest**](ProcessValueRecognitionRequest.md)|  | 

### Return type

[**ValueRecognitionResponse**](ValueRecognitionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_wallet_state_endpoint_v1**
> object project_wallet_state_endpoint_v1(wallet_id, tenant_id, pool_id, as_of=as_of)

Project Wallet State Endpoint

Project wallet state for a specific wallet.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp (for time travel) (optional)

    try:
        # Project Wallet State Endpoint
        api_response = api_instance.project_wallet_state_endpoint_v1(wallet_id, tenant_id, pool_id, as_of=as_of)
        print("The response of V1Api->project_wallet_state_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->project_wallet_state_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **as_of** | **datetime**| As-of timestamp (for time travel) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_event**
> object rate_event(usage_event_id)

Rate Event

Rate a single usage event.  This endpoint processes a PENDING usage event and creates: - Journal entry - Postings - Burn allocations - Updates grants  Also supports retrying events with retryable statuses: - UNPRICED: Can be retried if rate card is added - QUARANTINED: Can be retried if guardrails are adjusted - WAITING_FUNDS: Can be retried if funds are added  Returns:     Created journal entry or error

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    usage_event_id = 'usage_event_id_example' # str | 

    try:
        # Rate Event
        api_response = api_instance.rate_event(usage_event_id)
        print("The response of V1Api->rate_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->rate_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_event_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_usage**
> object record_usage(record_usage_request)

Record Usage

Record a usage event.  Features: - Idempotent recording (UNIQUE constraint on tenant_id, usage_event_id) - Automatic wallet resolution from subject_id - Usage fingerprint generation for duplicate detection - Event normalization (usage_vector → canonical JSON)  The event will be queued for rating (status: PENDING). A background worker will process it and create journal entries.  Returns:     Created or existing usage event

### Example


```python
import moolabs
from moolabs.models.record_usage_request import RecordUsageRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    record_usage_request = moolabs.RecordUsageRequest() # RecordUsageRequest | 

    try:
        # Record Usage
        api_response = api_instance.record_usage(record_usage_request)
        print("The response of V1Api->record_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->record_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_usage_request** | [**RecordUsageRequest**](RecordUsageRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_event**
> object resolve_event(usage_event_id, max_attempts=max_attempts)

Resolve Event

Resolve a single UNPRICED usage event.  This endpoint attempts to: - Retry wallet resolution - Retry subscription binding - Retry feature mapping - Re-attempt rating if resolution succeeds - Move to QUARANTINED if max attempts reached

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    usage_event_id = 'usage_event_id_example' # str | 
    max_attempts = 5 # int | Maximum retry attempts (optional) (default to 5)

    try:
        # Resolve Event
        api_response = api_instance.resolve_event(usage_event_id, max_attempts=max_attempts)
        print("The response of V1Api->resolve_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->resolve_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_event_id** | **str**|  | 
 **max_attempts** | **int**| Maximum retry attempts | [optional] [default to 5]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_tenant_and_pool**
> object resolve_tenant_and_pool(subject_id)

Resolve Tenant And Pool

Resolve tenant_id and pool_id for a given subject_id.  This endpoint automatically finds the tenant_id and pool_id for a customer/subject by looking up their wallet memberships. This allows the UI to query wallets/grants without requiring the user to manually configure tenant_id and pool_id.  Returns:     {         \"tenant_id\": \"uuid\",         \"pool_id\": \"uuid\" (Global Credits pool for the tenant)     }

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    subject_id = 'subject_id_example' # str | Subject identifier (customer ID or subject key)

    try:
        # Resolve Tenant And Pool
        api_response = api_instance.resolve_tenant_and_pool(subject_id)
        print("The response of V1Api->resolve_tenant_and_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->resolve_tenant_and_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Subject identifier (customer ID or subject key) | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    retry_unpriced_request = moolabs.RetryUnpricedRequest() # RetryUnpricedRequest | 

    try:
        # Retry Unpriced
        api_response = api_instance.retry_unpriced(retry_unpriced_request)
        print("The response of V1Api->retry_unpriced:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->retry_unpriced: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retry_unpriced_request** | [**RetryUnpricedRequest**](RetryUnpricedRequest.md)|  | 

### Return type

[**RetryUnpricedResponse**](RetryUnpricedResponse.md)

### Authorization

No authorization required

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


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    review_quarantined_request = moolabs.ReviewQuarantinedRequest() # ReviewQuarantinedRequest | 

    try:
        # Review Quarantined
        api_response = api_instance.review_quarantined(review_quarantined_request)
        print("The response of V1Api->review_quarantined:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->review_quarantined: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **review_quarantined_request** | [**ReviewQuarantinedRequest**](ReviewQuarantinedRequest.md)|  | 

### Return type

[**ReviewQuarantinedResponse**](ReviewQuarantinedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_subscription**
> object sync_subscription(tenant_id, subscription_sync_request)

Sync Subscription

Sync a subscription from OpenMeter to subscriptions_mirror.  This endpoint performs a bitemporal update: - Closes any existing row (sets effective_to) - Creates a new row with new effective_from

### Example


```python
import moolabs
from moolabs.models.subscription_sync_request import SubscriptionSyncRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | 
    subscription_sync_request = moolabs.SubscriptionSyncRequest() # SubscriptionSyncRequest | 

    try:
        # Sync Subscription
        api_response = api_instance.sync_subscription(tenant_id, subscription_sync_request)
        print("The response of V1Api->sync_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->sync_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **subscription_sync_request** | [**SubscriptionSyncRequest**](SubscriptionSyncRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

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


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    subscription_id = 'subscription_id_example' # str | Subscription ID to sync

    try:
        # Trigger Subscription Sync
        api_response = api_instance.trigger_subscription_sync(subscription_id)
        print("The response of V1Api->trigger_subscription_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->trigger_subscription_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription ID to sync | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule_v1**
> AutoTopupRuleResponse update_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)

Update Rule

Update an auto top-up rule.  Updates the specified fields of an existing rule.

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.models.update_auto_topup_rule_request import UpdateAutoTopupRuleRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier for validation (optional)
    update_auto_topup_rule_request = moolabs.UpdateAutoTopupRuleRequest() # UpdateAutoTopupRuleRequest |  (optional)

    try:
        # Update Rule
        api_response = api_instance.update_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)
        print("The response of V1Api->update_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 
 **wallet_id** | **str**| Optional wallet identifier for validation | [optional] 
 **update_auto_topup_rule_request** | [**UpdateAutoTopupRuleRequest**](UpdateAutoTopupRuleRequest.md)|  | [optional] 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_threshold_endpoint**
> object update_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id, update_threshold_request)

Update Threshold Endpoint

Update a wallet threshold.

### Example


```python
import moolabs
from moolabs.models.update_threshold_request import UpdateThresholdRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    threshold_id = 'threshold_id_example' # str | 
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    update_threshold_request = moolabs.UpdateThresholdRequest() # UpdateThresholdRequest | 

    try:
        # Update Threshold Endpoint
        api_response = api_instance.update_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id, update_threshold_request)
        print("The response of V1Api->update_threshold_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_threshold_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threshold_id** | **str**|  | 
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **update_threshold_request** | [**UpdateThresholdRequest**](UpdateThresholdRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wallet_settings**
> WalletResponse update_wallet_settings(wallet_id, update_wallet_settings_request, tenant_id=tenant_id, pool_id=pool_id)

Update Wallet Settings

Update wallet settings.  Updates parent_wallet_id, local_hard_cap_micros, and/or policy. - Setting parent_wallet_id to null detaches the wallet from hierarchy - Setting local_hard_cap_micros to null removes the override (reverts to inherited) - Policy controls at-cap behavior (SOFT_BORROW, HARD_BUDGET, NOTIFY_ONLY)

### Example


```python
import moolabs
from moolabs.models.update_wallet_settings_request import UpdateWalletSettingsRequest
from moolabs.models.wallet_response import WalletResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 
    update_wallet_settings_request = moolabs.UpdateWalletSettingsRequest() # UpdateWalletSettingsRequest | 
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)

    try:
        # Update Wallet Settings
        api_response = api_instance.update_wallet_settings(wallet_id, update_wallet_settings_request, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of V1Api->update_wallet_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_wallet_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **update_wallet_settings_request** | [**UpdateWalletSettingsRequest**](UpdateWalletSettingsRequest.md)|  | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wallet_thresholds**
> WalletResponse update_wallet_thresholds(wallet_id, update_wallet_thresholds_request, tenant_id=tenant_id, pool_id=pool_id)

Update Wallet Thresholds

Update wallet thresholds.  Updates local_soft_threshold_micros and/or local_hard_cap_micros. Setting a value to null removes the wallet override (reverts to inherited).

### Example


```python
import moolabs
from moolabs.models.update_wallet_thresholds_request import UpdateWalletThresholdsRequest
from moolabs.models.wallet_response import WalletResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    wallet_id = 'wallet_id_example' # str | 
    update_wallet_thresholds_request = moolabs.UpdateWalletThresholdsRequest() # UpdateWalletThresholdsRequest | 
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)

    try:
        # Update Wallet Thresholds
        api_response = api_instance.update_wallet_thresholds(wallet_id, update_wallet_thresholds_request, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of V1Api->update_wallet_thresholds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->update_wallet_thresholds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **update_wallet_thresholds_request** | [**UpdateWalletThresholdsRequest**](UpdateWalletThresholdsRequest.md)|  | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_snapshot_endpoint**
> ValidationResponse validate_snapshot_endpoint(snapshot_id)

Validate Snapshot Endpoint

Validate a balance snapshot by recomputing the balance and fingerprint.  This recomputes the balance at the snapshot's cut times and compares the fingerprint to ensure data integrity.

### Example


```python
import moolabs
from moolabs.models.validation_response import ValidationResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    snapshot_id = 'snapshot_id_example' # str | Snapshot identifier

    try:
        # Validate Snapshot Endpoint
        api_response = api_instance.validate_snapshot_endpoint(snapshot_id)
        print("The response of V1Api->validate_snapshot_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->validate_snapshot_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot identifier | 

### Return type

[**ValidationResponse**](ValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_grant**
> GrantResponse void_grant(grant_id, void_grant_request)

Void Grant

Void a grant.  This marks the grant as voided, making the remaining credits unavailable. The grant cannot be un-voided.

### Example


```python
import moolabs
from moolabs.models.grant_response import GrantResponse
from moolabs.models.void_grant_request import VoidGrantRequest
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    grant_id = 'grant_id_example' # str | 
    void_grant_request = moolabs.VoidGrantRequest() # VoidGrantRequest | 

    try:
        # Void Grant
        api_response = api_instance.void_grant(grant_id, void_grant_request)
        print("The response of V1Api->void_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->void_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  | 
 **void_grant_request** | [**VoidGrantRequest**](VoidGrantRequest.md)|  | 

### Return type

[**GrantResponse**](GrantResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warm_rate_card_cache_v1**
> object warm_rate_card_cache_v1(tenant_id=tenant_id, limit=limit)

Warm Rate Card Cache

Warm Dragonfly cache with active rate cards.  Pre-loads rate card data for frequently used features.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    limit = 50 # int | Maximum number of rate cards to warm (optional) (default to 50)

    try:
        # Warm Rate Card Cache
        api_response = api_instance.warm_rate_card_cache_v1(tenant_id=tenant_id, limit=limit)
        print("The response of V1Api->warm_rate_card_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->warm_rate_card_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter | [optional] 
 **limit** | **int**| Maximum number of rate cards to warm | [optional] [default to 50]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warm_wallet_cache**
> object warm_wallet_cache(tenant_id=tenant_id, pool_id=pool_id, limit=limit)

Warm Wallet Cache

Warm Dragonfly cache with hot wallet projections.  Pre-loads wallet balance projections for frequently accessed wallets.

### Example


```python
import moolabs
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.V1Api(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    pool_id = 'pool_id_example' # str | Optional pool filter (optional)
    limit = 100 # int | Maximum number of wallets to warm (optional) (default to 100)

    try:
        # Warm Wallet Cache
        api_response = api_instance.warm_wallet_cache(tenant_id=tenant_id, pool_id=pool_id, limit=limit)
        print("The response of V1Api->warm_wallet_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling V1Api->warm_wallet_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter | [optional] 
 **pool_id** | **str**| Optional pool filter | [optional] 
 **limit** | **int**| Maximum number of wallets to warm | [optional] [default to 100]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

