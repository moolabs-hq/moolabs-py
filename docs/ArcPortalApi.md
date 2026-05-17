# moolabs.ArcPortalApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portal_create_dispute**](ArcPortalApi.md#portal_create_dispute) | **POST** /v1/arc/portal/me/disputes | Portal Create Dispute
[**portal_create_ptp_v1_arc**](ArcPortalApi.md#portal_create_ptp_v1_arc) | **POST** /v1/arc/portal/me/promises-to-pay | Portal Create Ptp
[**portal_make_payment**](ArcPortalApi.md#portal_make_payment) | **POST** /v1/arc/portal/me/payments | Portal Make Payment
[**portal_my_cases**](ArcPortalApi.md#portal_my_cases) | **GET** /v1/arc/portal/me/cases | Portal My Cases
[**portal_my_invoices**](ArcPortalApi.md#portal_my_invoices) | **GET** /v1/arc/portal/me/invoices | Portal My Invoices
[**portal_update_preferences**](ArcPortalApi.md#portal_update_preferences) | **PUT** /v1/arc/portal/me/preferences | Portal Update Preferences


# **portal_create_dispute**
> object portal_create_dispute(authorization, portal_dispute_request)

Portal Create Dispute

POST /portal/me/disputes — File a dispute.

### Example


```python
import moolabs
from moolabs.models.portal_dispute_request import PortalDisputeRequest
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
    api_instance = moolabs.ArcPortalApi(api_client)
    authorization = 'authorization_example' # str | 
    portal_dispute_request = moolabs.PortalDisputeRequest() # PortalDisputeRequest | 

    try:
        # Portal Create Dispute
        api_response = api_instance.portal_create_dispute(authorization, portal_dispute_request)
        print("The response of ArcPortalApi->portal_create_dispute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcPortalApi->portal_create_dispute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **portal_dispute_request** | [**PortalDisputeRequest**](PortalDisputeRequest.md)|  | 

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

# **portal_create_ptp_v1_arc**
> object portal_create_ptp_v1_arc(authorization, portal_ptp_request)

Portal Create Ptp

POST /portal/me/promises-to-pay — Create a PTP.

### Example


```python
import moolabs
from moolabs.models.portal_ptp_request import PortalPTPRequest
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
    api_instance = moolabs.ArcPortalApi(api_client)
    authorization = 'authorization_example' # str | 
    portal_ptp_request = moolabs.PortalPTPRequest() # PortalPTPRequest | 

    try:
        # Portal Create Ptp
        api_response = api_instance.portal_create_ptp_v1_arc(authorization, portal_ptp_request)
        print("The response of ArcPortalApi->portal_create_ptp_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcPortalApi->portal_create_ptp_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **portal_ptp_request** | [**PortalPTPRequest**](PortalPTPRequest.md)|  | 

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

# **portal_make_payment**
> object portal_make_payment(authorization, portal_payment_request)

Portal Make Payment

POST /portal/me/payments — Initiate a payment.

### Example


```python
import moolabs
from moolabs.models.portal_payment_request import PortalPaymentRequest
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
    api_instance = moolabs.ArcPortalApi(api_client)
    authorization = 'authorization_example' # str | 
    portal_payment_request = moolabs.PortalPaymentRequest() # PortalPaymentRequest | 

    try:
        # Portal Make Payment
        api_response = api_instance.portal_make_payment(authorization, portal_payment_request)
        print("The response of ArcPortalApi->portal_make_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcPortalApi->portal_make_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **portal_payment_request** | [**PortalPaymentRequest**](PortalPaymentRequest.md)|  | 

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

# **portal_my_cases**
> object portal_my_cases(authorization)

Portal My Cases

GET /portal/me/cases — List my cases.

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
    api_instance = moolabs.ArcPortalApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        # Portal My Cases
        api_response = api_instance.portal_my_cases(authorization)
        print("The response of ArcPortalApi->portal_my_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcPortalApi->portal_my_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

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

# **portal_my_invoices**
> object portal_my_invoices(authorization)

Portal My Invoices

GET /portal/me/invoices — List my invoices.

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
    api_instance = moolabs.ArcPortalApi(api_client)
    authorization = 'authorization_example' # str | 

    try:
        # Portal My Invoices
        api_response = api_instance.portal_my_invoices(authorization)
        print("The response of ArcPortalApi->portal_my_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcPortalApi->portal_my_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 

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

# **portal_update_preferences**
> object portal_update_preferences(authorization, portal_preferences_request)

Portal Update Preferences

PUT /portal/me/preferences — Update communication preferences.

### Example


```python
import moolabs
from moolabs.models.portal_preferences_request import PortalPreferencesRequest
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
    api_instance = moolabs.ArcPortalApi(api_client)
    authorization = 'authorization_example' # str | 
    portal_preferences_request = moolabs.PortalPreferencesRequest() # PortalPreferencesRequest | 

    try:
        # Portal Update Preferences
        api_response = api_instance.portal_update_preferences(authorization, portal_preferences_request)
        print("The response of ArcPortalApi->portal_update_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcPortalApi->portal_update_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **portal_preferences_request** | [**PortalPreferencesRequest**](PortalPreferencesRequest.md)|  | 

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

