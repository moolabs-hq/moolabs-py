# moolabs.CostEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_event**](CostEventsApi.md#ingest_event) | **POST** /api/v1/cost/ingest | Ingest Cost Event
[**ingest_events_batch**](CostEventsApi.md#ingest_events_batch) | **POST** /api/v1/cost/ingest/batch | Batch Ingest Cost Events
[**list_cost_event_summaries_by_usage_event_api_v1**](CostEventsApi.md#list_cost_event_summaries_by_usage_event_api_v1) | **POST** /api/v1/cost/events/by-usage-event/summary | List Cost Event Summaries By Usage Event
[**list_cost_events_by_usage_event_api_v1**](CostEventsApi.md#list_cost_events_by_usage_event_api_v1) | **GET** /api/v1/cost/events/by-usage-event/{usage_event_id} | List Cost Events By Usage Event
[**list_cost_events_by_usage_event_query_api_v1**](CostEventsApi.md#list_cost_events_by_usage_event_query_api_v1) | **GET** /api/v1/cost/events/by-usage-event | List Cost Events By Usage Event Query
[**submit_adjustment**](CostEventsApi.md#submit_adjustment) | **POST** /api/v1/cost/adjustments | Submit Adjustment


# **ingest_event**
> CostEventResponse ingest_event(cost_event_ingest)

Ingest Cost Event

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.cost_event_ingest import CostEventIngest
from moolabs.models.cost_event_response import CostEventResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CostEventsApi(api_client)
    cost_event_ingest = moolabs.CostEventIngest() # CostEventIngest | 

    try:
        # Ingest Cost Event
        api_response = api_instance.ingest_event(cost_event_ingest)
        print("The response of CostEventsApi->ingest_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostEventsApi->ingest_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_event_ingest** | [**CostEventIngest**](CostEventIngest.md)|  | 

### Return type

[**CostEventResponse**](CostEventResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_events_batch**
> object ingest_events_batch(batch_ingest_request)

Batch Ingest Cost Events

Batch ingest cost events. Returns summary with inserted/duplicate counts.  Returns HTTP 207 Multi-Status when some events failed, 200 when all succeeded.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.batch_ingest_request import BatchIngestRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CostEventsApi(api_client)
    batch_ingest_request = moolabs.BatchIngestRequest() # BatchIngestRequest | 

    try:
        # Batch Ingest Cost Events
        api_response = api_instance.ingest_events_batch(batch_ingest_request)
        print("The response of CostEventsApi->ingest_events_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostEventsApi->ingest_events_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_ingest_request** | [**BatchIngestRequest**](BatchIngestRequest.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cost_event_summaries_by_usage_event_api_v1**
> CostEventSummaryResponse list_cost_event_summaries_by_usage_event_api_v1(x_tenant_id, cost_event_summary_request)

List Cost Event Summaries By Usage Event

Return compact cost summaries for a page of external usage event IDs.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.cost_event_summary_request import CostEventSummaryRequest
from moolabs.models.cost_event_summary_response import CostEventSummaryResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CostEventsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | Tenant UUID
    cost_event_summary_request = moolabs.CostEventSummaryRequest() # CostEventSummaryRequest | 

    try:
        # List Cost Event Summaries By Usage Event
        api_response = api_instance.list_cost_event_summaries_by_usage_event_api_v1(x_tenant_id, cost_event_summary_request)
        print("The response of CostEventsApi->list_cost_event_summaries_by_usage_event_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostEventsApi->list_cost_event_summaries_by_usage_event_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**| Tenant UUID | 
 **cost_event_summary_request** | [**CostEventSummaryRequest**](CostEventSummaryRequest.md)|  | 

### Return type

[**CostEventSummaryResponse**](CostEventSummaryResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cost_events_by_usage_event_api_v1**
> List[CostEventDetailResponse] list_cost_events_by_usage_event_api_v1(usage_event_id, x_tenant_id)

List Cost Events By Usage Event

Return all cost events and line items for one external usage event.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.cost_event_detail_response import CostEventDetailResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CostEventsApi(api_client)
    usage_event_id = 'usage_event_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | Tenant UUID

    try:
        # List Cost Events By Usage Event
        api_response = api_instance.list_cost_events_by_usage_event_api_v1(usage_event_id, x_tenant_id)
        print("The response of CostEventsApi->list_cost_events_by_usage_event_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostEventsApi->list_cost_events_by_usage_event_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_event_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant UUID | 

### Return type

[**List[CostEventDetailResponse]**](CostEventDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cost_events_by_usage_event_query_api_v1**
> List[CostEventDetailResponse] list_cost_events_by_usage_event_query_api_v1(usage_event_id, x_tenant_id)

List Cost Events By Usage Event Query

Return all cost events and line items for one external usage event.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.cost_event_detail_response import CostEventDetailResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CostEventsApi(api_client)
    usage_event_id = 'usage_event_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | Tenant UUID

    try:
        # List Cost Events By Usage Event Query
        api_response = api_instance.list_cost_events_by_usage_event_query_api_v1(usage_event_id, x_tenant_id)
        print("The response of CostEventsApi->list_cost_events_by_usage_event_query_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostEventsApi->list_cost_events_by_usage_event_query_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_event_id** | **str**|  | 
 **x_tenant_id** | **str**| Tenant UUID | 

### Return type

[**List[CostEventDetailResponse]**](CostEventDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_adjustment**
> CostAdjustmentResponse submit_adjustment(cost_adjustment_create)

Submit Adjustment

Submit an append-only cost correction.  T-21 (sdk-cost-capability-acute-backing rev 3 / CONTRACT-Q1 RESOLVED): if payload.external_adjustment_id is provided, dedup on (tenant_id, external_adjustment_id) — a re-POST returns the original 201 row. Without the field, the endpoint stays append-only.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.cost_adjustment_create import CostAdjustmentCreate
from moolabs.models.cost_adjustment_response import CostAdjustmentResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CostEventsApi(api_client)
    cost_adjustment_create = moolabs.CostAdjustmentCreate() # CostAdjustmentCreate | 

    try:
        # Submit Adjustment
        api_response = api_instance.submit_adjustment(cost_adjustment_create)
        print("The response of CostEventsApi->submit_adjustment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostEventsApi->submit_adjustment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_adjustment_create** | [**CostAdjustmentCreate**](CostAdjustmentCreate.md)|  | 

### Return type

[**CostAdjustmentResponse**](CostAdjustmentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

