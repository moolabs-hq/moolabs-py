# moolabs.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_upsert_v1**](IntegrationsApi.md#customer_upsert_v1) | **POST** /v1/integrations/netsuite-sim/events/customer | Customer Upsert
[**enqueue_arc_transaction_v1_integrations**](IntegrationsApi.md#enqueue_arc_transaction_v1_integrations) | **POST** /v1/integrations/netsuite-sim/arc-transactions | Enqueue Arc Transaction
[**invoice_upsert_v1**](IntegrationsApi.md#invoice_upsert_v1) | **POST** /v1/integrations/netsuite-sim/events/invoice | Invoice Upsert
[**openmeter_webhook**](IntegrationsApi.md#openmeter_webhook) | **POST** /v1/integrations/moometer/webhooks/moometer | Openmeter Webhook
[**openmeter_webhook_batch**](IntegrationsApi.md#openmeter_webhook_batch) | **POST** /v1/integrations/moometer/webhooks/moometer/batch | Openmeter Webhook Batch
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

