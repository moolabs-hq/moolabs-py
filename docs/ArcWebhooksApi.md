# moolabs.ArcWebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**moometer_webhook**](ArcWebhooksApi.md#moometer_webhook) | **POST** /v1/arc/webhooks/moometer | Moometer Webhook
[**resend_delivery_webhook**](ArcWebhooksApi.md#resend_delivery_webhook) | **POST** /v1/arc/webhooks/resend | Resend Delivery Webhook
[**resend_inbound_webhook**](ArcWebhooksApi.md#resend_inbound_webhook) | **POST** /v1/arc/webhooks/inbound/resend | Resend Inbound Webhook
[**sendgrid_webhook**](ArcWebhooksApi.md#sendgrid_webhook) | **POST** /v1/arc/webhooks/sendgrid | Sendgrid Webhook
[**stripe_webhook_post**](ArcWebhooksApi.md#stripe_webhook_post) | **POST** /v1/arc/webhooks/stripe | Stripe Webhook
[**twilio_webhook**](ArcWebhooksApi.md#twilio_webhook) | **POST** /v1/arc/webhooks/twilio | Twilio Webhook


# **moometer_webhook**
> object moometer_webhook(x_moo_meter_signature=x_moo_meter_signature)

Moometer Webhook

Handle MooMeter invoice lifecycle webhooks.

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
    api_instance = moolabs.ArcWebhooksApi(api_client)
    x_moo_meter_signature = 'x_moo_meter_signature_example' # str |  (optional)

    try:
        # Moometer Webhook
        api_response = api_instance.moometer_webhook(x_moo_meter_signature=x_moo_meter_signature)
        print("The response of ArcWebhooksApi->moometer_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcWebhooksApi->moometer_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_moo_meter_signature** | **str**|  | [optional] 

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

# **resend_delivery_webhook**
> object resend_delivery_webhook(x_resend_signature=x_resend_signature)

Resend Delivery Webhook

Handle Resend delivery status webhooks (delivered, bounced, opened, clicked).

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
    api_instance = moolabs.ArcWebhooksApi(api_client)
    x_resend_signature = 'x_resend_signature_example' # str |  (optional)

    try:
        # Resend Delivery Webhook
        api_response = api_instance.resend_delivery_webhook(x_resend_signature=x_resend_signature)
        print("The response of ArcWebhooksApi->resend_delivery_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcWebhooksApi->resend_delivery_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_resend_signature** | **str**|  | [optional] 

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

# **resend_inbound_webhook**
> object resend_inbound_webhook()

Resend Inbound Webhook

Receive a customer email reply routed to a tenant inbound address.  Resend sends a JSON payload describing the received email. We look up the target tenant via the recipient's plus-address tag (``billing+t-<tenant_uuid>@...``), verify the Svix signature headers using the tenant's ``inbound_secret``, persist an ``ArcCommunication(direction=INBOUND, status=RECEIVED)``, and hand off to the classifier agent.  Resend webhooks are delivered through Svix and signed with the canonical Svix scheme (``svix-id`` / ``svix-timestamp`` / ``svix-signature`` headers, ``HMAC-SHA256({id}.{ts}.{body}, secret)`` base64-encoded with a ``v1,`` version tag).  We forward the full header set to the verifier rather than picking individual headers so the Svix SDK can do its own header-name normalization (some proxies lower-case, some don't; some use ``webhook-*`` instead of ``svix-*``).  The earlier implementation only read a single ``X-Resend-Signature`` header that Resend never sends, so every inbound email returned 401 and stayed parked in Resend's retry queue indefinitely.  The classifier never mutates customer-facing state — it queues an ``ArcTask`` for a human review (see ``app/agents/inbound_classifier.py``).

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
    api_instance = moolabs.ArcWebhooksApi(api_client)

    try:
        # Resend Inbound Webhook
        api_response = api_instance.resend_inbound_webhook()
        print("The response of ArcWebhooksApi->resend_inbound_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcWebhooksApi->resend_inbound_webhook: %s\n" % e)
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

# **sendgrid_webhook**
> object sendgrid_webhook(x_twilio_email_event_webhook_signature=x_twilio_email_event_webhook_signature)

Sendgrid Webhook

Handle SendGrid delivery status webhooks.

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
    api_instance = moolabs.ArcWebhooksApi(api_client)
    x_twilio_email_event_webhook_signature = 'x_twilio_email_event_webhook_signature_example' # str |  (optional)

    try:
        # Sendgrid Webhook
        api_response = api_instance.sendgrid_webhook(x_twilio_email_event_webhook_signature=x_twilio_email_event_webhook_signature)
        print("The response of ArcWebhooksApi->sendgrid_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcWebhooksApi->sendgrid_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_twilio_email_event_webhook_signature** | **str**|  | [optional] 

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

# **stripe_webhook_post**
> object stripe_webhook_post(stripe_signature=stripe_signature)

Stripe Webhook

Handle Stripe payment webhooks. T9: Signature verified first.

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
    api_instance = moolabs.ArcWebhooksApi(api_client)
    stripe_signature = 'stripe_signature_example' # str |  (optional)

    try:
        # Stripe Webhook
        api_response = api_instance.stripe_webhook_post(stripe_signature=stripe_signature)
        print("The response of ArcWebhooksApi->stripe_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcWebhooksApi->stripe_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stripe_signature** | **str**|  | [optional] 

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

# **twilio_webhook**
> object twilio_webhook(x_twilio_signature=x_twilio_signature)

Twilio Webhook

Handle Twilio SMS status webhooks.

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
    api_instance = moolabs.ArcWebhooksApi(api_client)
    x_twilio_signature = 'x_twilio_signature_example' # str |  (optional)

    try:
        # Twilio Webhook
        api_response = api_instance.twilio_webhook(x_twilio_signature=x_twilio_signature)
        print("The response of ArcWebhooksApi->twilio_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcWebhooksApi->twilio_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_twilio_signature** | **str**|  | [optional] 

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

