# moolabs.AcuteAnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cost_by_customer_api**](AcuteAnalyticsApi.md#cost_by_customer_api) | **GET** /api/v1/cost/analytics/by-customer | Cost By Customer
[**cost_by_feature_api**](AcuteAnalyticsApi.md#cost_by_feature_api) | **GET** /api/v1/cost/analytics/by-feature | Cost By Feature
[**cost_by_model_api**](AcuteAnalyticsApi.md#cost_by_model_api) | **GET** /api/v1/cost/analytics/by-model | Cost By Model
[**cost_by_plan_api**](AcuteAnalyticsApi.md#cost_by_plan_api) | **GET** /api/v1/cost/analytics/by-plan | Cost By Plan
[**cost_trends**](AcuteAnalyticsApi.md#cost_trends) | **GET** /api/v1/cost/analytics/trends | Cost Trends
[**ingest_health**](AcuteAnalyticsApi.md#ingest_health) | **GET** /api/v1/cost/analytics/ingest/health | Ingest Health
[**overview**](AcuteAnalyticsApi.md#overview) | **GET** /api/v1/cost/analytics/overview | Overview
[**top_consumers_api**](AcuteAnalyticsApi.md#top_consumers_api) | **GET** /api/v1/cost/analytics/top-consumers | Top Consumers
[**unit_economics_api**](AcuteAnalyticsApi.md#unit_economics_api) | **GET** /api/v1/cost/analytics/unit-economics | Unit Economics


# **cost_by_customer_api**
> List[CustomerCostItem] cost_by_customer_api(start_date=start_date, end_date=end_date, limit=limit, x_tenant_id=x_tenant_id)

Cost By Customer

Cost breakdown by customer for the given date range.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.customer_cost_item import CustomerCostItem
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Cost By Customer
        api_response = api_instance.cost_by_customer_api(start_date=start_date, end_date=end_date, limit=limit, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->cost_by_customer_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->cost_by_customer_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[CustomerCostItem]**](CustomerCostItem.md)

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

# **cost_by_feature_api**
> List[FeatureCostItem] cost_by_feature_api(start_date=start_date, end_date=end_date, limit=limit, x_tenant_id=x_tenant_id)

Cost By Feature

Cost breakdown by feature key for the given date range.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.feature_cost_item import FeatureCostItem
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Cost By Feature
        api_response = api_instance.cost_by_feature_api(start_date=start_date, end_date=end_date, limit=limit, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->cost_by_feature_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->cost_by_feature_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[FeatureCostItem]**](FeatureCostItem.md)

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

# **cost_by_model_api**
> List[ModelCostItem] cost_by_model_api(start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)

Cost By Model

Cost breakdown by model and provider.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.model_cost_item import ModelCostItem
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Cost By Model
        api_response = api_instance.cost_by_model_api(start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->cost_by_model_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->cost_by_model_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[ModelCostItem]**](ModelCostItem.md)

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

# **cost_by_plan_api**
> List[Dict[str, object]] cost_by_plan_api(start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)

Cost By Plan

Cost breakdown by billing plan.  Stub — plan join requires CLS rate-plan data (Phase 2). Returns empty list with a note until Phase 2 is implemented.

### Example

* Api Key Authentication (APIKeyHeader):

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

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Cost By Plan
        api_response = api_instance.cost_by_plan_api(start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->cost_by_plan_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->cost_by_plan_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

**List[Dict[str, object]]**

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

# **cost_trends**
> List[TrendDataPoint] cost_trends(start_date=start_date, end_date=end_date, period=period, x_tenant_id=x_tenant_id)

Cost Trends

Time-series cost trends bucketed by day, week, or month.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.trend_data_point import TrendDataPoint
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    period = 'day' # str |  (optional) (default to 'day')
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Cost Trends
        api_response = api_instance.cost_trends(start_date=start_date, end_date=end_date, period=period, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->cost_trends:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->cost_trends: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **period** | **str**|  | [optional] [default to &#39;day&#39;]
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[TrendDataPoint]**](TrendDataPoint.md)

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

# **ingest_health**
> IngestHealth ingest_health(x_tenant_id=x_tenant_id)

Ingest Health

Ingestion pipeline health for a tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.ingest_health import IngestHealth
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Ingest Health
        api_response = api_instance.ingest_health(x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->ingest_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->ingest_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**IngestHealth**](IngestHealth.md)

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

# **overview**
> OverviewResponse overview(start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)

Overview

Aggregate overview powering the Phase 1A-ii OverviewPage UI.  Sums total cost + request count across the period, derives a basic reconciliation indicator, and embeds the live ingest health snapshot so the dashboard can render four KPIs from a single round-trip.  Returns zeros + null reconciliation on a fresh tenant rather than 404, so the UI's `AcuteQueryStatus` sees a successful response and the KPI cards render with placeholders instead of \"ACUTE overview is unavailable.\".

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.overview_response import OverviewResponse
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Overview
        api_response = api_instance.overview(start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**OverviewResponse**](OverviewResponse.md)

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

# **top_consumers_api**
> List[TopConsumer] top_consumers_api(start_date=start_date, end_date=end_date, top_n=top_n, x_tenant_id=x_tenant_id)

Top Consumers

Top N customers by total cost in the date range.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.top_consumer import TopConsumer
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    top_n = 10 # int |  (optional) (default to 10)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Top Consumers
        api_response = api_instance.top_consumers_api(start_date=start_date, end_date=end_date, top_n=top_n, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->top_consumers_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->top_consumers_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **top_n** | **int**|  | [optional] [default to 10]
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**List[TopConsumer]**](TopConsumer.md)

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

# **unit_economics_api**
> UnitEconomics unit_economics_api(feature_key, start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)

Unit Economics

Cost-per-request distribution (mean, p50, p95, p99) for a feature.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.unit_economics import UnitEconomics
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
    api_instance = moolabs.AcuteAnalyticsApi(api_client)
    feature_key = 'feature_key_example' # str | Feature key to analyse
    start_date = '2013-10-20' # date |  (optional)
    end_date = '2013-10-20' # date |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)

    try:
        # Unit Economics
        api_response = api_instance.unit_economics_api(feature_key, start_date=start_date, end_date=end_date, x_tenant_id=x_tenant_id)
        print("The response of AcuteAnalyticsApi->unit_economics_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AcuteAnalyticsApi->unit_economics_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_key** | **str**| Feature key to analyse | 
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 

### Return type

[**UnitEconomics**](UnitEconomics.md)

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

