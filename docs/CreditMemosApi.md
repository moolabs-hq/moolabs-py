# moolabs.CreditMemosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_credit_memo_v1**](CreditMemosApi.md#apply_credit_memo_v1) | **POST** /v1/arc/credit-memos/{memo_id}/apply | Apply Credit Memo
[**approve_credit_memo_v1**](CreditMemosApi.md#approve_credit_memo_v1) | **POST** /v1/arc/credit-memos/{memo_id}/approve | Approve Credit Memo
[**create_credit_memo_v1**](CreditMemosApi.md#create_credit_memo_v1) | **POST** /v1/arc/credit-memos | Create Credit Memo
[**get_credit_memo_v1**](CreditMemosApi.md#get_credit_memo_v1) | **GET** /v1/arc/credit-memos/{memo_id} | Get Credit Memo
[**list_credit_memos_v1_get**](CreditMemosApi.md#list_credit_memos_v1_get) | **GET** /v1/arc/credit-memos | List Credit Memos
[**update_credit_memo_v1**](CreditMemosApi.md#update_credit_memo_v1) | **PATCH** /v1/arc/credit-memos/{memo_id} | Update Credit Memo
[**void_credit_memo_v1**](CreditMemosApi.md#void_credit_memo_v1) | **POST** /v1/arc/credit-memos/{memo_id}/void | Void Credit Memo


# **apply_credit_memo_v1**
> CreditMemoResponse apply_credit_memo_v1(memo_id, x_api_key, credit_memo_apply_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Apply Credit Memo

Apply a credit memo to an invoice.

### Example


```python
import moolabs
from moolabs.models.credit_memo_apply_request import CreditMemoApplyRequest
from moolabs.models.credit_memo_response import CreditMemoResponse
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
    api_instance = moolabs.CreditMemosApi(api_client)
    memo_id = 'memo_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    credit_memo_apply_request = moolabs.CreditMemoApplyRequest() # CreditMemoApplyRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Apply Credit Memo
        api_response = api_instance.apply_credit_memo_v1(memo_id, x_api_key, credit_memo_apply_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->apply_credit_memo_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->apply_credit_memo_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memo_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **credit_memo_apply_request** | [**CreditMemoApplyRequest**](CreditMemoApplyRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoResponse**](CreditMemoResponse.md)

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

# **approve_credit_memo_v1**
> CreditMemoResponse approve_credit_memo_v1(memo_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Approve Credit Memo

Approve a credit memo.

### Example


```python
import moolabs
from moolabs.models.credit_memo_response import CreditMemoResponse
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
    api_instance = moolabs.CreditMemosApi(api_client)
    memo_id = 'memo_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Approve Credit Memo
        api_response = api_instance.approve_credit_memo_v1(memo_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->approve_credit_memo_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->approve_credit_memo_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memo_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoResponse**](CreditMemoResponse.md)

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

# **create_credit_memo_v1**
> CreditMemoResponse create_credit_memo_v1(x_api_key, credit_memo_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Create Credit Memo

Create a credit memo in draft status.

### Example


```python
import moolabs
from moolabs.models.credit_memo_create import CreditMemoCreate
from moolabs.models.credit_memo_response import CreditMemoResponse
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
    api_instance = moolabs.CreditMemosApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    credit_memo_create = moolabs.CreditMemoCreate() # CreditMemoCreate | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Create Credit Memo
        api_response = api_instance.create_credit_memo_v1(x_api_key, credit_memo_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->create_credit_memo_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->create_credit_memo_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **credit_memo_create** | [**CreditMemoCreate**](CreditMemoCreate.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoResponse**](CreditMemoResponse.md)

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

# **get_credit_memo_v1**
> CreditMemoResponse get_credit_memo_v1(memo_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Credit Memo

Get a single credit memo.

### Example


```python
import moolabs
from moolabs.models.credit_memo_response import CreditMemoResponse
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
    api_instance = moolabs.CreditMemosApi(api_client)
    memo_id = 'memo_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Credit Memo
        api_response = api_instance.get_credit_memo_v1(memo_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->get_credit_memo_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->get_credit_memo_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memo_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoResponse**](CreditMemoResponse.md)

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

# **list_credit_memos_v1_get**
> CreditMemoListResponse list_credit_memos_v1_get(x_api_key, account_id=account_id, status=status, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Credit Memos

List credit memos with pagination and optional filters.

### Example


```python
import moolabs
from moolabs.models.credit_memo_list_response import CreditMemoListResponse
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
    api_instance = moolabs.CreditMemosApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    account_id = 'account_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Credit Memos
        api_response = api_instance.list_credit_memos_v1_get(x_api_key, account_id=account_id, status=status, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->list_credit_memos_v1_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->list_credit_memos_v1_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **account_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoListResponse**](CreditMemoListResponse.md)

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

# **update_credit_memo_v1**
> CreditMemoResponse update_credit_memo_v1(memo_id, x_api_key, credit_memo_update, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Update Credit Memo

Update a credit memo (draft only).

### Example


```python
import moolabs
from moolabs.models.credit_memo_response import CreditMemoResponse
from moolabs.models.credit_memo_update import CreditMemoUpdate
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
    api_instance = moolabs.CreditMemosApi(api_client)
    memo_id = 'memo_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    credit_memo_update = moolabs.CreditMemoUpdate() # CreditMemoUpdate | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Update Credit Memo
        api_response = api_instance.update_credit_memo_v1(memo_id, x_api_key, credit_memo_update, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->update_credit_memo_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->update_credit_memo_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memo_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **credit_memo_update** | [**CreditMemoUpdate**](CreditMemoUpdate.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoResponse**](CreditMemoResponse.md)

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

# **void_credit_memo_v1**
> CreditMemoResponse void_credit_memo_v1(memo_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Void Credit Memo

Void a credit memo.

### Example


```python
import moolabs
from moolabs.models.credit_memo_response import CreditMemoResponse
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
    api_instance = moolabs.CreditMemosApi(api_client)
    memo_id = 'memo_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Void Credit Memo
        api_response = api_instance.void_credit_memo_v1(memo_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of CreditMemosApi->void_credit_memo_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditMemosApi->void_credit_memo_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memo_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**CreditMemoResponse**](CreditMemoResponse.md)

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

