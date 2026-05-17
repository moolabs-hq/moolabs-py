# moolabs.InternalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replay_tenant_provisioning_v1**](InternalApi.md#replay_tenant_provisioning_v1) | **POST** /v1/internal/tenant-provision/replay | Replay Tenant Provisioning
[**tenant_provision_v1**](InternalApi.md#tenant_provision_v1) | **POST** /v1/internal/tenant-provision | Tenant Provision


# **replay_tenant_provisioning_v1**
> object replay_tenant_provisioning_v1(limit=limit)

Replay Tenant Provisioning

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
    api_instance = moolabs.InternalApi(api_client)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # Replay Tenant Provisioning
        api_response = api_instance.replay_tenant_provisioning_v1(limit=limit)
        print("The response of InternalApi->replay_tenant_provisioning_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->replay_tenant_provisioning_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]

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

# **tenant_provision_v1**
> object tenant_provision_v1(tenant_provision_request)

Tenant Provision

### Example


```python
import moolabs
from moolabs.models.tenant_provision_request import TenantProvisionRequest
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
    api_instance = moolabs.InternalApi(api_client)
    tenant_provision_request = moolabs.TenantProvisionRequest() # TenantProvisionRequest | 

    try:
        # Tenant Provision
        api_response = api_instance.tenant_provision_v1(tenant_provision_request)
        print("The response of InternalApi->tenant_provision_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->tenant_provision_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_provision_request** | [**TenantProvisionRequest**](TenantProvisionRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

