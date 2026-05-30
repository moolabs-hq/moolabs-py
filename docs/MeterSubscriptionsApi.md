# moolabs.MeterSubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription**](MeterSubscriptionsApi.md#cancel_subscription) | **POST** /api/v1/subscriptions/{subscriptionId}/cancel | Cancel subscription
[**change_subscription**](MeterSubscriptionsApi.md#change_subscription) | **POST** /api/v1/subscriptions/{subscriptionId}/change | Change subscription
[**create_subscription**](MeterSubscriptionsApi.md#create_subscription) | **POST** /api/v1/subscriptions | Create subscription
[**create_subscription_addon**](MeterSubscriptionsApi.md#create_subscription_addon) | **POST** /api/v1/subscriptions/{subscriptionId}/addons | Create subscription addon
[**delete_subscription**](MeterSubscriptionsApi.md#delete_subscription) | **DELETE** /api/v1/subscriptions/{subscriptionId} | Delete subscription
[**edit_subscription**](MeterSubscriptionsApi.md#edit_subscription) | **PATCH** /api/v1/subscriptions/{subscriptionId} | Edit subscription
[**get_subscription_addon**](MeterSubscriptionsApi.md#get_subscription_addon) | **GET** /api/v1/subscriptions/{subscriptionId}/addons/{subscriptionAddonId} | Get subscription addon
[**get_subscription_get**](MeterSubscriptionsApi.md#get_subscription_get) | **GET** /api/v1/subscriptions/{subscriptionId} | Get subscription
[**list_subscription_addons**](MeterSubscriptionsApi.md#list_subscription_addons) | **GET** /api/v1/subscriptions/{subscriptionId}/addons | List subscription addons
[**list_subscriptions**](MeterSubscriptionsApi.md#list_subscriptions) | **GET** /api/v1/subscriptions | List subscriptions
[**migrate_subscription**](MeterSubscriptionsApi.md#migrate_subscription) | **POST** /api/v1/subscriptions/{subscriptionId}/migrate | Migrate subscription
[**restore_subscription**](MeterSubscriptionsApi.md#restore_subscription) | **POST** /api/v1/subscriptions/{subscriptionId}/restore | Restore subscription
[**unschedule_cancelation**](MeterSubscriptionsApi.md#unschedule_cancelation) | **POST** /api/v1/subscriptions/{subscriptionId}/unschedule-cancelation | Unschedule cancelation
[**update_subscription_addon**](MeterSubscriptionsApi.md#update_subscription_addon) | **PATCH** /api/v1/subscriptions/{subscriptionId}/addons/{subscriptionAddonId} | Update subscription addon


# **cancel_subscription**
> Subscription cancel_subscription(subscription_id, cancel_subscription_request)

Cancel subscription

Cancels the subscription. Will result in a scheduling conflict if there are other subscriptions scheduled to start after the cancellation time.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.cancel_subscription_request import CancelSubscriptionRequest
from moolabs.models.subscription import Subscription
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    cancel_subscription_request = moolabs.CancelSubscriptionRequest() # CancelSubscriptionRequest | 

    try:
        # Cancel subscription
        api_response = api_instance.cancel_subscription(subscription_id, cancel_subscription_request)
        print("The response of MeterSubscriptionsApi->cancel_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->cancel_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **cancel_subscription_request** | [**CancelSubscriptionRequest**](CancelSubscriptionRequest.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_subscription**
> SubscriptionChangeResponseBody change_subscription(subscription_id, subscription_change)

Change subscription

Closes a running subscription and starts a new one according to the specification. Can be used for upgrades, downgrades, and plan changes.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription_change import SubscriptionChange
from moolabs.models.subscription_change_response_body import SubscriptionChangeResponseBody
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    subscription_change = moolabs.SubscriptionChange() # SubscriptionChange | 

    try:
        # Change subscription
        api_response = api_instance.change_subscription(subscription_id, subscription_change)
        print("The response of MeterSubscriptionsApi->change_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->change_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **subscription_change** | [**SubscriptionChange**](SubscriptionChange.md)|  | 

### Return type

[**SubscriptionChangeResponseBody**](SubscriptionChangeResponseBody.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> Subscription create_subscription(subscription_create)

Create subscription

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription import Subscription
from moolabs.models.subscription_create import SubscriptionCreate
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_create = moolabs.SubscriptionCreate() # SubscriptionCreate | 

    try:
        # Create subscription
        api_response = api_instance.create_subscription(subscription_create)
        print("The response of MeterSubscriptionsApi->create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_create** | [**SubscriptionCreate**](SubscriptionCreate.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription_addon**
> SubscriptionAddon create_subscription_addon(subscription_id, subscription_addon_create)

Create subscription addon

Create a new subscription addon, either providing the key or the id of the addon.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription_addon import SubscriptionAddon
from moolabs.models.subscription_addon_create import SubscriptionAddonCreate
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    subscription_addon_create = moolabs.SubscriptionAddonCreate() # SubscriptionAddonCreate | 

    try:
        # Create subscription addon
        api_response = api_instance.create_subscription_addon(subscription_id, subscription_addon_create)
        print("The response of MeterSubscriptionsApi->create_subscription_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->create_subscription_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **subscription_addon_create** | [**SubscriptionAddonCreate**](SubscriptionAddonCreate.md)|  | 

### Return type

[**SubscriptionAddon**](SubscriptionAddon.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id)

Delete subscription

Deletes a subscription. Only scheduled subscriptions can be deleted.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete subscription
        api_instance.delete_subscription(subscription_id)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_subscription**
> Subscription edit_subscription(subscription_id, subscription_edit)

Edit subscription

Batch processing commands for manipulating running subscriptions. The key format is `/phases/{phaseKey}` or `/phases/{phaseKey}/items/{itemKey}`.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription import Subscription
from moolabs.models.subscription_edit import SubscriptionEdit
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    subscription_edit = moolabs.SubscriptionEdit() # SubscriptionEdit | 

    try:
        # Edit subscription
        api_response = api_instance.edit_subscription(subscription_id, subscription_edit)
        print("The response of MeterSubscriptionsApi->edit_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->edit_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **subscription_edit** | [**SubscriptionEdit**](SubscriptionEdit.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_addon**
> SubscriptionAddon get_subscription_addon(subscription_id, subscription_addon_id)

Get subscription addon

Get a subscription addon by id.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription_addon import SubscriptionAddon
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    subscription_addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Get subscription addon
        api_response = api_instance.get_subscription_addon(subscription_id, subscription_addon_id)
        print("The response of MeterSubscriptionsApi->get_subscription_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->get_subscription_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **subscription_addon_id** | **str**|  | 

### Return type

[**SubscriptionAddon**](SubscriptionAddon.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_subscription_get**
> SubscriptionExpanded get_subscription_get(subscription_id, at=at)

Get subscription

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription_expanded import SubscriptionExpanded
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    at = '2023-01-01T01:01:01.001Z' # datetime | The time at which the subscription should be queried. If not provided the current time is used. (optional)

    try:
        # Get subscription
        api_response = api_instance.get_subscription_get(subscription_id, at=at)
        print("The response of MeterSubscriptionsApi->get_subscription_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->get_subscription_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **at** | **datetime**| The time at which the subscription should be queried. If not provided the current time is used. | [optional] 

### Return type

[**SubscriptionExpanded**](SubscriptionExpanded.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_subscription_addons**
> List[SubscriptionAddon] list_subscription_addons(subscription_id)

List subscription addons

List all addons of a subscription. In the returned list will match to a set unique by addonId.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription_addon import SubscriptionAddon
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # List subscription addons
        api_response = api_instance.list_subscription_addons(subscription_id)
        print("The response of MeterSubscriptionsApi->list_subscription_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->list_subscription_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[SubscriptionAddon]**](SubscriptionAddon.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_subscriptions**
> SubscriptionPaginatedResponse list_subscriptions(customer_id=customer_id, status=status, order=order, order_by=order_by, page=page, page_size=page_size)

List subscriptions

Lists all subscriptions for the current namespace. Optionally filter by customer or status.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.customer_subscription_order_by import CustomerSubscriptionOrderBy
from moolabs.models.sort_order import SortOrder
from moolabs.models.subscription_paginated_response import SubscriptionPaginatedResponse
from moolabs.models.subscription_status import SubscriptionStatus
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    customer_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | Filter by customer ID. (optional)
    status = [moolabs.SubscriptionStatus()] # List[SubscriptionStatus] |  (optional)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.CustomerSubscriptionOrderBy() # CustomerSubscriptionOrderBy | The order by field. (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)

    try:
        # List subscriptions
        api_response = api_instance.list_subscriptions(customer_id=customer_id, status=status, order=order, order_by=order_by, page=page, page_size=page_size)
        print("The response of MeterSubscriptionsApi->list_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->list_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Filter by customer ID. | [optional] 
 **status** | [**List[SubscriptionStatus]**](SubscriptionStatus.md)|  | [optional] 
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**CustomerSubscriptionOrderBy**](.md)| The order by field. | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]

### Return type

[**SubscriptionPaginatedResponse**](SubscriptionPaginatedResponse.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **migrate_subscription**
> SubscriptionChangeResponseBody migrate_subscription(subscription_id, migrate_subscription_request)

Migrate subscription

Migrates the subscripiton to the provided version of the current plan. If possible, the migration will be done immediately. If not, the migration will be scheduled to the end of the current billing period.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.migrate_subscription_request import MigrateSubscriptionRequest
from moolabs.models.subscription_change_response_body import SubscriptionChangeResponseBody
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    migrate_subscription_request = moolabs.MigrateSubscriptionRequest() # MigrateSubscriptionRequest | 

    try:
        # Migrate subscription
        api_response = api_instance.migrate_subscription(subscription_id, migrate_subscription_request)
        print("The response of MeterSubscriptionsApi->migrate_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->migrate_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **migrate_subscription_request** | [**MigrateSubscriptionRequest**](MigrateSubscriptionRequest.md)|  | 

### Return type

[**SubscriptionChangeResponseBody**](SubscriptionChangeResponseBody.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_subscription**
> Subscription restore_subscription(subscription_id)

Restore subscription

Restores a canceled subscription. Any subscription scheduled to start later will be deleted and this subscription will be continued indefinitely.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription import Subscription
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Restore subscription
        api_response = api_instance.restore_subscription(subscription_id)
        print("The response of MeterSubscriptionsApi->restore_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->restore_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **unschedule_cancelation**
> Subscription unschedule_cancelation(subscription_id)

Unschedule cancelation

Cancels the scheduled cancelation.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription import Subscription
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Unschedule cancelation
        api_response = api_instance.unschedule_cancelation(subscription_id)
        print("The response of MeterSubscriptionsApi->unschedule_cancelation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->unschedule_cancelation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Variants with ErrorExtensions specific to subscriptions. |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. Variants with ErrorExtensions specific to subscriptions. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_addon**
> SubscriptionAddon update_subscription_addon(subscription_id, subscription_addon_id, subscription_addon_update)

Update subscription addon

Updates a subscription addon (allows changing the quantity: purchasing more instances or cancelling the current instances)

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subscription_addon import SubscriptionAddon
from moolabs.models.subscription_addon_update import SubscriptionAddonUpdate
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.MeterSubscriptionsApi(api_client)
    subscription_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    subscription_addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    subscription_addon_update = moolabs.SubscriptionAddonUpdate() # SubscriptionAddonUpdate | 

    try:
        # Update subscription addon
        api_response = api_instance.update_subscription_addon(subscription_id, subscription_addon_id, subscription_addon_update)
        print("The response of MeterSubscriptionsApi->update_subscription_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeterSubscriptionsApi->update_subscription_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **subscription_addon_id** | **str**|  | 
 **subscription_addon_update** | [**SubscriptionAddonUpdate**](SubscriptionAddonUpdate.md)|  | 

### Return type

[**SubscriptionAddon**](SubscriptionAddon.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

