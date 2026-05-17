# moolabs.AttributionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gate_status**](AttributionApi.md#get_gate_status) | **GET** /api/v1/attribution/shadow/{run_id}/gate | Evaluate go/no-go gate for a shadow run
[**get_shadow_run_metrics**](AttributionApi.md#get_shadow_run_metrics) | **GET** /api/v1/attribution/shadow/{run_id}/metrics | Get WAPE, coverage, and algorithm breakdown for a shadow run
[**list_algorithms**](AttributionApi.md#list_algorithms) | **GET** /api/v1/attribution/algorithms | List all 12 attribution algorithms
[**list_shadow_runs**](AttributionApi.md#list_shadow_runs) | **GET** /api/v1/attribution/shadow/runs | List all shadow attribution runs for tenant
[**promote_shadow_run**](AttributionApi.md#promote_shadow_run) | **POST** /api/v1/attribution/shadow/{run_id}/promote | Promote shadow attribution to production (gate must pass)
[**run_shadow_attribution**](AttributionApi.md#run_shadow_attribution) | **POST** /api/v1/attribution/shadow/run | Trigger shadow attribution run for a period


# **get_gate_status**
> GateStatusResponse get_gate_status(run_id, tenant_id)

Evaluate go/no-go gate for a shadow run

Evaluates the go/no-go gate for the shadow run. Gate passes when WAPE < 10% AND coverage > 80%.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.gate_status_response import GateStatusResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AttributionApi(api_client)
    run_id = 'run_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID

    try:
        # Evaluate go/no-go gate for a shadow run
        api_response = api_instance.get_gate_status(run_id, tenant_id)
        print("The response of AttributionApi->get_gate_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributionApi->get_gate_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 

### Return type

[**GateStatusResponse**](GateStatusResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shadow_run_metrics**
> ShadowRunMetrics get_shadow_run_metrics(run_id, tenant_id)

Get WAPE, coverage, and algorithm breakdown for a shadow run

Returns WAPE, coverage_pct, and per-algorithm breakdown for the shadow run.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.shadow_run_metrics import ShadowRunMetrics
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AttributionApi(api_client)
    run_id = 'run_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID

    try:
        # Get WAPE, coverage, and algorithm breakdown for a shadow run
        api_response = api_instance.get_shadow_run_metrics(run_id, tenant_id)
        print("The response of AttributionApi->get_shadow_run_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributionApi->get_shadow_run_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 

### Return type

[**ShadowRunMetrics**](ShadowRunMetrics.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_algorithms**
> List[AlgorithmInfo] list_algorithms()

List all 12 attribution algorithms

Returns the static list of all 12 attribution algorithms in priority order, with name, description, grade, and confidence. No DB query required.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.algorithm_info import AlgorithmInfo
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AttributionApi(api_client)

    try:
        # List all 12 attribution algorithms
        api_response = api_instance.list_algorithms()
        print("The response of AttributionApi->list_algorithms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributionApi->list_algorithms: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AlgorithmInfo]**](AlgorithmInfo.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shadow_runs**
> List[ShadowRunListItem] list_shadow_runs(tenant_id, limit=limit, offset=offset)

List all shadow attribution runs for tenant

Returns all shadow attribution runs for the tenant, most recent first.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.shadow_run_list_item import ShadowRunListItem
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AttributionApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int | Pagination offset (optional) (default to 0)

    try:
        # List all shadow attribution runs for tenant
        api_response = api_instance.list_shadow_runs(tenant_id, limit=limit, offset=offset)
        print("The response of AttributionApi->list_shadow_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributionApi->list_shadow_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant UUID | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**| Pagination offset | [optional] [default to 0]

### Return type

[**List[ShadowRunListItem]**](ShadowRunListItem.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_shadow_run**
> PromoteResponse promote_shadow_run(run_id, tenant_id)

Promote shadow attribution to production (gate must pass)

Promotes a shadow run's attribution results to cost_allocations with allocation_rule_id=NULL (auto-attributed). Gate must pass (WAPE<10%, coverage>80%). Fallback attributions are never promoted. Returns 409 if the gate has not passed.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.promote_response import PromoteResponse
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AttributionApi(api_client)
    run_id = 'run_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID

    try:
        # Promote shadow attribution to production (gate must pass)
        api_response = api_instance.promote_shadow_run(run_id, tenant_id)
        print("The response of AttributionApi->promote_shadow_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributionApi->promote_shadow_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 

### Return type

[**PromoteResponse**](PromoteResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_shadow_attribution**
> ShadowRunSummary run_shadow_attribution(shadow_run_request)

Trigger shadow attribution run for a period

Triggers a full attribution pass in shadow mode for the specified period. Writes results to attribution_shadow_log only — never to cost_allocations. Returns the shadow_run_id and summary statistics.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.shadow_run_request import ShadowRunRequest
from moolabs.models.shadow_run_summary import ShadowRunSummary
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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AttributionApi(api_client)
    shadow_run_request = moolabs.ShadowRunRequest() # ShadowRunRequest | 

    try:
        # Trigger shadow attribution run for a period
        api_response = api_instance.run_shadow_attribution(shadow_run_request)
        print("The response of AttributionApi->run_shadow_attribution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributionApi->run_shadow_attribution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shadow_run_request** | [**ShadowRunRequest**](ShadowRunRequest.md)|  | 

### Return type

[**ShadowRunSummary**](ShadowRunSummary.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

