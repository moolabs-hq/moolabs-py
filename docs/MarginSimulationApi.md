# moolabs.MarginSimulationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_scenarios**](MarginSimulationApi.md#compare_scenarios) | **POST** /api/v1/cost/margins/simulate/compare | ACE margin simulation — multi-scenario comparison
[**simulate_margin**](MarginSimulationApi.md#simulate_margin) | **POST** /api/v1/cost/margins/simulate | ACE margin simulation — single scenario


# **compare_scenarios**
> ScenarioCompareResponse compare_scenarios(scenario_request)

ACE margin simulation — multi-scenario comparison

Run multiple margin simulations and return side-by-side comparison. Each scenario can have different feature_key, price, volume, model_mix. Partial failures are included with an 'error' field (does not abort all scenarios).

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.scenario_compare_response import ScenarioCompareResponse
from moolabs.models.scenario_request import ScenarioRequest
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
    api_instance = moolabs.MarginSimulationApi(api_client)
    scenario_request = moolabs.ScenarioRequest() # ScenarioRequest | 

    try:
        # ACE margin simulation — multi-scenario comparison
        api_response = api_instance.compare_scenarios(scenario_request)
        print("The response of MarginSimulationApi->compare_scenarios:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginSimulationApi->compare_scenarios: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenario_request** | [**ScenarioRequest**](ScenarioRequest.md)|  | 

### Return type

[**ScenarioCompareResponse**](ScenarioCompareResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_margin**
> SimulateMarginResponse simulate_margin(simulate_margin_request)

ACE margin simulation — single scenario

Projects margin for a proposed deal using BOM standard costs.  1. Loads active BOM for feature_key. 2. Simulates cost with proposed_model_mix overrides at current rates. 3. Computes projected revenue, cost, and margin for the simulation period. 4. Returns risk_flags and reconciliation_basis.  projected_margin_pct = null if proposed_price_per_event <= 0 (zero-valued-burn).

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.simulate_margin_request import SimulateMarginRequest
from moolabs.models.simulate_margin_response import SimulateMarginResponse
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
    api_instance = moolabs.MarginSimulationApi(api_client)
    simulate_margin_request = moolabs.SimulateMarginRequest() # SimulateMarginRequest | 

    try:
        # ACE margin simulation — single scenario
        api_response = api_instance.simulate_margin(simulate_margin_request)
        print("The response of MarginSimulationApi->simulate_margin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginSimulationApi->simulate_margin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulate_margin_request** | [**SimulateMarginRequest**](SimulateMarginRequest.md)|  | 

### Return type

[**SimulateMarginResponse**](SimulateMarginResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

