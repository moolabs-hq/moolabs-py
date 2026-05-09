# moolabs.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](NotificationsApi.md#create_notification_channel) | **POST** /api/v1/notification/channels | Create a notification channel
[**create_notification_rule**](NotificationsApi.md#create_notification_rule) | **POST** /api/v1/notification/rules | Create a notification rule
[**delete_notification_channel**](NotificationsApi.md#delete_notification_channel) | **DELETE** /api/v1/notification/channels/{channelId} | Delete a notification channel
[**delete_notification_rule**](NotificationsApi.md#delete_notification_rule) | **DELETE** /api/v1/notification/rules/{ruleId} | Delete a notification rule
[**get_notification_channel**](NotificationsApi.md#get_notification_channel) | **GET** /api/v1/notification/channels/{channelId} | Get notification channel
[**get_notification_event**](NotificationsApi.md#get_notification_event) | **GET** /api/v1/notification/events/{eventId} | Get notification event
[**get_notification_rule**](NotificationsApi.md#get_notification_rule) | **GET** /api/v1/notification/rules/{ruleId} | Get notification rule
[**list_notification_channels**](NotificationsApi.md#list_notification_channels) | **GET** /api/v1/notification/channels | List notification channels
[**list_notification_events**](NotificationsApi.md#list_notification_events) | **GET** /api/v1/notification/events | List notification events
[**list_notification_rules**](NotificationsApi.md#list_notification_rules) | **GET** /api/v1/notification/rules | List notification rules
[**resend_notification_event**](NotificationsApi.md#resend_notification_event) | **POST** /api/v1/notification/events/{eventId}/resend | Re-send notification event
[**test_notification_rule**](NotificationsApi.md#test_notification_rule) | **POST** /api/v1/notification/rules/{ruleId}/test | Test notification rule
[**update_notification_channel**](NotificationsApi.md#update_notification_channel) | **PUT** /api/v1/notification/channels/{channelId} | Update a notification channel
[**update_notification_rule**](NotificationsApi.md#update_notification_rule) | **PUT** /api/v1/notification/rules/{ruleId} | Update a notification rule


# **create_notification_channel**
> NotificationChannelWebhook create_notification_channel(body)

Create a notification channel

Create a new notification channel.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_channel_webhook import NotificationChannelWebhook
from moolabs.models.notification_channel_webhook_create_request import NotificationChannelWebhookCreateRequest
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
    api_instance = moolabs.NotificationsApi(api_client)
    body = moolabs.NotificationChannelWebhookCreateRequest() # NotificationChannelWebhookCreateRequest | 

    try:
        # Create a notification channel
        api_response = api_instance.create_notification_channel(body)
        print("The response of NotificationsApi->create_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **NotificationChannelWebhookCreateRequest**|  | 

### Return type

[**NotificationChannelWebhook**](NotificationChannelWebhook.md)

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
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_notification_rule**
> NotificationRule create_notification_rule(notification_rule_create_request)

Create a notification rule

Create a new notification rule.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_rule import NotificationRule
from moolabs.models.notification_rule_create_request import NotificationRuleCreateRequest
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
    api_instance = moolabs.NotificationsApi(api_client)
    notification_rule_create_request = moolabs.NotificationRuleCreateRequest() # NotificationRuleCreateRequest | 

    try:
        # Create a notification rule
        api_response = api_instance.create_notification_rule(notification_rule_create_request)
        print("The response of NotificationsApi->create_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->create_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_rule_create_request** | [**NotificationRuleCreateRequest**](NotificationRuleCreateRequest.md)|  | 

### Return type

[**NotificationRule**](NotificationRule.md)

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
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_channel**
> delete_notification_channel(channel_id)

Delete a notification channel

Soft delete notification channel by id.  Once a notification channel is deleted it cannot be undeleted.

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
    api_instance = moolabs.NotificationsApi(api_client)
    channel_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete a notification channel
        api_instance.delete_notification_channel(channel_id)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

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
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_rule**
> delete_notification_rule(rule_id)

Delete a notification rule

Soft delete notification rule by id.  Once a notification rule is deleted it cannot be undeleted.

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
    api_instance = moolabs.NotificationsApi(api_client)
    rule_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete a notification rule
        api_instance.delete_notification_rule(rule_id)
    except Exception as e:
        print("Exception when calling NotificationsApi->delete_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

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
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_channel**
> NotificationChannelWebhook get_notification_channel(channel_id)

Get notification channel

Get a notification channel by id.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_channel_webhook import NotificationChannelWebhook
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
    api_instance = moolabs.NotificationsApi(api_client)
    channel_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Get notification channel
        api_response = api_instance.get_notification_channel(channel_id)
        print("The response of NotificationsApi->get_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 

### Return type

[**NotificationChannelWebhook**](NotificationChannelWebhook.md)

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

# **get_notification_event**
> NotificationEvent get_notification_event(event_id)

Get notification event

Get a notification event by id.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_event import NotificationEvent
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
    api_instance = moolabs.NotificationsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get notification event
        api_response = api_instance.get_notification_event(event_id)
        print("The response of NotificationsApi->get_notification_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**NotificationEvent**](NotificationEvent.md)

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

# **get_notification_rule**
> NotificationRule get_notification_rule(rule_id)

Get notification rule

Get a notification rule by id.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_rule import NotificationRule
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
    api_instance = moolabs.NotificationsApi(api_client)
    rule_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Get notification rule
        api_response = api_instance.get_notification_rule(rule_id)
        print("The response of NotificationsApi->get_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**NotificationRule**](NotificationRule.md)

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

# **list_notification_channels**
> NotificationChannelPaginatedResponse list_notification_channels(include_deleted=include_deleted, include_disabled=include_disabled, page=page, page_size=page_size, order=order, order_by=order_by)

List notification channels

List all notification channels.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_channel_order_by import NotificationChannelOrderBy
from moolabs.models.notification_channel_paginated_response import NotificationChannelPaginatedResponse
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.NotificationsApi(api_client)
    include_deleted = False # bool | Include deleted notification channels in response.  Usage: `?includeDeleted=true` (optional) (default to False)
    include_disabled = False # bool | Include disabled notification channels in response.  Usage: `?includeDisabled=false` (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.NotificationChannelOrderBy() # NotificationChannelOrderBy | The order by field. (optional)

    try:
        # List notification channels
        api_response = api_instance.list_notification_channels(include_deleted=include_deleted, include_disabled=include_disabled, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of NotificationsApi->list_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| Include deleted notification channels in response.  Usage: &#x60;?includeDeleted&#x3D;true&#x60; | [optional] [default to False]
 **include_disabled** | **bool**| Include disabled notification channels in response.  Usage: &#x60;?includeDisabled&#x3D;false&#x60; | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**NotificationChannelOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**NotificationChannelPaginatedResponse**](NotificationChannelPaginatedResponse.md)

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

# **list_notification_events**
> NotificationEventPaginatedResponse list_notification_events(var_from=var_from, to=to, feature=feature, subject=subject, rule=rule, channel=channel, page=page, page_size=page_size, order=order, order_by=order_by)

List notification events

List all notification events.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_event_order_by import NotificationEventOrderBy
from moolabs.models.notification_event_paginated_response import NotificationEventPaginatedResponse
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.NotificationsApi(api_client)
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start date-time in RFC 3339 format. Inclusive. (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End date-time in RFC 3339 format. Inclusive. (optional)
    feature = ['feature_example'] # List[str] | Filtering by multiple feature ids or keys.  Usage: `?feature=feature-1&feature=feature-2` (optional)
    subject = ['subject_example'] # List[str] | Filtering by multiple subject ids or keys.  Usage: `?subject=subject-1&subject=subject-2` (optional)
    rule = ['rule_example'] # List[str] | Filtering by multiple rule ids.  Usage: `?rule=01J8J2XYZ2N5WBYK09EDZFBSZM&rule=01J8J4R4VZH180KRKQ63NB2VA5` (optional)
    channel = ['channel_example'] # List[str] | Filtering by multiple channel ids.  Usage: `?channel=01J8J4RXH778XB056JS088PCYT&channel=01J8J4S1R1G9EVN62RG23A9M6J` (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.NotificationEventOrderBy() # NotificationEventOrderBy | The order by field. (optional)

    try:
        # List notification events
        api_response = api_instance.list_notification_events(var_from=var_from, to=to, feature=feature, subject=subject, rule=rule, channel=channel, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of NotificationsApi->list_notification_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Start date-time in RFC 3339 format. Inclusive. | [optional] 
 **to** | **datetime**| End date-time in RFC 3339 format. Inclusive. | [optional] 
 **feature** | [**List[str]**](str.md)| Filtering by multiple feature ids or keys.  Usage: &#x60;?feature&#x3D;feature-1&amp;feature&#x3D;feature-2&#x60; | [optional] 
 **subject** | [**List[str]**](str.md)| Filtering by multiple subject ids or keys.  Usage: &#x60;?subject&#x3D;subject-1&amp;subject&#x3D;subject-2&#x60; | [optional] 
 **rule** | [**List[str]**](str.md)| Filtering by multiple rule ids.  Usage: &#x60;?rule&#x3D;01J8J2XYZ2N5WBYK09EDZFBSZM&amp;rule&#x3D;01J8J4R4VZH180KRKQ63NB2VA5&#x60; | [optional] 
 **channel** | [**List[str]**](str.md)| Filtering by multiple channel ids.  Usage: &#x60;?channel&#x3D;01J8J4RXH778XB056JS088PCYT&amp;channel&#x3D;01J8J4S1R1G9EVN62RG23A9M6J&#x60; | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**NotificationEventOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**NotificationEventPaginatedResponse**](NotificationEventPaginatedResponse.md)

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

# **list_notification_rules**
> NotificationRulePaginatedResponse list_notification_rules(include_deleted=include_deleted, include_disabled=include_disabled, feature=feature, channel=channel, page=page, page_size=page_size, order=order, order_by=order_by)

List notification rules

List all notification rules.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_rule_order_by import NotificationRuleOrderBy
from moolabs.models.notification_rule_paginated_response import NotificationRulePaginatedResponse
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.NotificationsApi(api_client)
    include_deleted = False # bool | Include deleted notification rules in response.  Usage: `?includeDeleted=true` (optional) (default to False)
    include_disabled = False # bool | Include disabled notification rules in response.  Usage: `?includeDisabled=false` (optional) (default to False)
    feature = ['feature_example'] # List[str] | Filtering by multiple feature ids/keys.  Usage: `?feature=feature-1&feature=feature-2` (optional)
    channel = ['channel_example'] # List[str] | Filtering by multiple notifiaction channel ids.  Usage: `?channel=01ARZ3NDEKTSV4RRFFQ69G5FAV&channel=01J8J2Y5X4NNGQS32CF81W95E3` (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.NotificationRuleOrderBy() # NotificationRuleOrderBy | The order by field. (optional)

    try:
        # List notification rules
        api_response = api_instance.list_notification_rules(include_deleted=include_deleted, include_disabled=include_disabled, feature=feature, channel=channel, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of NotificationsApi->list_notification_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->list_notification_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| Include deleted notification rules in response.  Usage: &#x60;?includeDeleted&#x3D;true&#x60; | [optional] [default to False]
 **include_disabled** | **bool**| Include disabled notification rules in response.  Usage: &#x60;?includeDisabled&#x3D;false&#x60; | [optional] [default to False]
 **feature** | [**List[str]**](str.md)| Filtering by multiple feature ids/keys.  Usage: &#x60;?feature&#x3D;feature-1&amp;feature&#x3D;feature-2&#x60; | [optional] 
 **channel** | [**List[str]**](str.md)| Filtering by multiple notifiaction channel ids.  Usage: &#x60;?channel&#x3D;01ARZ3NDEKTSV4RRFFQ69G5FAV&amp;channel&#x3D;01J8J2Y5X4NNGQS32CF81W95E3&#x60; | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**NotificationRuleOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**NotificationRulePaginatedResponse**](NotificationRulePaginatedResponse.md)

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

# **resend_notification_event**
> resend_notification_event(event_id, notification_event_resend_request)

Re-send notification event

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_event_resend_request import NotificationEventResendRequest
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
    api_instance = moolabs.NotificationsApi(api_client)
    event_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    notification_event_resend_request = moolabs.NotificationEventResendRequest() # NotificationEventResendRequest | 

    try:
        # Re-send notification event
        api_instance.resend_notification_event(event_id, notification_event_resend_request)
    except Exception as e:
        print("Exception when calling NotificationsApi->resend_notification_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **notification_event_resend_request** | [**NotificationEventResendRequest**](NotificationEventResendRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The request has been accepted for processing, but processing has not yet completed. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_notification_rule**
> NotificationEvent test_notification_rule(rule_id)

Test notification rule

Test a notification rule by sending a test event with random data.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_event import NotificationEvent
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
    api_instance = moolabs.NotificationsApi(api_client)
    rule_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Test notification rule
        api_response = api_instance.test_notification_rule(rule_id)
        print("The response of NotificationsApi->test_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->test_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**NotificationEvent**](NotificationEvent.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_channel**
> NotificationChannelWebhook update_notification_channel(channel_id, body)

Update a notification channel

Update notification channel.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_channel_webhook import NotificationChannelWebhook
from moolabs.models.notification_channel_webhook_create_request import NotificationChannelWebhookCreateRequest
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
    api_instance = moolabs.NotificationsApi(api_client)
    channel_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    body = moolabs.NotificationChannelWebhookCreateRequest() # NotificationChannelWebhookCreateRequest | 

    try:
        # Update a notification channel
        api_response = api_instance.update_notification_channel(channel_id, body)
        print("The response of NotificationsApi->update_notification_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_notification_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**|  | 
 **body** | **NotificationChannelWebhookCreateRequest**|  | 

### Return type

[**NotificationChannelWebhook**](NotificationChannelWebhook.md)

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

# **update_notification_rule**
> NotificationRule update_notification_rule(rule_id, notification_rule_create_request)

Update a notification rule

Update notification rule.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.notification_rule import NotificationRule
from moolabs.models.notification_rule_create_request import NotificationRuleCreateRequest
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
    api_instance = moolabs.NotificationsApi(api_client)
    rule_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    notification_rule_create_request = moolabs.NotificationRuleCreateRequest() # NotificationRuleCreateRequest | 

    try:
        # Update a notification rule
        api_response = api_instance.update_notification_rule(rule_id, notification_rule_create_request)
        print("The response of NotificationsApi->update_notification_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->update_notification_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **notification_rule_create_request** | [**NotificationRuleCreateRequest**](NotificationRuleCreateRequest.md)|  | 

### Return type

[**NotificationRule**](NotificationRule.md)

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

