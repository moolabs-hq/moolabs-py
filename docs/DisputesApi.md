# moolabs.DisputesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_evidence_endpoint**](DisputesApi.md#add_evidence_endpoint) | **POST** /v1/arc/disputes/{dispute_id}/evidence | Add Evidence Endpoint
[**add_external_doc_evidence_endpoint**](DisputesApi.md#add_external_doc_evidence_endpoint) | **POST** /v1/arc/disputes/{dispute_id}/evidence/upload | Add External Doc Evidence Endpoint
[**approve_dispute_endpoint**](DisputesApi.md#approve_dispute_endpoint) | **POST** /v1/arc/disputes/{dispute_id}/approve | Approve Dispute Endpoint
[**get_dispute_endpoint**](DisputesApi.md#get_dispute_endpoint) | **GET** /v1/arc/disputes/{dispute_id} | Get Dispute Endpoint
[**list_disputes_endpoint**](DisputesApi.md#list_disputes_endpoint) | **GET** /v1/arc/disputes | List Disputes Endpoint
[**list_evidence_endpoint**](DisputesApi.md#list_evidence_endpoint) | **GET** /v1/arc/disputes/{dispute_id}/evidence | List Evidence Endpoint
[**reject_dispute_endpoint**](DisputesApi.md#reject_dispute_endpoint) | **POST** /v1/arc/disputes/{dispute_id}/reject | Reject Dispute Endpoint
[**resolve_dispute_endpoint**](DisputesApi.md#resolve_dispute_endpoint) | **POST** /v1/arc/disputes/{dispute_id}/resolve | Resolve Dispute Endpoint
[**review_evidence_endpoint**](DisputesApi.md#review_evidence_endpoint) | **POST** /v1/arc/disputes/{dispute_id}/evidence/{evidence_id}/review | Review Evidence Endpoint
[**update_dispute_endpoint**](DisputesApi.md#update_dispute_endpoint) | **PATCH** /v1/arc/disputes/{dispute_id} | Update Dispute Endpoint


# **add_evidence_endpoint**
> EvidenceResponse add_evidence_endpoint(dispute_id, evidence_create_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Add Evidence Endpoint

POST /disputes/{id}/evidence — Add non-file-backed evidence to a dispute.

### Example


```python
import moolabs
from moolabs.models.evidence_create_request import EvidenceCreateRequest
from moolabs.models.evidence_response import EvidenceResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    evidence_create_request = moolabs.EvidenceCreateRequest() # EvidenceCreateRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Add Evidence Endpoint
        api_response = api_instance.add_evidence_endpoint(dispute_id, evidence_create_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->add_evidence_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->add_evidence_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **evidence_create_request** | [**EvidenceCreateRequest**](EvidenceCreateRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**EvidenceResponse**](EvidenceResponse.md)

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

# **add_external_doc_evidence_endpoint**
> EvidenceResponse add_external_doc_evidence_endpoint(dispute_id, evidence_type, attachment, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, summary=summary, amount_micros=amount_micros)

Add External Doc Evidence Endpoint

POST /disputes/{id}/evidence/upload — Add file-backed external-doc evidence.

### Example


```python
import moolabs
from moolabs.models.evidence_response import EvidenceResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    evidence_type = 'evidence_type_example' # str | 
    attachment = None # bytearray | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    summary = 'summary_example' # str |  (optional)
    amount_micros = 56 # int |  (optional)

    try:
        # Add External Doc Evidence Endpoint
        api_response = api_instance.add_external_doc_evidence_endpoint(dispute_id, evidence_type, attachment, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, summary=summary, amount_micros=amount_micros)
        print("The response of DisputesApi->add_external_doc_evidence_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->add_external_doc_evidence_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **evidence_type** | **str**|  | 
 **attachment** | **bytearray**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **summary** | **str**|  | [optional] 
 **amount_micros** | **int**|  | [optional] 

### Return type

[**EvidenceResponse**](EvidenceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_dispute_endpoint**
> DisputeResponse approve_dispute_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, dispute_approval_request=dispute_approval_request)

Approve Dispute Endpoint

POST /disputes/{id}/approve — Approve an auto-proposed dispute: flip PROPOSED → OPEN, create the invoice link, bump ``anchor.disputed_micros``, and complete the linked RESOLVE_DISPUTE task.

### Example


```python
import moolabs
from moolabs.models.dispute_approval_request import DisputeApprovalRequest
from moolabs.models.dispute_response import DisputeResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    dispute_approval_request = moolabs.DisputeApprovalRequest() # DisputeApprovalRequest |  (optional)

    try:
        # Approve Dispute Endpoint
        api_response = api_instance.approve_dispute_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, dispute_approval_request=dispute_approval_request)
        print("The response of DisputesApi->approve_dispute_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->approve_dispute_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **dispute_approval_request** | [**DisputeApprovalRequest**](DisputeApprovalRequest.md)|  | [optional] 

### Return type

[**DisputeResponse**](DisputeResponse.md)

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

# **get_dispute_endpoint**
> DisputeResponse get_dispute_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Get Dispute Endpoint

GET /disputes/{id} — Get a single dispute.

### Example


```python
import moolabs
from moolabs.models.dispute_response import DisputeResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Dispute Endpoint
        api_response = api_instance.get_dispute_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->get_dispute_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->get_dispute_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DisputeResponse**](DisputeResponse.md)

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

# **list_disputes_endpoint**
> DisputeListResponse list_disputes_endpoint(page=page, page_size=page_size, case_id=case_id, status=status, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Disputes Endpoint

GET /disputes — List disputes with filters.

### Example


```python
import moolabs
from moolabs.models.dispute_list_response import DisputeListResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    case_id = 'case_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Disputes Endpoint
        api_response = api_instance.list_disputes_endpoint(page=page, page_size=page_size, case_id=case_id, status=status, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->list_disputes_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->list_disputes_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **case_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DisputeListResponse**](DisputeListResponse.md)

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

# **list_evidence_endpoint**
> EvidenceListResponse list_evidence_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Evidence Endpoint

GET /disputes/{id}/evidence — List evidence for a dispute.

### Example


```python
import moolabs
from moolabs.models.evidence_list_response import EvidenceListResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Evidence Endpoint
        api_response = api_instance.list_evidence_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->list_evidence_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->list_evidence_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**EvidenceListResponse**](EvidenceListResponse.md)

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

# **reject_dispute_endpoint**
> DisputeResponse reject_dispute_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, dispute_approval_request=dispute_approval_request)

Reject Dispute Endpoint

POST /disputes/{id}/reject — Reject an auto-proposed dispute: flip PROPOSED → RESOLVED_INVALID, leave AR accounting untouched, and complete the RESOLVE_DISPUTE task with outcome=rejected.

### Example


```python
import moolabs
from moolabs.models.dispute_approval_request import DisputeApprovalRequest
from moolabs.models.dispute_response import DisputeResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    dispute_approval_request = moolabs.DisputeApprovalRequest() # DisputeApprovalRequest |  (optional)

    try:
        # Reject Dispute Endpoint
        api_response = api_instance.reject_dispute_endpoint(dispute_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, dispute_approval_request=dispute_approval_request)
        print("The response of DisputesApi->reject_dispute_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->reject_dispute_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **dispute_approval_request** | [**DisputeApprovalRequest**](DisputeApprovalRequest.md)|  | [optional] 

### Return type

[**DisputeResponse**](DisputeResponse.md)

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

# **resolve_dispute_endpoint**
> DisputeResponse resolve_dispute_endpoint(dispute_id, dispute_resolve_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Resolve Dispute Endpoint

POST /disputes/{id}/resolve — Resolve a dispute.

### Example


```python
import moolabs
from moolabs.models.dispute_resolve_request import DisputeResolveRequest
from moolabs.models.dispute_response import DisputeResponse
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    dispute_resolve_request = moolabs.DisputeResolveRequest() # DisputeResolveRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Resolve Dispute Endpoint
        api_response = api_instance.resolve_dispute_endpoint(dispute_id, dispute_resolve_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->resolve_dispute_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->resolve_dispute_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **dispute_resolve_request** | [**DisputeResolveRequest**](DisputeResolveRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DisputeResponse**](DisputeResponse.md)

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

# **review_evidence_endpoint**
> EvidenceResponse review_evidence_endpoint(dispute_id, evidence_id, evidence_review_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Review Evidence Endpoint

POST /disputes/{id}/evidence/{eid}/review — Review evidence.

### Example


```python
import moolabs
from moolabs.models.evidence_response import EvidenceResponse
from moolabs.models.evidence_review_request import EvidenceReviewRequest
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    evidence_id = 'evidence_id_example' # str | 
    evidence_review_request = moolabs.EvidenceReviewRequest() # EvidenceReviewRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Review Evidence Endpoint
        api_response = api_instance.review_evidence_endpoint(dispute_id, evidence_id, evidence_review_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->review_evidence_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->review_evidence_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **evidence_id** | **str**|  | 
 **evidence_review_request** | [**EvidenceReviewRequest**](EvidenceReviewRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**EvidenceResponse**](EvidenceResponse.md)

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

# **update_dispute_endpoint**
> DisputeResponse update_dispute_endpoint(dispute_id, dispute_update_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Update Dispute Endpoint

PATCH /disputes/{id} — Update dispute fields.

### Example


```python
import moolabs
from moolabs.models.dispute_response import DisputeResponse
from moolabs.models.dispute_update_request import DisputeUpdateRequest
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
    api_instance = moolabs.DisputesApi(api_client)
    dispute_id = 'dispute_id_example' # str | 
    dispute_update_request = moolabs.DisputeUpdateRequest() # DisputeUpdateRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update Dispute Endpoint
        api_response = api_instance.update_dispute_endpoint(dispute_id, dispute_update_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of DisputesApi->update_dispute_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->update_dispute_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispute_id** | **str**|  | 
 **dispute_update_request** | [**DisputeUpdateRequest**](DisputeUpdateRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DisputeResponse**](DisputeResponse.md)

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

