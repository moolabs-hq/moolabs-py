# moolabs.BudgetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_alert**](BudgetsApi.md#acknowledge_alert) | **POST** /api/v1/budgets/{budget_id}/alerts/{alert_id}/acknowledge | Acknowledge an alert
[**create_budget**](BudgetsApi.md#create_budget) | **POST** /api/v1/budgets | Create a budget
[**get_budget**](BudgetsApi.md#get_budget) | **GET** /api/v1/budgets/{budget_id} | Get budget with current utilization
[**get_budget_alerts**](BudgetsApi.md#get_budget_alerts) | **GET** /api/v1/budgets/{budget_id}/alerts | Get alerts for this budget
[**get_budget_status**](BudgetsApi.md#get_budget_status) | **GET** /api/v1/budgets/status | Get all budget utilization summary
[**list_budgets**](BudgetsApi.md#list_budgets) | **GET** /api/v1/budgets | List budgets for tenant
[**update_budget**](BudgetsApi.md#update_budget) | **PUT** /api/v1/budgets/{budget_id} | Update a budget


# **acknowledge_alert**
> BudgetAlertResponse acknowledge_alert(budget_id, alert_id)

Acknowledge an alert

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_alert_response import BudgetAlertResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    budget_id = 'budget_id_example' # str | 
    alert_id = 'alert_id_example' # str | 

    try:
        # Acknowledge an alert
        api_response = api_instance.acknowledge_alert(budget_id, alert_id)
        print("The response of BudgetsApi->acknowledge_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->acknowledge_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**|  | 
 **alert_id** | **str**|  | 

### Return type

[**BudgetAlertResponse**](BudgetAlertResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_budget**
> BudgetResponse create_budget(budget_create)

Create a budget

Creates a new cost budget. Default alert thresholds: [50, 80, 95, 100].

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_create import BudgetCreate
from moolabs.models.budget_response import BudgetResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    budget_create = moolabs.BudgetCreate() # BudgetCreate | 

    try:
        # Create a budget
        api_response = api_instance.create_budget(budget_create)
        print("The response of BudgetsApi->create_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->create_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_create** | [**BudgetCreate**](BudgetCreate.md)|  | 

### Return type

[**BudgetResponse**](BudgetResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget**
> BudgetWithUtilization get_budget(budget_id, period_start=period_start, period_end=period_end)

Get budget with current utilization

Returns a budget with its current spend and utilization percentage.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_with_utilization import BudgetWithUtilization
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    budget_id = 'budget_id_example' # str | 
    period_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get budget with current utilization
        api_response = api_instance.get_budget(budget_id, period_start=period_start, period_end=period_end)
        print("The response of BudgetsApi->get_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**|  | 
 **period_start** | **datetime**|  | [optional] 
 **period_end** | **datetime**|  | [optional] 

### Return type

[**BudgetWithUtilization**](BudgetWithUtilization.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_alerts**
> List[BudgetAlertResponse] get_budget_alerts(budget_id, acknowledged=acknowledged, limit=limit, offset=offset)

Get alerts for this budget

Returns fired alerts for a budget, most recent first. Finance acknowledges via API.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_alert_response import BudgetAlertResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    budget_id = 'budget_id_example' # str | 
    acknowledged = True # bool | Filter by acknowledgement state (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get alerts for this budget
        api_response = api_instance.get_budget_alerts(budget_id, acknowledged=acknowledged, limit=limit, offset=offset)
        print("The response of BudgetsApi->get_budget_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**|  | 
 **acknowledged** | **bool**| Filter by acknowledgement state | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[BudgetAlertResponse]**](BudgetAlertResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_budget_status**
> List[BudgetStatusItem] get_budget_status(period_start=period_start, period_end=period_end)

Get all budget utilization summary

Returns current spend and utilization_pct for all active budgets. Uses current month boundaries if period not specified.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_status_item import BudgetStatusItem
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    period_start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get all budget utilization summary
        api_response = api_instance.get_budget_status(period_start=period_start, period_end=period_end)
        print("The response of BudgetsApi->get_budget_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->get_budget_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_start** | **datetime**|  | [optional] 
 **period_end** | **datetime**|  | [optional] 

### Return type

[**List[BudgetStatusItem]**](BudgetStatusItem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_budgets**
> List[BudgetResponse] list_budgets(is_active=is_active, scope_type=scope_type)

List budgets for tenant

Returns all budgets for the tenant.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_response import BudgetResponse
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    is_active = True # bool |  (optional)
    scope_type = 'scope_type_example' # str |  (optional)

    try:
        # List budgets for tenant
        api_response = api_instance.list_budgets(is_active=is_active, scope_type=scope_type)
        print("The response of BudgetsApi->list_budgets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->list_budgets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **bool**|  | [optional] 
 **scope_type** | **str**|  | [optional] 

### Return type

[**List[BudgetResponse]**](BudgetResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_budget**
> BudgetResponse update_budget(budget_id, budget_update)

Update a budget

Updates a cost budget.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.budget_response import BudgetResponse
from moolabs.models.budget_update import BudgetUpdate
from moolabs.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = moolabs.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BudgetsApi(api_client)
    budget_id = 'budget_id_example' # str | 
    budget_update = moolabs.BudgetUpdate() # BudgetUpdate | 

    try:
        # Update a budget
        api_response = api_instance.update_budget(budget_id, budget_update)
        print("The response of BudgetsApi->update_budget:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->update_budget: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_id** | **str**|  | 
 **budget_update** | [**BudgetUpdate**](BudgetUpdate.md)|  | 

### Return type

[**BudgetResponse**](BudgetResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

