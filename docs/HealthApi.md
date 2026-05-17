# moolabs.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readiness_check**](HealthApi.md#readiness_check) | **GET** /health/ready | Readiness Check


# **readiness_check**
> object readiness_check()

Readiness Check

Readiness probe — returns 200 only when DB is available.

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
    api_instance = moolabs.HealthApi(api_client)

    try:
        # Readiness Check
        api_response = api_instance.readiness_check()
        print("The response of HealthApi->readiness_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->readiness_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

