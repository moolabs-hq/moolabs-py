# moolabs.QuotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quote**](QuotesApi.md#get_quote) | **GET** /v1/quotes/{quote_id} | Get Quote
[**get_quote_version**](QuotesApi.md#get_quote_version) | **GET** /v1/quotes/{quote_id}/versions/{version} | Get Quote Version
[**list_quote_activation_failures_v1**](QuotesApi.md#list_quote_activation_failures_v1) | **GET** /v1/quotes/activation-failures | List Quote Activation Failures
[**list_quotes**](QuotesApi.md#list_quotes) | **GET** /v1/quotes | List Quotes
[**post_quote**](QuotesApi.md#post_quote) | **POST** /v1/quotes | Post Quote
[**post_quote_accept**](QuotesApi.md#post_quote_accept) | **POST** /v1/quotes/{quote_id}/accept | Post Quote Accept
[**post_quote_activate**](QuotesApi.md#post_quote_activate) | **POST** /v1/quotes/{quote_id}/activate | Post Quote Activate
[**post_quote_approve**](QuotesApi.md#post_quote_approve) | **POST** /v1/quotes/{quote_id}/approve | Post Quote Approve
[**post_quote_lock**](QuotesApi.md#post_quote_lock) | **POST** /v1/quotes/{quote_id}/lock | Post Quote Lock
[**post_quote_reject**](QuotesApi.md#post_quote_reject) | **POST** /v1/quotes/{quote_id}/reject | Post Quote Reject
[**post_quote_send**](QuotesApi.md#post_quote_send) | **POST** /v1/quotes/{quote_id}/send | Post Quote Send
[**post_quote_session**](QuotesApi.md#post_quote_session) | **POST** /v1/quotes/{quote_id}/sessions | Post Quote Session
[**post_quote_signing_webhook**](QuotesApi.md#post_quote_signing_webhook) | **POST** /v1/quotes/signing/webhooks/{provider} | Post Quote Signing Webhook
[**post_quote_submit_approval_v1**](QuotesApi.md#post_quote_submit_approval_v1) | **POST** /v1/quotes/{quote_id}/submit-approval | Post Quote Submit Approval
[**post_quote_unlock**](QuotesApi.md#post_quote_unlock) | **POST** /v1/quotes/{quote_id}/unlock | Post Quote Unlock


# **get_quote**
> QuoteResponse get_quote(quote_id)

Get Quote

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_response import QuoteResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Quote
        api_response = api_instance.get_quote(quote_id)
        print("The response of QuotesApi->get_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

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

# **get_quote_version**
> QuoteVersionResponse get_quote_version(quote_id, version)

Get Quote Version

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    version = 56 # int | 

    try:
        # Get Quote Version
        api_response = api_instance.get_quote_version(quote_id, version)
        print("The response of QuotesApi->get_quote_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

# **list_quote_activation_failures_v1**
> object list_quote_activation_failures_v1(limit=limit, offset=offset)

List Quote Activation Failures

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
    api_instance = moolabs.QuotesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Quote Activation Failures
        api_response = api_instance.list_quote_activation_failures_v1(limit=limit, offset=offset)
        print("The response of QuotesApi->list_quote_activation_failures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quote_activation_failures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

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

# **list_quotes**
> QuoteListResponse list_quotes(limit=limit, offset=offset)

List Quotes

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_list_response import QuoteListResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Quotes
        api_response = api_instance.list_quotes(limit=limit, offset=offset)
        print("The response of QuotesApi->list_quotes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quotes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**QuoteListResponse**](QuoteListResponse.md)

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

# **post_quote**
> QuoteResponse post_quote(create_quote_request, idempotency_key=idempotency_key)

Post Quote

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_quote_request import CreateQuoteRequest
from moolabs.models.quote_response import QuoteResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    create_quote_request = moolabs.CreateQuoteRequest() # CreateQuoteRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote
        api_response = api_instance.post_quote(create_quote_request, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_quote_request** | [**CreateQuoteRequest**](CreateQuoteRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_accept**
> object post_quote_accept(quote_id, idempotency_key=idempotency_key, signed_document=signed_document, buyer_signer_ref=buyer_signer_ref, verified_by_ref=verified_by_ref, seller_signer_ref=seller_signer_ref)

Post Quote Accept

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    signed_document = None # bytearray |  (optional)
    buyer_signer_ref = 'buyer_signer_ref_example' # str |  (optional)
    verified_by_ref = 'verified_by_ref_example' # str |  (optional)
    seller_signer_ref = 'seller_signer_ref_example' # str |  (optional)

    try:
        # Post Quote Accept
        api_response = api_instance.post_quote_accept(quote_id, idempotency_key=idempotency_key, signed_document=signed_document, buyer_signer_ref=buyer_signer_ref, verified_by_ref=verified_by_ref, seller_signer_ref=seller_signer_ref)
        print("The response of QuotesApi->post_quote_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_accept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **signed_document** | **bytearray**|  | [optional] 
 **buyer_signer_ref** | **str**|  | [optional] 
 **verified_by_ref** | **str**|  | [optional] 
 **seller_signer_ref** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_activate**
> object post_quote_activate(quote_id, idempotency_key=idempotency_key)

Post Quote Activate

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Activate
        api_response = api_instance.post_quote_activate(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

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

# **post_quote_approve**
> QuoteApprovalResponse post_quote_approve(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)

Post Quote Approve

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_approval_decision_request import QuoteApprovalDecisionRequest
from moolabs.models.quote_approval_response import QuoteApprovalResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    quote_approval_decision_request = moolabs.QuoteApprovalDecisionRequest() # QuoteApprovalDecisionRequest |  (optional)

    try:
        # Post Quote Approve
        api_response = api_instance.post_quote_approve(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)
        print("The response of QuotesApi->post_quote_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **quote_approval_decision_request** | [**QuoteApprovalDecisionRequest**](QuoteApprovalDecisionRequest.md)|  | [optional] 

### Return type

[**QuoteApprovalResponse**](QuoteApprovalResponse.md)

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

# **post_quote_lock**
> QuoteVersionResponse post_quote_lock(quote_id, idempotency_key=idempotency_key)

Post Quote Lock

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Lock
        api_response = api_instance.post_quote_lock(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

# **post_quote_reject**
> QuoteApprovalResponse post_quote_reject(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)

Post Quote Reject

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_approval_decision_request import QuoteApprovalDecisionRequest
from moolabs.models.quote_approval_response import QuoteApprovalResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    quote_approval_decision_request = moolabs.QuoteApprovalDecisionRequest() # QuoteApprovalDecisionRequest |  (optional)

    try:
        # Post Quote Reject
        api_response = api_instance.post_quote_reject(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)
        print("The response of QuotesApi->post_quote_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_reject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **quote_approval_decision_request** | [**QuoteApprovalDecisionRequest**](QuoteApprovalDecisionRequest.md)|  | [optional] 

### Return type

[**QuoteApprovalResponse**](QuoteApprovalResponse.md)

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

# **post_quote_send**
> QuoteResponse post_quote_send(quote_id, idempotency_key=idempotency_key)

Post Quote Send

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_response import QuoteResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Send
        api_response = api_instance.post_quote_send(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteResponse**](QuoteResponse.md)

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

# **post_quote_session**
> CreateSessionResponse post_quote_session(quote_id, idempotency_key=idempotency_key)

Post Quote Session

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_session_response import CreateSessionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Session
        api_response = api_instance.post_quote_session(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_signing_webhook**
> object post_quote_signing_webhook(provider, x_quote_signature=x_quote_signature)

Post Quote Signing Webhook

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
    api_instance = moolabs.QuotesApi(api_client)
    provider = 'provider_example' # str | 
    x_quote_signature = 'x_quote_signature_example' # str |  (optional)

    try:
        # Post Quote Signing Webhook
        api_response = api_instance.post_quote_signing_webhook(provider, x_quote_signature=x_quote_signature)
        print("The response of QuotesApi->post_quote_signing_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_signing_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **x_quote_signature** | **str**|  | [optional] 

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

# **post_quote_submit_approval_v1**
> QuoteApprovalResponse post_quote_submit_approval_v1(quote_id, idempotency_key=idempotency_key)

Post Quote Submit Approval

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_approval_response import QuoteApprovalResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Submit Approval
        api_response = api_instance.post_quote_submit_approval_v1(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_submit_approval_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_submit_approval_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteApprovalResponse**](QuoteApprovalResponse.md)

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

# **post_quote_unlock**
> QuoteVersionResponse post_quote_unlock(quote_id, idempotency_key=idempotency_key)

Post Quote Unlock

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Unlock
        api_response = api_instance.post_quote_unlock(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_unlock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

