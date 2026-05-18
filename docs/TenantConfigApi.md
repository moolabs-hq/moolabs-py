# moolabs.TenantConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tenant_config**](TenantConfigApi.md#get_tenant_config) | **GET** /v1/tenant/config | Get tenant regional config for SDK auto-discovery


# **get_tenant_config**
> TenantConfigResponse get_tenant_config()

Get tenant regional config for SDK auto-discovery

Return the authenticated tenant's region and regional endpoints.  SDKs call this once at startup to discover which ingest endpoint to use. The response is cacheable for 1 hour.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.tenant_config_response import TenantConfigResponse
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
    api_instance = moolabs.TenantConfigApi(api_client)

    try:
        # Get tenant regional config for SDK auto-discovery
        api_response = api_instance.get_tenant_config()
        print("The response of TenantConfigApi->get_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantConfigApi->get_tenant_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantConfigResponse**](TenantConfigResponse.md)

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

