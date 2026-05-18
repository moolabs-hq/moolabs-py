# moolabs.ArcCommunicationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_communication**](ArcCommunicationsApi.md#approve_communication) | **POST** /v1/arc/cases/{case_id}/communications/{comm_id}/approve | Approve Communication
[**create_communication**](ArcCommunicationsApi.md#create_communication) | **POST** /v1/arc/cases/{case_id}/communications | Create Communication
[**list_communications**](ArcCommunicationsApi.md#list_communications) | **GET** /v1/arc/cases/{case_id}/communications | List Communications
[**reject_communication**](ArcCommunicationsApi.md#reject_communication) | **POST** /v1/arc/cases/{case_id}/communications/{comm_id}/reject | Reject Communication
[**resolve_provider_confirmation_v1_arc**](ArcCommunicationsApi.md#resolve_provider_confirmation_v1_arc) | **POST** /v1/arc/cases/{case_id}/communications/{comm_id}/resolve-provider-confirmation | Resolve Provider Confirmation


# **approve_communication**
> ApprovalActionResponse approve_communication(case_id, comm_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, approval_action_request=approval_action_request)

Approve Communication

Approve and send a draft communication.

### Example


```python
import moolabs
from moolabs.models.approval_action_request import ApprovalActionRequest
from moolabs.models.approval_action_response import ApprovalActionResponse
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
    api_instance = moolabs.ArcCommunicationsApi(api_client)
    case_id = 'case_id_example' # str | 
    comm_id = 'comm_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    approval_action_request = moolabs.ApprovalActionRequest() # ApprovalActionRequest |  (optional)

    try:
        # Approve Communication
        api_response = api_instance.approve_communication(case_id, comm_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, approval_action_request=approval_action_request)
        print("The response of ArcCommunicationsApi->approve_communication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcCommunicationsApi->approve_communication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **comm_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **approval_action_request** | [**ApprovalActionRequest**](ApprovalActionRequest.md)|  | [optional] 

### Return type

[**ApprovalActionResponse**](ApprovalActionResponse.md)

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

# **create_communication**
> CommunicationResponse create_communication(case_id, communication_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Communication

Create a communication for a case.

### Example


```python
import moolabs
from moolabs.models.communication_create import CommunicationCreate
from moolabs.models.communication_response import CommunicationResponse
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
    api_instance = moolabs.ArcCommunicationsApi(api_client)
    case_id = 'case_id_example' # str | 
    communication_create = moolabs.CommunicationCreate() # CommunicationCreate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Communication
        api_response = api_instance.create_communication(case_id, communication_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of ArcCommunicationsApi->create_communication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcCommunicationsApi->create_communication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **communication_create** | [**CommunicationCreate**](CommunicationCreate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CommunicationResponse**](CommunicationResponse.md)

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

# **list_communications**
> CommunicationListResponse list_communications(case_id, page=page, page_size=page_size, direction=direction, channel=channel, status=status, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Communications

List communications for a case.

### Example


```python
import moolabs
from moolabs.models.communication_list_response import CommunicationListResponse
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
    api_instance = moolabs.ArcCommunicationsApi(api_client)
    case_id = 'case_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    direction = 'direction_example' # str |  (optional)
    channel = 'channel_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Communications
        api_response = api_instance.list_communications(case_id, page=page, page_size=page_size, direction=direction, channel=channel, status=status, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of ArcCommunicationsApi->list_communications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcCommunicationsApi->list_communications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **direction** | **str**|  | [optional] 
 **channel** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CommunicationListResponse**](CommunicationListResponse.md)

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

# **reject_communication**
> ApprovalActionResponse reject_communication(case_id, comm_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, approval_action_request=approval_action_request)

Reject Communication

Reject a draft communication.

### Example


```python
import moolabs
from moolabs.models.approval_action_request import ApprovalActionRequest
from moolabs.models.approval_action_response import ApprovalActionResponse
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
    api_instance = moolabs.ArcCommunicationsApi(api_client)
    case_id = 'case_id_example' # str | 
    comm_id = 'comm_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    approval_action_request = moolabs.ApprovalActionRequest() # ApprovalActionRequest |  (optional)

    try:
        # Reject Communication
        api_response = api_instance.reject_communication(case_id, comm_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, approval_action_request=approval_action_request)
        print("The response of ArcCommunicationsApi->reject_communication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcCommunicationsApi->reject_communication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **comm_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **approval_action_request** | [**ApprovalActionRequest**](ApprovalActionRequest.md)|  | [optional] 

### Return type

[**ApprovalActionResponse**](ApprovalActionResponse.md)

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

# **resolve_provider_confirmation_v1_arc**
> ApprovalActionResponse resolve_provider_confirmation_v1_arc(case_id, comm_id, provider_confirmation_repair_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Resolve Provider Confirmation

Operator repair for a communication with unknown provider outcome.

### Example


```python
import moolabs
from moolabs.models.approval_action_response import ApprovalActionResponse
from moolabs.models.provider_confirmation_repair_request import ProviderConfirmationRepairRequest
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
    api_instance = moolabs.ArcCommunicationsApi(api_client)
    case_id = 'case_id_example' # str | 
    comm_id = 'comm_id_example' # str | 
    provider_confirmation_repair_request = moolabs.ProviderConfirmationRepairRequest() # ProviderConfirmationRepairRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Resolve Provider Confirmation
        api_response = api_instance.resolve_provider_confirmation_v1_arc(case_id, comm_id, provider_confirmation_repair_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of ArcCommunicationsApi->resolve_provider_confirmation_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcCommunicationsApi->resolve_provider_confirmation_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **comm_id** | **str**|  | 
 **provider_confirmation_repair_request** | [**ProviderConfirmationRepairRequest**](ProviderConfirmationRepairRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

### Return type

[**ApprovalActionResponse**](ApprovalActionResponse.md)

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

