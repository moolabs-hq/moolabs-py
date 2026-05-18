# moolabs.CasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_case**](CasesApi.md#create_case) | **POST** /v1/arc/cases | Create Case
[**dunning_history_v1**](CasesApi.md#dunning_history_v1) | **GET** /v1/arc/cases/{case_id}/dunning-history | Dunning History
[**escalate_case**](CasesApi.md#escalate_case) | **POST** /v1/arc/cases/{case_id}/escalate | Escalate Case
[**flag_disputed_v1**](CasesApi.md#flag_disputed_v1) | **POST** /v1/arc/cases/{case_id}/invoices/{invoice_id}/flag-disputed | Flag Disputed
[**get_case**](CasesApi.md#get_case) | **GET** /v1/arc/cases/{case_id} | Get Case
[**list_case_tasks**](CasesApi.md#list_case_tasks) | **GET** /v1/arc/cases/{case_id}/tasks | List Case Tasks
[**list_cases**](CasesApi.md#list_cases) | **GET** /v1/arc/cases | List Cases
[**open_from_scope_v1_arc**](CasesApi.md#open_from_scope_v1_arc) | **POST** /v1/arc/cases/open-from-scope | Open From Scope
[**pause_case**](CasesApi.md#pause_case) | **POST** /v1/arc/cases/{case_id}/pause | Pause Case
[**re_scope_case_v1**](CasesApi.md#re_scope_case_v1) | **POST** /v1/arc/cases/{case_id}/re-scope | Re Scope Case
[**recompute_strategy_v1**](CasesApi.md#recompute_strategy_v1) | **POST** /v1/arc/cases/{case_id}/recompute-strategy | Recompute Strategy
[**resume_case**](CasesApi.md#resume_case) | **POST** /v1/arc/cases/{case_id}/resume | Resume Case
[**update_case**](CasesApi.md#update_case) | **PATCH** /v1/arc/cases/{case_id} | Update Case
[**write_off_case_v1**](CasesApi.md#write_off_case_v1) | **POST** /v1/arc/cases/{case_id}/write-off | Write Off Case


# **create_case**
> CaseResponse create_case(case_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Case

Create a new collection case.

### Example


```python
import moolabs
from moolabs.models.case_create import CaseCreate
from moolabs.models.case_response import CaseResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_create = moolabs.CaseCreate() # CaseCreate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Case
        api_response = api_instance.create_case(case_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->create_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->create_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_create** | [**CaseCreate**](CaseCreate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **dunning_history_v1**
> object dunning_history_v1(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Dunning History

GET /cases/{case_id}/dunning-history — Dunning step execution timeline.

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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Dunning History
        api_response = api_instance.dunning_history_v1(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->dunning_history_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->dunning_history_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
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

# **escalate_case**
> CaseResponse escalate_case(case_id, case_escalate_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Escalate Case

Escalate a case. Creates escalation task.

### Example


```python
import moolabs
from moolabs.models.case_escalate_request import CaseEscalateRequest
from moolabs.models.case_response import CaseResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    case_escalate_request = moolabs.CaseEscalateRequest() # CaseEscalateRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Escalate Case
        api_response = api_instance.escalate_case(case_id, case_escalate_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->escalate_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->escalate_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **case_escalate_request** | [**CaseEscalateRequest**](CaseEscalateRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **flag_disputed_v1**
> FlagDisputedResponse flag_disputed_v1(case_id, invoice_id, flag_disputed_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Flag Disputed

Flag invoice as disputed. Invariant 5: disputed ≤ amount. Creates human task.

### Example


```python
import moolabs
from moolabs.models.flag_disputed_request import FlagDisputedRequest
from moolabs.models.flag_disputed_response import FlagDisputedResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    invoice_id = 'invoice_id_example' # str | 
    flag_disputed_request = moolabs.FlagDisputedRequest() # FlagDisputedRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Flag Disputed
        api_response = api_instance.flag_disputed_v1(case_id, invoice_id, flag_disputed_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->flag_disputed_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->flag_disputed_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **invoice_id** | **str**|  | 
 **flag_disputed_request** | [**FlagDisputedRequest**](FlagDisputedRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**FlagDisputedResponse**](FlagDisputedResponse.md)

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

# **get_case**
> CaseResponse get_case(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Get Case

Get a single case by ID.

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Case
        api_response = api_instance.get_case(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->get_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->get_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **list_case_tasks**
> TaskListResponse list_case_tasks(case_id, page=page, page_size=page_size, status=status, task_type=task_type, assigned_to=assigned_to, search=search, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Case Tasks

List tasks scoped to a single case.  Mirrors ``GET /v1/arc/tasks?case_id={id}`` so the case-detail UI can deep-link without composing a query string. Delegates to the same service function — identical response shape.

### Example


```python
import moolabs
from moolabs.models.task_list_response import TaskListResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    status = 'status_example' # str |  (optional)
    task_type = 'task_type_example' # str |  (optional)
    assigned_to = 'assigned_to_example' # str |  (optional)
    search = 'search_example' # str | Substring match on title/description/customer name (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Case Tasks
        api_response = api_instance.list_case_tasks(case_id, page=page, page_size=page_size, status=status, task_type=task_type, assigned_to=assigned_to, search=search, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->list_case_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->list_case_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **status** | **str**|  | [optional] 
 **task_type** | **str**|  | [optional] 
 **assigned_to** | **str**|  | [optional] 
 **search** | **str**| Substring match on title/description/customer name | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TaskListResponse**](TaskListResponse.md)

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

# **list_cases**
> CaseListResponse list_cases(page=page, page_size=page_size, status=status, risk_tier=risk_tier, aging_bucket=aging_bucket, account_id=account_id, customer_id=customer_id, q=q, search=search, has_ptp=has_ptp, sort_by=sort_by, include_invoices=include_invoices, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Cases

List cases with pagination, filters, search, and sort.

### Example


```python
import moolabs
from moolabs.models.case_list_response import CaseListResponse
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
    api_instance = moolabs.CasesApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    status = ['status_example'] # List[str] |  (optional)
    risk_tier = ['risk_tier_example'] # List[str] |  (optional)
    aging_bucket = ['aging_bucket_example'] # List[str] |  (optional)
    account_id = 'account_id_example' # str |  (optional)
    customer_id = 'customer_id_example' # str |  (optional)
    q = 'q_example' # str | Backwards-compatible free-text search alias. Newer callers should prefer `search`. (optional)
    search = 'search_example' # str | Search by account name, customer ID, case ID, or invoice number (optional)
    has_ptp = True # bool | When true, only cases with at least one open PTP; when false, only cases without. Drives the PTP dashboard tile. (optional)
    sort_by = 'sort_by_example' # str | Sort order. Accepted values: created-desc (newest first, default), created-asc (oldest first), amount-desc (highest outstanding first), amount-asc (lowest outstanding first), risk-desc (high risk first). Unknown values fall back to the default active-cases-first ordering. (optional)
    include_invoices = False # bool | Include embedded invoices in each list item (optional) (default to False)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Cases
        api_response = api_instance.list_cases(page=page, page_size=page_size, status=status, risk_tier=risk_tier, aging_bucket=aging_bucket, account_id=account_id, customer_id=customer_id, q=q, search=search, has_ptp=has_ptp, sort_by=sort_by, include_invoices=include_invoices, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->list_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->list_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **status** | [**List[str]**](str.md)|  | [optional] 
 **risk_tier** | [**List[str]**](str.md)|  | [optional] 
 **aging_bucket** | [**List[str]**](str.md)|  | [optional] 
 **account_id** | **str**|  | [optional] 
 **customer_id** | **str**|  | [optional] 
 **q** | **str**| Backwards-compatible free-text search alias. Newer callers should prefer &#x60;search&#x60;. | [optional] 
 **search** | **str**| Search by account name, customer ID, case ID, or invoice number | [optional] 
 **has_ptp** | **bool**| When true, only cases with at least one open PTP; when false, only cases without. Drives the PTP dashboard tile. | [optional] 
 **sort_by** | **str**| Sort order. Accepted values: created-desc (newest first, default), created-asc (oldest first), amount-desc (highest outstanding first), amount-asc (lowest outstanding first), risk-desc (high risk first). Unknown values fall back to the default active-cases-first ordering. | [optional] 
 **include_invoices** | **bool**| Include embedded invoices in each list item | [optional] [default to False]
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseListResponse**](CaseListResponse.md)

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

# **open_from_scope_v1_arc**
> CaseResponse open_from_scope_v1_arc(open_from_scope_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Open From Scope

Idempotent case creation. T1: handles concurrent creation via partial unique index.

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
from moolabs.models.open_from_scope_request import OpenFromScopeRequest
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
    api_instance = moolabs.CasesApi(api_client)
    open_from_scope_request = moolabs.OpenFromScopeRequest() # OpenFromScopeRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Open From Scope
        api_response = api_instance.open_from_scope_v1_arc(open_from_scope_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->open_from_scope_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->open_from_scope_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **open_from_scope_request** | [**OpenFromScopeRequest**](OpenFromScopeRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **pause_case**
> CaseResponse pause_case(case_id, case_pause_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Pause Case

Pause a case — suspends all dunning activity.

### Example


```python
import moolabs
from moolabs.models.case_pause_request import CasePauseRequest
from moolabs.models.case_response import CaseResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    case_pause_request = moolabs.CasePauseRequest() # CasePauseRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Pause Case
        api_response = api_instance.pause_case(case_id, case_pause_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->pause_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->pause_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **case_pause_request** | [**CasePauseRequest**](CasePauseRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **re_scope_case_v1**
> CaseResponse re_scope_case_v1(case_id, re_scope_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Re Scope Case

Add/remove invoices. Recalculates total_outstanding_micros (Invariant 9).

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
from moolabs.models.re_scope_request import ReScopeRequest
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    re_scope_request = moolabs.ReScopeRequest() # ReScopeRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Re Scope Case
        api_response = api_instance.re_scope_case_v1(case_id, re_scope_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->re_scope_case_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->re_scope_case_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **re_scope_request** | [**ReScopeRequest**](ReScopeRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **recompute_strategy_v1**
> CaseResponse recompute_strategy_v1(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Recompute Strategy

Recompute dunning strategy based on current risk tier.

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Recompute Strategy
        api_response = api_instance.recompute_strategy_v1(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->recompute_strategy_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->recompute_strategy_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **resume_case**
> CaseResponse resume_case(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Resume Case

Resume a paused case.

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Resume Case
        api_response = api_instance.resume_case(case_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->resume_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->resume_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **update_case**
> CaseResponse update_case(case_id, case_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Update Case

Partial update of a case.

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
from moolabs.models.case_update import CaseUpdate
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    case_update = moolabs.CaseUpdate() # CaseUpdate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update Case
        api_response = api_instance.update_case(case_id, case_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->update_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->update_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **case_update** | [**CaseUpdate**](CaseUpdate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

# **write_off_case_v1**
> CaseResponse write_off_case_v1(case_id, case_write_off_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Write Off Case

Request write-off. D5: Never autonomous — creates approval task.

### Example


```python
import moolabs
from moolabs.models.case_response import CaseResponse
from moolabs.models.case_write_off_request import CaseWriteOffRequest
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
    api_instance = moolabs.CasesApi(api_client)
    case_id = 'case_id_example' # str | 
    case_write_off_request = moolabs.CaseWriteOffRequest() # CaseWriteOffRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Write Off Case
        api_response = api_instance.write_off_case_v1(case_id, case_write_off_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CasesApi->write_off_case_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CasesApi->write_off_case_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **case_write_off_request** | [**CaseWriteOffRequest**](CaseWriteOffRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**CaseResponse**](CaseResponse.md)

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

