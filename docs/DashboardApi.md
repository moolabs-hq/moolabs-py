# moolabs.DashboardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clerk_webhook**](DashboardApi.md#clerk_webhook) | **POST** /v1/webhooks/clerk | Clerk Webhook
[**netsuite_webhook**](DashboardApi.md#netsuite_webhook) | **POST** /v1/webhooks/netsuite | Netsuite Webhook
[**stripe_webhook**](DashboardApi.md#stripe_webhook) | **POST** /v1/webhooks/stripe | Stripe Webhook


# **clerk_webhook**
> object clerk_webhook()

Clerk Webhook

Receive Clerk webhooks. On organization.created, create tenant + API key.  Configure in Clerk Dashboard: Webhooks → Add Endpoint → URL: https://your-bff/v1/webhooks/clerk Subscribe to `organization.created`. Set CLERK_WEBHOOK_SECRET in BFF env from the endpoint's signing secret.

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
    api_instance = moolabs.DashboardApi(api_client)

    try:
        # Clerk Webhook
        api_response = api_instance.clerk_webhook()
        print("The response of DashboardApi->clerk_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->clerk_webhook: %s\n" % e)
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

# **netsuite_webhook**
> object netsuite_webhook()

Netsuite Webhook

Receive NetSuite outbound webhook events.  Authenticated via Bearer integration key (require_integration_key ensures correct scope). On first call, atomically activates the integration (status: pending → active).

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
    api_instance = moolabs.DashboardApi(api_client)

    try:
        # Netsuite Webhook
        api_response = api_instance.netsuite_webhook()
        print("The response of DashboardApi->netsuite_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->netsuite_webhook: %s\n" % e)
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

# **stripe_webhook**
> object stripe_webhook()

Stripe Webhook

Receive Stripe webhooks for wallet top-up outcomes.  Uses the webhook signing secret from Settings → Integrations (Stripe) for the tenant in the event metadata. If no tenant config is found, falls back to STRIPE_WEBHOOK_SECRET env. Configure in Stripe Dashboard: Developers → Webhooks → Add endpoint → URL: https://your-bff/v1/webhooks/stripe Subscribe to `checkout.session.completed` and `checkout.session.async_payment_failed`.

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
    api_instance = moolabs.DashboardApi(api_client)

    try:
        # Stripe Webhook
        api_response = api_instance.stripe_webhook()
        print("The response of DashboardApi->stripe_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardApi->stripe_webhook: %s\n" % e)
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

