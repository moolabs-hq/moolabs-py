# moolabs.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_upsert_v1**](IntegrationsApi.md#customer_upsert_v1) | **POST** /v1/integrations/netsuite-sim/events/customer | Customer Upsert
[**enqueue_arc_transaction_v1_integrations**](IntegrationsApi.md#enqueue_arc_transaction_v1_integrations) | **POST** /v1/integrations/netsuite-sim/arc-transactions | Enqueue Arc Transaction
[**get_crm_quote_record_card**](IntegrationsApi.md#get_crm_quote_record_card) | **GET** /v1/integrations/crm/quotes/{provider}/cards/{quote_id} | Get Crm Quote Record Card
[**invoice_upsert_v1**](IntegrationsApi.md#invoice_upsert_v1) | **POST** /v1/integrations/netsuite-sim/events/invoice | Invoice Upsert
[**openmeter_webhook**](IntegrationsApi.md#openmeter_webhook) | **POST** /v1/integrations/moometer/webhooks/moometer | Openmeter Webhook
[**openmeter_webhook_batch**](IntegrationsApi.md#openmeter_webhook_batch) | **POST** /v1/integrations/moometer/webhooks/moometer/batch | Openmeter Webhook Batch
[**post_crm_quote_context**](IntegrationsApi.md#post_crm_quote_context) | **POST** /v1/integrations/crm/quotes/{provider}/context | Post Crm Quote Context
[**post_crm_quote_draft**](IntegrationsApi.md#post_crm_quote_draft) | **POST** /v1/integrations/crm/quotes/{provider}/draft | Post Crm Quote Draft
[**post_google_chat_quote_event_v1**](IntegrationsApi.md#post_google_chat_quote_event_v1) | **POST** /v1/integrations/google-chat/quotes/events | Post Google Chat Quote Event
[**post_slack_quote_command**](IntegrationsApi.md#post_slack_quote_command) | **POST** /v1/integrations/slack/quotes/commands | Post Slack Quote Command
[**process_pending_v1_integrations**](IntegrationsApi.md#process_pending_v1_integrations) | **POST** /v1/integrations/netsuite-sim/process-pending | Process Pending
[**readiness_v1**](IntegrationsApi.md#readiness_v1) | **GET** /v1/integrations/netsuite-sim/readiness | Readiness


# **customer_upsert_v1**
> object customer_upsert_v1(customer_upsert_request, x_idempotency_key=x_idempotency_key)

Customer Upsert

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.customer_upsert_request import CustomerUpsertRequest
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    customer_upsert_request = moolabs.CustomerUpsertRequest() # CustomerUpsertRequest | 
    x_idempotency_key = 'x_idempotency_key_example' # str |  (optional)

    try:
        # Customer Upsert
        api_response = api_instance.customer_upsert_v1(customer_upsert_request, x_idempotency_key=x_idempotency_key)
        print("The response of IntegrationsApi->customer_upsert_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->customer_upsert_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_upsert_request** | [**CustomerUpsertRequest**](CustomerUpsertRequest.md)|  | 
 **x_idempotency_key** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_arc_transaction_v1_integrations**
> object enqueue_arc_transaction_v1_integrations(arc_transaction_request, x_idempotency_key=x_idempotency_key)

Enqueue Arc Transaction

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.arc_transaction_request import ArcTransactionRequest
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    arc_transaction_request = moolabs.ArcTransactionRequest() # ArcTransactionRequest | 
    x_idempotency_key = 'x_idempotency_key_example' # str |  (optional)

    try:
        # Enqueue Arc Transaction
        api_response = api_instance.enqueue_arc_transaction_v1_integrations(arc_transaction_request, x_idempotency_key=x_idempotency_key)
        print("The response of IntegrationsApi->enqueue_arc_transaction_v1_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->enqueue_arc_transaction_v1_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arc_transaction_request** | [**ArcTransactionRequest**](ArcTransactionRequest.md)|  | 
 **x_idempotency_key** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crm_quote_record_card**
> CrmQuoteRecordCardResponse get_crm_quote_record_card(provider, quote_id, quote_version=quote_version, record_type=record_type, record_id=record_id)

Get Crm Quote Record Card

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.crm_quote_record_card_response import CrmQuoteRecordCardResponse
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    provider = 'provider_example' # str | 
    quote_id = 'quote_id_example' # str | 
    quote_version = 56 # int |  (optional)
    record_type = 'record_type_example' # str |  (optional)
    record_id = 'record_id_example' # str |  (optional)

    try:
        # Get Crm Quote Record Card
        api_response = api_instance.get_crm_quote_record_card(provider, quote_id, quote_version=quote_version, record_type=record_type, record_id=record_id)
        print("The response of IntegrationsApi->get_crm_quote_record_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->get_crm_quote_record_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **quote_id** | **str**|  | 
 **quote_version** | **int**|  | [optional] 
 **record_type** | **str**|  | [optional] 
 **record_id** | **str**|  | [optional] 

### Return type

[**CrmQuoteRecordCardResponse**](CrmQuoteRecordCardResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoice_upsert_v1**
> object invoice_upsert_v1(invoice_upsert_request, x_idempotency_key=x_idempotency_key)

Invoice Upsert

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.invoice_upsert_request import InvoiceUpsertRequest
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    invoice_upsert_request = moolabs.InvoiceUpsertRequest() # InvoiceUpsertRequest | 
    x_idempotency_key = 'x_idempotency_key_example' # str |  (optional)

    try:
        # Invoice Upsert
        api_response = api_instance.invoice_upsert_v1(invoice_upsert_request, x_idempotency_key=x_idempotency_key)
        print("The response of IntegrationsApi->invoice_upsert_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->invoice_upsert_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_upsert_request** | [**InvoiceUpsertRequest**](InvoiceUpsertRequest.md)|  | 
 **x_idempotency_key** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openmeter_webhook**
> object openmeter_webhook(tenant_id=tenant_id, pool_id=pool_id)

Openmeter Webhook

Handle Moo-meter webhook CloudEvent.  This endpoint receives CloudEvents from Moo-meter and normalizes them into CLS usage events.  **CloudEvent Format:** Moo-meter sends CloudEvents in CloudEvents v1.0 format: ```json {   \"specversion\": \"1.0\",   \"type\": \"usage\",   \"id\": \"event-id-123\",   \"time\": \"2026-01-13T21:00:00Z\",   \"source\": \"https://api.openmeter.io/v1/meters/meter-slug\",   \"subject\": \"customer-id-123\",   \"data\": {     \"value\": 100,     \"meter\": \"meter-slug\",     ...   } } ```  Or wrapped format (API v2): ```json {   \"event\": {     \"specversion\": \"1.0\",     \"type\": \"usage\",     ...   },   \"ingestedAt\": \"...\",   \"storedAt\": \"...\" } ```  **Request Headers:** - `X-Moometer-Signature` (optional): Webhook signature for verification  **Query Parameters:** - `tenant_id` (required): Tenant identifier - `pool_id` (required): Credit pool identifier  **Response:** - 201: Event processed successfully - 400: Invalid event format or missing required fields - 500: Processing error  **Idempotency:** - Uses CloudEvent `id` field as idempotency key - Duplicate events are safely ignored (UNIQUE constraint)

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
    api_instance = moolabs.IntegrationsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    pool_id = 'pool_id_example' # str |  (optional)

    try:
        # Openmeter Webhook
        api_response = api_instance.openmeter_webhook(tenant_id=tenant_id, pool_id=pool_id)
        print("The response of IntegrationsApi->openmeter_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->openmeter_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **pool_id** | **str**|  | [optional] 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openmeter_webhook_batch**
> object openmeter_webhook_batch(tenant_id=tenant_id, pool_id=pool_id)

Openmeter Webhook Batch

Handle batch of Moo-meter webhook CloudEvents.  Processes multiple CloudEvents in a single request. Each event is processed independently (idempotent).  **Request Body:** ```json {   \"events\": [     { \"specversion\": \"1.0\", \"type\": \"usage\", ... },     { \"specversion\": \"1.0\", \"type\": \"usage\", ... }   ] } ```  **Response:** - 201: All events processed (some may have failed individually) - Results include per-event status  **Query Parameters:** - `tenant_id` (required): Tenant identifier - `pool_id` (required): Credit pool identifier

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
    api_instance = moolabs.IntegrationsApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    pool_id = 'pool_id_example' # str |  (optional)

    try:
        # Openmeter Webhook Batch
        api_response = api_instance.openmeter_webhook_batch(tenant_id=tenant_id, pool_id=pool_id)
        print("The response of IntegrationsApi->openmeter_webhook_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->openmeter_webhook_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **pool_id** | **str**|  | [optional] 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_crm_quote_context**
> CrmQuoteContextResponse post_crm_quote_context(provider, crm_quote_context_request)

Post Crm Quote Context

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.crm_quote_context_request import CrmQuoteContextRequest
from moolabs.models.crm_quote_context_response import CrmQuoteContextResponse
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    provider = 'provider_example' # str | 
    crm_quote_context_request = moolabs.CrmQuoteContextRequest() # CrmQuoteContextRequest | 

    try:
        # Post Crm Quote Context
        api_response = api_instance.post_crm_quote_context(provider, crm_quote_context_request)
        print("The response of IntegrationsApi->post_crm_quote_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->post_crm_quote_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **crm_quote_context_request** | [**CrmQuoteContextRequest**](CrmQuoteContextRequest.md)|  | 

### Return type

[**CrmQuoteContextResponse**](CrmQuoteContextResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_crm_quote_draft**
> CrmQuoteDraftResponse post_crm_quote_draft(provider, crm_quote_draft_request)

Post Crm Quote Draft

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.crm_quote_draft_request import CrmQuoteDraftRequest
from moolabs.models.crm_quote_draft_response import CrmQuoteDraftResponse
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    provider = 'provider_example' # str | 
    crm_quote_draft_request = moolabs.CrmQuoteDraftRequest() # CrmQuoteDraftRequest | 

    try:
        # Post Crm Quote Draft
        api_response = api_instance.post_crm_quote_draft(provider, crm_quote_draft_request)
        print("The response of IntegrationsApi->post_crm_quote_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->post_crm_quote_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **crm_quote_draft_request** | [**CrmQuoteDraftRequest**](CrmQuoteDraftRequest.md)|  | 

### Return type

[**CrmQuoteDraftResponse**](CrmQuoteDraftResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_google_chat_quote_event_v1**
> GoogleChatQuoteResponse post_google_chat_quote_event_v1()

Post Google Chat Quote Event

### Example


```python
import moolabs
from moolabs.models.google_chat_quote_response import GoogleChatQuoteResponse
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
    api_instance = moolabs.IntegrationsApi(api_client)

    try:
        # Post Google Chat Quote Event
        api_response = api_instance.post_google_chat_quote_event_v1()
        print("The response of IntegrationsApi->post_google_chat_quote_event_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->post_google_chat_quote_event_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GoogleChatQuoteResponse**](GoogleChatQuoteResponse.md)

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

# **post_slack_quote_command**
> SlackQuoteCommandResponse post_slack_quote_command()

Post Slack Quote Command

### Example


```python
import moolabs
from moolabs.models.slack_quote_command_response import SlackQuoteCommandResponse
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
    api_instance = moolabs.IntegrationsApi(api_client)

    try:
        # Post Slack Quote Command
        api_response = api_instance.post_slack_quote_command()
        print("The response of IntegrationsApi->post_slack_quote_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->post_slack_quote_command: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SlackQuoteCommandResponse**](SlackQuoteCommandResponse.md)

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

# **process_pending_v1_integrations**
> object process_pending_v1_integrations(limit=limit)

Process Pending

### Example

* Bearer (opaque) Authentication (HTTPBearer):

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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Process Pending
        api_response = api_instance.process_pending_v1_integrations(limit=limit)
        print("The response of IntegrationsApi->process_pending_v1_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->process_pending_v1_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **readiness_v1**
> object readiness_v1()

Readiness

### Example

* Bearer (opaque) Authentication (HTTPBearer):

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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.IntegrationsApi(api_client)

    try:
        # Readiness
        api_response = api_instance.readiness_v1()
        print("The response of IntegrationsApi->readiness_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->readiness_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

