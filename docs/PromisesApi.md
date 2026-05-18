# moolabs.PromisesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_ptp_endpoint**](PromisesApi.md#approve_ptp_endpoint) | **POST** /v1/arc/promises/{ptp_id}/approve | Approve Ptp Endpoint
[**break_ptp_endpoint_v1_arc**](PromisesApi.md#break_ptp_endpoint_v1_arc) | **POST** /v1/arc/cases/{case_id}/promises-to-pay/{ptp_id}/break | Break Ptp Endpoint
[**cancel_ptp_endpoint_v1_arc**](PromisesApi.md#cancel_ptp_endpoint_v1_arc) | **POST** /v1/arc/cases/{case_id}/promises-to-pay/{ptp_id}/cancel | Cancel Ptp Endpoint
[**create_ptp_endpoint_v1_arc**](PromisesApi.md#create_ptp_endpoint_v1_arc) | **POST** /v1/arc/cases/{case_id}/promises-to-pay | Create Ptp Endpoint
[**create_ptp_payment_link_endpoint_v1_arc_cases**](PromisesApi.md#create_ptp_payment_link_endpoint_v1_arc_cases) | **POST** /v1/arc/cases/{case_id}/promises-to-pay/{ptp_id}/payment-link | Create Ptp Payment Link Endpoint
[**fulfill_ptp_endpoint_v1_arc**](PromisesApi.md#fulfill_ptp_endpoint_v1_arc) | **POST** /v1/arc/cases/{case_id}/promises-to-pay/{ptp_id}/fulfill | Fulfill Ptp Endpoint
[**list_ptps_endpoint_v1_arc**](PromisesApi.md#list_ptps_endpoint_v1_arc) | **GET** /v1/arc/cases/{case_id}/promises-to-pay | List Ptps Endpoint
[**reject_ptp_endpoint**](PromisesApi.md#reject_ptp_endpoint) | **POST** /v1/arc/promises/{ptp_id}/reject | Reject Ptp Endpoint


# **approve_ptp_endpoint**
> object approve_ptp_endpoint(ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, ptp_approval_request=ptp_approval_request)

Approve Ptp Endpoint

POST /promises/{ptp_id}/approve — Approve an auto-proposed PTP: flip PROPOSED → OPEN, set ``case.next_promise_due_at``, complete the linked CONFIRM_PTP task.

### Example


```python
import moolabs
from moolabs.models.ptp_approval_request import PTPApprovalRequest
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
    api_instance = moolabs.PromisesApi(api_client)
    ptp_id = 'ptp_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    ptp_approval_request = moolabs.PTPApprovalRequest() # PTPApprovalRequest |  (optional)

    try:
        # Approve Ptp Endpoint
        api_response = api_instance.approve_ptp_endpoint(ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, ptp_approval_request=ptp_approval_request)
        print("The response of PromisesApi->approve_ptp_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->approve_ptp_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptp_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **ptp_approval_request** | [**PTPApprovalRequest**](PTPApprovalRequest.md)|  | [optional] 

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

# **break_ptp_endpoint_v1_arc**
> object break_ptp_endpoint_v1_arc(case_id, ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Break Ptp Endpoint

POST /promises-to-pay/{ptp_id}/break — Mark PTP as broken.

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
    api_instance = moolabs.PromisesApi(api_client)
    case_id = 'case_id_example' # str | 
    ptp_id = 'ptp_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Break Ptp Endpoint
        api_response = api_instance.break_ptp_endpoint_v1_arc(case_id, ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PromisesApi->break_ptp_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->break_ptp_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **ptp_id** | **str**|  | 
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

# **cancel_ptp_endpoint_v1_arc**
> object cancel_ptp_endpoint_v1_arc(case_id, ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Cancel Ptp Endpoint

POST /promises-to-pay/{ptp_id}/cancel — Cancel PTP.

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
    api_instance = moolabs.PromisesApi(api_client)
    case_id = 'case_id_example' # str | 
    ptp_id = 'ptp_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Cancel Ptp Endpoint
        api_response = api_instance.cancel_ptp_endpoint_v1_arc(case_id, ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PromisesApi->cancel_ptp_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->cancel_ptp_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **ptp_id** | **str**|  | 
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

# **create_ptp_endpoint_v1_arc**
> object create_ptp_endpoint_v1_arc(case_id, ptp_create_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Ptp Endpoint

POST /cases/{case_id}/promises-to-pay — Create a promise-to-pay.

### Example


```python
import moolabs
from moolabs.models.ptp_create_request import PTPCreateRequest
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
    api_instance = moolabs.PromisesApi(api_client)
    case_id = 'case_id_example' # str | 
    ptp_create_request = moolabs.PTPCreateRequest() # PTPCreateRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Ptp Endpoint
        api_response = api_instance.create_ptp_endpoint_v1_arc(case_id, ptp_create_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PromisesApi->create_ptp_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->create_ptp_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **ptp_create_request** | [**PTPCreateRequest**](PTPCreateRequest.md)|  | 
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

# **create_ptp_payment_link_endpoint_v1_arc_cases**
> PTPPaymentLinkResponse create_ptp_payment_link_endpoint_v1_arc_cases(case_id, ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Ptp Payment Link Endpoint

POST /promises-to-pay/{ptp_id}/payment-link — Create a hosted card-payment link.

### Example


```python
import moolabs
from moolabs.models.ptp_payment_link_response import PTPPaymentLinkResponse
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
    api_instance = moolabs.PromisesApi(api_client)
    case_id = 'case_id_example' # str | 
    ptp_id = 'ptp_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Ptp Payment Link Endpoint
        api_response = api_instance.create_ptp_payment_link_endpoint_v1_arc_cases(case_id, ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PromisesApi->create_ptp_payment_link_endpoint_v1_arc_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->create_ptp_payment_link_endpoint_v1_arc_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **ptp_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PTPPaymentLinkResponse**](PTPPaymentLinkResponse.md)

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

# **fulfill_ptp_endpoint_v1_arc**
> object fulfill_ptp_endpoint_v1_arc(case_id, ptp_id, ptp_fulfill_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Fulfill Ptp Endpoint

POST /promises-to-pay/{ptp_id}/fulfill — Record fulfillment.

### Example


```python
import moolabs
from moolabs.models.ptp_fulfill_request import PTPFulfillRequest
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
    api_instance = moolabs.PromisesApi(api_client)
    case_id = 'case_id_example' # str | 
    ptp_id = 'ptp_id_example' # str | 
    ptp_fulfill_request = moolabs.PTPFulfillRequest() # PTPFulfillRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Fulfill Ptp Endpoint
        api_response = api_instance.fulfill_ptp_endpoint_v1_arc(case_id, ptp_id, ptp_fulfill_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PromisesApi->fulfill_ptp_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->fulfill_ptp_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **ptp_id** | **str**|  | 
 **ptp_fulfill_request** | [**PTPFulfillRequest**](PTPFulfillRequest.md)|  | 
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

# **list_ptps_endpoint_v1_arc**
> object list_ptps_endpoint_v1_arc(case_id, status=status, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Ptps Endpoint

GET /cases/{case_id}/promises-to-pay — List PTPs.

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
    api_instance = moolabs.PromisesApi(api_client)
    case_id = 'case_id_example' # str | 
    status = 'status_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Ptps Endpoint
        api_response = api_instance.list_ptps_endpoint_v1_arc(case_id, status=status, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of PromisesApi->list_ptps_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->list_ptps_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **status** | **str**|  | [optional] 
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

# **reject_ptp_endpoint**
> object reject_ptp_endpoint(ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, ptp_approval_request=ptp_approval_request)

Reject Ptp Endpoint

POST /promises/{ptp_id}/reject — Reject an auto-proposed PTP: flip PROPOSED → CANCELLED, leave case scheduling untouched, complete the CONFIRM_PTP task with outcome=rejected.

### Example


```python
import moolabs
from moolabs.models.ptp_approval_request import PTPApprovalRequest
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
    api_instance = moolabs.PromisesApi(api_client)
    ptp_id = 'ptp_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    ptp_approval_request = moolabs.PTPApprovalRequest() # PTPApprovalRequest |  (optional)

    try:
        # Reject Ptp Endpoint
        api_response = api_instance.reject_ptp_endpoint(ptp_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, ptp_approval_request=ptp_approval_request)
        print("The response of PromisesApi->reject_ptp_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromisesApi->reject_ptp_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ptp_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **ptp_approval_request** | [**PTPApprovalRequest**](PTPApprovalRequest.md)|  | [optional] 

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

