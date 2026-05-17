# moolabs.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report_endpoint**](ReportsApi.md#create_report_endpoint) | **POST** /v1/arc/reports | Create Report Endpoint
[**download_report_endpoint**](ReportsApi.md#download_report_endpoint) | **GET** /v1/arc/reports/{report_id}/download | Download Report Endpoint


# **create_report_endpoint**
> ReportCreateResponse create_report_endpoint(x_api_key, report_create_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id, x_user_id=x_user_id, x_arc_roles=x_arc_roles)

Create Report Endpoint

### Example


```python
import moolabs
from moolabs.models.report_create_request import ReportCreateRequest
from moolabs.models.report_create_response import ReportCreateResponse
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
    api_instance = moolabs.ReportsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    report_create_request = moolabs.ReportCreateRequest() # ReportCreateRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)

    try:
        # Create Report Endpoint
        api_response = api_instance.create_report_endpoint(x_api_key, report_create_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id, x_user_id=x_user_id, x_arc_roles=x_arc_roles)
        print("The response of ReportsApi->create_report_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->create_report_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **report_create_request** | [**ReportCreateRequest**](ReportCreateRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 

### Return type

[**ReportCreateResponse**](ReportCreateResponse.md)

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

# **download_report_endpoint**
> object download_report_endpoint(report_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Download Report Endpoint

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
    api_instance = moolabs.ReportsApi(api_client)
    report_id = 'report_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Download Report Endpoint
        api_response = api_instance.download_report_endpoint(report_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ReportsApi->download_report_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->download_report_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

