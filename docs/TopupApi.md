# moolabs.TopupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_link_v1**](TopupApi.md#create_payment_link_v1) | **POST** /v1/topup/payment-link | Create Payment Link
[**topup_checkout**](TopupApi.md#topup_checkout) | **GET** /v1/topup/checkout | Topup Checkout


# **create_payment_link_v1**
> PaymentLinkResponse create_payment_link_v1(payment_link_request)

Create Payment Link

Create a hosted checkout link for ARC invoice/PTP card payments.

### Example


```python
import moolabs
from moolabs.models.payment_link_request import PaymentLinkRequest
from moolabs.models.payment_link_response import PaymentLinkResponse
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
    api_instance = moolabs.TopupApi(api_client)
    payment_link_request = moolabs.PaymentLinkRequest() # PaymentLinkRequest | 

    try:
        # Create Payment Link
        api_response = api_instance.create_payment_link_v1(payment_link_request)
        print("The response of TopupApi->create_payment_link_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopupApi->create_payment_link_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_link_request** | [**PaymentLinkRequest**](PaymentLinkRequest.md)|  | 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

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

# **topup_checkout**
> object topup_checkout(wallet_id, tenant_id=tenant_id, pool_id=pool_id, amount_usd=amount_usd)

Topup Checkout

Redirect to Stripe Checkout for wallet top-up.  Used by the \"Top up this wallet\" link in alert emails. Accepts only wallet_id and amount_usd so we do not expose tenant_id/pool_id to customers; looks up tenant and pool from the wallet when not provided.

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
    api_instance = moolabs.TopupApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet to top up
    tenant_id = 'tenant_id_example' # str | Tenant ID (optional; looked up from wallet if omitted) (optional)
    pool_id = 'pool_id_example' # str | Pool ID (optional; looked up from wallet if omitted) (optional)
    amount_usd = 50.0 # float | Amount in USD (optional) (default to 50.0)

    try:
        # Topup Checkout
        api_response = api_instance.topup_checkout(wallet_id, tenant_id=tenant_id, pool_id=pool_id, amount_usd=amount_usd)
        print("The response of TopupApi->topup_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TopupApi->topup_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet to top up | 
 **tenant_id** | **str**| Tenant ID (optional; looked up from wallet if omitted) | [optional] 
 **pool_id** | **str**| Pool ID (optional; looked up from wallet if omitted) | [optional] 
 **amount_usd** | **float**| Amount in USD | [optional] [default to 50.0]

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

