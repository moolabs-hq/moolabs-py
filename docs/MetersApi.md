# moolabs.MetersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meter**](MetersApi.md#create_meter) | **POST** /api/v1/meters | Create meter
[**delete_meter**](MetersApi.md#delete_meter) | **DELETE** /api/v1/meters/{meterIdOrSlug} | Delete meter
[**get_meter**](MetersApi.md#get_meter) | **GET** /api/v1/meters/{meterIdOrSlug} | Get meter
[**get_usage_summary**](MetersApi.md#get_usage_summary) | **GET** /api/v1/usage/summary | Get multi-meter usage summary
[**list_meter_group_by_values**](MetersApi.md#list_meter_group_by_values) | **GET** /api/v1/meters/{meterIdOrSlug}/group-by/{groupByKey}/values | List meter group by values
[**list_meter_subjects**](MetersApi.md#list_meter_subjects) | **GET** /api/v1/meters/{meterIdOrSlug}/subjects | List meter subjects
[**list_meters**](MetersApi.md#list_meters) | **GET** /api/v1/meters | List meters
[**query_meter**](MetersApi.md#query_meter) | **GET** /api/v1/meters/{meterIdOrSlug}/query | Query meter
[**query_meter_post**](MetersApi.md#query_meter_post) | **POST** /api/v1/meters/{meterIdOrSlug}/query | Query meter
[**test_meter_event**](MetersApi.md#test_meter_event) | **POST** /api/v1/meters/{meterIdOrSlug}/test-event | Validate a sample event payload against the meter
[**update_meter**](MetersApi.md#update_meter) | **PUT** /api/v1/meters/{meterIdOrSlug} | Update meter


# **create_meter**
> Meter create_meter(meter_create)

Create meter

Create a meter.

### Example


```python
import moolabs
from moolabs.models.meter import Meter
from moolabs.models.meter_create import MeterCreate
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
    api_instance = moolabs.MetersApi(api_client)
    meter_create = moolabs.MeterCreate() # MeterCreate | 

    try:
        # Create meter
        api_response = api_instance.create_meter(meter_create)
        print("The response of MetersApi->create_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->create_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_create** | [**MeterCreate**](MeterCreate.md)|  | 

### Return type

[**Meter**](Meter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meter**
> delete_meter(meter_id_or_slug)

Delete meter

Delete a meter.

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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 

    try:
        # Delete meter
        api_instance.delete_meter(meter_id_or_slug)
    except Exception as e:
        print("Exception when calling MetersApi->delete_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **get_meter**
> Meter get_meter(meter_id_or_slug)

Get meter

Get a meter by ID or slug.

### Example


```python
import moolabs
from moolabs.models.meter import Meter
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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 

    try:
        # Get meter
        api_response = api_instance.get_meter(meter_id_or_slug)
        print("The response of MetersApi->get_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->get_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 

### Return type

[**Meter**](Meter.md)

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
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_summary**
> MeterUsageSummaryResponse get_usage_summary(subject, var_from, to, window_size=window_size, meter_slugs=meter_slugs)

Get multi-meter usage summary

Returns usage across all meters for a subject in a single query. Reads from pre-aggregated materialized views. Meters with unsupported aggregation types (MIN, MAX, UNIQUE_COUNT, LATEST) are omitted until the aggregation table is extended.

### Example


```python
import moolabs
from moolabs.models.meter_usage_summary_response import MeterUsageSummaryResponse
from moolabs.models.usage_summary_window_size import UsageSummaryWindowSize
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
    api_instance = moolabs.MetersApi(api_client)
    subject = 'subject_example' # str | The subject to query usage for (required).
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start of the time range (RFC 3339, required).
    to = '2023-01-01T01:01:01.001Z' # datetime | End of the time range (RFC 3339, required).
    window_size = moolabs.UsageSummaryWindowSize() # UsageSummaryWindowSize | Window size for breakdown. Omit for totals only. (optional)
    meter_slugs = ['meter_slugs_example'] # List[str] | Filter to specific meter slugs. Omit to query all meters. (optional)

    try:
        # Get multi-meter usage summary
        api_response = api_instance.get_usage_summary(subject, var_from, to, window_size=window_size, meter_slugs=meter_slugs)
        print("The response of MetersApi->get_usage_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->get_usage_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| The subject to query usage for (required). | 
 **var_from** | **datetime**| Start of the time range (RFC 3339, required). | 
 **to** | **datetime**| End of the time range (RFC 3339, required). | 
 **window_size** | [**UsageSummaryWindowSize**](.md)| Window size for breakdown. Omit for totals only. | [optional] 
 **meter_slugs** | [**List[str]**](str.md)| Filter to specific meter slugs. Omit to query all meters. | [optional] 

### Return type

[**MeterUsageSummaryResponse**](MeterUsageSummaryResponse.md)

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

# **list_meter_group_by_values**
> List[str] list_meter_group_by_values(meter_id_or_slug, group_by_key, var_from=var_from, to=to)

List meter group by values

List meter group by values.

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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 
    group_by_key = 'group_by_key_example' # str | 
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start date-time in RFC 3339 format.  Inclusive. Defaults to 24 hours ago.  For example: ?from=2025-01-01T00%3A00%3A00.000Z (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End date-time in RFC 3339 format.  Inclusive.  For example: ?to=2025-02-01T00%3A00%3A00.000Z (optional)

    try:
        # List meter group by values
        api_response = api_instance.list_meter_group_by_values(meter_id_or_slug, group_by_key, var_from=var_from, to=to)
        print("The response of MetersApi->list_meter_group_by_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->list_meter_group_by_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 
 **group_by_key** | **str**|  | 
 **var_from** | **datetime**| Start date-time in RFC 3339 format.  Inclusive. Defaults to 24 hours ago.  For example: ?from&#x3D;2025-01-01T00%3A00%3A00.000Z | [optional] 
 **to** | **datetime**| End date-time in RFC 3339 format.  Inclusive.  For example: ?to&#x3D;2025-02-01T00%3A00%3A00.000Z | [optional] 

### Return type

**List[str]**

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

# **list_meter_subjects**
> List[str] list_meter_subjects(meter_id_or_slug, var_from=var_from, to=to)

List meter subjects

List subjects for a meter.

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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start date-time in RFC 3339 format.  Inclusive. Defaults to the beginning of time.  For example: ?from=2025-01-01T00%3A00%3A00.000Z (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End date-time in RFC 3339 format.  Inclusive.  For example: ?to=2025-02-01T00%3A00%3A00.000Z (optional)

    try:
        # List meter subjects
        api_response = api_instance.list_meter_subjects(meter_id_or_slug, var_from=var_from, to=to)
        print("The response of MetersApi->list_meter_subjects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->list_meter_subjects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 
 **var_from** | **datetime**| Start date-time in RFC 3339 format.  Inclusive. Defaults to the beginning of time.  For example: ?from&#x3D;2025-01-01T00%3A00%3A00.000Z | [optional] 
 **to** | **datetime**| End date-time in RFC 3339 format.  Inclusive.  For example: ?to&#x3D;2025-02-01T00%3A00%3A00.000Z | [optional] 

### Return type

**List[str]**

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

# **list_meters**
> List[Meter] list_meters(page=page, page_size=page_size, order=order, order_by=order_by, include_deleted=include_deleted)

List meters

List meters.

### Example


```python
import moolabs
from moolabs.models.meter import Meter
from moolabs.models.meter_order_by import MeterOrderBy
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.MetersApi(api_client)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.MeterOrderBy() # MeterOrderBy | The order by field. (optional)
    include_deleted = False # bool | Include deleted meters. (optional) (default to False)

    try:
        # List meters
        api_response = api_instance.list_meters(page=page, page_size=page_size, order=order, order_by=order_by, include_deleted=include_deleted)
        print("The response of MetersApi->list_meters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->list_meters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**MeterOrderBy**](.md)| The order by field. | [optional] 
 **include_deleted** | **bool**| Include deleted meters. | [optional] [default to False]

### Return type

[**List[Meter]**](Meter.md)

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

# **query_meter**
> MeterQueryResult query_meter(meter_id_or_slug, client_id=client_id, var_from=var_from, to=to, window_size=window_size, window_time_zone=window_time_zone, subject=subject, filter_customer_id=filter_customer_id, filter_group_by=filter_group_by, advanced_meter_group_by_filters=advanced_meter_group_by_filters, group_by=group_by)

Query meter

Query meter for usage.

### Example


```python
import moolabs
from moolabs.models.filter_string import FilterString
from moolabs.models.meter_query_result import MeterQueryResult
from moolabs.models.window_size import WindowSize
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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 
    client_id = 'client_id_example' # str | Client ID Useful to track progress of a query. (optional)
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start date-time in RFC 3339 format.  Inclusive.  For example: ?from=2025-01-01T00%3A00%3A00.000Z (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End date-time in RFC 3339 format.  Inclusive.  For example: ?to=2025-02-01T00%3A00%3A00.000Z (optional)
    window_size = moolabs.WindowSize() # WindowSize | If not specified, a single usage aggregate will be returned for the entirety of the specified period for each subject and group.  For example: ?windowSize=DAY (optional)
    window_time_zone = 'UTC' # str | The value is the name of the time zone as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). If not specified, the UTC timezone will be used.  For example: ?windowTimeZone=UTC (optional) (default to 'UTC')
    subject = ['subject_example'] # List[str] | Filtering by multiple subjects.  For example: ?subject=subject-1&subject=subject-2 (optional)
    filter_customer_id = ['filter_customer_id_example'] # List[str] | Filtering by multiple customers.  For example: ?filterCustomerId=customer-1&filterCustomerId=customer-2 (optional)
    filter_group_by = {'key': 'filter_group_by_example'} # Dict[str, str] | Simple filter for group bys with exact match.  For example: ?filterGroupBy[vendor]=openai&filterGroupBy[model]=gpt-4-turbo (optional)
    advanced_meter_group_by_filters = {'key': moolabs.FilterString()} # Dict[str, FilterString] | Optional advanced meter group by filters. You can use this to filter for values of the meter groupBy fields. (optional)
    group_by = ['group_by_example'] # List[str] | If not specified a single aggregate will be returned for each subject and time window. `subject` is a reserved group by value.  For example: ?groupBy=subject&groupBy=model (optional)

    try:
        # Query meter
        api_response = api_instance.query_meter(meter_id_or_slug, client_id=client_id, var_from=var_from, to=to, window_size=window_size, window_time_zone=window_time_zone, subject=subject, filter_customer_id=filter_customer_id, filter_group_by=filter_group_by, advanced_meter_group_by_filters=advanced_meter_group_by_filters, group_by=group_by)
        print("The response of MetersApi->query_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->query_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 
 **client_id** | **str**| Client ID Useful to track progress of a query. | [optional] 
 **var_from** | **datetime**| Start date-time in RFC 3339 format.  Inclusive.  For example: ?from&#x3D;2025-01-01T00%3A00%3A00.000Z | [optional] 
 **to** | **datetime**| End date-time in RFC 3339 format.  Inclusive.  For example: ?to&#x3D;2025-02-01T00%3A00%3A00.000Z | [optional] 
 **window_size** | [**WindowSize**](.md)| If not specified, a single usage aggregate will be returned for the entirety of the specified period for each subject and group.  For example: ?windowSize&#x3D;DAY | [optional] 
 **window_time_zone** | **str**| The value is the name of the time zone as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). If not specified, the UTC timezone will be used.  For example: ?windowTimeZone&#x3D;UTC | [optional] [default to &#39;UTC&#39;]
 **subject** | [**List[str]**](str.md)| Filtering by multiple subjects.  For example: ?subject&#x3D;subject-1&amp;subject&#x3D;subject-2 | [optional] 
 **filter_customer_id** | [**List[str]**](str.md)| Filtering by multiple customers.  For example: ?filterCustomerId&#x3D;customer-1&amp;filterCustomerId&#x3D;customer-2 | [optional] 
 **filter_group_by** | [**Dict[str, str]**](str.md)| Simple filter for group bys with exact match.  For example: ?filterGroupBy[vendor]&#x3D;openai&amp;filterGroupBy[model]&#x3D;gpt-4-turbo | [optional] 
 **advanced_meter_group_by_filters** | [**Dict[str, FilterString]**](FilterString.md)| Optional advanced meter group by filters. You can use this to filter for values of the meter groupBy fields. | [optional] 
 **group_by** | [**List[str]**](str.md)| If not specified a single aggregate will be returned for each subject and time window. &#x60;subject&#x60; is a reserved group by value.  For example: ?groupBy&#x3D;subject&amp;groupBy&#x3D;model | [optional] 

### Return type

[**MeterQueryResult**](MeterQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_meter_post**
> MeterQueryResult query_meter_post(meter_id_or_slug, meter_query_request)

Query meter

### Example


```python
import moolabs
from moolabs.models.meter_query_request import MeterQueryRequest
from moolabs.models.meter_query_result import MeterQueryResult
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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 
    meter_query_request = moolabs.MeterQueryRequest() # MeterQueryRequest | 

    try:
        # Query meter
        api_response = api_instance.query_meter_post(meter_id_or_slug, meter_query_request)
        print("The response of MetersApi->query_meter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->query_meter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 
 **meter_query_request** | [**MeterQueryRequest**](MeterQueryRequest.md)|  | 

### Return type

[**MeterQueryResult**](MeterQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_meter_event**
> TestMeterEvent200Response test_meter_event(meter_id_or_slug, test_meter_event_request)

Validate a sample event payload against the meter

Validate a sample event payload against the meter's local JSONPath extraction rules.

### Example


```python
import moolabs
from moolabs.models.test_meter_event200_response import TestMeterEvent200Response
from moolabs.models.test_meter_event_request import TestMeterEventRequest
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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 
    test_meter_event_request = moolabs.TestMeterEventRequest() # TestMeterEventRequest | 

    try:
        # Validate a sample event payload against the meter
        api_response = api_instance.test_meter_event(meter_id_or_slug, test_meter_event_request)
        print("The response of MetersApi->test_meter_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->test_meter_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 
 **test_meter_event_request** | [**TestMeterEventRequest**](TestMeterEventRequest.md)|  | 

### Return type

[**TestMeterEvent200Response**](TestMeterEvent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meter**
> Meter update_meter(meter_id_or_slug, meter_update)

Update meter

Update a meter.

### Example


```python
import moolabs
from moolabs.models.meter import Meter
from moolabs.models.meter_update import MeterUpdate
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
    api_instance = moolabs.MetersApi(api_client)
    meter_id_or_slug = 'meter_id_or_slug_example' # str | 
    meter_update = moolabs.MeterUpdate() # MeterUpdate | 

    try:
        # Update meter
        api_response = api_instance.update_meter(meter_id_or_slug, meter_update)
        print("The response of MetersApi->update_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->update_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_id_or_slug** | **str**|  | 
 **meter_update** | [**MeterUpdate**](MeterUpdate.md)|  | 

### Return type

[**Meter**](Meter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

