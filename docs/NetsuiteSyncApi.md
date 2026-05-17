# moolabs.NetsuiteSyncApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_run**](NetsuiteSyncApi.md#get_run) | **GET** /v1/integrations/netsuite/sync/runs/{sync_run_id} | Get Run
[**list_credit_memos_v1**](NetsuiteSyncApi.md#list_credit_memos_v1) | **GET** /v1/integrations/netsuite/sync/credit-memos | List Credit Memos
[**list_customers**](NetsuiteSyncApi.md#list_customers) | **GET** /v1/integrations/netsuite/sync/customers | List Customers
[**list_invoices**](NetsuiteSyncApi.md#list_invoices) | **GET** /v1/integrations/netsuite/sync/invoices | List Invoices
[**list_payments**](NetsuiteSyncApi.md#list_payments) | **GET** /v1/integrations/netsuite/sync/payments | List Payments
[**list_runs**](NetsuiteSyncApi.md#list_runs) | **GET** /v1/integrations/netsuite/sync/runs | List Runs
[**trigger_sync**](NetsuiteSyncApi.md#trigger_sync) | **POST** /v1/integrations/netsuite/sync/trigger | Trigger Sync


# **get_run**
> SyncRunItem get_run(sync_run_id)

Get Run

### Example


```python
import moolabs
from moolabs.models.sync_run_item import SyncRunItem
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    sync_run_id = 'sync_run_id_example' # str | 

    try:
        # Get Run
        api_response = api_instance.get_run(sync_run_id)
        print("The response of NetsuiteSyncApi->get_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->get_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_run_id** | **str**|  | 

### Return type

[**SyncRunItem**](SyncRunItem.md)

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

# **list_credit_memos_v1**
> PaginatedCreditMemos list_credit_memos_v1(customer_id=customer_id, modified_since=modified_since, limit=limit, cursor=cursor)

List Credit Memos

### Example


```python
import moolabs
from moolabs.models.paginated_credit_memos import PaginatedCreditMemos
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    customer_id = 'customer_id_example' # str |  (optional)
    modified_since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List Credit Memos
        api_response = api_instance.list_credit_memos_v1(customer_id=customer_id, modified_since=modified_since, limit=limit, cursor=cursor)
        print("The response of NetsuiteSyncApi->list_credit_memos_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->list_credit_memos_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | [optional] 
 **modified_since** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 

### Return type

[**PaginatedCreditMemos**](PaginatedCreditMemos.md)

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

# **list_customers**
> PaginatedCustomers list_customers(modified_since=modified_since, limit=limit, cursor=cursor, netsuite_id=netsuite_id)

List Customers

### Example


```python
import moolabs
from moolabs.models.paginated_customers import PaginatedCustomers
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    modified_since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    netsuite_id = 'netsuite_id_example' # str |  (optional)

    try:
        # List Customers
        api_response = api_instance.list_customers(modified_since=modified_since, limit=limit, cursor=cursor, netsuite_id=netsuite_id)
        print("The response of NetsuiteSyncApi->list_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->list_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modified_since** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **netsuite_id** | **str**|  | [optional] 

### Return type

[**PaginatedCustomers**](PaginatedCustomers.md)

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

# **list_invoices**
> PaginatedInvoices list_invoices(customer_id=customer_id, status=status, modified_since=modified_since, limit=limit, cursor=cursor)

List Invoices

### Example


```python
import moolabs
from moolabs.models.paginated_invoices import PaginatedInvoices
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    customer_id = 'customer_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    modified_since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List Invoices
        api_response = api_instance.list_invoices(customer_id=customer_id, status=status, modified_since=modified_since, limit=limit, cursor=cursor)
        print("The response of NetsuiteSyncApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **modified_since** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 

### Return type

[**PaginatedInvoices**](PaginatedInvoices.md)

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

# **list_payments**
> PaginatedPayments list_payments(customer_id=customer_id, modified_since=modified_since, limit=limit, cursor=cursor)

List Payments

### Example


```python
import moolabs
from moolabs.models.paginated_payments import PaginatedPayments
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    customer_id = 'customer_id_example' # str |  (optional)
    modified_since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List Payments
        api_response = api_instance.list_payments(customer_id=customer_id, modified_since=modified_since, limit=limit, cursor=cursor)
        print("The response of NetsuiteSyncApi->list_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->list_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | [optional] 
 **modified_since** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 

### Return type

[**PaginatedPayments**](PaginatedPayments.md)

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

# **list_runs**
> PaginatedSyncRuns list_runs(status=status, limit=limit, cursor=cursor)

List Runs

### Example


```python
import moolabs
from moolabs.models.paginated_sync_runs import PaginatedSyncRuns
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    status = 'status_example' # str |  (optional)
    limit = 56 # int |  (optional)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List Runs
        api_response = api_instance.list_runs(status=status, limit=limit, cursor=cursor)
        print("The response of NetsuiteSyncApi->list_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->list_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 

### Return type

[**PaginatedSyncRuns**](PaginatedSyncRuns.md)

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

# **trigger_sync**
> AppApiV1IntegrationsNetsuiteSyncRouterTriggerResponse trigger_sync(trigger_request=trigger_request)

Trigger Sync

### Example


```python
import moolabs
from moolabs.models.app_api_v1_integrations_netsuite_sync_router_trigger_response import AppApiV1IntegrationsNetsuiteSyncRouterTriggerResponse
from moolabs.models.trigger_request import TriggerRequest
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
    api_instance = moolabs.NetsuiteSyncApi(api_client)
    trigger_request = moolabs.TriggerRequest() # TriggerRequest |  (optional)

    try:
        # Trigger Sync
        api_response = api_instance.trigger_sync(trigger_request=trigger_request)
        print("The response of NetsuiteSyncApi->trigger_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetsuiteSyncApi->trigger_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_request** | [**TriggerRequest**](TriggerRequest.md)|  | [optional] 

### Return type

[**AppApiV1IntegrationsNetsuiteSyncRouterTriggerResponse**](AppApiV1IntegrationsNetsuiteSyncRouterTriggerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

