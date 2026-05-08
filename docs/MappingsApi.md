# moolabs.MappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mapping**](MappingsApi.md#create_mapping) | **POST** /v1/mappings | Create Mapping
[**list_mappings**](MappingsApi.md#list_mappings) | **GET** /v1/mappings | List Mappings


# **create_mapping**
> MappingResponse create_mapping(tenant_id, create_mapping_request)

Create Mapping

Create or update a feature key mapping.  Maps a meter_slug to a feature_key for usage event rating. This is a bitemporal update - closes any existing active mapping and creates a new one.

### Example


```python
import moolabs
from moolabs.models.create_mapping_request import CreateMappingRequest
from moolabs.models.mapping_response import MappingResponse
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
    api_instance = moolabs.MappingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    create_mapping_request = moolabs.CreateMappingRequest() # CreateMappingRequest | 

    try:
        # Create Mapping
        api_response = api_instance.create_mapping(tenant_id, create_mapping_request)
        print("The response of MappingsApi->create_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->create_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **create_mapping_request** | [**CreateMappingRequest**](CreateMappingRequest.md)|  | 

### Return type

[**MappingResponse**](MappingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mappings**
> List[MappingResponse] list_mappings(tenant_id, meter_slug=meter_slug, feature_key=feature_key)

List Mappings

List feature key mappings.  Returns all mappings for the tenant, optionally filtered by meter_slug or feature_key.

### Example


```python
import moolabs
from moolabs.models.mapping_response import MappingResponse
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
    api_instance = moolabs.MappingsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    meter_slug = 'meter_slug_example' # str | Filter by meter slug (optional)
    feature_key = 'feature_key_example' # str | Filter by feature key (optional)

    try:
        # List Mappings
        api_response = api_instance.list_mappings(tenant_id, meter_slug=meter_slug, feature_key=feature_key)
        print("The response of MappingsApi->list_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->list_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **meter_slug** | **str**| Filter by meter slug | [optional] 
 **feature_key** | **str**| Filter by feature key | [optional] 

### Return type

[**List[MappingResponse]**](MappingResponse.md)

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

