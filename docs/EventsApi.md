# moolabs.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_events**](EventsApi.md#ingest_events) | **POST** /api/v1/events | Ingest events  
[**list_events**](EventsApi.md#list_events) | **GET** /api/v1/events | List ingested events
[**list_events_v2**](EventsApi.md#list_events_v2) | **GET** /api/v2/events | List ingested events


# **ingest_events**
> ingest_events(event)

Ingest events  

Ingests an event or batch of events following the CloudEvents specification.

### Example


```python
import moolabs
from moolabs.models.event import Event
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
    api_instance = moolabs.EventsApi(api_client)
    event = moolabs.Event() # Event | 

    try:
        # Ingest events  
        api_instance.ingest_events(event)
    except Exception as e:
        print("Exception when calling EventsApi->ingest_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event** | [**Event**](Event.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/cloudevents+json, application/cloudevents-batch+json, application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> List[IngestedEvent] list_events(client_id=client_id, ingested_at_from=ingested_at_from, ingested_at_to=ingested_at_to, id=id, subject=subject, customer_id=customer_id, var_from=var_from, to=to, limit=limit)

List ingested events

List ingested events within a time range.  If the from query param is not provided it defaults to last 72 hours.

### Example


```python
import moolabs
from moolabs.models.ingested_event import IngestedEvent
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
    api_instance = moolabs.EventsApi(api_client)
    client_id = 'client_id_example' # str | Client ID Useful to track progress of a query. (optional)
    ingested_at_from = '2013-10-20T19:20:30+01:00' # datetime | Start date-time in RFC 3339 format.  Inclusive. (optional)
    ingested_at_to = '2013-10-20T19:20:30+01:00' # datetime | End date-time in RFC 3339 format.  Inclusive. (optional)
    id = 'id_example' # str | The event ID.  Accepts partial ID. (optional)
    subject = 'subject_example' # str | The event subject.  Accepts partial subject. (optional)
    customer_id = ['customer_id_example'] # List[str] | The event customer ID. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Start date-time in RFC 3339 format.  Inclusive. (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | End date-time in RFC 3339 format.  Inclusive. (optional)
    limit = 100 # int | Number of events to return. (optional) (default to 100)

    try:
        # List ingested events
        api_response = api_instance.list_events(client_id=client_id, ingested_at_from=ingested_at_from, ingested_at_to=ingested_at_to, id=id, subject=subject, customer_id=customer_id, var_from=var_from, to=to, limit=limit)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client ID Useful to track progress of a query. | [optional] 
 **ingested_at_from** | **datetime**| Start date-time in RFC 3339 format.  Inclusive. | [optional] 
 **ingested_at_to** | **datetime**| End date-time in RFC 3339 format.  Inclusive. | [optional] 
 **id** | **str**| The event ID.  Accepts partial ID. | [optional] 
 **subject** | **str**| The event subject.  Accepts partial subject. | [optional] 
 **customer_id** | [**List[str]**](str.md)| The event customer ID. | [optional] 
 **var_from** | **datetime**| Start date-time in RFC 3339 format.  Inclusive. | [optional] 
 **to** | **datetime**| End date-time in RFC 3339 format.  Inclusive. | [optional] 
 **limit** | **int**| Number of events to return. | [optional] [default to 100]

### Return type

[**List[IngestedEvent]**](IngestedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events_v2**
> IngestedEventCursorPaginatedResponse list_events_v2(cursor=cursor, limit=limit, client_id=client_id, filter=filter)

List ingested events

List ingested events with advanced filtering and cursor pagination.

### Example


```python
import moolabs
from moolabs.models.ingested_event_cursor_paginated_response import IngestedEventCursorPaginatedResponse
from moolabs.models.list_events_v2_filter_param import ListEventsV2FilterParam
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
    api_instance = moolabs.EventsApi(api_client)
    cursor = 'cursor_example' # str | The cursor after which to start the pagination. (optional)
    limit = 100 # int | The limit of the pagination. (optional) (default to 100)
    client_id = 'client_id_example' # str | Client ID Useful to track progress of a query. (optional)
    filter = moolabs.ListEventsV2FilterParam() # ListEventsV2FilterParam | The filter for the events encoded as JSON string. (optional)

    try:
        # List ingested events
        api_response = api_instance.list_events_v2(cursor=cursor, limit=limit, client_id=client_id, filter=filter)
        print("The response of EventsApi->list_events_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The cursor after which to start the pagination. | [optional] 
 **limit** | **int**| The limit of the pagination. | [optional] [default to 100]
 **client_id** | **str**| Client ID Useful to track progress of a query. | [optional] 
 **filter** | [**ListEventsV2FilterParam**](.md)| The filter for the events encoded as JSON string. | [optional] 

### Return type

[**IngestedEventCursorPaginatedResponse**](IngestedEventCursorPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

