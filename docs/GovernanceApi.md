# moolabs.GovernanceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_strategy_endpoint**](GovernanceApi.md#create_strategy_endpoint) | **POST** /v1/arc/governance/strategies | Create Strategy Endpoint
[**delete_strategy_endpoint**](GovernanceApi.md#delete_strategy_endpoint) | **DELETE** /v1/arc/governance/strategies/{strategy_id} | Delete Strategy Endpoint
[**get_cash_app_config_endpoint_v1_arc**](GovernanceApi.md#get_cash_app_config_endpoint_v1_arc) | **GET** /v1/arc/governance/cash-app-config | Get Cash App Config Endpoint
[**get_strategy_endpoint**](GovernanceApi.md#get_strategy_endpoint) | **GET** /v1/arc/governance/strategies/{strategy_id} | Get Strategy Endpoint
[**kill_switch_endpoint_v1_arc**](GovernanceApi.md#kill_switch_endpoint_v1_arc) | **POST** /v1/arc/governance/agent-policies/{agent_type}/kill-switch | Kill Switch Endpoint
[**list_evaluations_endpoint**](GovernanceApi.md#list_evaluations_endpoint) | **GET** /v1/arc/governance/evaluations | List Evaluations Endpoint
[**list_policies_endpoint_v1**](GovernanceApi.md#list_policies_endpoint_v1) | **GET** /v1/arc/governance/agent-policies | List Policies Endpoint
[**list_strategies_endpoint**](GovernanceApi.md#list_strategies_endpoint) | **GET** /v1/arc/governance/strategies | List Strategies Endpoint
[**shadow_mode_endpoint_v1_arc**](GovernanceApi.md#shadow_mode_endpoint_v1_arc) | **POST** /v1/arc/governance/agent-policies/{agent_type}/shadow-mode | Shadow Mode Endpoint
[**strategy_preview_endpoint_v1**](GovernanceApi.md#strategy_preview_endpoint_v1) | **POST** /v1/arc/governance/strategy-preview | Strategy Preview Endpoint
[**update_cash_app_config_endpoint_v1_arc**](GovernanceApi.md#update_cash_app_config_endpoint_v1_arc) | **PUT** /v1/arc/governance/cash-app-config | Update Cash App Config Endpoint
[**update_policy_endpoint_v1**](GovernanceApi.md#update_policy_endpoint_v1) | **PUT** /v1/arc/governance/agent-policies/{policy_id} | Update Policy Endpoint
[**update_strategy_endpoint**](GovernanceApi.md#update_strategy_endpoint) | **PUT** /v1/arc/governance/strategies/{strategy_id} | Update Strategy Endpoint


# **create_strategy_endpoint**
> object create_strategy_endpoint(x_api_key, strategy_create_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Create Strategy Endpoint

POST /governance/strategies — Create a new dunning strategy.

### Example


```python
import moolabs
from moolabs.models.strategy_create_request import StrategyCreateRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    strategy_create_request = moolabs.StrategyCreateRequest() # StrategyCreateRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Create Strategy Endpoint
        api_response = api_instance.create_strategy_endpoint(x_api_key, strategy_create_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->create_strategy_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->create_strategy_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **strategy_create_request** | [**StrategyCreateRequest**](StrategyCreateRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_strategy_endpoint**
> object delete_strategy_endpoint(strategy_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Delete Strategy Endpoint

DELETE /governance/strategies/{id} — Delete a dunning strategy.

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
    api_instance = moolabs.GovernanceApi(api_client)
    strategy_id = 'strategy_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Delete Strategy Endpoint
        api_response = api_instance.delete_strategy_endpoint(strategy_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->delete_strategy_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->delete_strategy_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_cash_app_config_endpoint_v1_arc**
> object get_cash_app_config_endpoint_v1_arc(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Cash App Config Endpoint

GET /governance/cash-app-config — Read cash application configuration.

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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Cash App Config Endpoint
        api_response = api_instance.get_cash_app_config_endpoint_v1_arc(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->get_cash_app_config_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->get_cash_app_config_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_strategy_endpoint**
> object get_strategy_endpoint(strategy_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Strategy Endpoint

GET /governance/strategies/{id} — Get a single strategy.

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
    api_instance = moolabs.GovernanceApi(api_client)
    strategy_id = 'strategy_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Strategy Endpoint
        api_response = api_instance.get_strategy_endpoint(strategy_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->get_strategy_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->get_strategy_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **kill_switch_endpoint_v1_arc**
> object kill_switch_endpoint_v1_arc(agent_type, x_api_key, kill_switch_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Kill Switch Endpoint

POST /governance/agent-policies/{agent_type}/kill-switch — Toggle kill switch.

### Example


```python
import moolabs
from moolabs.models.kill_switch_request import KillSwitchRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    agent_type = 'agent_type_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    kill_switch_request = moolabs.KillSwitchRequest() # KillSwitchRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Kill Switch Endpoint
        api_response = api_instance.kill_switch_endpoint_v1_arc(agent_type, x_api_key, kill_switch_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->kill_switch_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->kill_switch_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_type** | **str**|  | 
 **x_api_key** | **str**|  | 
 **kill_switch_request** | [**KillSwitchRequest**](KillSwitchRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **list_evaluations_endpoint**
> object list_evaluations_endpoint(x_api_key, agent_type=agent_type, evaluation_type=evaluation_type, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Evaluations Endpoint

GET /governance/evaluations — List agent evaluations.

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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    agent_type = 'agent_type_example' # str |  (optional)
    evaluation_type = 'evaluation_type_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Evaluations Endpoint
        api_response = api_instance.list_evaluations_endpoint(x_api_key, agent_type=agent_type, evaluation_type=evaluation_type, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->list_evaluations_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->list_evaluations_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **agent_type** | **str**|  | [optional] 
 **evaluation_type** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **list_policies_endpoint_v1**
> object list_policies_endpoint_v1(x_api_key, agent_type=agent_type, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Policies Endpoint

GET /governance/agent-policies — List agent policies.

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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    agent_type = 'agent_type_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Policies Endpoint
        api_response = api_instance.list_policies_endpoint_v1(x_api_key, agent_type=agent_type, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->list_policies_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->list_policies_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **agent_type** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **list_strategies_endpoint**
> object list_strategies_endpoint(x_api_key, risk_tier=risk_tier, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Strategies Endpoint

GET /governance/strategies — List dunning strategies.

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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    risk_tier = 'risk_tier_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Strategies Endpoint
        api_response = api_instance.list_strategies_endpoint(x_api_key, risk_tier=risk_tier, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->list_strategies_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->list_strategies_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **risk_tier** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **shadow_mode_endpoint_v1_arc**
> object shadow_mode_endpoint_v1_arc(agent_type, x_api_key, shadow_mode_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Shadow Mode Endpoint

POST /governance/agent-policies/{agent_type}/shadow-mode — Toggle shadow mode.

### Example


```python
import moolabs
from moolabs.models.shadow_mode_request import ShadowModeRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    agent_type = 'agent_type_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    shadow_mode_request = moolabs.ShadowModeRequest() # ShadowModeRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Shadow Mode Endpoint
        api_response = api_instance.shadow_mode_endpoint_v1_arc(agent_type, x_api_key, shadow_mode_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->shadow_mode_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->shadow_mode_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_type** | **str**|  | 
 **x_api_key** | **str**|  | 
 **shadow_mode_request** | [**ShadowModeRequest**](ShadowModeRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **strategy_preview_endpoint_v1**
> object strategy_preview_endpoint_v1(x_api_key, strategy_preview_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Strategy Preview Endpoint

POST /governance/strategy-preview — Dry-run strategy preview.

### Example


```python
import moolabs
from moolabs.models.strategy_preview_request import StrategyPreviewRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    strategy_preview_request = moolabs.StrategyPreviewRequest() # StrategyPreviewRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Strategy Preview Endpoint
        api_response = api_instance.strategy_preview_endpoint_v1(x_api_key, strategy_preview_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->strategy_preview_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->strategy_preview_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **strategy_preview_request** | [**StrategyPreviewRequest**](StrategyPreviewRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **update_cash_app_config_endpoint_v1_arc**
> object update_cash_app_config_endpoint_v1_arc(x_api_key, cash_app_config_update_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Update Cash App Config Endpoint

PUT /governance/cash-app-config — Update cash application configuration.

### Example


```python
import moolabs
from moolabs.models.cash_app_config_update_request import CashAppConfigUpdateRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    cash_app_config_update_request = moolabs.CashAppConfigUpdateRequest() # CashAppConfigUpdateRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Update Cash App Config Endpoint
        api_response = api_instance.update_cash_app_config_endpoint_v1_arc(x_api_key, cash_app_config_update_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->update_cash_app_config_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->update_cash_app_config_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **cash_app_config_update_request** | [**CashAppConfigUpdateRequest**](CashAppConfigUpdateRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **update_policy_endpoint_v1**
> object update_policy_endpoint_v1(policy_id, x_api_key, policy_update_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Update Policy Endpoint

PUT /governance/agent-policies/{id} — Update an agent policy.

### Example


```python
import moolabs
from moolabs.models.policy_update_request import PolicyUpdateRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    policy_id = 'policy_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    policy_update_request = moolabs.PolicyUpdateRequest() # PolicyUpdateRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Update Policy Endpoint
        api_response = api_instance.update_policy_endpoint_v1(policy_id, x_api_key, policy_update_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->update_policy_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->update_policy_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **policy_update_request** | [**PolicyUpdateRequest**](PolicyUpdateRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **update_strategy_endpoint**
> object update_strategy_endpoint(strategy_id, x_api_key, strategy_update_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Update Strategy Endpoint

PUT /governance/strategies/{id} — Update a dunning strategy.

### Example


```python
import moolabs
from moolabs.models.strategy_update_request import StrategyUpdateRequest
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
    api_instance = moolabs.GovernanceApi(api_client)
    strategy_id = 'strategy_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    strategy_update_request = moolabs.StrategyUpdateRequest() # StrategyUpdateRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Update Strategy Endpoint
        api_response = api_instance.update_strategy_endpoint(strategy_id, x_api_key, strategy_update_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of GovernanceApi->update_strategy_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GovernanceApi->update_strategy_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **strategy_update_request** | [**StrategyUpdateRequest**](StrategyUpdateRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

