# moolabs.RateCatalogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_import_rates**](RateCatalogApi.md#bulk_import_rates) | **POST** /api/v1/rates/import | Bulk Import Rates
[**create_rate_entry**](RateCatalogApi.md#create_rate_entry) | **POST** /api/v1/rates | Create Rate Entry
[**get_rate_entry**](RateCatalogApi.md#get_rate_entry) | **GET** /api/v1/rates/{rate_id} | Get Rate Entry
[**list_current_rates**](RateCatalogApi.md#list_current_rates) | **GET** /api/v1/rates/current | List Current Rates
[**rate_history**](RateCatalogApi.md#rate_history) | **GET** /api/v1/rates/history | Rate History
[**rates_changed_since**](RateCatalogApi.md#rates_changed_since) | **GET** /api/v1/rates/changes | Rates Changed Since
[**update_rate_entry**](RateCatalogApi.md#update_rate_entry) | **PUT** /api/v1/rates/{rate_id} | Update Rate Entry


# **bulk_import_rates**
> RateBulkImportResponse bulk_import_rates(rate_bulk_import_request)

Bulk Import Rates

Bulk import rates. Source=community_catalog does not overwrite contract/manual_override.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_bulk_import_request import RateBulkImportRequest
from moolabs.models.rate_bulk_import_response import RateBulkImportResponse
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
    api_instance = moolabs.RateCatalogApi(api_client)
    rate_bulk_import_request = moolabs.RateBulkImportRequest() # RateBulkImportRequest | 

    try:
        # Bulk Import Rates
        api_response = api_instance.bulk_import_rates(rate_bulk_import_request)
        print("The response of RateCatalogApi->bulk_import_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->bulk_import_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_bulk_import_request** | [**RateBulkImportRequest**](RateBulkImportRequest.md)|  | 

### Return type

[**RateBulkImportResponse**](RateBulkImportResponse.md)

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

# **create_rate_entry**
> RateCatalogResponse create_rate_entry(rate_catalog_create)

Create Rate Entry

Create a new rate entry. SCD Type 2: closes existing active entry for same key.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_catalog_create import RateCatalogCreate
from moolabs.models.rate_catalog_response import RateCatalogResponse
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
    api_instance = moolabs.RateCatalogApi(api_client)
    rate_catalog_create = moolabs.RateCatalogCreate() # RateCatalogCreate | 

    try:
        # Create Rate Entry
        api_response = api_instance.create_rate_entry(rate_catalog_create)
        print("The response of RateCatalogApi->create_rate_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->create_rate_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_catalog_create** | [**RateCatalogCreate**](RateCatalogCreate.md)|  | 

### Return type

[**RateCatalogResponse**](RateCatalogResponse.md)

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

# **get_rate_entry**
> RateCatalogResponse get_rate_entry(rate_id)

Get Rate Entry

Get a specific rate catalog entry by ID.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_catalog_response import RateCatalogResponse
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
    api_instance = moolabs.RateCatalogApi(api_client)
    rate_id = 'rate_id_example' # str | 

    try:
        # Get Rate Entry
        api_response = api_instance.get_rate_entry(rate_id)
        print("The response of RateCatalogApi->get_rate_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->get_rate_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_id** | **str**|  | 

### Return type

[**RateCatalogResponse**](RateCatalogResponse.md)

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

# **list_current_rates**
> List[RateCatalogResponse] list_current_rates(tenant_id=tenant_id, provider=provider)

List Current Rates

List all currently active rates (effective_to IS NULL) for a tenant.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_catalog_response import RateCatalogResponse
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
    api_instance = moolabs.RateCatalogApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)

    try:
        # List Current Rates
        api_response = api_instance.list_current_rates(tenant_id=tenant_id, provider=provider)
        print("The response of RateCatalogApi->list_current_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->list_current_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 

### Return type

[**List[RateCatalogResponse]**](RateCatalogResponse.md)

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

# **rate_history**
> List[RateCatalogResponse] rate_history(tenant_id=tenant_id, provider=provider, model=model, metric_type=metric_type)

Rate History

Full SCD history for a tenant's rate catalog.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_catalog_response import RateCatalogResponse
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
    api_instance = moolabs.RateCatalogApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    provider = 'provider_example' # str |  (optional)
    model = 'model_example' # str |  (optional)
    metric_type = 'metric_type_example' # str |  (optional)

    try:
        # Rate History
        api_response = api_instance.rate_history(tenant_id=tenant_id, provider=provider, model=model, metric_type=metric_type)
        print("The response of RateCatalogApi->rate_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->rate_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 
 **metric_type** | **str**|  | [optional] 

### Return type

[**List[RateCatalogResponse]**](RateCatalogResponse.md)

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

# **rates_changed_since**
> List[RateCatalogResponse] rates_changed_since(tenant_id=tenant_id, since=since)

Rates Changed Since

Rates changed (created or updated) since the given timestamp.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_catalog_response import RateCatalogResponse
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
    api_instance = moolabs.RateCatalogApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    since = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 timestamp; default = 30 days ago (optional)

    try:
        # Rates Changed Since
        api_response = api_instance.rates_changed_since(tenant_id=tenant_id, since=since)
        print("The response of RateCatalogApi->rates_changed_since:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->rates_changed_since: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **since** | **datetime**| ISO 8601 timestamp; default &#x3D; 30 days ago | [optional] 

### Return type

[**List[RateCatalogResponse]**](RateCatalogResponse.md)

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

# **update_rate_entry**
> RateCatalogResponse update_rate_entry(rate_id, rate_catalog_update)

Update Rate Entry

Supersede-in-place: close old entry, create new one with updated values.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_catalog_response import RateCatalogResponse
from moolabs.models.rate_catalog_update import RateCatalogUpdate
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
    api_instance = moolabs.RateCatalogApi(api_client)
    rate_id = 'rate_id_example' # str | 
    rate_catalog_update = moolabs.RateCatalogUpdate() # RateCatalogUpdate | 

    try:
        # Update Rate Entry
        api_response = api_instance.update_rate_entry(rate_id, rate_catalog_update)
        print("The response of RateCatalogApi->update_rate_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCatalogApi->update_rate_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_id** | **str**|  | 
 **rate_catalog_update** | [**RateCatalogUpdate**](RateCatalogUpdate.md)|  | 

### Return type

[**RateCatalogResponse**](RateCatalogResponse.md)

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

