# moolabs.AllocationRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allocation_rule_api**](AllocationRulesApi.md#create_allocation_rule_api) | **POST** /api/v1/allocation-rules | Create an allocation rule
[**delete_allocation_rule_api**](AllocationRulesApi.md#delete_allocation_rule_api) | **DELETE** /api/v1/allocation-rules/{rule_id} | Soft-delete allocation rule (is_active&#x3D;false)
[**get_allocation_rule_api**](AllocationRulesApi.md#get_allocation_rule_api) | **GET** /api/v1/allocation-rules/{rule_id} | Get allocation rule detail
[**list_allocation_rules_api**](AllocationRulesApi.md#list_allocation_rules_api) | **GET** /api/v1/allocation-rules | List allocation rules for tenant
[**trigger_reallocate_api**](AllocationRulesApi.md#trigger_reallocate_api) | **POST** /api/v1/allocation-rules/{rule_id}/reallocate | Manually trigger reallocation for a period
[**update_allocation_rule_api**](AllocationRulesApi.md#update_allocation_rule_api) | **PUT** /api/v1/allocation-rules/{rule_id} | Update allocation rule (triggers retroactive recompute signal)


# **create_allocation_rule_api**
> AllocationRuleResponse create_allocation_rule_api(allocation_rule_create)

Create an allocation rule

Creates a new allocation rule. Validates rule_type and target_type.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.allocation_rule_create import AllocationRuleCreate
from moolabs.models.allocation_rule_response import AllocationRuleResponse
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
    api_instance = moolabs.AllocationRulesApi(api_client)
    allocation_rule_create = moolabs.AllocationRuleCreate() # AllocationRuleCreate | 

    try:
        # Create an allocation rule
        api_response = api_instance.create_allocation_rule_api(allocation_rule_create)
        print("The response of AllocationRulesApi->create_allocation_rule_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationRulesApi->create_allocation_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_rule_create** | [**AllocationRuleCreate**](AllocationRuleCreate.md)|  | 

### Return type

[**AllocationRuleResponse**](AllocationRuleResponse.md)

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

# **delete_allocation_rule_api**
> delete_allocation_rule_api(rule_id)

Soft-delete allocation rule (is_active=false)

Soft-deletes a rule by setting is_active=false. Does not delete historical allocations.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
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
    api_instance = moolabs.AllocationRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Soft-delete allocation rule (is_active=false)
        api_instance.delete_allocation_rule_api(rule_id)
    except Exception as e:
        print("Exception when calling AllocationRulesApi->delete_allocation_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocation_rule_api**
> AllocationRuleResponse get_allocation_rule_api(rule_id)

Get allocation rule detail

Returns a single allocation rule by ID.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.allocation_rule_response import AllocationRuleResponse
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
    api_instance = moolabs.AllocationRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Get allocation rule detail
        api_response = api_instance.get_allocation_rule_api(rule_id)
        print("The response of AllocationRulesApi->get_allocation_rule_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationRulesApi->get_allocation_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**AllocationRuleResponse**](AllocationRuleResponse.md)

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

# **list_allocation_rules_api**
> List[AllocationRuleResponse] list_allocation_rules_api(is_active=is_active, rule_type=rule_type)

List allocation rules for tenant

Returns all allocation rules for the tenant, ordered by priority ASC.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.allocation_rule_response import AllocationRuleResponse
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
    api_instance = moolabs.AllocationRulesApi(api_client)
    is_active = True # bool |  (optional)
    rule_type = 'rule_type_example' # str |  (optional)

    try:
        # List allocation rules for tenant
        api_response = api_instance.list_allocation_rules_api(is_active=is_active, rule_type=rule_type)
        print("The response of AllocationRulesApi->list_allocation_rules_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationRulesApi->list_allocation_rules_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **bool**|  | [optional] 
 **rule_type** | **str**|  | [optional] 

### Return type

[**List[AllocationRuleResponse]**](AllocationRuleResponse.md)

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

# **trigger_reallocate_api**
> ReallocateResponse trigger_reallocate_api(rule_id, reallocate_request)

Manually trigger reallocation for a period

Retroactive recomputation for the specified period.  NOTE: This endpoint re-runs ALL active allocation rules for the specified period, not just the rule identified by rule_id. The rule_id is used only to verify the rule exists and belongs to the tenant. The allocation engine applies every active rule — existing cost_allocations for the period are deleted first, then recreated from scratch. Returns count of new allocation rows created.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.reallocate_request import ReallocateRequest
from moolabs.models.reallocate_response import ReallocateResponse
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
    api_instance = moolabs.AllocationRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    reallocate_request = moolabs.ReallocateRequest() # ReallocateRequest | 

    try:
        # Manually trigger reallocation for a period
        api_response = api_instance.trigger_reallocate_api(rule_id, reallocate_request)
        print("The response of AllocationRulesApi->trigger_reallocate_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationRulesApi->trigger_reallocate_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **reallocate_request** | [**ReallocateRequest**](ReallocateRequest.md)|  | 

### Return type

[**ReallocateResponse**](ReallocateResponse.md)

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

# **update_allocation_rule_api**
> AllocationRuleResponse update_allocation_rule_api(rule_id, allocation_rule_update)

Update allocation rule (triggers retroactive recompute signal)

Updates an allocation rule. Caller should subsequently trigger reallocate via POST /{id}/reallocate for affected periods. The API returns the updated rule; reallocation is not automatically triggered to allow the caller to specify the period.

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.allocation_rule_response import AllocationRuleResponse
from moolabs.models.allocation_rule_update import AllocationRuleUpdate
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
    api_instance = moolabs.AllocationRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    allocation_rule_update = moolabs.AllocationRuleUpdate() # AllocationRuleUpdate | 

    try:
        # Update allocation rule (triggers retroactive recompute signal)
        api_response = api_instance.update_allocation_rule_api(rule_id, allocation_rule_update)
        print("The response of AllocationRulesApi->update_allocation_rule_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllocationRulesApi->update_allocation_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **allocation_rule_update** | [**AllocationRuleUpdate**](AllocationRuleUpdate.md)|  | 

### Return type

[**AllocationRuleResponse**](AllocationRuleResponse.md)

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

