# moolabs.EscalationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_escalation**](EscalationsApi.md#create_escalation) | **POST** /v1/arc/cases/{case_id}/escalations | Create Escalation
[**dismiss_escalation**](EscalationsApi.md#dismiss_escalation) | **POST** /v1/arc/cases/{case_id}/escalations/{escalation_id}/dismiss | Dismiss Escalation
[**dispatch_escalation_action**](EscalationsApi.md#dispatch_escalation_action) | **POST** /v1/arc/escalations/{escalation_id}/actions | Dispatch Escalation Action
[**get_escalation**](EscalationsApi.md#get_escalation) | **GET** /v1/arc/cases/{case_id}/escalations/{escalation_id} | Get Escalation
[**list_escalations**](EscalationsApi.md#list_escalations) | **GET** /v1/arc/cases/{case_id}/escalations | List Escalations
[**resolve_escalation**](EscalationsApi.md#resolve_escalation) | **POST** /v1/arc/cases/{case_id}/escalations/{escalation_id}/resolve | Resolve Escalation
[**update_escalation**](EscalationsApi.md#update_escalation) | **PATCH** /v1/arc/cases/{case_id}/escalations/{escalation_id} | Update Escalation


# **create_escalation**
> EscalationResponse create_escalation(case_id, x_api_key, escalation_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Create Escalation

Create an escalation.

### Example


```python
import moolabs
from moolabs.models.escalation_create import EscalationCreate
from moolabs.models.escalation_response import EscalationResponse
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
    api_instance = moolabs.EscalationsApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    escalation_create = moolabs.EscalationCreate() # EscalationCreate | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Create Escalation
        api_response = api_instance.create_escalation(case_id, x_api_key, escalation_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->create_escalation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->create_escalation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **escalation_create** | [**EscalationCreate**](EscalationCreate.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationResponse**](EscalationResponse.md)

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

# **dismiss_escalation**
> EscalationResponse dismiss_escalation(case_id, escalation_id, x_api_key, escalation_dismiss_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Dismiss Escalation

Dismiss an escalation (Spec B Task 10).  ``hard=true`` additionally suppresses the no-response trigger from immediately re-firing on the same case.  Always emits a ``DISMISS_REASON`` learning signal for Spec D consumption.

### Example


```python
import moolabs
from moolabs.models.escalation_dismiss_request import EscalationDismissRequest
from moolabs.models.escalation_response import EscalationResponse
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
    api_instance = moolabs.EscalationsApi(api_client)
    case_id = 'case_id_example' # str | 
    escalation_id = 'escalation_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    escalation_dismiss_request = moolabs.EscalationDismissRequest() # EscalationDismissRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Dismiss Escalation
        api_response = api_instance.dismiss_escalation(case_id, escalation_id, x_api_key, escalation_dismiss_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->dismiss_escalation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->dismiss_escalation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **escalation_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **escalation_dismiss_request** | [**EscalationDismissRequest**](EscalationDismissRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationResponse**](EscalationResponse.md)

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

# **dispatch_escalation_action**
> EscalationActionResponse dispatch_escalation_action(escalation_id, x_api_key, escalation_action_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Dispatch Escalation Action

Run one of the 8 card actions against the escalation's case.  ``tenant_id`` comes from the auth context — never the request body. The escalation row must belong to this tenant or we 404 (no info leak about whether the id exists in another tenant).

### Example


```python
import moolabs
from moolabs.models.escalation_action_request import EscalationActionRequest
from moolabs.models.escalation_action_response import EscalationActionResponse
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
    api_instance = moolabs.EscalationsApi(api_client)
    escalation_id = 'escalation_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    escalation_action_request = moolabs.EscalationActionRequest() # EscalationActionRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Dispatch Escalation Action
        api_response = api_instance.dispatch_escalation_action(escalation_id, x_api_key, escalation_action_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->dispatch_escalation_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->dispatch_escalation_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escalation_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **escalation_action_request** | [**EscalationActionRequest**](EscalationActionRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationActionResponse**](EscalationActionResponse.md)

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

# **get_escalation**
> EscalationResponse get_escalation(case_id, escalation_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Escalation

Get a single escalation.

### Example


```python
import moolabs
from moolabs.models.escalation_response import EscalationResponse
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
    api_instance = moolabs.EscalationsApi(api_client)
    case_id = 'case_id_example' # str | 
    escalation_id = 'escalation_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Escalation
        api_response = api_instance.get_escalation(case_id, escalation_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->get_escalation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->get_escalation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **escalation_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationResponse**](EscalationResponse.md)

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

# **list_escalations**
> EscalationListResponse list_escalations(case_id, x_api_key, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Escalations

List escalations for a case.

### Example


```python
import moolabs
from moolabs.models.escalation_list_response import EscalationListResponse
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
    api_instance = moolabs.EscalationsApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Escalations
        api_response = api_instance.list_escalations(case_id, x_api_key, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->list_escalations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->list_escalations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationListResponse**](EscalationListResponse.md)

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

# **resolve_escalation**
> EscalationResponse resolve_escalation(case_id, escalation_id, x_api_key, escalation_resolve_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Resolve Escalation

Resolve an escalation.

### Example


```python
import moolabs
from moolabs.models.escalation_resolve_request import EscalationResolveRequest
from moolabs.models.escalation_response import EscalationResponse
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
    api_instance = moolabs.EscalationsApi(api_client)
    case_id = 'case_id_example' # str | 
    escalation_id = 'escalation_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    escalation_resolve_request = moolabs.EscalationResolveRequest() # EscalationResolveRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Resolve Escalation
        api_response = api_instance.resolve_escalation(case_id, escalation_id, x_api_key, escalation_resolve_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->resolve_escalation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->resolve_escalation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **escalation_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **escalation_resolve_request** | [**EscalationResolveRequest**](EscalationResolveRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationResponse**](EscalationResponse.md)

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

# **update_escalation**
> EscalationResponse update_escalation(case_id, escalation_id, x_api_key, escalation_update, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Update Escalation

Update an escalation.

### Example


```python
import moolabs
from moolabs.models.escalation_response import EscalationResponse
from moolabs.models.escalation_update import EscalationUpdate
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
    api_instance = moolabs.EscalationsApi(api_client)
    case_id = 'case_id_example' # str | 
    escalation_id = 'escalation_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    escalation_update = moolabs.EscalationUpdate() # EscalationUpdate | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Update Escalation
        api_response = api_instance.update_escalation(case_id, escalation_id, x_api_key, escalation_update, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of EscalationsApi->update_escalation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EscalationsApi->update_escalation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **escalation_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **escalation_update** | [**EscalationUpdate**](EscalationUpdate.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EscalationResponse**](EscalationResponse.md)

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

