# moolabs.VarianceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_variance**](VarianceApi.md#compute_variance) | **POST** /api/v1/variance/compute | Trigger variance computation (operator)
[**get_bom_variance**](VarianceApi.md#get_bom_variance) | **GET** /api/v1/variance/bom/{bom_id} | BOM-level variance: standard vs actual
[**get_variance_decomposition**](VarianceApi.md#get_variance_decomposition) | **GET** /api/v1/variance/decomposition | Full four-way variance decomposition for feature+period
[**get_variance_summary**](VarianceApi.md#get_variance_summary) | **GET** /api/v1/variance | Variance summary for all features in period


# **compute_variance**
> ComputeVarianceResponse compute_variance(compute_variance_request)

Trigger variance computation (operator)

Operator endpoint: trigger variance computation for feature+period. Upserts into cost_variances table. Returns the computed variance.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.compute_variance_request import ComputeVarianceRequest
from moolabs.models.compute_variance_response import ComputeVarianceResponse
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
    api_instance = moolabs.VarianceApi(api_client)
    compute_variance_request = moolabs.ComputeVarianceRequest() # ComputeVarianceRequest | 

    try:
        # Trigger variance computation (operator)
        api_response = api_instance.compute_variance(compute_variance_request)
        print("The response of VarianceApi->compute_variance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VarianceApi->compute_variance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_variance_request** | [**ComputeVarianceRequest**](ComputeVarianceRequest.md)|  | 

### Return type

[**ComputeVarianceResponse**](ComputeVarianceResponse.md)

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

# **get_bom_variance**
> BomVarianceOut get_bom_variance(bom_id, tenant_id, period_start, period_end)

BOM-level variance: standard vs actual

Computes BOM-level variance (standard total vs actual total) with per-component breakdown.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_variance_out import BomVarianceOut
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
    api_instance = moolabs.VarianceApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    period_start = '2013-10-20T19:20:30+01:00' # datetime | Period start (ISO datetime)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | Period end (ISO datetime)

    try:
        # BOM-level variance: standard vs actual
        api_response = api_instance.get_bom_variance(bom_id, tenant_id, period_start, period_end)
        print("The response of VarianceApi->get_bom_variance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VarianceApi->get_bom_variance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 
 **period_start** | **datetime**| Period start (ISO datetime) | 
 **period_end** | **datetime**| Period end (ISO datetime) | 

### Return type

[**BomVarianceOut**](BomVarianceOut.md)

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

# **get_variance_decomposition**
> VarianceDecompositionOut get_variance_decomposition(tenant_id, feature_key, period_start, period_end, bom_template_id)

Full four-way variance decomposition for feature+period

Full four-way variance decomposition for a specific feature and period. price + usage + volume + mix == total_variance (guaranteed).

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.variance_decomposition_out import VarianceDecompositionOut
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
    api_instance = moolabs.VarianceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    feature_key = 'feature_key_example' # str | Feature key
    period_start = '2013-10-20T19:20:30+01:00' # datetime | Period start (ISO datetime)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | Period end (ISO datetime)
    bom_template_id = 'bom_template_id_example' # str | BOM template UUID

    try:
        # Full four-way variance decomposition for feature+period
        api_response = api_instance.get_variance_decomposition(tenant_id, feature_key, period_start, period_end, bom_template_id)
        print("The response of VarianceApi->get_variance_decomposition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VarianceApi->get_variance_decomposition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant UUID | 
 **feature_key** | **str**| Feature key | 
 **period_start** | **datetime**| Period start (ISO datetime) | 
 **period_end** | **datetime**| Period end (ISO datetime) | 
 **bom_template_id** | **str**| BOM template UUID | 

### Return type

[**VarianceDecompositionOut**](VarianceDecompositionOut.md)

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

# **get_variance_summary**
> VarianceSummaryResponse get_variance_summary(tenant_id, period_start, period_end)

Variance summary for all features in period

Returns variance decomposition for all features in the period. Flags heuristic variances (heuristic_alert=True) with a 2× threshold note.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.variance_summary_response import VarianceSummaryResponse
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
    api_instance = moolabs.VarianceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    period_start = '2013-10-20T19:20:30+01:00' # datetime | Period start (ISO datetime)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | Period end (ISO datetime)

    try:
        # Variance summary for all features in period
        api_response = api_instance.get_variance_summary(tenant_id, period_start, period_end)
        print("The response of VarianceApi->get_variance_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VarianceApi->get_variance_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant UUID | 
 **period_start** | **datetime**| Period start (ISO datetime) | 
 **period_end** | **datetime**| Period end (ISO datetime) | 

### Return type

[**VarianceSummaryResponse**](VarianceSummaryResponse.md)

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

