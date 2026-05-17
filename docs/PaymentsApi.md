# moolabs.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_allocations**](PaymentsApi.md#get_payment_allocations) | **GET** /v1/arc/payments/{payment_id}/allocations | Get Payment Allocations
[**list_account_payments_v1**](PaymentsApi.md#list_account_payments_v1) | **GET** /v1/arc/payments/by-account/{account_id} | List Account Payments
[**list_case_payments_v1**](PaymentsApi.md#list_case_payments_v1) | **GET** /v1/arc/payments/by-case/{case_id} | List Case Payments
[**match_payment**](PaymentsApi.md#match_payment) | **POST** /v1/arc/payments/{payment_id}/match | Match Payment
[**record_payment**](PaymentsApi.md#record_payment) | **POST** /v1/arc/payments | Record Payment
[**reverse_payment**](PaymentsApi.md#reverse_payment) | **POST** /v1/arc/payments/{payment_id}/reverse | Reverse Payment
[**settle_hosted_checkout_v1_arc**](PaymentsApi.md#settle_hosted_checkout_v1_arc) | **POST** /v1/arc/payments/hosted-checkout-settlements | Settle Hosted Checkout


# **get_payment_allocations**
> AllocationsListResponse get_payment_allocations(payment_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Payment Allocations

Get allocations for a payment.

### Example


```python
import moolabs
from moolabs.models.allocations_list_response import AllocationsListResponse
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
    api_instance = moolabs.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Payment Allocations
        api_response = api_instance.get_payment_allocations(payment_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of PaymentsApi->get_payment_allocations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_payment_allocations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**AllocationsListResponse**](AllocationsListResponse.md)

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

# **list_account_payments_v1**
> List[PaymentResponse] list_account_payments_v1(account_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Account Payments

List every payment landed against any case on this account.  Used by Customer 360 (``CustomerView``) to compute the \"Last Payment\" KPI and the payments-history tab.  Returns a flat array (NOT the paginated shape used by ``/by-case``) because the caller aggregates across all payments and a single account's lifetime payment count is bounded enough that pagination would only add caller complexity.  See ``service.list_account_payments`` for the JOIN rationale + tenant-scope defense.

### Example


```python
import moolabs
from moolabs.models.payment_response import PaymentResponse
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
    api_instance = moolabs.PaymentsApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Account Payments
        api_response = api_instance.list_account_payments_v1(account_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of PaymentsApi->list_account_payments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->list_account_payments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**List[PaymentResponse]**](PaymentResponse.md)

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

# **list_case_payments_v1**
> PaymentListResponse list_case_payments_v1(case_id, x_api_key, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

List Case Payments

List payments for a case.

### Example


```python
import moolabs
from moolabs.models.payment_list_response import PaymentListResponse
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
    api_instance = moolabs.PaymentsApi(api_client)
    case_id = 'case_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # List Case Payments
        api_response = api_instance.list_case_payments_v1(case_id, x_api_key, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of PaymentsApi->list_case_payments_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->list_case_payments_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**PaymentListResponse**](PaymentListResponse.md)

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

# **match_payment**
> PaymentResponse match_payment(payment_id, x_api_key, payment_match_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Match Payment

Exact match a payment to an invoice. Invariant 1 enforced.

### Example


```python
import moolabs
from moolabs.models.payment_match_request import PaymentMatchRequest
from moolabs.models.payment_response import PaymentResponse
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
    api_instance = moolabs.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    payment_match_request = moolabs.PaymentMatchRequest() # PaymentMatchRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Match Payment
        api_response = api_instance.match_payment(payment_id, x_api_key, payment_match_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of PaymentsApi->match_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->match_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **payment_match_request** | [**PaymentMatchRequest**](PaymentMatchRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**PaymentResponse**](PaymentResponse.md)

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

# **record_payment**
> PaymentResponse record_payment(x_api_key, payment_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Record Payment

Record a new payment for a case.

### Example


```python
import moolabs
from moolabs.models.payment_create import PaymentCreate
from moolabs.models.payment_response import PaymentResponse
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
    api_instance = moolabs.PaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    payment_create = moolabs.PaymentCreate() # PaymentCreate | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Record Payment
        api_response = api_instance.record_payment(x_api_key, payment_create, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of PaymentsApi->record_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->record_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **payment_create** | [**PaymentCreate**](PaymentCreate.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**PaymentResponse**](PaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_payment**
> PaymentResponse reverse_payment(payment_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, payment_reversal_request=payment_reversal_request)

Reverse Payment

Reverse a payment — undoes allocations and recalculates case outstanding.

### Example


```python
import moolabs
from moolabs.models.payment_response import PaymentResponse
from moolabs.models.payment_reversal_request import PaymentReversalRequest
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
    api_instance = moolabs.PaymentsApi(api_client)
    payment_id = 'payment_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    payment_reversal_request = moolabs.PaymentReversalRequest() # PaymentReversalRequest |  (optional)

    try:
        # Reverse Payment
        api_response = api_instance.reverse_payment(payment_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, payment_reversal_request=payment_reversal_request)
        print("The response of PaymentsApi->reverse_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->reverse_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **payment_reversal_request** | [**PaymentReversalRequest**](PaymentReversalRequest.md)|  | [optional] 

### Return type

[**PaymentResponse**](PaymentResponse.md)

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

# **settle_hosted_checkout_v1_arc**
> HostedCheckoutSettlementResponse settle_hosted_checkout_v1_arc(x_api_key, hosted_checkout_settlement_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Settle Hosted Checkout

Record a hosted checkout payment, apply it, and fulfill the referenced PTP.

### Example


```python
import moolabs
from moolabs.models.hosted_checkout_settlement_request import HostedCheckoutSettlementRequest
from moolabs.models.hosted_checkout_settlement_response import HostedCheckoutSettlementResponse
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
    api_instance = moolabs.PaymentsApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    hosted_checkout_settlement_request = moolabs.HostedCheckoutSettlementRequest() # HostedCheckoutSettlementRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Settle Hosted Checkout
        api_response = api_instance.settle_hosted_checkout_v1_arc(x_api_key, hosted_checkout_settlement_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of PaymentsApi->settle_hosted_checkout_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->settle_hosted_checkout_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **hosted_checkout_settlement_request** | [**HostedCheckoutSettlementRequest**](HostedCheckoutSettlementRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**HostedCheckoutSettlementResponse**](HostedCheckoutSettlementResponse.md)

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

