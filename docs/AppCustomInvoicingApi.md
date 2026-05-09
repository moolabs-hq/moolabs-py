# moolabs.AppCustomInvoicingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_custom_invoicing_draft_synchronized**](AppCustomInvoicingApi.md#app_custom_invoicing_draft_synchronized) | **POST** /api/v1/apps/custom-invoicing/{invoiceId}/draft/synchronized | Submit draft synchronization results
[**app_custom_invoicing_issuing_synchronized**](AppCustomInvoicingApi.md#app_custom_invoicing_issuing_synchronized) | **POST** /api/v1/apps/custom-invoicing/{invoiceId}/issuing/synchronized | Submit issuing synchronization results
[**app_custom_invoicing_update_payment_status**](AppCustomInvoicingApi.md#app_custom_invoicing_update_payment_status) | **POST** /api/v1/apps/custom-invoicing/{invoiceId}/payment/status | Update payment status


# **app_custom_invoicing_draft_synchronized**
> app_custom_invoicing_draft_synchronized(invoice_id, custom_invoicing_draft_synchronized_request)

Submit draft synchronization results

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.custom_invoicing_draft_synchronized_request import CustomInvoicingDraftSynchronizedRequest
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AppCustomInvoicingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    custom_invoicing_draft_synchronized_request = moolabs.CustomInvoicingDraftSynchronizedRequest() # CustomInvoicingDraftSynchronizedRequest | 

    try:
        # Submit draft synchronization results
        api_instance.app_custom_invoicing_draft_synchronized(invoice_id, custom_invoicing_draft_synchronized_request)
    except Exception as e:
        print("Exception when calling AppCustomInvoicingApi->app_custom_invoicing_draft_synchronized: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **custom_invoicing_draft_synchronized_request** | [**CustomInvoicingDraftSynchronizedRequest**](CustomInvoicingDraftSynchronizedRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_custom_invoicing_issuing_synchronized**
> app_custom_invoicing_issuing_synchronized(invoice_id, custom_invoicing_finalized_request)

Submit issuing synchronization results

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.custom_invoicing_finalized_request import CustomInvoicingFinalizedRequest
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AppCustomInvoicingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    custom_invoicing_finalized_request = moolabs.CustomInvoicingFinalizedRequest() # CustomInvoicingFinalizedRequest | 

    try:
        # Submit issuing synchronization results
        api_instance.app_custom_invoicing_issuing_synchronized(invoice_id, custom_invoicing_finalized_request)
    except Exception as e:
        print("Exception when calling AppCustomInvoicingApi->app_custom_invoicing_issuing_synchronized: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **custom_invoicing_finalized_request** | [**CustomInvoicingFinalizedRequest**](CustomInvoicingFinalizedRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_custom_invoicing_update_payment_status**
> app_custom_invoicing_update_payment_status(invoice_id, custom_invoicing_update_payment_status_request)

Update payment status

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.custom_invoicing_update_payment_status_request import CustomInvoicingUpdatePaymentStatusRequest
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.AppCustomInvoicingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    custom_invoicing_update_payment_status_request = moolabs.CustomInvoicingUpdatePaymentStatusRequest() # CustomInvoicingUpdatePaymentStatusRequest | 

    try:
        # Update payment status
        api_instance.app_custom_invoicing_update_payment_status(invoice_id, custom_invoicing_update_payment_status_request)
    except Exception as e:
        print("Exception when calling AppCustomInvoicingApi->app_custom_invoicing_update_payment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **custom_invoicing_update_payment_status_request** | [**CustomInvoicingUpdatePaymentStatusRequest**](CustomInvoicingUpdatePaymentStatusRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

