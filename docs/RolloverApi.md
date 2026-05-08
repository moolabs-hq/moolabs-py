# moolabs.RolloverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_rollover**](RolloverApi.md#process_rollover) | **POST** /v1/rollover/process | Process Rollover


# **process_rollover**
> RolloverResponse process_rollover(rollover_request)

Process Rollover

Process period-close rollover for a subscription.  This endpoint: - Computes period boundaries based on subscription anchor_at and cadence - Identifies eligible grants with rollover enabled - Calculates rollover amounts (FULL or PARTIAL) - Creates rollover grants - Creates ROLLOVER journal entries - Emits BILLING_CYCLE_CLOSED outbox events  Uses advisory locks to prevent concurrent closes.

### Example


```python
import moolabs
from moolabs.models.rollover_request import RolloverRequest
from moolabs.models.rollover_response import RolloverResponse
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
    api_instance = moolabs.RolloverApi(api_client)
    rollover_request = moolabs.RolloverRequest() # RolloverRequest | 

    try:
        # Process Rollover
        api_response = api_instance.process_rollover(rollover_request)
        print("The response of RolloverApi->process_rollover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolloverApi->process_rollover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollover_request** | [**RolloverRequest**](RolloverRequest.md)|  | 

### Return type

[**RolloverResponse**](RolloverResponse.md)

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

