# moolabs.MoometerProxyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proxy_openmeter**](MoometerProxyApi.md#proxy_openmeter) | **GET** /v1/moometer/{path} | Proxy Openmeter
[**proxy_openmeter_0**](MoometerProxyApi.md#proxy_openmeter_0) | **PUT** /v1/moometer/{path} | Proxy Openmeter
[**proxy_openmeter_1**](MoometerProxyApi.md#proxy_openmeter_1) | **POST** /v1/moometer/{path} | Proxy Openmeter
[**proxy_openmeter_2**](MoometerProxyApi.md#proxy_openmeter_2) | **DELETE** /v1/moometer/{path} | Proxy Openmeter
[**proxy_openmeter_3**](MoometerProxyApi.md#proxy_openmeter_3) | **PATCH** /v1/moometer/{path} | Proxy Openmeter


# **proxy_openmeter**
> object proxy_openmeter(path)

Proxy Openmeter

Generic pass-through proxy to Moo-meter with per-tenant OM-Namespace.

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
    api_instance = moolabs.MoometerProxyApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy Openmeter
        api_response = api_instance.proxy_openmeter(path)
        print("The response of MoometerProxyApi->proxy_openmeter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoometerProxyApi->proxy_openmeter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

# **proxy_openmeter_0**
> object proxy_openmeter_0(path)

Proxy Openmeter

Generic pass-through proxy to Moo-meter with per-tenant OM-Namespace.

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
    api_instance = moolabs.MoometerProxyApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy Openmeter
        api_response = api_instance.proxy_openmeter_0(path)
        print("The response of MoometerProxyApi->proxy_openmeter_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoometerProxyApi->proxy_openmeter_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

# **proxy_openmeter_1**
> object proxy_openmeter_1(path)

Proxy Openmeter

Generic pass-through proxy to Moo-meter with per-tenant OM-Namespace.

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
    api_instance = moolabs.MoometerProxyApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy Openmeter
        api_response = api_instance.proxy_openmeter_1(path)
        print("The response of MoometerProxyApi->proxy_openmeter_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoometerProxyApi->proxy_openmeter_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

# **proxy_openmeter_2**
> object proxy_openmeter_2(path)

Proxy Openmeter

Generic pass-through proxy to Moo-meter with per-tenant OM-Namespace.

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
    api_instance = moolabs.MoometerProxyApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy Openmeter
        api_response = api_instance.proxy_openmeter_2(path)
        print("The response of MoometerProxyApi->proxy_openmeter_2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoometerProxyApi->proxy_openmeter_2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

# **proxy_openmeter_3**
> object proxy_openmeter_3(path)

Proxy Openmeter

Generic pass-through proxy to Moo-meter with per-tenant OM-Namespace.

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
    api_instance = moolabs.MoometerProxyApi(api_client)
    path = 'path_example' # str | 

    try:
        # Proxy Openmeter
        api_response = api_instance.proxy_openmeter_3(path)
        print("The response of MoometerProxyApi->proxy_openmeter_3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoometerProxyApi->proxy_openmeter_3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

