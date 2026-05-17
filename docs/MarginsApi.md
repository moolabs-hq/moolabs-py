# moolabs.MarginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_completeness**](MarginsApi.md#get_completeness) | **GET** /api/v1/cost/margins/completeness | Financial completeness metric
[**get_credit_cost_ratio_api_v1**](MarginsApi.md#get_credit_cost_ratio_api_v1) | **GET** /api/v1/cost/margins/credit-cost-ratio | Daily valued_burn / total_cost ratio time series
[**get_margin_by_customer_api**](MarginsApi.md#get_margin_by_customer_api) | **GET** /api/v1/cost/margins/by-customer | Margin per customer
[**get_margin_by_feature_api**](MarginsApi.md#get_margin_by_feature_api) | **GET** /api/v1/cost/margins/by-feature | Margin per feature
[**get_margin_snapshot**](MarginsApi.md#get_margin_snapshot) | **GET** /api/v1/cost/margins/snapshot | Period margin snapshot with reconciliation breakdown
[**trigger_reconciliation**](MarginsApi.md#trigger_reconciliation) | **POST** /api/v1/cost/margins/reconcile | Trigger manual reconciliation (operator)
[**trigger_snapshot_compute**](MarginsApi.md#trigger_snapshot_compute) | **POST** /api/v1/cost/margins/snapshot/compute | Trigger snapshot computation (operator)


# **get_completeness**
> CompletenessResponse get_completeness(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)

Financial completeness metric

Financial completeness = count(usage_events with status=fully_reconciled)                         / count(all AI usage_events in usage_event_log)

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.completeness_response import CompletenessResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    match_grade = 'financial_only' # str | 'financial_only' or 'include_operational' (optional) (default to 'financial_only')
    include_partial = False # bool | Include partially_reconciled billing events (optional) (default to False)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime start (inclusive) (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime end (exclusive) (optional)

    try:
        # Financial completeness metric
        api_response = api_instance.get_completeness(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)
        print("The response of MarginsApi->get_completeness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->get_completeness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_grade** | **str**| &#39;financial_only&#39; or &#39;include_operational&#39; | [optional] [default to &#39;financial_only&#39;]
 **include_partial** | **bool**| Include partially_reconciled billing events | [optional] [default to False]
 **period_start** | **datetime**| ISO datetime start (inclusive) | [optional] 
 **period_end** | **datetime**| ISO datetime end (exclusive) | [optional] 

### Return type

[**CompletenessResponse**](CompletenessResponse.md)

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

# **get_credit_cost_ratio_api_v1**
> CreditCostRatioResponse get_credit_cost_ratio_api_v1(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)

Daily valued_burn / total_cost ratio time series

Daily time series of valued_burn / total_cost ratio. Uses fully_reconciled events only.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.credit_cost_ratio_response import CreditCostRatioResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    match_grade = 'financial_only' # str | 'financial_only' or 'include_operational' (optional) (default to 'financial_only')
    include_partial = False # bool | Include partially_reconciled billing events (optional) (default to False)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime start (inclusive) (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime end (exclusive) (optional)

    try:
        # Daily valued_burn / total_cost ratio time series
        api_response = api_instance.get_credit_cost_ratio_api_v1(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)
        print("The response of MarginsApi->get_credit_cost_ratio_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->get_credit_cost_ratio_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_grade** | **str**| &#39;financial_only&#39; or &#39;include_operational&#39; | [optional] [default to &#39;financial_only&#39;]
 **include_partial** | **bool**| Include partially_reconciled billing events | [optional] [default to False]
 **period_start** | **datetime**| ISO datetime start (inclusive) | [optional] 
 **period_end** | **datetime**| ISO datetime end (exclusive) | [optional] 

### Return type

[**CreditCostRatioResponse**](CreditCostRatioResponse.md)

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

# **get_margin_by_customer_api**
> CustomerMarginResponse get_margin_by_customer_api(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)

Margin per customer

Returns margin aggregated per customer_id. Only includes fully_reconciled billing events by default (include_partial=false). Zero-valued-burn: margin_pct=null, margin_reason='zero_valued_burn'.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.customer_margin_response import CustomerMarginResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    match_grade = 'financial_only' # str | 'financial_only' or 'include_operational' (optional) (default to 'financial_only')
    include_partial = False # bool | Include partially_reconciled billing events (optional) (default to False)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime start (inclusive) (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime end (exclusive) (optional)

    try:
        # Margin per customer
        api_response = api_instance.get_margin_by_customer_api(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)
        print("The response of MarginsApi->get_margin_by_customer_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->get_margin_by_customer_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_grade** | **str**| &#39;financial_only&#39; or &#39;include_operational&#39; | [optional] [default to &#39;financial_only&#39;]
 **include_partial** | **bool**| Include partially_reconciled billing events | [optional] [default to False]
 **period_start** | **datetime**| ISO datetime start (inclusive) | [optional] 
 **period_end** | **datetime**| ISO datetime end (exclusive) | [optional] 

### Return type

[**CustomerMarginResponse**](CustomerMarginResponse.md)

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

# **get_margin_by_feature_api**
> FeatureMarginResponse get_margin_by_feature_api(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)

Margin per feature

Returns margin aggregated per feature_id.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.feature_margin_response import FeatureMarginResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    match_grade = 'financial_only' # str | 'financial_only' or 'include_operational' (optional) (default to 'financial_only')
    include_partial = False # bool | Include partially_reconciled billing events (optional) (default to False)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime start (inclusive) (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime end (exclusive) (optional)

    try:
        # Margin per feature
        api_response = api_instance.get_margin_by_feature_api(match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)
        print("The response of MarginsApi->get_margin_by_feature_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->get_margin_by_feature_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_grade** | **str**| &#39;financial_only&#39; or &#39;include_operational&#39; | [optional] [default to &#39;financial_only&#39;]
 **include_partial** | **bool**| Include partially_reconciled billing events | [optional] [default to False]
 **period_start** | **datetime**| ISO datetime start (inclusive) | [optional] 
 **period_end** | **datetime**| ISO datetime end (exclusive) | [optional] 

### Return type

[**FeatureMarginResponse**](FeatureMarginResponse.md)

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

# **get_margin_snapshot**
> MarginSnapshotResponse get_margin_snapshot(period_type=period_type, match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)

Period margin snapshot with reconciliation breakdown

Returns margin snapshot for the given period. Includes per-billing-event reconciliation status breakdown. Zero-valued-burn events excluded from margin_pct but included in cost totals.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.margin_snapshot_response import MarginSnapshotResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    period_type = 'daily' # str | 'daily', 'weekly', or 'monthly' (optional) (default to 'daily')
    match_grade = 'financial_only' # str | 'financial_only' or 'include_operational' (optional) (default to 'financial_only')
    include_partial = False # bool | Include partially_reconciled billing events (optional) (default to False)
    period_start = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime start (inclusive) (optional)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | ISO datetime end (exclusive) (optional)

    try:
        # Period margin snapshot with reconciliation breakdown
        api_response = api_instance.get_margin_snapshot(period_type=period_type, match_grade=match_grade, include_partial=include_partial, period_start=period_start, period_end=period_end)
        print("The response of MarginsApi->get_margin_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->get_margin_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_type** | **str**| &#39;daily&#39;, &#39;weekly&#39;, or &#39;monthly&#39; | [optional] [default to &#39;daily&#39;]
 **match_grade** | **str**| &#39;financial_only&#39; or &#39;include_operational&#39; | [optional] [default to &#39;financial_only&#39;]
 **include_partial** | **bool**| Include partially_reconciled billing events | [optional] [default to False]
 **period_start** | **datetime**| ISO datetime start (inclusive) | [optional] 
 **period_end** | **datetime**| ISO datetime end (exclusive) | [optional] 

### Return type

[**MarginSnapshotResponse**](MarginSnapshotResponse.md)

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

# **trigger_reconciliation**
> ReconcileResponse trigger_reconciliation(reconcile_request)

Trigger manual reconciliation (operator)

Operator endpoint: trigger reconciliation for specific cost_event_ids or all pending. Returns a job_id for tracking (synchronous in this implementation; async in production). body.tenant_id must match the API-key-derived tenant for security.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.reconcile_request import ReconcileRequest
from moolabs.models.reconcile_response import ReconcileResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    reconcile_request = moolabs.ReconcileRequest() # ReconcileRequest | 

    try:
        # Trigger manual reconciliation (operator)
        api_response = api_instance.trigger_reconciliation(reconcile_request)
        print("The response of MarginsApi->trigger_reconciliation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->trigger_reconciliation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reconcile_request** | [**ReconcileRequest**](ReconcileRequest.md)|  | 

### Return type

[**ReconcileResponse**](ReconcileResponse.md)

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

# **trigger_snapshot_compute**
> SnapshotComputeResponse trigger_snapshot_compute(snapshot_compute_request)

Trigger snapshot computation (operator)

Operator endpoint: compute and upsert a margin_snapshot for the given period. body.tenant_id must match the API-key-derived tenant for security.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.snapshot_compute_request import SnapshotComputeRequest
from moolabs.models.snapshot_compute_response import SnapshotComputeResponse
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
    api_instance = moolabs.MarginsApi(api_client)
    snapshot_compute_request = moolabs.SnapshotComputeRequest() # SnapshotComputeRequest | 

    try:
        # Trigger snapshot computation (operator)
        api_response = api_instance.trigger_snapshot_compute(snapshot_compute_request)
        print("The response of MarginsApi->trigger_snapshot_compute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarginsApi->trigger_snapshot_compute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_compute_request** | [**SnapshotComputeRequest**](SnapshotComputeRequest.md)|  | 

### Return type

[**SnapshotComputeResponse**](SnapshotComputeResponse.md)

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

