# moolabs.CustomersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /api/v1/customers | Create customer
[**create_customer_stripe_portal_session**](CustomersApi.md#create_customer_stripe_portal_session) | **POST** /api/v1/customers/{customerIdOrKey}/stripe/portal | Create Stripe customer portal session
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /api/v1/customers/{customerIdOrKey} | Delete customer
[**delete_customer_app_data**](CustomersApi.md#delete_customer_app_data) | **DELETE** /api/v1/customers/{customerIdOrKey}/apps/{appId} | Delete customer app data
[**get_customer**](CustomersApi.md#get_customer) | **GET** /api/v1/customers/{customerIdOrKey} | Get customer
[**get_customer_stripe_app_data**](CustomersApi.md#get_customer_stripe_app_data) | **GET** /api/v1/customers/{customerIdOrKey}/stripe | Get customer stripe app data
[**list_customer_app_data**](CustomersApi.md#list_customer_app_data) | **GET** /api/v1/customers/{customerIdOrKey}/apps | List customer app data
[**list_customer_subscriptions**](CustomersApi.md#list_customer_subscriptions) | **GET** /api/v1/customers/{customerIdOrKey}/subscriptions | List customer subscriptions
[**list_customers**](CustomersApi.md#list_customers) | **GET** /api/v1/customers | List customers
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /api/v1/customers/{customerIdOrKey} | Update customer
[**upsert_customer_app_data**](CustomersApi.md#upsert_customer_app_data) | **PUT** /api/v1/customers/{customerIdOrKey}/apps | Upsert customer app data
[**upsert_customer_stripe_app_data**](CustomersApi.md#upsert_customer_stripe_app_data) | **PUT** /api/v1/customers/{customerIdOrKey}/stripe | Upsert customer stripe app data


# **create_customer**
> Customer create_customer(customer_create)

Create customer

Create a new customer.

### Example


```python
import moolabs
from moolabs.models.customer import Customer
from moolabs.models.customer_create import CustomerCreate
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_create = moolabs.CustomerCreate() # CustomerCreate | 

    try:
        # Create customer
        api_response = api_instance.create_customer(customer_create)
        print("The response of CustomersApi->create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_create** | [**CustomerCreate**](CustomerCreate.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_stripe_portal_session**
> StripeCustomerPortalSession create_customer_stripe_portal_session(customer_id_or_key, create_stripe_customer_portal_session_params)

Create Stripe customer portal session

Create Stripe customer portal session. Only returns URL if the customer billing profile is linked to a stripe app and customer.  Useful to redirect the customer to the Stripe customer portal to manage their payment methods, change their billing address and access their invoice history.

### Example


```python
import moolabs
from moolabs.models.create_stripe_customer_portal_session_params import CreateStripeCustomerPortalSessionParams
from moolabs.models.stripe_customer_portal_session import StripeCustomerPortalSession
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    create_stripe_customer_portal_session_params = moolabs.CreateStripeCustomerPortalSessionParams() # CreateStripeCustomerPortalSessionParams | 

    try:
        # Create Stripe customer portal session
        api_response = api_instance.create_customer_stripe_portal_session(customer_id_or_key, create_stripe_customer_portal_session_params)
        print("The response of CustomersApi->create_customer_stripe_portal_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_customer_stripe_portal_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **create_stripe_customer_portal_session_params** | [**CreateStripeCustomerPortalSessionParams**](CreateStripeCustomerPortalSessionParams.md)|  | 

### Return type

[**StripeCustomerPortalSession**](StripeCustomerPortalSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(customer_id_or_key)

Delete customer

Delete a customer by ID.

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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 

    try:
        # Delete customer
        api_instance.delete_customer(customer_id_or_key)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_app_data**
> delete_customer_app_data(customer_id_or_key, app_id)

Delete customer app data

Delete customer app data.

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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    app_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete customer app data
        api_instance.delete_customer_app_data(customer_id_or_key, app_id)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customer_app_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> Customer get_customer(customer_id_or_key, expand=expand)

Get customer

Get a customer by ID or key.

### Example


```python
import moolabs
from moolabs.models.customer import Customer
from moolabs.models.customer_expand import CustomerExpand
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    expand = [moolabs.CustomerExpand()] # List[CustomerExpand] | What parts of the customer output to expand (optional)

    try:
        # Get customer
        api_response = api_instance.get_customer(customer_id_or_key, expand=expand)
        print("The response of CustomersApi->get_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **expand** | [**List[CustomerExpand]**](CustomerExpand.md)| What parts of the customer output to expand | [optional] 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_stripe_app_data**
> StripeCustomerAppData get_customer_stripe_app_data(customer_id_or_key)

Get customer stripe app data

Get stripe app data for a customer. Only returns data if the customer billing profile is linked to a stripe app.

### Example


```python
import moolabs
from moolabs.models.stripe_customer_app_data import StripeCustomerAppData
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 

    try:
        # Get customer stripe app data
        api_response = api_instance.get_customer_stripe_app_data(customer_id_or_key)
        print("The response of CustomersApi->get_customer_stripe_app_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customer_stripe_app_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 

### Return type

[**StripeCustomerAppData**](StripeCustomerAppData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_app_data**
> CustomerAppDataPaginatedResponse list_customer_app_data(customer_id_or_key, page=page, page_size=page_size, type=type)

List customer app data

List customers app data.

### Example


```python
import moolabs
from moolabs.models.app_type import AppType
from moolabs.models.customer_app_data_paginated_response import CustomerAppDataPaginatedResponse
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    type = moolabs.AppType() # AppType | Filter customer data by app type. (optional)

    try:
        # List customer app data
        api_response = api_instance.list_customer_app_data(customer_id_or_key, page=page, page_size=page_size, type=type)
        print("The response of CustomersApi->list_customer_app_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_app_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **type** | [**AppType**](.md)| Filter customer data by app type. | [optional] 

### Return type

[**CustomerAppDataPaginatedResponse**](CustomerAppDataPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_subscriptions**
> SubscriptionPaginatedResponse list_customer_subscriptions(customer_id_or_key, status=status, order=order, order_by=order_by, page=page, page_size=page_size)

List customer subscriptions

Lists all subscriptions for a customer.

### Example


```python
import moolabs
from moolabs.models.customer_subscription_order_by import CustomerSubscriptionOrderBy
from moolabs.models.sort_order import SortOrder
from moolabs.models.subscription_paginated_response import SubscriptionPaginatedResponse
from moolabs.models.subscription_status import SubscriptionStatus
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    status = [moolabs.SubscriptionStatus()] # List[SubscriptionStatus] |  (optional)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.CustomerSubscriptionOrderBy() # CustomerSubscriptionOrderBy | The order by field. (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)

    try:
        # List customer subscriptions
        api_response = api_instance.list_customer_subscriptions(customer_id_or_key, status=status, order=order, order_by=order_by, page=page, page_size=page_size)
        print("The response of CustomersApi->list_customer_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **status** | [**List[SubscriptionStatus]**](SubscriptionStatus.md)|  | [optional] 
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**CustomerSubscriptionOrderBy**](.md)| The order by field. | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]

### Return type

[**SubscriptionPaginatedResponse**](SubscriptionPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> CustomerPaginatedResponse list_customers(page=page, page_size=page_size, order=order, order_by=order_by, include_deleted=include_deleted, key=key, name=name, primary_email=primary_email, subject=subject, plan_key=plan_key, expand=expand)

List customers

List customers.

### Example


```python
import moolabs
from moolabs.models.customer_expand import CustomerExpand
from moolabs.models.customer_order_by import CustomerOrderBy
from moolabs.models.customer_paginated_response import CustomerPaginatedResponse
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.CustomersApi(api_client)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.CustomerOrderBy() # CustomerOrderBy | The order by field. (optional)
    include_deleted = False # bool | Include deleted customers. (optional) (default to False)
    key = 'key_example' # str | Filter customers by key. Case-insensitive partial match. (optional)
    name = 'name_example' # str | Filter customers by name. Case-insensitive partial match. (optional)
    primary_email = 'primary_email_example' # str | Filter customers by primary email. Case-insensitive partial match. (optional)
    subject = 'subject_example' # str | Filter customers by usage attribution subject. Case-insensitive partial match. (optional)
    plan_key = 'plan_key_example' # str | Filter customers by the plan key of their susbcription. (optional)
    expand = [moolabs.CustomerExpand()] # List[CustomerExpand] | What parts of the list output to expand in listings (optional)

    try:
        # List customers
        api_response = api_instance.list_customers(page=page, page_size=page_size, order=order, order_by=order_by, include_deleted=include_deleted, key=key, name=name, primary_email=primary_email, subject=subject, plan_key=plan_key, expand=expand)
        print("The response of CustomersApi->list_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**CustomerOrderBy**](.md)| The order by field. | [optional] 
 **include_deleted** | **bool**| Include deleted customers. | [optional] [default to False]
 **key** | **str**| Filter customers by key. Case-insensitive partial match. | [optional] 
 **name** | **str**| Filter customers by name. Case-insensitive partial match. | [optional] 
 **primary_email** | **str**| Filter customers by primary email. Case-insensitive partial match. | [optional] 
 **subject** | **str**| Filter customers by usage attribution subject. Case-insensitive partial match. | [optional] 
 **plan_key** | **str**| Filter customers by the plan key of their susbcription. | [optional] 
 **expand** | [**List[CustomerExpand]**](CustomerExpand.md)| What parts of the list output to expand in listings | [optional] 

### Return type

[**CustomerPaginatedResponse**](CustomerPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> Customer update_customer(customer_id_or_key, customer_replace_update)

Update customer

Update a customer by ID.

### Example


```python
import moolabs
from moolabs.models.customer import Customer
from moolabs.models.customer_replace_update import CustomerReplaceUpdate
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    customer_replace_update = moolabs.CustomerReplaceUpdate() # CustomerReplaceUpdate | 

    try:
        # Update customer
        api_response = api_instance.update_customer(customer_id_or_key, customer_replace_update)
        print("The response of CustomersApi->update_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **customer_replace_update** | [**CustomerReplaceUpdate**](CustomerReplaceUpdate.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_customer_app_data**
> List[CustomerAppData] upsert_customer_app_data(customer_id_or_key, customer_app_data_create_or_update_item)

Upsert customer app data

Upsert customer app data.

### Example


```python
import moolabs
from moolabs.models.customer_app_data import CustomerAppData
from moolabs.models.customer_app_data_create_or_update_item import CustomerAppDataCreateOrUpdateItem
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    customer_app_data_create_or_update_item = [moolabs.CustomerAppDataCreateOrUpdateItem()] # List[CustomerAppDataCreateOrUpdateItem] | 

    try:
        # Upsert customer app data
        api_response = api_instance.upsert_customer_app_data(customer_id_or_key, customer_app_data_create_or_update_item)
        print("The response of CustomersApi->upsert_customer_app_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->upsert_customer_app_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **customer_app_data_create_or_update_item** | [**List[CustomerAppDataCreateOrUpdateItem]**](CustomerAppDataCreateOrUpdateItem.md)|  | 

### Return type

[**List[CustomerAppData]**](CustomerAppData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_customer_stripe_app_data**
> StripeCustomerAppData upsert_customer_stripe_app_data(customer_id_or_key, stripe_customer_app_data_base)

Upsert customer stripe app data

Upsert stripe app data for a customer. Only updates data if the customer billing profile is linked to a stripe app.

### Example


```python
import moolabs
from moolabs.models.stripe_customer_app_data import StripeCustomerAppData
from moolabs.models.stripe_customer_app_data_base import StripeCustomerAppDataBase
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
    api_instance = moolabs.CustomersApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    stripe_customer_app_data_base = moolabs.StripeCustomerAppDataBase() # StripeCustomerAppDataBase | 

    try:
        # Upsert customer stripe app data
        api_response = api_instance.upsert_customer_stripe_app_data(customer_id_or_key, stripe_customer_app_data_base)
        print("The response of CustomersApi->upsert_customer_stripe_app_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->upsert_customer_stripe_app_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **stripe_customer_app_data_base** | [**StripeCustomerAppDataBase**](StripeCustomerAppDataBase.md)|  | 

### Return type

[**StripeCustomerAppData**](StripeCustomerAppData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

