# moolabs.CloudBillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_sync_api**](CloudBillingApi.md#configure_sync_api) | **POST** /api/v1/cloud-billing/sync | Configure scheduled sync (stores config, returns 202)
[**get_import_batch_api**](CloudBillingApi.md#get_import_batch_api) | **GET** /api/v1/cloud-billing/imports/{batch_id} | Get batch details with row-level data
[**import_billing_batch_api**](CloudBillingApi.md#import_billing_batch_api) | **POST** /api/v1/cloud-billing/import | Import a billing batch
[**list_import_batches_api**](CloudBillingApi.md#list_import_batches_api) | **GET** /api/v1/cloud-billing/imports | List recent import batches
[**list_resource_map_api_v1**](CloudBillingApi.md#list_resource_map_api_v1) | **GET** /api/v1/cloud-billing/resource-map | List resource_service_map entries
[**upsert_resource_map_api_v1**](CloudBillingApi.md#upsert_resource_map_api_v1) | **POST** /api/v1/cloud-billing/resource-map | Create or update a resource mapping


# **configure_sync_api**
> SyncConfigResponse configure_sync_api(sync_config_request)

Configure scheduled sync (stores config, returns 202)

Configure a scheduled sync for cloud billing data. Actual scheduler integration is out of scope for Phase 3a. Returns 202 Accepted with scheduled status.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.sync_config_request import SyncConfigRequest
from moolabs.models.sync_config_response import SyncConfigResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CloudBillingApi(api_client)
    sync_config_request = moolabs.SyncConfigRequest() # SyncConfigRequest | 

    try:
        # Configure scheduled sync (stores config, returns 202)
        api_response = api_instance.configure_sync_api(sync_config_request)
        print("The response of CloudBillingApi->configure_sync_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudBillingApi->configure_sync_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_config_request** | [**SyncConfigRequest**](SyncConfigRequest.md)|  | 

### Return type

[**SyncConfigResponse**](SyncConfigResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_batch_api**
> ImportBatchDetailResponse get_import_batch_api(batch_id)

Get batch details with row-level data

Returns all rows for a specific import_batch_id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.import_batch_detail_response import ImportBatchDetailResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CloudBillingApi(api_client)
    batch_id = 'batch_id_example' # str | 

    try:
        # Get batch details with row-level data
        api_response = api_instance.get_import_batch_api(batch_id)
        print("The response of CloudBillingApi->get_import_batch_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudBillingApi->get_import_batch_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**|  | 

### Return type

[**ImportBatchDetailResponse**](ImportBatchDetailResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_billing_batch_api**
> ImportBatchResponse import_billing_batch_api(import_batch_request)

Import a billing batch

Import a batch of cloud cost rows for a given provider and billing period. Re-importing the same (tenant, provider, period) supersedes the previous batch. FX conversion is applied at import time and locked.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.import_batch_request import ImportBatchRequest
from moolabs.models.import_batch_response import ImportBatchResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CloudBillingApi(api_client)
    import_batch_request = moolabs.ImportBatchRequest() # ImportBatchRequest | 

    try:
        # Import a billing batch
        api_response = api_instance.import_billing_batch_api(import_batch_request)
        print("The response of CloudBillingApi->import_billing_batch_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudBillingApi->import_billing_batch_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_batch_request** | [**ImportBatchRequest**](ImportBatchRequest.md)|  | 

### Return type

[**ImportBatchResponse**](ImportBatchResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_import_batches_api**
> List[ImportBatchSummary] list_import_batches_api(cloud_provider, limit=limit)

List recent import batches

Returns recent import batches ordered by imported_at DESC, one entry per batch_id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.import_batch_summary import ImportBatchSummary
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CloudBillingApi(api_client)
    cloud_provider = 'cloud_provider_example' # str | 'aws', 'gcp', or 'azure'
    limit = 20 # int |  (optional) (default to 20)

    try:
        # List recent import batches
        api_response = api_instance.list_import_batches_api(cloud_provider, limit=limit)
        print("The response of CloudBillingApi->list_import_batches_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudBillingApi->list_import_batches_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**| &#39;aws&#39;, &#39;gcp&#39;, or &#39;azure&#39; | 
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**List[ImportBatchSummary]**](ImportBatchSummary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_map_api_v1**
> List[ResourceMapResponse] list_resource_map_api_v1(cloud_provider=cloud_provider, is_active=is_active, limit=limit, offset=offset)

List resource_service_map entries

Returns resource-to-service mapping entries for the tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.resource_map_response import ResourceMapResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CloudBillingApi(api_client)
    cloud_provider = 'cloud_provider_example' # str |  (optional)
    is_active = True # bool |  (optional) (default to True)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List resource_service_map entries
        api_response = api_instance.list_resource_map_api_v1(cloud_provider=cloud_provider, is_active=is_active, limit=limit, offset=offset)
        print("The response of CloudBillingApi->list_resource_map_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudBillingApi->list_resource_map_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_provider** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] [default to True]
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[ResourceMapResponse]**](ResourceMapResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_resource_map_api_v1**
> ResourceMapResponse upsert_resource_map_api_v1(resource_map_create_request)

Create or update a resource mapping

Create or update a resource_service_map entry. On conflict (tenant_id, cloud_provider, resource_id), updates existing row.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.resource_map_create_request import ResourceMapCreateRequest
from moolabs.models.resource_map_response import ResourceMapResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.CloudBillingApi(api_client)
    resource_map_create_request = moolabs.ResourceMapCreateRequest() # ResourceMapCreateRequest | 

    try:
        # Create or update a resource mapping
        api_response = api_instance.upsert_resource_map_api_v1(resource_map_create_request)
        print("The response of CloudBillingApi->upsert_resource_map_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudBillingApi->upsert_resource_map_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_map_create_request** | [**ResourceMapCreateRequest**](ResourceMapCreateRequest.md)|  | 

### Return type

[**ResourceMapResponse**](ResourceMapResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

