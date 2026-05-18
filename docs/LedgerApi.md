# moolabs.LedgerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_audit**](LedgerApi.md#get_ledger_audit) | **GET** /v1/ledger/audit | Get Ledger Audit
[**get_ledger_balance**](LedgerApi.md#get_ledger_balance) | **GET** /v1/ledger/balance | Get Ledger Balance
[**get_wallet_state**](LedgerApi.md#get_wallet_state) | **GET** /v1/ledger/state | Get Wallet State
[**get_wallet_states_batch**](LedgerApi.md#get_wallet_states_batch) | **POST** /v1/ledger/state/batch | Get Wallet States Batch


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
    api_instance = moolabs.LedgerApi(api_client)
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
        print("The response of LedgerApi->get_ledger_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_ledger_audit: %s\n" % e)
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
    api_instance = moolabs.LedgerApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    as_of_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Effective timestamp (for time travel)
    as_of_recorded_at = '2013-10-20T19:20:30+01:00' # datetime | Recorded timestamp (for time travel) (optional)

    try:
        # Get Ledger Balance
        api_response = api_instance.get_ledger_balance(tenant_id, pool_id, wallet_id, as_of_effective_at, as_of_recorded_at=as_of_recorded_at)
        print("The response of LedgerApi->get_ledger_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_ledger_balance: %s\n" % e)
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

# **get_wallet_state**
> object get_wallet_state(wallet_id, tenant_id=tenant_id, pool_id=pool_id, as_of=as_of, consistency=consistency, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)

Get Wallet State

Get wallet state (balance and credit state).  - Eventually consistent by default (fast, uses denormalized remaining_micros) - STRONG consistency available for admin/debug (slower, uses state projection) - Returns balance, state (OK/LOW/OVERDRAFT/OVER_CAP), and metadata - Includes last_projected_at and projected_from_recorded_cut for STRONG consistency - Sets cache headers for eventual consistency reads

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
    api_instance = moolabs.LedgerApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier (resolved from auth when absent) (optional)
    pool_id = 'pool_id_example' # str | Credit pool identifier (resolved from auth when absent) (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp (for time travel, legacy, use effective_as_of instead) (optional)
    consistency = 'eventual' # str | Consistency level: 'eventual' or 'STRONG' (optional) (default to 'eventual')
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency (overrides consistency param if True) (optional)

    try:
        # Get Wallet State
        api_response = api_instance.get_wallet_state(wallet_id, tenant_id=tenant_id, pool_id=pool_id, as_of=as_of, consistency=consistency, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)
        print("The response of LedgerApi->get_wallet_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_wallet_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier (resolved from auth when absent) | [optional] 
 **pool_id** | **str**| Credit pool identifier (resolved from auth when absent) | [optional] 
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

# **get_wallet_states_batch**
> BatchWalletStateResponse get_wallet_states_batch(batch_wallet_state_request)

Get Wallet States Batch

Get states for multiple wallets in a single request.  This endpoint allows fetching wallet states (balance, state) for multiple wallets in a single API call, which is much more efficient than making individual requests.  - Supports up to 100 wallets per request - Eventually consistent by default (fast, uses denormalized remaining_micros) - STRONG consistency available for admin/debug (slower, uses state projection) - Returns states and any errors separately

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.batch_wallet_state_request import BatchWalletStateRequest
from moolabs.models.batch_wallet_state_response import BatchWalletStateResponse
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
    api_instance = moolabs.LedgerApi(api_client)
    batch_wallet_state_request = moolabs.BatchWalletStateRequest() # BatchWalletStateRequest | 

    try:
        # Get Wallet States Batch
        api_response = api_instance.get_wallet_states_batch(batch_wallet_state_request)
        print("The response of LedgerApi->get_wallet_states_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerApi->get_wallet_states_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_wallet_state_request** | [**BatchWalletStateRequest**](BatchWalletStateRequest.md)|  | 

### Return type

[**BatchWalletStateResponse**](BatchWalletStateResponse.md)

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

