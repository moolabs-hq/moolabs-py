# moolabs.CashCreditsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_credit_endpoint_v1**](CashCreditsApi.md#apply_credit_endpoint_v1) | **POST** /v1/arc/cash-credits/{credit_id}/apply | Apply Credit Endpoint
[**convert_credit_endpoint_v1**](CashCreditsApi.md#convert_credit_endpoint_v1) | **POST** /v1/arc/cash-credits/{credit_id}/convert | Convert Credit Endpoint
[**list_credits_endpoint_v1**](CashCreditsApi.md#list_credits_endpoint_v1) | **GET** /v1/arc/cash-credits | List Credits Endpoint
[**refund_credit_endpoint_v1**](CashCreditsApi.md#refund_credit_endpoint_v1) | **POST** /v1/arc/cash-credits/{credit_id}/refund | Refund Credit Endpoint


# **apply_credit_endpoint_v1**
> object apply_credit_endpoint_v1(credit_id, apply_credit_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Apply Credit Endpoint

POST /cash-credits/{id}/apply — Apply credit to invoice.

### Example


```python
import moolabs
from moolabs.models.apply_credit_request import ApplyCreditRequest
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
    api_instance = moolabs.CashCreditsApi(api_client)
    credit_id = 'credit_id_example' # str | 
    apply_credit_request = moolabs.ApplyCreditRequest() # ApplyCreditRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Apply Credit Endpoint
        api_response = api_instance.apply_credit_endpoint_v1(credit_id, apply_credit_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CashCreditsApi->apply_credit_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashCreditsApi->apply_credit_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | **str**|  | 
 **apply_credit_request** | [**ApplyCreditRequest**](ApplyCreditRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **convert_credit_endpoint_v1**
> object convert_credit_endpoint_v1(credit_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Convert Credit Endpoint

POST /cash-credits/{id}/convert — Convert to usage grant.

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
    api_instance = moolabs.CashCreditsApi(api_client)
    credit_id = 'credit_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Convert Credit Endpoint
        api_response = api_instance.convert_credit_endpoint_v1(credit_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CashCreditsApi->convert_credit_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashCreditsApi->convert_credit_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **list_credits_endpoint_v1**
> object list_credits_endpoint_v1(account_id=account_id, status=status, page=page, page_size=page_size, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Credits Endpoint

GET /cash-credits — List cash credits.

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
    api_instance = moolabs.CashCreditsApi(api_client)
    account_id = 'account_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Credits Endpoint
        api_response = api_instance.list_credits_endpoint_v1(account_id=account_id, status=status, page=page, page_size=page_size, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CashCreditsApi->list_credits_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashCreditsApi->list_credits_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **refund_credit_endpoint_v1**
> object refund_credit_endpoint_v1(credit_id, refund_credit_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Refund Credit Endpoint

POST /cash-credits/{id}/refund — Refund credit.

### Example


```python
import moolabs
from moolabs.models.refund_credit_request import RefundCreditRequest
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
    api_instance = moolabs.CashCreditsApi(api_client)
    credit_id = 'credit_id_example' # str | 
    refund_credit_request = moolabs.RefundCreditRequest() # RefundCreditRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Refund Credit Endpoint
        api_response = api_instance.refund_credit_endpoint_v1(credit_id, refund_credit_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of CashCreditsApi->refund_credit_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CashCreditsApi->refund_credit_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | **str**|  | 
 **refund_credit_request** | [**RefundCreditRequest**](RefundCreditRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

