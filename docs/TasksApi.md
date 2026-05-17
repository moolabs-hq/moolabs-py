# moolabs.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_task**](TasksApi.md#complete_task) | **POST** /v1/arc/tasks/{task_id}/complete | Complete Task
[**get_task**](TasksApi.md#get_task) | **GET** /v1/arc/tasks/{task_id} | Get Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /v1/arc/tasks | List Tasks
[**update_task**](TasksApi.md#update_task) | **PATCH** /v1/arc/tasks/{task_id} | Update Task


# **complete_task**
> TaskResponse complete_task(task_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, task_complete_request=task_complete_request)

Complete Task

Complete a task with optional resolution + run task_type dispatch.

### Example


```python
import moolabs
from moolabs.models.task_complete_request import TaskCompleteRequest
from moolabs.models.task_response import TaskResponse
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
    api_instance = moolabs.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    task_complete_request = moolabs.TaskCompleteRequest() # TaskCompleteRequest |  (optional)

    try:
        # Complete Task
        api_response = api_instance.complete_task(task_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, task_complete_request=task_complete_request)
        print("The response of TasksApi->complete_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->complete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **task_complete_request** | [**TaskCompleteRequest**](TaskCompleteRequest.md)|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **get_task**
> TaskResponse get_task(task_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Task

Get a single task.

### Example


```python
import moolabs
from moolabs.models.task_response import TaskResponse
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
    api_instance = moolabs.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Task
        api_response = api_instance.get_task(task_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of TasksApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

# **list_tasks**
> TaskListResponse list_tasks(x_api_key, page=page, page_size=page_size, status=status, task_type=task_type, assigned_to=assigned_to, case_id=case_id, search=search, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Tasks

List tasks with filters.

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
    api_instance = moolabs.TasksApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    status = 'status_example' # str |  (optional)
    task_type = 'task_type_example' # str |  (optional)
    assigned_to = 'assigned_to_example' # str |  (optional)
    case_id = 'case_id_example' # str |  (optional)
    search = 'search_example' # str | Substring match on title/description/customer name (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Tasks
        api_response = api_instance.list_tasks(x_api_key, page=page, page_size=page_size, status=status, task_type=task_type, assigned_to=assigned_to, case_id=case_id, search=search, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of TasksApi->list_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **status** | **str**|  | [optional] 
 **task_type** | **str**|  | [optional] 
 **assigned_to** | **str**|  | [optional] 
 **case_id** | **str**|  | [optional] 
 **search** | **str**| Substring match on title/description/customer name | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **update_task**
> TaskResponse update_task(task_id, x_api_key, task_update, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Update Task

Update task (assign, priority, due date).

### Example


```python
import moolabs
from moolabs.models.task_response import TaskResponse
from moolabs.models.task_update import TaskUpdate
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
    api_instance = moolabs.TasksApi(api_client)
    task_id = 'task_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    task_update = moolabs.TaskUpdate() # TaskUpdate | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Update Task
        api_response = api_instance.update_task(task_id, x_api_key, task_update, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of TasksApi->update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **task_update** | [**TaskUpdate**](TaskUpdate.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

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

