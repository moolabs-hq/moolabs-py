# moolabs.PerformanceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explain_query**](PerformanceApi.md#explain_query) | **POST** /v1/performance/queries/explain | Explain Query
[**get_connection_pool_info_v1**](PerformanceApi.md#get_connection_pool_info_v1) | **GET** /v1/performance/connection-pool | Get Connection Pool Info
[**get_index_usage**](PerformanceApi.md#get_index_usage) | **GET** /v1/performance/indexes/usage | Get Index Usage
[**get_missing_index_recommendations**](PerformanceApi.md#get_missing_index_recommendations) | **GET** /v1/performance/indexes/missing | Get Missing Index Recommendations
[**get_performance_report_endpoint**](PerformanceApi.md#get_performance_report_endpoint) | **GET** /v1/performance/report | Get Performance Report Endpoint
[**get_slow_queries**](PerformanceApi.md#get_slow_queries) | **GET** /v1/performance/queries/slow | Get Slow Queries
[**get_table_size_analysis**](PerformanceApi.md#get_table_size_analysis) | **GET** /v1/performance/tables/sizes | Get Table Size Analysis
[**warm_rate_card_cache_v1**](PerformanceApi.md#warm_rate_card_cache_v1) | **POST** /v1/performance/cache/warm/rate-cards | Warm Rate Card Cache
[**warm_wallet_cache**](PerformanceApi.md#warm_wallet_cache) | **POST** /v1/performance/cache/warm/wallets | Warm Wallet Cache


# **explain_query**
> object explain_query(query_sql)

Explain Query

Explain query execution plan.  Uses PostgreSQL EXPLAIN to analyze query performance.

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
    api_instance = moolabs.PerformanceApi(api_client)
    query_sql = 'query_sql_example' # str | 

    try:
        # Explain Query
        api_response = api_instance.explain_query(query_sql)
        print("The response of PerformanceApi->explain_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->explain_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_sql** | **str**|  | 

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

# **get_connection_pool_info_v1**
> object get_connection_pool_info_v1()

Get Connection Pool Info

Get connection pool statistics.

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
    api_instance = moolabs.PerformanceApi(api_client)

    try:
        # Get Connection Pool Info
        api_response = api_instance.get_connection_pool_info_v1()
        print("The response of PerformanceApi->get_connection_pool_info_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->get_connection_pool_info_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index_usage**
> object get_index_usage(var_schema=var_schema)

Get Index Usage

Get index usage statistics.  Analyzes which indexes are being used and which are unused.

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
    api_instance = moolabs.PerformanceApi(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Index Usage
        api_response = api_instance.get_index_usage(var_schema=var_schema)
        print("The response of PerformanceApi->get_index_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->get_index_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

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

# **get_missing_index_recommendations**
> object get_missing_index_recommendations(var_schema=var_schema)

Get Missing Index Recommendations

Identify potentially missing indexes.  Uses pg_stat_statements to identify sequential scans that might benefit from indexes.

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
    api_instance = moolabs.PerformanceApi(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Missing Index Recommendations
        api_response = api_instance.get_missing_index_recommendations(var_schema=var_schema)
        print("The response of PerformanceApi->get_missing_index_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->get_missing_index_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

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

# **get_performance_report_endpoint**
> object get_performance_report_endpoint(var_schema=var_schema)

Get Performance Report Endpoint

Generate comprehensive performance report.  Combines query analysis, index stats, connection pool stats, and table sizes.

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
    api_instance = moolabs.PerformanceApi(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Performance Report Endpoint
        api_response = api_instance.get_performance_report_endpoint(var_schema=var_schema)
        print("The response of PerformanceApi->get_performance_report_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->get_performance_report_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

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

# **get_slow_queries**
> object get_slow_queries(min_duration_ms=min_duration_ms, limit=limit)

Get Slow Queries

Analyze slow queries from PostgreSQL.  Uses pg_stat_statements to identify slow queries. Requires pg_stat_statements extension to be enabled.

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
    api_instance = moolabs.PerformanceApi(api_client)
    min_duration_ms = 100.0 # float | Minimum query duration in milliseconds (optional) (default to 100.0)
    limit = 20 # int | Maximum number of results (optional) (default to 20)

    try:
        # Get Slow Queries
        api_response = api_instance.get_slow_queries(min_duration_ms=min_duration_ms, limit=limit)
        print("The response of PerformanceApi->get_slow_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->get_slow_queries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_duration_ms** | **float**| Minimum query duration in milliseconds | [optional] [default to 100.0]
 **limit** | **int**| Maximum number of results | [optional] [default to 20]

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

# **get_table_size_analysis**
> object get_table_size_analysis(var_schema=var_schema)

Get Table Size Analysis

Analyze table sizes for partitioning consideration.  Identifies large tables that might benefit from partitioning.

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
    api_instance = moolabs.PerformanceApi(api_client)
    var_schema = 'billing' # str | Schema name (optional) (default to 'billing')

    try:
        # Get Table Size Analysis
        api_response = api_instance.get_table_size_analysis(var_schema=var_schema)
        print("The response of PerformanceApi->get_table_size_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->get_table_size_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_schema** | **str**| Schema name | [optional] [default to &#39;billing&#39;]

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

# **warm_rate_card_cache_v1**
> object warm_rate_card_cache_v1(tenant_id=tenant_id, limit=limit)

Warm Rate Card Cache

Warm Dragonfly cache with active rate cards.  Pre-loads rate card data for frequently used features.

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
    api_instance = moolabs.PerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    limit = 50 # int | Maximum number of rate cards to warm (optional) (default to 50)

    try:
        # Warm Rate Card Cache
        api_response = api_instance.warm_rate_card_cache_v1(tenant_id=tenant_id, limit=limit)
        print("The response of PerformanceApi->warm_rate_card_cache_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->warm_rate_card_cache_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter | [optional] 
 **limit** | **int**| Maximum number of rate cards to warm | [optional] [default to 50]

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

# **warm_wallet_cache**
> object warm_wallet_cache(tenant_id=tenant_id, pool_id=pool_id, limit=limit)

Warm Wallet Cache

Warm Dragonfly cache with hot wallet projections.  Pre-loads wallet balance projections for frequently accessed wallets.

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
    api_instance = moolabs.PerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Optional tenant filter (optional)
    pool_id = 'pool_id_example' # str | Optional pool filter (optional)
    limit = 100 # int | Maximum number of wallets to warm (optional) (default to 100)

    try:
        # Warm Wallet Cache
        api_response = api_instance.warm_wallet_cache(tenant_id=tenant_id, pool_id=pool_id, limit=limit)
        print("The response of PerformanceApi->warm_wallet_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PerformanceApi->warm_wallet_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Optional tenant filter | [optional] 
 **pool_id** | **str**| Optional pool filter | [optional] 
 **limit** | **int**| Maximum number of wallets to warm | [optional] [default to 100]

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

