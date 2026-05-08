# moolabs.MeterPortalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_portal_token**](MeterPortalApi.md#create_portal_token) | **POST** /api/v1/portal/tokens | Create consumer portal token
[**invalidate_portal_tokens**](MeterPortalApi.md#invalidate_portal_tokens) | **POST** /api/v1/portal/tokens/invalidate | Invalidate portal tokens
[**list_portal_tokens**](MeterPortalApi.md#list_portal_tokens) | **GET** /api/v1/portal/tokens | List consumer portal tokens
[**query_portal_meter**](MeterPortalApi.md#query_portal_meter) | **GET** /api/v1/portal/meters/{meterSlug}/query | Query meter Query meter


# **create_portal_token**
> PortalToken create_portal_token(portal_token)

Create consumer portal token

Create a consumer portal token.

### Example


```python
import moolabs
from moolabs.models.portal_token import PortalToken
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
    api_instance = moolabs.MeterPortalApi(api_client)
    portal_token = moolabs.PortalToken() # PortalToken | 

    try:
        # Create consumer portal token
        api_response = api_instance.create_portal_token(portal_token)
        print("The response of MeterPortalApi->create_portal_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterPortalApi->create_portal_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_token** | [**PortalToken**](PortalToken.md)|  | 

### Return type

[**PortalToken**](PortalToken.md)

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

# **invalidate_portal_tokens**
> invalidate_portal_tokens(invalidate_portal_tokens_request)

Invalidate portal tokens

Invalidates consumer portal tokens by ID or subject.

### Example


```python
import moolabs
from moolabs.models.invalidate_portal_tokens_request import InvalidatePortalTokensRequest
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
    api_instance = moolabs.MeterPortalApi(api_client)
    invalidate_portal_tokens_request = moolabs.InvalidatePortalTokensRequest() # InvalidatePortalTokensRequest | 

    try:
        # Invalidate portal tokens
        api_instance.invalidate_portal_tokens(invalidate_portal_tokens_request)
    except Exception as e:
        print("Exception when calling MeterPortalApi->invalidate_portal_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invalidate_portal_tokens_request** | [**InvalidatePortalTokensRequest**](InvalidatePortalTokensRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **list_portal_tokens**
> List[PortalToken] list_portal_tokens(limit=limit)

List consumer portal tokens

List tokens.

### Example


```python
import moolabs
from moolabs.models.portal_token import PortalToken
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
    api_instance = moolabs.MeterPortalApi(api_client)
    limit = 25 # int |  (optional) (default to 25)

    try:
        # List consumer portal tokens
        api_response = api_instance.list_portal_tokens(limit=limit)
        print("The response of MeterPortalApi->list_portal_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterPortalApi->list_portal_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 25]

### Return type

[**List[PortalToken]**](PortalToken.md)

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

# **query_portal_meter**
> MeterQueryResult query_portal_meter(meter_slug, client_id=client_id, var_from=var_from, to=to, window_size=window_size, window_time_zone=window_time_zone, filter_customer_id=filter_customer_id, filter_group_by=filter_group_by, advanced_meter_group_by_filters=advanced_meter_group_by_filters, group_by=group_by)

Query meter Query meter

Query meter for consumer portal. This endpoint is publicly exposable to consumers. Query meter for consumer portal. This endpoint is publicly exposable to consumers.

### Example

* Bearer Authentication (PortalTokenAuth):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: PortalTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterPortalApi(api_client)
    meter_slug = 'meter_slug_example' # str | 
    client_id = 'client_id_example' # str | Client ID Useful to track progress of a query. (optional)
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start date-time in RFC 3339 format.  Inclusive.  For example: ?from=2025-01-01T00%3A00%3A00.000Z (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End date-time in RFC 3339 format.  Inclusive.  For example: ?to=2025-02-01T00%3A00%3A00.000Z (optional)
    window_size = moolabs.WindowSize() # WindowSize | If not specified, a single usage aggregate will be returned for the entirety of the specified period for each subject and group.  For example: ?windowSize=DAY (optional)
    window_time_zone = 'UTC' # str | The value is the name of the time zone as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). If not specified, the UTC timezone will be used.  For example: ?windowTimeZone=UTC (optional) (default to 'UTC')
    filter_customer_id = ['filter_customer_id_example'] # List[str] | Filtering by multiple customers.  For example: ?filterCustomerId=customer-1&filterCustomerId=customer-2 (optional)
    filter_group_by = {'key': 'filter_group_by_example'} # Dict[str, str] | Simple filter for group bys with exact match.  For example: ?filterGroupBy[vendor]=openai&filterGroupBy[model]=gpt-4-turbo (optional)
    advanced_meter_group_by_filters = {'key': moolabs.FilterString()} # Dict[str, FilterString] | Optional advanced meter group by filters. You can use this to filter for values of the meter groupBy fields. (optional)
    group_by = ['group_by_example'] # List[str] | If not specified a single aggregate will be returned for each subject and time window. `subject` is a reserved group by value.  For example: ?groupBy=subject&groupBy=model (optional)

    try:
        # Query meter Query meter
        api_response = api_instance.query_portal_meter(meter_slug, client_id=client_id, var_from=var_from, to=to, window_size=window_size, window_time_zone=window_time_zone, filter_customer_id=filter_customer_id, filter_group_by=filter_group_by, advanced_meter_group_by_filters=advanced_meter_group_by_filters, group_by=group_by)
        print("The response of MeterPortalApi->query_portal_meter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterPortalApi->query_portal_meter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_slug** | **str**|  | 
 **client_id** | **str**| Client ID Useful to track progress of a query. | [optional] 
 **var_from** | **datetime**| Start date-time in RFC 3339 format.  Inclusive.  For example: ?from&#x3D;2025-01-01T00%3A00%3A00.000Z | [optional] 
 **to** | **datetime**| End date-time in RFC 3339 format.  Inclusive.  For example: ?to&#x3D;2025-02-01T00%3A00%3A00.000Z | [optional] 
 **window_size** | [**WindowSize**](.md)| If not specified, a single usage aggregate will be returned for the entirety of the specified period for each subject and group.  For example: ?windowSize&#x3D;DAY | [optional] 
 **window_time_zone** | **str**| The value is the name of the time zone as defined in the IANA Time Zone Database (http://www.iana.org/time-zones). If not specified, the UTC timezone will be used.  For example: ?windowTimeZone&#x3D;UTC | [optional] [default to &#39;UTC&#39;]
 **filter_customer_id** | [**List[str]**](str.md)| Filtering by multiple customers.  For example: ?filterCustomerId&#x3D;customer-1&amp;filterCustomerId&#x3D;customer-2 | [optional] 
 **filter_group_by** | [**Dict[str, str]**](str.md)| Simple filter for group bys with exact match.  For example: ?filterGroupBy[vendor]&#x3D;openai&amp;filterGroupBy[model]&#x3D;gpt-4-turbo | [optional] 
 **advanced_meter_group_by_filters** | [**Dict[str, FilterString]**](FilterString.md)| Optional advanced meter group by filters. You can use this to filter for values of the meter groupBy fields. | [optional] 
 **group_by** | [**List[str]**](str.md)| If not specified a single aggregate will be returned for each subject and time window. &#x60;subject&#x60; is a reserved group by value.  For example: ?groupBy&#x3D;subject&amp;groupBy&#x3D;model | [optional] 

### Return type

[**MeterQueryResult**](MeterQueryResult.md)

### Authorization

[PortalTokenAuth](../README.md#PortalTokenAuth)

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

