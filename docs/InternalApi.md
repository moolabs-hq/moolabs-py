# moolabs.InternalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**grant_arc_dunning_template_permission_v1_internal_arc**](InternalApi.md#grant_arc_dunning_template_permission_v1_internal_arc) | **POST** /v1/internal/arc-dunning-template-permissions/grants | Grant Arc Dunning Template Permission
[**replay_tenant_provisioning_v1**](InternalApi.md#replay_tenant_provisioning_v1) | **POST** /v1/internal/tenant-provision/replay | Replay Tenant Provisioning
[**revoke_arc_dunning_template_permission_v1_internal_arc**](InternalApi.md#revoke_arc_dunning_template_permission_v1_internal_arc) | **POST** /v1/internal/arc-dunning-template-permissions/grants/{grant_id}/revoke | Revoke Arc Dunning Template Permission
[**tenant_provision_v1**](InternalApi.md#tenant_provision_v1) | **POST** /v1/internal/tenant-provision | Tenant Provision


# **grant_arc_dunning_template_permission_v1_internal_arc**
> object grant_arc_dunning_template_permission_v1_internal_arc(arc_dunning_permission_grant_request)

Grant Arc Dunning Template Permission

### Example


```python
import moolabs
from moolabs.models.arc_dunning_permission_grant_request import ArcDunningPermissionGrantRequest
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
    arc_dunning_permission_grant_request = moolabs.ArcDunningPermissionGrantRequest() # ArcDunningPermissionGrantRequest | 

    try:
        # Grant Arc Dunning Template Permission
        api_response = api_instance.grant_arc_dunning_template_permission_v1_internal_arc(arc_dunning_permission_grant_request)
        print("The response of InternalApi->grant_arc_dunning_template_permission_v1_internal_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->grant_arc_dunning_template_permission_v1_internal_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arc_dunning_permission_grant_request** | [**ArcDunningPermissionGrantRequest**](ArcDunningPermissionGrantRequest.md)|  | 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **revoke_arc_dunning_template_permission_v1_internal_arc**
> object revoke_arc_dunning_template_permission_v1_internal_arc(grant_id, arc_dunning_permission_revoke_request)

Revoke Arc Dunning Template Permission

### Example


```python
import moolabs
from moolabs.models.arc_dunning_permission_revoke_request import ArcDunningPermissionRevokeRequest
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
    grant_id = 'grant_id_example' # str | 
    arc_dunning_permission_revoke_request = moolabs.ArcDunningPermissionRevokeRequest() # ArcDunningPermissionRevokeRequest | 

    try:
        # Revoke Arc Dunning Template Permission
        api_response = api_instance.revoke_arc_dunning_template_permission_v1_internal_arc(grant_id, arc_dunning_permission_revoke_request)
        print("The response of InternalApi->revoke_arc_dunning_template_permission_v1_internal_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalApi->revoke_arc_dunning_template_permission_v1_internal_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  | 
 **arc_dunning_permission_revoke_request** | [**ArcDunningPermissionRevokeRequest**](ArcDunningPermissionRevokeRequest.md)|  | 

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

