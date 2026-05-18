# moolabs.PortalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_endpoint**](PortalApi.md#create_token_endpoint) | **POST** /v1/portal/tokens | Create Token Endpoint
[**get_portal_context**](PortalApi.md#get_portal_context) | **GET** /v1/portal/context | Get Portal Context
[**invalidate_tokens_endpoint**](PortalApi.md#invalidate_tokens_endpoint) | **POST** /v1/portal/tokens/invalidate | Invalidate Tokens Endpoint
[**list_tokens_endpoint**](PortalApi.md#list_tokens_endpoint) | **GET** /v1/portal/tokens | List Tokens Endpoint


# **create_token_endpoint**
> object create_token_endpoint(app_api_v1_portal_router_create_portal_token_request)

Create Token Endpoint

Create a portal token for a subject.  The token is scoped to the subject's tenant and pool (resolved server-side). Plaintext is returned only once — only the SHA-256 hash is stored. tenant_id is resolved from the authenticated API key (per-tenant key → billing.api_keys; global key → TENANT_ID config). Never a query param.

### Example


```python
import moolabs
from moolabs.models.app_api_v1_portal_router_create_portal_token_request import AppApiV1PortalRouterCreatePortalTokenRequest
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
    api_instance = moolabs.PortalApi(api_client)
    app_api_v1_portal_router_create_portal_token_request = moolabs.AppApiV1PortalRouterCreatePortalTokenRequest() # AppApiV1PortalRouterCreatePortalTokenRequest | 

    try:
        # Create Token Endpoint
        api_response = api_instance.create_token_endpoint(app_api_v1_portal_router_create_portal_token_request)
        print("The response of PortalApi->create_token_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalApi->create_token_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_api_v1_portal_router_create_portal_token_request** | [**AppApiV1PortalRouterCreatePortalTokenRequest**](AppApiV1PortalRouterCreatePortalTokenRequest.md)|  | 

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

# **get_portal_context**
> object get_portal_context()

Get Portal Context

Return resolved tenant/pool/subject for the authenticated portal token.  Called by MoolabsProvider on mount to resolve CLS queryParams (tenant_id, pool_id) without exposing them in browser code.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.PortalApi(api_client)

    try:
        # Get Portal Context
        api_response = api_instance.get_portal_context()
        print("The response of PortalApi->get_portal_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalApi->get_portal_context: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_tokens_endpoint**
> object invalidate_tokens_endpoint(invalidate_portal_token_request)

Invalidate Tokens Endpoint

Invalidate portal token(s) by token value or subject.  At least one of token or subject must be provided. Revocation is soft — sets revoked_at, never deletes.

### Example


```python
import moolabs
from moolabs.models.invalidate_portal_token_request import InvalidatePortalTokenRequest
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
    api_instance = moolabs.PortalApi(api_client)
    invalidate_portal_token_request = moolabs.InvalidatePortalTokenRequest() # InvalidatePortalTokenRequest | 

    try:
        # Invalidate Tokens Endpoint
        api_response = api_instance.invalidate_tokens_endpoint(invalidate_portal_token_request)
        print("The response of PortalApi->invalidate_tokens_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalApi->invalidate_tokens_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invalidate_portal_token_request** | [**InvalidatePortalTokenRequest**](InvalidatePortalTokenRequest.md)|  | 

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

# **list_tokens_endpoint**
> object list_tokens_endpoint(subject=subject)

List Tokens Endpoint

List active portal tokens for tenant (optionally filtered by subject).

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
    api_instance = moolabs.PortalApi(api_client)
    subject = 'subject_example' # str | Filter by subject (optional)

    try:
        # List Tokens Endpoint
        api_response = api_instance.list_tokens_endpoint(subject=subject)
        print("The response of PortalApi->list_tokens_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalApi->list_tokens_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Filter by subject | [optional] 

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

