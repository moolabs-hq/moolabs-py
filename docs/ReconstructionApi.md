# moolabs.ReconstructionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reconstruction_run**](ReconstructionApi.md#create_reconstruction_run) | **POST** /v1/reconstruction/runs | Create Reconstruction Run
[**get_affected_events_endpoint_v1**](ReconstructionApi.md#get_affected_events_endpoint_v1) | **GET** /v1/reconstruction/affected-events | Get Affected Events Endpoint
[**get_late_events_v1**](ReconstructionApi.md#get_late_events_v1) | **GET** /v1/reconstruction/late-events | Get Late Events
[**get_wallet_subtree**](ReconstructionApi.md#get_wallet_subtree) | **GET** /v1/reconstruction/wallets/{wallet_id}/subtree | Get Wallet Subtree


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
    api_instance = moolabs.ReconstructionApi(api_client)
    create_reconstruction_run_request = moolabs.CreateReconstructionRunRequest() # CreateReconstructionRunRequest | 

    try:
        # Create Reconstruction Run
        api_response = api_instance.create_reconstruction_run(create_reconstruction_run_request)
        print("The response of ReconstructionApi->create_reconstruction_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconstructionApi->create_reconstruction_run: %s\n" % e)
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
    api_instance = moolabs.ReconstructionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_ids = 'wallet_ids_example' # str | Comma-separated wallet IDs
    from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Start of effective time window
    to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | End of effective time window

    try:
        # Get Affected Events Endpoint
        api_response = api_instance.get_affected_events_endpoint_v1(tenant_id, pool_id, wallet_ids, from_effective_at, to_effective_at)
        print("The response of ReconstructionApi->get_affected_events_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconstructionApi->get_affected_events_endpoint_v1: %s\n" % e)
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
    api_instance = moolabs.ReconstructionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    late_threshold_seconds = 3600 # int | LATE event threshold (seconds) (optional) (default to 3600)

    try:
        # Get Late Events
        api_response = api_instance.get_late_events_v1(tenant_id, pool_id, late_threshold_seconds=late_threshold_seconds)
        print("The response of ReconstructionApi->get_late_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconstructionApi->get_late_events_v1: %s\n" % e)
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
    api_instance = moolabs.ReconstructionApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    max_depth = 3 # int | Maximum depth to traverse (optional) (default to 3)

    try:
        # Get Wallet Subtree
        api_response = api_instance.get_wallet_subtree(wallet_id, tenant_id, pool_id, max_depth=max_depth)
        print("The response of ReconstructionApi->get_wallet_subtree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReconstructionApi->get_wallet_subtree: %s\n" % e)
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

