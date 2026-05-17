# moolabs.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retry_remediation_event**](BillingApi.md#retry_remediation_event) | **POST** /v1/billing/remediation/events/{usage_event_id}/retry | Retry Remediation Event


# **retry_remediation_event**
> object retry_remediation_event(usage_event_id)

Retry Remediation Event

Retry a manual-required/resolved event through async financial pipeline.

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
    api_instance = moolabs.BillingApi(api_client)
    usage_event_id = 'usage_event_id_example' # str | 

    try:
        # Retry Remediation Event
        api_response = api_instance.retry_remediation_event(usage_event_id)
        print("The response of BillingApi->retry_remediation_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retry_remediation_event: %s\n" % e)
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

