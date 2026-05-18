# moolabs.PlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amend_plan_endpoint_v1**](PlansApi.md#amend_plan_endpoint_v1) | **POST** /v1/arc/cases/{case_id}/payment-plans/{plan_id}/amend | Amend Plan Endpoint
[**create_plan_endpoint_v1**](PlansApi.md#create_plan_endpoint_v1) | **POST** /v1/arc/cases/{case_id}/payment-plans | Create Plan Endpoint
[**list_installments_endpoint_v1**](PlansApi.md#list_installments_endpoint_v1) | **GET** /v1/arc/cases/{case_id}/payment-plans/{plan_id}/installments | List Installments Endpoint
[**reschedule_installment_endpoint_v1**](PlansApi.md#reschedule_installment_endpoint_v1) | **POST** /v1/arc/cases/{case_id}/payment-plans/{plan_id}/installments/{installment_id}/reschedule | Reschedule Installment Endpoint
[**waive_installment_endpoint_v1**](PlansApi.md#waive_installment_endpoint_v1) | **POST** /v1/arc/cases/{case_id}/payment-plans/{plan_id}/installments/{installment_id}/waive | Waive Installment Endpoint


# **amend_plan_endpoint_v1**
> object amend_plan_endpoint_v1(case_id, plan_id, plan_amend_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Amend Plan Endpoint

POST /payment-plans/{plan_id}/amend — Amend plan (creates new version).

### Example


```python
import moolabs
from moolabs.models.plan_amend_request import PlanAmendRequest
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
    api_instance = moolabs.PlansApi(api_client)
    case_id = 'case_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    plan_amend_request = moolabs.PlanAmendRequest() # PlanAmendRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Amend Plan Endpoint
        api_response = api_instance.amend_plan_endpoint_v1(case_id, plan_id, plan_amend_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PlansApi->amend_plan_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->amend_plan_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **plan_amend_request** | [**PlanAmendRequest**](PlanAmendRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **create_plan_endpoint_v1**
> object create_plan_endpoint_v1(case_id, plan_create_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Plan Endpoint

POST /cases/{case_id}/payment-plans — Create a payment plan.

### Example


```python
import moolabs
from moolabs.models.plan_create_request import PlanCreateRequest
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
    api_instance = moolabs.PlansApi(api_client)
    case_id = 'case_id_example' # str | 
    plan_create_request = moolabs.PlanCreateRequest() # PlanCreateRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Plan Endpoint
        api_response = api_instance.create_plan_endpoint_v1(case_id, plan_create_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PlansApi->create_plan_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->create_plan_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **plan_create_request** | [**PlanCreateRequest**](PlanCreateRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **list_installments_endpoint_v1**
> object list_installments_endpoint_v1(case_id, plan_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Installments Endpoint

GET /payment-plans/{plan_id}/installments — List installments.

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
    api_instance = moolabs.PlansApi(api_client)
    case_id = 'case_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Installments Endpoint
        api_response = api_instance.list_installments_endpoint_v1(case_id, plan_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PlansApi->list_installments_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->list_installments_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **reschedule_installment_endpoint_v1**
> object reschedule_installment_endpoint_v1(case_id, plan_id, installment_id, reschedule_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Reschedule Installment Endpoint

POST /installments/{inst_id}/reschedule — Reschedule an installment.

### Example


```python
import moolabs
from moolabs.models.reschedule_request import RescheduleRequest
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
    api_instance = moolabs.PlansApi(api_client)
    case_id = 'case_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    installment_id = 'installment_id_example' # str | 
    reschedule_request = moolabs.RescheduleRequest() # RescheduleRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Reschedule Installment Endpoint
        api_response = api_instance.reschedule_installment_endpoint_v1(case_id, plan_id, installment_id, reschedule_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PlansApi->reschedule_installment_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->reschedule_installment_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **installment_id** | **str**|  | 
 **reschedule_request** | [**RescheduleRequest**](RescheduleRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **waive_installment_endpoint_v1**
> object waive_installment_endpoint_v1(case_id, plan_id, installment_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Waive Installment Endpoint

POST /installments/{inst_id}/waive — Waive an installment.

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
    api_instance = moolabs.PlansApi(api_client)
    case_id = 'case_id_example' # str | 
    plan_id = 'plan_id_example' # str | 
    installment_id = 'installment_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Waive Installment Endpoint
        api_response = api_instance.waive_installment_endpoint_v1(case_id, plan_id, installment_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PlansApi->waive_installment_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->waive_installment_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **plan_id** | **str**|  | 
 **installment_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

