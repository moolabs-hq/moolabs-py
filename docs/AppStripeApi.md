# moolabs.AppStripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_stripe_webhook**](AppStripeApi.md#app_stripe_webhook) | **POST** /api/v1/apps/{id}/stripe/webhook | Stripe webhook
[**create_stripe_checkout_session**](AppStripeApi.md#create_stripe_checkout_session) | **POST** /api/v1/stripe/checkout/sessions | Create checkout session
[**update_stripe_api_key**](AppStripeApi.md#update_stripe_api_key) | **PUT** /api/v1/apps/{id}/stripe/api-key | Update Stripe API key


# **app_stripe_webhook**
> StripeWebhookResponse app_stripe_webhook(id, stripe_webhook_event)

Stripe webhook

Handle stripe webhooks for apps.

### Example


```python
import moolabs
from moolabs.models.stripe_webhook_event import StripeWebhookEvent
from moolabs.models.stripe_webhook_response import StripeWebhookResponse
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
    api_instance = moolabs.AppStripeApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    stripe_webhook_event = moolabs.StripeWebhookEvent() # StripeWebhookEvent | 

    try:
        # Stripe webhook
        api_response = api_instance.app_stripe_webhook(id, stripe_webhook_event)
        print("The response of AppStripeApi->app_stripe_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppStripeApi->app_stripe_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **stripe_webhook_event** | [**StripeWebhookEvent**](StripeWebhookEvent.md)|  | 

### Return type

[**StripeWebhookResponse**](StripeWebhookResponse.md)

### Authorization

No authorization required

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

# **create_stripe_checkout_session**
> CreateStripeCheckoutSessionResult create_stripe_checkout_session(create_stripe_checkout_session_request)

Create checkout session

Create checkout session.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.create_stripe_checkout_session_request import CreateStripeCheckoutSessionRequest
from moolabs.models.create_stripe_checkout_session_result import CreateStripeCheckoutSessionResult
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
    api_instance = moolabs.AppStripeApi(api_client)
    create_stripe_checkout_session_request = moolabs.CreateStripeCheckoutSessionRequest() # CreateStripeCheckoutSessionRequest | 

    try:
        # Create checkout session
        api_response = api_instance.create_stripe_checkout_session(create_stripe_checkout_session_request)
        print("The response of AppStripeApi->create_stripe_checkout_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppStripeApi->create_stripe_checkout_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_stripe_checkout_session_request** | [**CreateStripeCheckoutSessionRequest**](CreateStripeCheckoutSessionRequest.md)|  | 

### Return type

[**CreateStripeCheckoutSessionResult**](CreateStripeCheckoutSessionResult.md)

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
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stripe_api_key**
> update_stripe_api_key(id, stripe_api_key_input)

Update Stripe API key

Update the Stripe API key.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.stripe_api_key_input import StripeAPIKeyInput
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
    api_instance = moolabs.AppStripeApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    stripe_api_key_input = moolabs.StripeAPIKeyInput() # StripeAPIKeyInput | 

    try:
        # Update Stripe API key
        api_instance.update_stripe_api_key(id, stripe_api_key_input)
    except Exception as e:
        print("Exception when calling AppStripeApi->update_stripe_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **stripe_api_key_input** | [**StripeAPIKeyInput**](StripeAPIKeyInput.md)|  | 

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
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

