# moolabs.InternalPlanPricingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_plan_pricing_v1**](InternalPlanPricingApi.md#sync_plan_pricing_v1) | **POST** /v1/internal/plan-pricing/sync | Sync Plan Pricing


# **sync_plan_pricing_v1**
> object sync_plan_pricing_v1(plan_pricing_sync_request, authorization=authorization)

Sync Plan Pricing

### Example


```python
import moolabs
from moolabs.models.plan_pricing_sync_request import PlanPricingSyncRequest
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
    api_instance = moolabs.InternalPlanPricingApi(api_client)
    plan_pricing_sync_request = moolabs.PlanPricingSyncRequest() # PlanPricingSyncRequest | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Sync Plan Pricing
        api_response = api_instance.sync_plan_pricing_v1(plan_pricing_sync_request, authorization=authorization)
        print("The response of InternalPlanPricingApi->sync_plan_pricing_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalPlanPricingApi->sync_plan_pricing_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_pricing_sync_request** | [**PlanPricingSyncRequest**](PlanPricingSyncRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

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

