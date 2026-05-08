# moolabs.UnpricedApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_unpriced_events**](UnpricedApi.md#list_unpriced_events) | **GET** /v1/unpriced/events | List Unpriced Events
[**process_events**](UnpricedApi.md#process_events) | **POST** /v1/unpriced/process | Process Events
[**resolve_event**](UnpricedApi.md#resolve_event) | **POST** /v1/unpriced/resolve/{usage_event_id} | Resolve Event


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
    api_instance = moolabs.UnpricedApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID (optional)
    pool_id = 'pool_id_example' # str | Filter by pool ID (optional)
    limit = 100 # int | Maximum events to return (optional) (default to 100)

    try:
        # List Unpriced Events
        api_response = api_instance.list_unpriced_events(tenant_id=tenant_id, pool_id=pool_id, limit=limit)
        print("The response of UnpricedApi->list_unpriced_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnpricedApi->list_unpriced_events: %s\n" % e)
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
    api_instance = moolabs.UnpricedApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID (optional)
    pool_id = 'pool_id_example' # str | Filter by pool ID (optional)
    limit = 100 # int | Maximum events to process (optional) (default to 100)
    max_attempts = 5 # int | Maximum retry attempts (optional) (default to 5)

    try:
        # Process Events
        api_response = api_instance.process_events(tenant_id=tenant_id, pool_id=pool_id, limit=limit, max_attempts=max_attempts)
        print("The response of UnpricedApi->process_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnpricedApi->process_events: %s\n" % e)
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
    api_instance = moolabs.UnpricedApi(api_client)
    usage_event_id = 'usage_event_id_example' # str | 
    max_attempts = 5 # int | Maximum retry attempts (optional) (default to 5)

    try:
        # Resolve Event
        api_response = api_instance.resolve_event(usage_event_id, max_attempts=max_attempts)
        print("The response of UnpricedApi->resolve_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnpricedApi->resolve_event: %s\n" % e)
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

