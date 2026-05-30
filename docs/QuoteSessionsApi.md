# moolabs.QuoteSessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_quote_session_v1**](QuoteSessionsApi.md#patch_quote_session_v1) | **PATCH** /v1/quote-sessions/{session_id} | Patch Quote Session
[**post_quote_session_price_v1**](QuoteSessionsApi.md#post_quote_session_price_v1) | **POST** /v1/quote-sessions/{session_id}/price | Post Quote Session Price
[**post_quote_session_shadow_price_v1_quote**](QuoteSessionsApi.md#post_quote_session_shadow_price_v1_quote) | **POST** /v1/quote-sessions/{session_id}/shadow-price | Post Quote Session Shadow Price


# **patch_quote_session_v1**
> CreateSessionResponse patch_quote_session_v1(session_id, patch_session_request, idempotency_key=idempotency_key)

Patch Quote Session

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_session_response import CreateSessionResponse
from moolabs.models.patch_session_request import PatchSessionRequest
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
    api_instance = moolabs.QuoteSessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    patch_session_request = moolabs.PatchSessionRequest() # PatchSessionRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Patch Quote Session
        api_response = api_instance.patch_quote_session_v1(session_id, patch_session_request, idempotency_key=idempotency_key)
        print("The response of QuoteSessionsApi->patch_quote_session_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteSessionsApi->patch_quote_session_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **patch_session_request** | [**PatchSessionRequest**](PatchSessionRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

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

# **post_quote_session_price_v1**
> PriceSessionResponse post_quote_session_price_v1(session_id, idempotency_key=idempotency_key)

Post Quote Session Price

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.price_session_response import PriceSessionResponse
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
    api_instance = moolabs.QuoteSessionsApi(api_client)
    session_id = 'session_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Session Price
        api_response = api_instance.post_quote_session_price_v1(session_id, idempotency_key=idempotency_key)
        print("The response of QuoteSessionsApi->post_quote_session_price_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteSessionsApi->post_quote_session_price_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**PriceSessionResponse**](PriceSessionResponse.md)

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

# **post_quote_session_shadow_price_v1_quote**
> object post_quote_session_shadow_price_v1_quote(session_id)

Post Quote Session Shadow Price

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
    api_instance = moolabs.QuoteSessionsApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Post Quote Session Shadow Price
        api_response = api_instance.post_quote_session_shadow_price_v1_quote(session_id)
        print("The response of QuoteSessionsApi->post_quote_session_shadow_price_v1_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteSessionsApi->post_quote_session_shadow_price_v1_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

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

