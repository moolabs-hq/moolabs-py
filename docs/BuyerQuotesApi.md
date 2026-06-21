# moolabs.BuyerQuotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_buyer_quote**](BuyerQuotesApi.md#accept_buyer_quote) | **POST** /v1/buyer/quotes/accept | Accept Buyer Quote
[**get_buyer_contract_pdf_v1**](BuyerQuotesApi.md#get_buyer_contract_pdf_v1) | **GET** /v1/buyer/quotes/contract.pdf | Get Buyer Contract Pdf
[**get_buyer_quote**](BuyerQuotesApi.md#get_buyer_quote) | **GET** /v1/buyer/quotes | Get Buyer Quote
[**reject_buyer_quote**](BuyerQuotesApi.md#reject_buyer_quote) | **POST** /v1/buyer/quotes/reject | Reject Buyer Quote
[**request_buyer_quote_changes_v1**](BuyerQuotesApi.md#request_buyer_quote_changes_v1) | **POST** /v1/buyer/quotes/request-changes | Request Buyer Quote Changes
[**request_otp**](BuyerQuotesApi.md#request_otp) | **POST** /v1/buyer/quotes/otp | Request Otp
[**verify_otp**](BuyerQuotesApi.md#verify_otp) | **POST** /v1/buyer/quotes/otp/verify | Verify Otp


# **accept_buyer_quote**
> Dict[str, object] accept_buyer_quote(buyer_accept_request, idempotency_key=idempotency_key, x_quote_buyer_token=x_quote_buyer_token)

Accept Buyer Quote

### Example


```python
import moolabs
from moolabs.models.buyer_accept_request import BuyerAcceptRequest
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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    buyer_accept_request = moolabs.BuyerAcceptRequest() # BuyerAcceptRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Accept Buyer Quote
        api_response = api_instance.accept_buyer_quote(buyer_accept_request, idempotency_key=idempotency_key, x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->accept_buyer_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->accept_buyer_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_accept_request** | [**BuyerAcceptRequest**](BuyerAcceptRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 
 **x_quote_buyer_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **get_buyer_contract_pdf_v1**
> object get_buyer_contract_pdf_v1(x_quote_buyer_token=x_quote_buyer_token)

Get Buyer Contract Pdf

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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Get Buyer Contract Pdf
        api_response = api_instance.get_buyer_contract_pdf_v1(x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->get_buyer_contract_pdf_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->get_buyer_contract_pdf_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_quote_buyer_token** | **str**|  | [optional] 

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

# **get_buyer_quote**
> BuyerQuoteProjection get_buyer_quote(x_quote_buyer_token=x_quote_buyer_token)

Get Buyer Quote

### Example


```python
import moolabs
from moolabs.models.buyer_quote_projection import BuyerQuoteProjection
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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Get Buyer Quote
        api_response = api_instance.get_buyer_quote(x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->get_buyer_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->get_buyer_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_quote_buyer_token** | **str**|  | [optional] 

### Return type

[**BuyerQuoteProjection**](BuyerQuoteProjection.md)

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

# **reject_buyer_quote**
> Dict[str, object] reject_buyer_quote(buyer_reject_request, x_quote_buyer_token=x_quote_buyer_token)

Reject Buyer Quote

### Example


```python
import moolabs
from moolabs.models.buyer_reject_request import BuyerRejectRequest
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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    buyer_reject_request = moolabs.BuyerRejectRequest() # BuyerRejectRequest | 
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Reject Buyer Quote
        api_response = api_instance.reject_buyer_quote(buyer_reject_request, x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->reject_buyer_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->reject_buyer_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_reject_request** | [**BuyerRejectRequest**](BuyerRejectRequest.md)|  | 
 **x_quote_buyer_token** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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

# **request_buyer_quote_changes_v1**
> BuyerRequestChangesResponse request_buyer_quote_changes_v1(buyer_request_changes_request, idempotency_key=idempotency_key, x_quote_buyer_token=x_quote_buyer_token)

Request Buyer Quote Changes

### Example


```python
import moolabs
from moolabs.models.buyer_request_changes_request import BuyerRequestChangesRequest
from moolabs.models.buyer_request_changes_response import BuyerRequestChangesResponse
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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    buyer_request_changes_request = moolabs.BuyerRequestChangesRequest() # BuyerRequestChangesRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Request Buyer Quote Changes
        api_response = api_instance.request_buyer_quote_changes_v1(buyer_request_changes_request, idempotency_key=idempotency_key, x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->request_buyer_quote_changes_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->request_buyer_quote_changes_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_request_changes_request** | [**BuyerRequestChangesRequest**](BuyerRequestChangesRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 
 **x_quote_buyer_token** | **str**|  | [optional] 

### Return type

[**BuyerRequestChangesResponse**](BuyerRequestChangesResponse.md)

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

# **request_otp**
> BuyerOtpRequestResponse request_otp(x_quote_buyer_token=x_quote_buyer_token)

Request Otp

### Example


```python
import moolabs
from moolabs.models.buyer_otp_request_response import BuyerOtpRequestResponse
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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Request Otp
        api_response = api_instance.request_otp(x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->request_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->request_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_quote_buyer_token** | **str**|  | [optional] 

### Return type

[**BuyerOtpRequestResponse**](BuyerOtpRequestResponse.md)

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

# **verify_otp**
> BuyerOtpVerifyResponse verify_otp(buyer_otp_verify_request, x_quote_buyer_token=x_quote_buyer_token)

Verify Otp

### Example


```python
import moolabs
from moolabs.models.buyer_otp_verify_request import BuyerOtpVerifyRequest
from moolabs.models.buyer_otp_verify_response import BuyerOtpVerifyResponse
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
    api_instance = moolabs.BuyerQuotesApi(api_client)
    buyer_otp_verify_request = moolabs.BuyerOtpVerifyRequest() # BuyerOtpVerifyRequest | 
    x_quote_buyer_token = 'x_quote_buyer_token_example' # str |  (optional)

    try:
        # Verify Otp
        api_response = api_instance.verify_otp(buyer_otp_verify_request, x_quote_buyer_token=x_quote_buyer_token)
        print("The response of BuyerQuotesApi->verify_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerQuotesApi->verify_otp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_otp_verify_request** | [**BuyerOtpVerifyRequest**](BuyerOtpVerifyRequest.md)|  | 
 **x_quote_buyer_token** | **str**|  | [optional] 

### Return type

[**BuyerOtpVerifyResponse**](BuyerOtpVerifyResponse.md)

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

