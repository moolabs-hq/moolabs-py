# moolabs.OutboxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_outbox_events_endpoint**](OutboxApi.md#list_outbox_events_endpoint) | **GET** /v1/outbox/events | List Outbox Events Endpoint
[**process_outbox_endpoint**](OutboxApi.md#process_outbox_endpoint) | **POST** /v1/outbox/process | Process Outbox Endpoint


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
    api_instance = moolabs.OutboxApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID (optional)
    event_type = 'event_type_example' # str | Filter by event type (optional)
    status = 'status_example' # str | Filter by status: pending, delivered, failed (optional)
    limit = 100 # int | Maximum events to return (optional) (default to 100)

    try:
        # List Outbox Events Endpoint
        api_response = api_instance.list_outbox_events_endpoint(tenant_id=tenant_id, event_type=event_type, status=status, limit=limit)
        print("The response of OutboxApi->list_outbox_events_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboxApi->list_outbox_events_endpoint: %s\n" % e)
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
    api_instance = moolabs.OutboxApi(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    batch_size = 100 # int | Maximum events to process (optional) (default to 100)
    max_attempts = 10 # int | Maximum retry attempts (optional) (default to 10)

    try:
        # Process Outbox Endpoint
        api_response = api_instance.process_outbox_endpoint(tenant_id=tenant_id, batch_size=batch_size, max_attempts=max_attempts)
        print("The response of OutboxApi->process_outbox_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutboxApi->process_outbox_endpoint: %s\n" % e)
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

