# moolabs.PoolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pool**](PoolsApi.md#get_pool) | **GET** /v1/pools/{pool_id} | Get Pool
[**get_pool_impact_summary_v1**](PoolsApi.md#get_pool_impact_summary_v1) | **GET** /v1/pools/{pool_id}/impact-summary | Get Pool Impact Summary
[**get_pool_notification_config_v1**](PoolsApi.md#get_pool_notification_config_v1) | **GET** /v1/pools/{pool_id}/notification-config | Get Pool Notification Config
[**get_pool_topup_defaults_v1**](PoolsApi.md#get_pool_topup_defaults_v1) | **GET** /v1/pools/{pool_id}/topup-defaults | Get Pool Topup Defaults
[**list_pools**](PoolsApi.md#list_pools) | **GET** /v1/pools | List Pools
[**update_pool**](PoolsApi.md#update_pool) | **PUT** /v1/pools/{pool_id} | Update Pool
[**update_pool_notification_config_v1**](PoolsApi.md#update_pool_notification_config_v1) | **PUT** /v1/pools/{pool_id}/notification-config | Update Pool Notification Config
[**update_pool_topup_defaults_v1**](PoolsApi.md#update_pool_topup_defaults_v1) | **PUT** /v1/pools/{pool_id}/topup-defaults | Update Pool Topup Defaults


# **get_pool**
> object get_pool(pool_id, tenant_id)

Get Pool

Get a single credit pool. Auth tenant must match tenant_id.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Get Pool
        api_response = api_instance.get_pool(pool_id, tenant_id)
        print("The response of PoolsApi->get_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->get_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_impact_summary_v1**
> object get_pool_impact_summary_v1(pool_id, tenant_id)

Get Pool Impact Summary

Aggregate impact statistics for a pool: wallet counts, last rate change, last policy update.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Get Pool Impact Summary
        api_response = api_instance.get_pool_impact_summary_v1(pool_id, tenant_id)
        print("The response of PoolsApi->get_pool_impact_summary_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->get_pool_impact_summary_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_notification_config_v1**
> object get_pool_notification_config_v1(pool_id, tenant_id)

Get Pool Notification Config

Get notification email recipients for a global credit pool.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Get Pool Notification Config
        api_response = api_instance.get_pool_notification_config_v1(pool_id, tenant_id)
        print("The response of PoolsApi->get_pool_notification_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->get_pool_notification_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pool_topup_defaults_v1**
> object get_pool_topup_defaults_v1(pool_id, tenant_id)

Get Pool Topup Defaults

Get pool-level top-up defaults (applied when new wallets are created).

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # Get Pool Topup Defaults
        api_response = api_instance.get_pool_topup_defaults_v1(pool_id, tenant_id)
        print("The response of PoolsApi->get_pool_topup_defaults_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->get_pool_topup_defaults_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pools**
> object list_pools(tenant_id)

List Pools

List credit pools for a tenant. Auth tenant must match tenant_id.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier

    try:
        # List Pools
        api_response = api_instance.list_pools(tenant_id)
        print("The response of PoolsApi->list_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->list_pools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pool**
> object update_pool(pool_id, tenant_id, update_credit_pool_request)

Update Pool

Update pool settings (name, currency, notification_emails). Only provided fields are updated.

### Example

* Bearer Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.update_credit_pool_request import UpdateCreditPoolRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    update_credit_pool_request = moolabs.UpdateCreditPoolRequest() # UpdateCreditPoolRequest | 

    try:
        # Update Pool
        api_response = api_instance.update_pool(pool_id, tenant_id, update_credit_pool_request)
        print("The response of PoolsApi->update_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->update_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 
 **update_credit_pool_request** | [**UpdateCreditPoolRequest**](UpdateCreditPoolRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pool_notification_config_v1**
> object update_pool_notification_config_v1(pool_id, tenant_id, pool_notification_config_request)

Update Pool Notification Config

Set notification email recipients for a global credit pool.  Replaces the full list of notification emails. Send an empty list to disable all pool-level email notifications.

### Example

* Bearer Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.pool_notification_config_request import PoolNotificationConfigRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_notification_config_request = moolabs.PoolNotificationConfigRequest() # PoolNotificationConfigRequest | 

    try:
        # Update Pool Notification Config
        api_response = api_instance.update_pool_notification_config_v1(pool_id, tenant_id, pool_notification_config_request)
        print("The response of PoolsApi->update_pool_notification_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->update_pool_notification_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_notification_config_request** | [**PoolNotificationConfigRequest**](PoolNotificationConfigRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pool_topup_defaults_v1**
> object update_pool_topup_defaults_v1(pool_id, tenant_id, topup_defaults_request)

Update Pool Topup Defaults

Update pool-level top-up defaults. Creates the row on first PUT (lazy upsert).

### Example

* Bearer Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.topup_defaults_request import TopupDefaultsRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PoolsApi(api_client)
    pool_id = 'pool_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    topup_defaults_request = moolabs.TopupDefaultsRequest() # TopupDefaultsRequest | 

    try:
        # Update Pool Topup Defaults
        api_response = api_instance.update_pool_topup_defaults_v1(pool_id, tenant_id, topup_defaults_request)
        print("The response of PoolsApi->update_pool_topup_defaults_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoolsApi->update_pool_topup_defaults_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**|  | 
 **tenant_id** | **str**| Tenant identifier | 
 **topup_defaults_request** | [**TopupDefaultsRequest**](TopupDefaultsRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

