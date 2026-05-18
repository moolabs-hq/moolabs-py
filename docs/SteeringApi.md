# moolabs.SteeringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_task**](SteeringApi.md#approve_task) | **POST** /v1/arc/tasks/{task_id}/approve | Approve Task
[**steer_ask_customer_v1**](SteeringApi.md#steer_ask_customer_v1) | **POST** /v1/arc/tasks/{task_id}/steer/ask-customer | Steer Ask Customer
[**steer_escalate**](SteeringApi.md#steer_escalate) | **POST** /v1/arc/tasks/{task_id}/steer/escalate | Steer Escalate
[**steer_override**](SteeringApi.md#steer_override) | **POST** /v1/arc/tasks/{task_id}/steer/override | Steer Override
[**steer_reattempt**](SteeringApi.md#steer_reattempt) | **POST** /v1/arc/tasks/{task_id}/steer/reattempt | Steer Reattempt


# **approve_task**
> ApproveResponse approve_task(task_id, approve_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)

Approve Task

### Example


```python
import moolabs
from moolabs.models.approve_request import ApproveRequest
from moolabs.models.approve_response import ApproveResponse
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
    api_instance = moolabs.SteeringApi(api_client)
    task_id = 'task_id_example' # str | 
    approve_request = moolabs.ApproveRequest() # ApproveRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_acting_user = 'x_acting_user_example' # str |  (optional)

    try:
        # Approve Task
        api_response = api_instance.approve_task(task_id, approve_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)
        print("The response of SteeringApi->approve_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteeringApi->approve_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **approve_request** | [**ApproveRequest**](ApproveRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_acting_user** | **str**|  | [optional] 

### Return type

[**ApproveResponse**](ApproveResponse.md)

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

# **steer_ask_customer_v1**
> AskCustomerResponse steer_ask_customer_v1(task_id, ask_customer_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)

Steer Ask Customer

### Example


```python
import moolabs
from moolabs.models.ask_customer_request import AskCustomerRequest
from moolabs.models.ask_customer_response import AskCustomerResponse
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
    api_instance = moolabs.SteeringApi(api_client)
    task_id = 'task_id_example' # str | 
    ask_customer_request = moolabs.AskCustomerRequest() # AskCustomerRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_acting_user = 'x_acting_user_example' # str |  (optional)

    try:
        # Steer Ask Customer
        api_response = api_instance.steer_ask_customer_v1(task_id, ask_customer_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)
        print("The response of SteeringApi->steer_ask_customer_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteeringApi->steer_ask_customer_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **ask_customer_request** | [**AskCustomerRequest**](AskCustomerRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_acting_user** | **str**|  | [optional] 

### Return type

[**AskCustomerResponse**](AskCustomerResponse.md)

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

# **steer_escalate**
> EscalateResponse steer_escalate(task_id, escalate_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)

Steer Escalate

### Example


```python
import moolabs
from moolabs.models.escalate_request import EscalateRequest
from moolabs.models.escalate_response import EscalateResponse
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
    api_instance = moolabs.SteeringApi(api_client)
    task_id = 'task_id_example' # str | 
    escalate_request = moolabs.EscalateRequest() # EscalateRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_acting_user = 'x_acting_user_example' # str |  (optional)

    try:
        # Steer Escalate
        api_response = api_instance.steer_escalate(task_id, escalate_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)
        print("The response of SteeringApi->steer_escalate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteeringApi->steer_escalate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **escalate_request** | [**EscalateRequest**](EscalateRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_acting_user** | **str**|  | [optional] 

### Return type

[**EscalateResponse**](EscalateResponse.md)

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

# **steer_override**
> OverrideResponse steer_override(task_id, override_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)

Steer Override

### Example


```python
import moolabs
from moolabs.models.override_request import OverrideRequest
from moolabs.models.override_response import OverrideResponse
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
    api_instance = moolabs.SteeringApi(api_client)
    task_id = 'task_id_example' # str | 
    override_request = moolabs.OverrideRequest() # OverrideRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_acting_user = 'x_acting_user_example' # str |  (optional)

    try:
        # Steer Override
        api_response = api_instance.steer_override(task_id, override_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)
        print("The response of SteeringApi->steer_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteeringApi->steer_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **override_request** | [**OverrideRequest**](OverrideRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_acting_user** | **str**|  | [optional] 

### Return type

[**OverrideResponse**](OverrideResponse.md)

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

# **steer_reattempt**
> ReattemptResponse steer_reattempt(task_id, reattempt_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)

Steer Reattempt

### Example


```python
import moolabs
from moolabs.models.reattempt_request import ReattemptRequest
from moolabs.models.reattempt_response import ReattemptResponse
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
    api_instance = moolabs.SteeringApi(api_client)
    task_id = 'task_id_example' # str | 
    reattempt_request = moolabs.ReattemptRequest() # ReattemptRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_acting_user = 'x_acting_user_example' # str |  (optional)

    try:
        # Steer Reattempt
        api_response = api_instance.steer_reattempt(task_id, reattempt_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_acting_user=x_acting_user)
        print("The response of SteeringApi->steer_reattempt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SteeringApi->steer_reattempt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **reattempt_request** | [**ReattemptRequest**](ReattemptRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_acting_user** | **str**|  | [optional] 

### Return type

[**ReattemptResponse**](ReattemptResponse.md)

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

