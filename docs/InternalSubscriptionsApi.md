# moolabs.InternalSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_subscription_post**](InternalSubscriptionsApi.md#sync_subscription_post) | **POST** /v1/internal/subscriptions/sync | Sync Subscription


# **sync_subscription_post**
> object sync_subscription_post(app_api_v1_internal_subscription_sync_schemas_subscription_sync_request, authorization=authorization)

Sync Subscription

### Example


```python
import moolabs
from moolabs.models.app_api_v1_internal_subscription_sync_schemas_subscription_sync_request import AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest
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
    api_instance = moolabs.InternalSubscriptionsApi(api_client)
    app_api_v1_internal_subscription_sync_schemas_subscription_sync_request = moolabs.AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest() # AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Sync Subscription
        api_response = api_instance.sync_subscription_post(app_api_v1_internal_subscription_sync_schemas_subscription_sync_request, authorization=authorization)
        print("The response of InternalSubscriptionsApi->sync_subscription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalSubscriptionsApi->sync_subscription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_api_v1_internal_subscription_sync_schemas_subscription_sync_request** | [**AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest**](AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest.md)|  | 
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

