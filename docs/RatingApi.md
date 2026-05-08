# moolabs.RatingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_pending_events_v1**](RatingApi.md#process_pending_events_v1) | **POST** /v1/rating/process-pending | Process Pending Events
[**rate_event**](RatingApi.md#rate_event) | **POST** /v1/rating/rate/{usage_event_id} | Rate Event


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
    api_instance = moolabs.RatingApi(api_client)
    limit = 10 # int | Number of events to process (optional) (default to 10)
    shard_attempt_offset = 0 # int | Shard attempt offset (optional) (default to 0)
    tenant_id = 'tenant_id_example' # str | Filter by tenant_id (for testing) (optional)
    pool_id = 'pool_id_example' # str | Filter by pool_id (for testing) (optional)

    try:
        # Process Pending Events
        api_response = api_instance.process_pending_events_v1(limit=limit, shard_attempt_offset=shard_attempt_offset, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of RatingApi->process_pending_events_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->process_pending_events_v1: %s\n" % e)
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
    api_instance = moolabs.RatingApi(api_client)
    usage_event_id = 'usage_event_id_example' # str | 

    try:
        # Rate Event
        api_response = api_instance.rate_event(usage_event_id)
        print("The response of RatingApi->rate_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->rate_event: %s\n" % e)
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

