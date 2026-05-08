# moolabs.UsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_event**](UsageApi.md#get_usage_event) | **GET** /v1/usage/{event_id} | Get Usage Event
[**list_usage_events**](UsageApi.md#list_usage_events) | **GET** /v1/usage/ | List Usage Events
[**record_usage**](UsageApi.md#record_usage) | **POST** /v1/usage/record | Record Usage


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
    api_instance = moolabs.UsageApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get Usage Event
        api_response = api_instance.get_usage_event(event_id)
        print("The response of UsageApi->get_usage_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_usage_event: %s\n" % e)
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
    api_instance = moolabs.UsageApi(api_client)
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
        print("The response of UsageApi->list_usage_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->list_usage_events: %s\n" % e)
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
    api_instance = moolabs.UsageApi(api_client)
    record_usage_request = moolabs.RecordUsageRequest() # RecordUsageRequest | 

    try:
        # Record Usage
        api_response = api_instance.record_usage(record_usage_request)
        print("The response of UsageApi->record_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->record_usage: %s\n" % e)
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

