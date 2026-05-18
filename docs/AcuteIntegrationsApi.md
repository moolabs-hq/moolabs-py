# moolabs.AcuteIntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_import**](AcuteIntegrationsApi.md#billing_import) | **POST** /api/v1/cost/integrations/billing/import | Manual Tier 5 aggregate billing import
[**configure_helicone**](AcuteIntegrationsApi.md#configure_helicone) | **POST** /api/v1/cost/integrations/helicone | Configure Helicone pull connector
[**configure_langfuse**](AcuteIntegrationsApi.md#configure_langfuse) | **POST** /api/v1/cost/integrations/langfuse | Configure Langfuse pull connector
[**helicone_webhook**](AcuteIntegrationsApi.md#helicone_webhook) | **POST** /api/v1/cost/integrations/helicone/webhook | Receive Helicone webhook push events
[**ingest_otel**](AcuteIntegrationsApi.md#ingest_otel) | **POST** /api/v1/cost/ingest/otel | OTLP/HTTP span ingestion (Tier 2)
[**list_connectors**](AcuteIntegrationsApi.md#list_connectors) | **GET** /api/v1/cost/integrations/connectors | List connector health
[**list_providers**](AcuteIntegrationsApi.md#list_providers) | **GET** /api/v1/cost/integrations/providers | List providers configured in rate catalog
[**rotate_key_api**](AcuteIntegrationsApi.md#rotate_key_api) | **PUT** /api/v1/cost/integrations/{connector_type}/rotate-key | Rotate connector API key (24h grace period for previous key)


# **billing_import**
> BillingImportResponse billing_import(billing_import_request, x_tenant_id=x_tenant_id)

Manual Tier 5 aggregate billing import

Manually import aggregate spend for a provider and period.  NOTE: Tier 5 data is aggregate-only — no customer or feature drill-down.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.billing_import_request import BillingImportRequest
from moolabs.models.billing_import_response import BillingImportResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    billing_import_request = moolabs.BillingImportRequest() # BillingImportRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Manual Tier 5 aggregate billing import
        api_response = api_instance.billing_import(billing_import_request, x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->billing_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->billing_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_import_request** | [**BillingImportRequest**](BillingImportRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**BillingImportResponse**](BillingImportResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_helicone**
> ConnectorConfigResponse configure_helicone(helicone_config_request, x_tenant_id=x_tenant_id)

Configure Helicone pull connector

Store encrypted Helicone API key and upsert connector_state.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.connector_config_response import ConnectorConfigResponse
from moolabs.models.helicone_config_request import HeliconeConfigRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    helicone_config_request = moolabs.HeliconeConfigRequest() # HeliconeConfigRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Configure Helicone pull connector
        api_response = api_instance.configure_helicone(helicone_config_request, x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->configure_helicone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->configure_helicone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helicone_config_request** | [**HeliconeConfigRequest**](HeliconeConfigRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**ConnectorConfigResponse**](ConnectorConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_langfuse**
> ConnectorConfigResponse configure_langfuse(langfuse_config_request, x_tenant_id=x_tenant_id)

Configure Langfuse pull connector

Store encrypted Langfuse credentials and upsert connector_state.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.connector_config_response import ConnectorConfigResponse
from moolabs.models.langfuse_config_request import LangfuseConfigRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    langfuse_config_request = moolabs.LangfuseConfigRequest() # LangfuseConfigRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Configure Langfuse pull connector
        api_response = api_instance.configure_langfuse(langfuse_config_request, x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->configure_langfuse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->configure_langfuse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langfuse_config_request** | [**LangfuseConfigRequest**](LangfuseConfigRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**ConnectorConfigResponse**](ConnectorConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helicone_webhook**
> OTLPIngestResponse helicone_webhook(helicone_signature=helicone_signature, x_tenant_id=x_tenant_id)

Receive Helicone webhook push events

Receive a Helicone webhook payload (single request/response). Verifies HMAC-SHA256 signature using the configured webhook secret. Parses and writes cost_event with idempotency_key = helicone:{response_id}.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.otlp_ingest_response import OTLPIngestResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    helicone_signature = 'helicone_signature_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Receive Helicone webhook push events
        api_response = api_instance.helicone_webhook(helicone_signature=helicone_signature, x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->helicone_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->helicone_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helicone_signature** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**OTLPIngestResponse**](OTLPIngestResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_otel**
> OTLPIngestResponse ingest_otel(request_body, x_tenant_id=x_tenant_id)

OTLP/HTTP span ingestion (Tier 2)

Accept OTLP JSON body with resourceSpans[].scopeSpans[].spans[]. Filters spans to those with gen_ai.* attributes only.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.otlp_ingest_response import OTLPIngestResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    request_body = None # Dict[str, object] | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # OTLP/HTTP span ingestion (Tier 2)
        api_response = api_instance.ingest_otel(request_body, x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->ingest_otel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->ingest_otel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**OTLPIngestResponse**](OTLPIngestResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> List[ConnectorHealthResponse] list_connectors(x_tenant_id=x_tenant_id)

List connector health

Return connector_state rows for this tenant with health metrics. Tier 5 connectors are flagged with is_aggregate_only=True.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.connector_health_response import ConnectorHealthResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # List connector health
        api_response = api_instance.list_connectors(x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->list_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->list_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[ConnectorHealthResponse]**](ConnectorHealthResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> List[ProviderSummary] list_providers(x_tenant_id=x_tenant_id)

List providers configured in rate catalog

Return distinct providers with active rate catalog entries for this tenant.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.provider_summary import ProviderSummary
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # List providers configured in rate catalog
        api_response = api_instance.list_providers(x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->list_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[ProviderSummary]**](ProviderSummary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_key_api**
> RotateKeyResponse rotate_key_api(connector_type, rotate_key_request, x_tenant_id=x_tenant_id)

Rotate connector API key (24h grace period for previous key)

Rotate the API key for a connector.  Both current_key and previous_key are stored in encrypted_config with timestamps so the external service has a 24h window to propagate the new key.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rotate_key_request import RotateKeyRequest
from moolabs.models.rotate_key_response import RotateKeyResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteIntegrationsApi(api_client)
    connector_type = 'connector_type_example' # str | 
    rotate_key_request = moolabs.RotateKeyRequest() # RotateKeyRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Rotate connector API key (24h grace period for previous key)
        api_response = api_instance.rotate_key_api(connector_type, rotate_key_request, x_tenant_id=x_tenant_id)
        print("The response of AcuteIntegrationsApi->rotate_key_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteIntegrationsApi->rotate_key_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_type** | **str**|  | 
 **rotate_key_request** | [**RotateKeyRequest**](RotateKeyRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**RotateKeyResponse**](RotateKeyResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

