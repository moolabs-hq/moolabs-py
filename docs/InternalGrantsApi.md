# moolabs.InternalGrantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_grants**](InternalGrantsApi.md#activate_grants) | **POST** /v1/internal/grants/activate | Activate Grants
[**plan_change_grants_v1**](InternalGrantsApi.md#plan_change_grants_v1) | **POST** /v1/internal/grants/plan-change | Plan Change Grants
[**renew_grants**](InternalGrantsApi.md#renew_grants) | **POST** /v1/internal/grants/renew | Renew Grants


# **activate_grants**
> object activate_grants(grant_activation_request, dry_run=dry_run, idempotency_key=idempotency_key, authorization=authorization)

Activate Grants

### Example


```python
import moolabs
from moolabs.models.grant_activation_request import GrantActivationRequest
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
    api_instance = moolabs.InternalGrantsApi(api_client)
    grant_activation_request = moolabs.GrantActivationRequest() # GrantActivationRequest | 
    dry_run = False # bool |  (optional) (default to False)
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Activate Grants
        api_response = api_instance.activate_grants(grant_activation_request, dry_run=dry_run, idempotency_key=idempotency_key, authorization=authorization)
        print("The response of InternalGrantsApi->activate_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalGrantsApi->activate_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_activation_request** | [**GrantActivationRequest**](GrantActivationRequest.md)|  | 
 **dry_run** | **bool**|  | [optional] [default to False]
 **idempotency_key** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **plan_change_grants_v1**
> object plan_change_grants_v1(grant_plan_change_request, dry_run=dry_run, idempotency_key=idempotency_key, authorization=authorization)

Plan Change Grants

### Example


```python
import moolabs
from moolabs.models.grant_plan_change_request import GrantPlanChangeRequest
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
    api_instance = moolabs.InternalGrantsApi(api_client)
    grant_plan_change_request = moolabs.GrantPlanChangeRequest() # GrantPlanChangeRequest | 
    dry_run = False # bool |  (optional) (default to False)
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Plan Change Grants
        api_response = api_instance.plan_change_grants_v1(grant_plan_change_request, dry_run=dry_run, idempotency_key=idempotency_key, authorization=authorization)
        print("The response of InternalGrantsApi->plan_change_grants_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalGrantsApi->plan_change_grants_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_plan_change_request** | [**GrantPlanChangeRequest**](GrantPlanChangeRequest.md)|  | 
 **dry_run** | **bool**|  | [optional] [default to False]
 **idempotency_key** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **renew_grants**
> object renew_grants(grant_renewal_request, dry_run=dry_run, idempotency_key=idempotency_key, authorization=authorization)

Renew Grants

### Example


```python
import moolabs
from moolabs.models.grant_renewal_request import GrantRenewalRequest
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
    api_instance = moolabs.InternalGrantsApi(api_client)
    grant_renewal_request = moolabs.GrantRenewalRequest() # GrantRenewalRequest | 
    dry_run = False # bool |  (optional) (default to False)
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Renew Grants
        api_response = api_instance.renew_grants(grant_renewal_request, dry_run=dry_run, idempotency_key=idempotency_key, authorization=authorization)
        print("The response of InternalGrantsApi->renew_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalGrantsApi->renew_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_renewal_request** | [**GrantRenewalRequest**](GrantRenewalRequest.md)|  | 
 **dry_run** | **bool**|  | [optional] [default to False]
 **idempotency_key** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

