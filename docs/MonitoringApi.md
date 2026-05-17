# moolabs.MonitoringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alerts**](MonitoringApi.md#get_alerts) | **GET** /v1/monitoring/alerts | Get Alerts
[**get_metrics**](MonitoringApi.md#get_metrics) | **GET** /v1/monitoring/metrics | Get Metrics


# **get_alerts**
> object get_alerts()

Get Alerts

Get active alerts.

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
    api_instance = moolabs.MonitoringApi(api_client)

    try:
        # Get Alerts
        api_response = api_instance.get_alerts()
        print("The response of MonitoringApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->get_alerts: %s\n" % e)
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

# **get_metrics**
> str get_metrics()

Get Metrics

Prometheus metrics endpoint.

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
    api_instance = moolabs.MonitoringApi(api_client)

    try:
        # Get Metrics
        api_response = api_instance.get_metrics()
        print("The response of MonitoringApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitoringApi->get_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

