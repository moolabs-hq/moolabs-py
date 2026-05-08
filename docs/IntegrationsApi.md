# moolabs.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openmeter_webhook**](IntegrationsApi.md#openmeter_webhook) | **POST** /v1/integrations/openmeter/webhooks/openmeter | Openmeter Webhook
[**openmeter_webhook_batch**](IntegrationsApi.md#openmeter_webhook_batch) | **POST** /v1/integrations/openmeter/webhooks/openmeter/batch | Openmeter Webhook Batch


# **openmeter_webhook**
> object openmeter_webhook(tenant_id=tenant_id, pool_id=pool_id)

Openmeter Webhook

Handle OpenMeter webhook CloudEvent.  This endpoint receives CloudEvents from OpenMeter and normalizes them into CLS usage events.  **CloudEvent Format:** OpenMeter sends CloudEvents in CloudEvents v1.0 format: ```json {   \"specversion\": \"1.0\",   \"type\": \"usage\",   \"id\": \"event-id-123\",   \"time\": \"2026-01-13T21:00:00Z\",   \"source\": \"https://api.openmeter.io/v1/meters/meter-slug\",   \"subject\": \"customer-id-123\",   \"data\": {     \"value\": 100,     \"meter\": \"meter-slug\",     ...   } } ```  Or wrapped format (API v2): ```json {   \"event\": {     \"specversion\": \"1.0\",     \"type\": \"usage\",     ...   },   \"ingestedAt\": \"...\",   \"storedAt\": \"...\" } ```  **Request Headers:** - `X-OpenMeter-Signature` (optional): Webhook signature for verification  **Query Parameters:** - `tenant_id` (required): Tenant identifier - `pool_id` (required): Credit pool identifier  **Response:** - 201: Event processed successfully - 400: Invalid event format or missing required fields - 500: Processing error  **Idempotency:** - Uses CloudEvent `id` field as idempotency key - Duplicate events are safely ignored (UNIQUE constraint)

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

Handle batch of OpenMeter webhook CloudEvents.  Processes multiple CloudEvents in a single request. Each event is processed independently (idempotent).  **Request Body:** ```json {   \"events\": [     { \"specversion\": \"1.0\", \"type\": \"usage\", ... },     { \"specversion\": \"1.0\", \"type\": \"usage\", ... }   ] } ```  **Response:** - 201: All events processed (some may have failed individually) - Results include per-event status  **Query Parameters:** - `tenant_id` (required): Tenant identifier - `pool_id` (required): Credit pool identifier

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

