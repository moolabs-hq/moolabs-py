# moolabs.AlertsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_threshold_endpoint**](AlertsApi.md#create_threshold_endpoint) | **POST** /v1/alerts/thresholds | Create Threshold Endpoint
[**delete_threshold_endpoint**](AlertsApi.md#delete_threshold_endpoint) | **DELETE** /v1/alerts/thresholds/{threshold_id} | Delete Threshold Endpoint
[**get_alerts_state_endpoint**](AlertsApi.md#get_alerts_state_endpoint) | **GET** /v1/alerts/state | Get Alerts State Endpoint
[**list_thresholds_endpoint**](AlertsApi.md#list_thresholds_endpoint) | **GET** /v1/alerts/thresholds | List Thresholds Endpoint
[**update_threshold_endpoint**](AlertsApi.md#update_threshold_endpoint) | **PUT** /v1/alerts/thresholds/{threshold_id} | Update Threshold Endpoint


# **create_threshold_endpoint**
> object create_threshold_endpoint(wallet_id, tenant_id, pool_id, create_threshold_request)

Create Threshold Endpoint

Create a wallet threshold.  Thresholds trigger alerts when wallet state crosses the threshold. - PERCENT: 0-100, triggers when spent_percent >= threshold - ABSOLUTE: micros, triggers when effective_available_micros <= threshold

### Example


```python
import moolabs
from moolabs.models.create_threshold_request import CreateThresholdRequest
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
    api_instance = moolabs.AlertsApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    create_threshold_request = moolabs.CreateThresholdRequest() # CreateThresholdRequest | 

    try:
        # Create Threshold Endpoint
        api_response = api_instance.create_threshold_endpoint(wallet_id, tenant_id, pool_id, create_threshold_request)
        print("The response of AlertsApi->create_threshold_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_threshold_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **create_threshold_request** | [**CreateThresholdRequest**](CreateThresholdRequest.md)|  | 

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

# **delete_threshold_endpoint**
> object delete_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id)

Delete Threshold Endpoint

Delete a wallet threshold.

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
    api_instance = moolabs.AlertsApi(api_client)
    threshold_id = 'threshold_id_example' # str | 
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier

    try:
        # Delete Threshold Endpoint
        api_response = api_instance.delete_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id)
        print("The response of AlertsApi->delete_threshold_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->delete_threshold_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threshold_id** | **str**|  | 
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 

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

# **get_alerts_state_endpoint**
> object get_alerts_state_endpoint(wallet_id, tenant_id, pool_id)

Get Alerts State Endpoint

Get alert state for a wallet.  Returns the current state of all alerts (ACTIVE/CLEARED) for the wallet.

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
    api_instance = moolabs.AlertsApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier

    try:
        # Get Alerts State Endpoint
        api_response = api_instance.get_alerts_state_endpoint(wallet_id, tenant_id, pool_id)
        print("The response of AlertsApi->get_alerts_state_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alerts_state_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 

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

# **list_thresholds_endpoint**
> object list_thresholds_endpoint(wallet_id, tenant_id, pool_id)

List Thresholds Endpoint

List all thresholds for a wallet.

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
    api_instance = moolabs.AlertsApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier

    try:
        # List Thresholds Endpoint
        api_response = api_instance.list_thresholds_endpoint(wallet_id, tenant_id, pool_id)
        print("The response of AlertsApi->list_thresholds_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_thresholds_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 

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

# **update_threshold_endpoint**
> object update_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id, update_threshold_request)

Update Threshold Endpoint

Update a wallet threshold.

### Example


```python
import moolabs
from moolabs.models.update_threshold_request import UpdateThresholdRequest
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
    api_instance = moolabs.AlertsApi(api_client)
    threshold_id = 'threshold_id_example' # str | 
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    update_threshold_request = moolabs.UpdateThresholdRequest() # UpdateThresholdRequest | 

    try:
        # Update Threshold Endpoint
        api_response = api_instance.update_threshold_endpoint(threshold_id, wallet_id, tenant_id, pool_id, update_threshold_request)
        print("The response of AlertsApi->update_threshold_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->update_threshold_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threshold_id** | **str**|  | 
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **update_threshold_request** | [**UpdateThresholdRequest**](UpdateThresholdRequest.md)|  | 

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

