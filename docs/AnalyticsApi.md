# moolabs.AnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_action_audit_v1**](AnalyticsApi.md#agent_action_audit_v1) | **GET** /v1/arc/analytics/agent-actions | Agent Action Audit
[**agent_performance_v1**](AnalyticsApi.md#agent_performance_v1) | **GET** /v1/arc/analytics/agent-performance | Agent Performance
[**aging_report**](AnalyticsApi.md#aging_report) | **GET** /v1/arc/analytics/aging | Aging Report
[**aging_trend**](AnalyticsApi.md#aging_trend) | **GET** /v1/arc/analytics/aging/trend | Aging Trend
[**cei_report**](AnalyticsApi.md#cei_report) | **GET** /v1/arc/analytics/cei | Cei Report
[**create_aging_snapshot**](AnalyticsApi.md#create_aging_snapshot) | **POST** /v1/arc/analytics/aging/snapshot | Create Aging Snapshot
[**dashboard_overview**](AnalyticsApi.md#dashboard_overview) | **GET** /v1/arc/analytics/overview | Dashboard Overview
[**dispute_summary_v1**](AnalyticsApi.md#dispute_summary_v1) | **GET** /v1/arc/analytics/dispute-summary | Dispute Summary
[**dso_report**](AnalyticsApi.md#dso_report) | **GET** /v1/arc/analytics/dso | Dso Report
[**ptp_summary_v1**](AnalyticsApi.md#ptp_summary_v1) | **GET** /v1/arc/analytics/ptp-summary | Ptp Summary


# **agent_action_audit_v1**
> object agent_action_audit_v1(x_api_key, agent_type=agent_type, case_id=case_id, limit=limit, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Agent Action Audit

GET /analytics/agent-actions — Individual agent action audit rows.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    agent_type = 'agent_type_example' # str |  (optional)
    case_id = 'case_id_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Agent Action Audit
        api_response = api_instance.agent_action_audit_v1(x_api_key, agent_type=agent_type, case_id=case_id, limit=limit, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->agent_action_audit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->agent_action_audit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **agent_type** | **str**|  | [optional] 
 **case_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
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

# **agent_performance_v1**
> object agent_performance_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Agent Performance

GET /analytics/agent-performance — Agent performance metrics.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Agent Performance
        api_response = api_instance.agent_performance_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->agent_performance_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->agent_performance_v1: %s\n" % e)
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

# **aging_report**
> object aging_report(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Aging Report

GET /analytics/aging — Aging bucket distribution of outstanding AR.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Aging Report
        api_response = api_instance.aging_report(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->aging_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->aging_report: %s\n" % e)
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

# **aging_trend**
> object aging_trend(x_api_key, days=days, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Aging Trend

GET /analytics/aging/trend — Historical aging trend (last N days).

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    days = 30 # int |  (optional) (default to 30)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Aging Trend
        api_response = api_instance.aging_trend(x_api_key, days=days, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->aging_trend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->aging_trend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **days** | **int**|  | [optional] [default to 30]
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

# **cei_report**
> object cei_report(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Cei Report

GET /analytics/cei — Collection Effectiveness Index.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Cei Report
        api_response = api_instance.cei_report(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->cei_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->cei_report: %s\n" % e)
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

# **create_aging_snapshot**
> object create_aging_snapshot(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Create Aging Snapshot

POST /analytics/aging/snapshot — Manually capture an aging snapshot.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Create Aging Snapshot
        api_response = api_instance.create_aging_snapshot(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->create_aging_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->create_aging_snapshot: %s\n" % e)
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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dashboard_overview**
> DashboardOverviewResponse dashboard_overview(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Dashboard Overview

GET /analytics/overview — Combined dashboard analytics payload.

### Example


```python
import moolabs
from moolabs.models.dashboard_overview_response import DashboardOverviewResponse
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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Dashboard Overview
        api_response = api_instance.dashboard_overview(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->dashboard_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->dashboard_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**DashboardOverviewResponse**](DashboardOverviewResponse.md)

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

# **dispute_summary_v1**
> object dispute_summary_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Dispute Summary

GET /analytics/dispute-summary — Dispute statistics.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Dispute Summary
        api_response = api_instance.dispute_summary_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->dispute_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->dispute_summary_v1: %s\n" % e)
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

# **dso_report**
> object dso_report(x_api_key, period_days=period_days, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Dso Report

GET /analytics/dso — Days Sales Outstanding calculation.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    period_days = 90 # int |  (optional) (default to 90)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Dso Report
        api_response = api_instance.dso_report(x_api_key, period_days=period_days, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->dso_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->dso_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **period_days** | **int**|  | [optional] [default to 90]
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

# **ptp_summary_v1**
> object ptp_summary_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Ptp Summary

GET /analytics/ptp-summary — Promise-to-Pay statistics.

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
    api_instance = moolabs.AnalyticsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Ptp Summary
        api_response = api_instance.ptp_summary_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of AnalyticsApi->ptp_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->ptp_summary_v1: %s\n" % e)
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

