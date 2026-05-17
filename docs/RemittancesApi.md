# moolabs.RemittancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remittance**](RemittancesApi.md#create_remittance) | **POST** /v1/arc/remittances | Create Remittance
[**get_unapplied_cash_v1**](RemittancesApi.md#get_unapplied_cash_v1) | **GET** /v1/arc/remittances/{remittance_id}/unapplied-cash | Get Unapplied Cash
[**resolve_unapplied_endpoint_v1**](RemittancesApi.md#resolve_unapplied_endpoint_v1) | **POST** /v1/arc/remittances/{remittance_id}/unapplied-cash/{uc_id}/resolve | Resolve Unapplied Endpoint


# **create_remittance**
> RemittanceResponse create_remittance(x_api_key, remittance_create_request, force_create=force_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Create Remittance

POST /remittances — Ingest remittance with dedup checks.

### Example


```python
import moolabs
from moolabs.models.remittance_create_request import RemittanceCreateRequest
from moolabs.models.remittance_response import RemittanceResponse
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
    api_instance = moolabs.RemittancesApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    remittance_create_request = moolabs.RemittanceCreateRequest() # RemittanceCreateRequest | 
    force_create = False # bool |  (optional) (default to False)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Create Remittance
        api_response = api_instance.create_remittance(x_api_key, remittance_create_request, force_create=force_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of RemittancesApi->create_remittance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemittancesApi->create_remittance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **remittance_create_request** | [**RemittanceCreateRequest**](RemittanceCreateRequest.md)|  | 
 **force_create** | **bool**|  | [optional] [default to False]
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**RemittanceResponse**](RemittanceResponse.md)

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

# **get_unapplied_cash_v1**
> List[UnappliedCashResponse] get_unapplied_cash_v1(remittance_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Unapplied Cash

GET /remittances/{id}/unapplied-cash — List unapplied cash.

### Example


```python
import moolabs
from moolabs.models.unapplied_cash_response import UnappliedCashResponse
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
    api_instance = moolabs.RemittancesApi(api_client)
    remittance_id = 'remittance_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Unapplied Cash
        api_response = api_instance.get_unapplied_cash_v1(remittance_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of RemittancesApi->get_unapplied_cash_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemittancesApi->get_unapplied_cash_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remittance_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**List[UnappliedCashResponse]**](UnappliedCashResponse.md)

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

# **resolve_unapplied_endpoint_v1**
> UnappliedCashResponse resolve_unapplied_endpoint_v1(remittance_id, uc_id, x_api_key, resolve_unapplied_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Resolve Unapplied Endpoint

POST /remittances/{id}/unapplied-cash/{uc_id}/resolve — Resolve unapplied cash.

### Example


```python
import moolabs
from moolabs.models.resolve_unapplied_request import ResolveUnappliedRequest
from moolabs.models.unapplied_cash_response import UnappliedCashResponse
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
    api_instance = moolabs.RemittancesApi(api_client)
    remittance_id = 'remittance_id_example' # str | 
    uc_id = 'uc_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    resolve_unapplied_request = moolabs.ResolveUnappliedRequest() # ResolveUnappliedRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Resolve Unapplied Endpoint
        api_response = api_instance.resolve_unapplied_endpoint_v1(remittance_id, uc_id, x_api_key, resolve_unapplied_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of RemittancesApi->resolve_unapplied_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemittancesApi->resolve_unapplied_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remittance_id** | **str**|  | 
 **uc_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **resolve_unapplied_request** | [**ResolveUnappliedRequest**](ResolveUnappliedRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**UnappliedCashResponse**](UnappliedCashResponse.md)

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

