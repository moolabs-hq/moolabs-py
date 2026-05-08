# moolabs.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /v1/subscriptions/{subscription_id} | Get Subscription
[**handle_lifecycle_event**](SubscriptionsApi.md#handle_lifecycle_event) | **POST** /v1/subscriptions/lifecycle | Handle Lifecycle Event
[**sync_subscription**](SubscriptionsApi.md#sync_subscription) | **POST** /v1/subscriptions/sync | Sync Subscription


# **get_subscription**
> object get_subscription(subscription_id, tenant_id, as_of=as_of)

Get Subscription

Get subscription mirror as-of a specific time (bitemporal query).  Args:     subscription_id: Subscription ID     tenant_id: Tenant ID (query parameter)     as_of: Optional ISO 8601 datetime (defaults to now)

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
    api_instance = moolabs.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | 
    as_of = 'as_of_example' # str |  (optional)

    try:
        # Get Subscription
        api_response = api_instance.get_subscription(subscription_id, tenant_id, as_of=as_of)
        print("The response of SubscriptionsApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **tenant_id** | **str**|  | 
 **as_of** | **str**|  | [optional] 

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

# **handle_lifecycle_event**
> object handle_lifecycle_event(tenant_id, lifecycle_event_request)

Handle Lifecycle Event

Handle a subscription lifecycle event (write-through).  This endpoint: 1. Records the lifecycle event (idempotent) 2. Updates subscriptions_mirror (bitemporal) 3. For CANCELLED events, voids allowance grants (transactional)

### Example


```python
import moolabs
from moolabs.models.lifecycle_event_request import LifecycleEventRequest
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
    api_instance = moolabs.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    lifecycle_event_request = moolabs.LifecycleEventRequest() # LifecycleEventRequest | 

    try:
        # Handle Lifecycle Event
        api_response = api_instance.handle_lifecycle_event(tenant_id, lifecycle_event_request)
        print("The response of SubscriptionsApi->handle_lifecycle_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->handle_lifecycle_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **lifecycle_event_request** | [**LifecycleEventRequest**](LifecycleEventRequest.md)|  | 

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

# **sync_subscription**
> object sync_subscription(tenant_id, subscription_sync_request)

Sync Subscription

Sync a subscription from OpenMeter to subscriptions_mirror.  This endpoint performs a bitemporal update: - Closes any existing row (sets effective_to) - Creates a new row with new effective_from

### Example


```python
import moolabs
from moolabs.models.subscription_sync_request import SubscriptionSyncRequest
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
    api_instance = moolabs.SubscriptionsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    subscription_sync_request = moolabs.SubscriptionSyncRequest() # SubscriptionSyncRequest | 

    try:
        # Sync Subscription
        api_response = api_instance.sync_subscription(tenant_id, subscription_sync_request)
        print("The response of SubscriptionsApi->sync_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->sync_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **subscription_sync_request** | [**SubscriptionSyncRequest**](SubscriptionSyncRequest.md)|  | 

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

