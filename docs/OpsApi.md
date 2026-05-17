# moolabs.OpsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deep_health_check**](OpsApi.md#deep_health_check) | **GET** /health/deep | Deep Health Check


# **deep_health_check**
> Dict[str, object] deep_health_check(x_metrics_token=x_metrics_token)

Deep Health Check

Authenticated dependency readiness check for operator diagnostics.

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
    api_instance = moolabs.OpsApi(api_client)
    x_metrics_token = 'x_metrics_token_example' # str |  (optional)

    try:
        # Deep Health Check
        api_response = api_instance.deep_health_check(x_metrics_token=x_metrics_token)
        print("The response of OpsApi->deep_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpsApi->deep_health_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_metrics_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

