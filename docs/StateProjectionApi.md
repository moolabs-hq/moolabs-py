# moolabs.StateProjectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wallet_state_projection_endpoint_v1**](StateProjectionApi.md#get_wallet_state_projection_endpoint_v1) | **GET** /v1/state-projection/wallet/{wallet_id} | Get Wallet State Projection Endpoint
[**process_pending_projections_endpoint_v1**](StateProjectionApi.md#process_pending_projections_endpoint_v1) | **POST** /v1/state-projection/process | Process Pending Projections Endpoint
[**project_wallet_state_endpoint_v1**](StateProjectionApi.md#project_wallet_state_endpoint_v1) | **POST** /v1/state-projection/project/{wallet_id} | Project Wallet State Endpoint


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
    api_instance = moolabs.StateProjectionApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp (for time travel) (optional)

    try:
        # Get Wallet State Projection Endpoint
        api_response = api_instance.get_wallet_state_projection_endpoint_v1(wallet_id, tenant_id, pool_id, as_of=as_of)
        print("The response of StateProjectionApi->get_wallet_state_projection_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateProjectionApi->get_wallet_state_projection_endpoint_v1: %s\n" % e)
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
    api_instance = moolabs.StateProjectionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    pool_id = 'pool_id_example' # str | Optional pool filter (optional)
    batch_size = 100 # int | Maximum number of wallets to process (optional) (default to 100)

    try:
        # Process Pending Projections Endpoint
        api_response = api_instance.process_pending_projections_endpoint_v1(tenant_id=tenant_id, pool_id=pool_id, batch_size=batch_size)
        print("The response of StateProjectionApi->process_pending_projections_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateProjectionApi->process_pending_projections_endpoint_v1: %s\n" % e)
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
    api_instance = moolabs.StateProjectionApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp (for time travel) (optional)

    try:
        # Project Wallet State Endpoint
        api_response = api_instance.project_wallet_state_endpoint_v1(wallet_id, tenant_id, pool_id, as_of=as_of)
        print("The response of StateProjectionApi->project_wallet_state_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StateProjectionApi->project_wallet_state_endpoint_v1: %s\n" % e)
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

