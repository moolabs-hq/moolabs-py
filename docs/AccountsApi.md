# moolabs.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountsApi.md#create_account) | **POST** /v1/arc/accounts | Create Account
[**create_contact**](AccountsApi.md#create_contact) | **POST** /v1/arc/accounts/{account_id}/contacts | Create Contact
[**get_account**](AccountsApi.md#get_account) | **GET** /v1/arc/accounts/{account_id} | Get Account
[**get_account_filter_options_v1**](AccountsApi.md#get_account_filter_options_v1) | **GET** /v1/arc/accounts/filter-options | Get Account Filter Options
[**get_account_overview**](AccountsApi.md#get_account_overview) | **GET** /v1/arc/accounts/{account_id}/overview | Get Account Overview
[**get_channel_preferences**](AccountsApi.md#get_channel_preferences) | **GET** /v1/arc/accounts/contacts/{contact_id}/preferences | Get Channel Preferences
[**list_account_invoices**](AccountsApi.md#list_account_invoices) | **GET** /v1/arc/accounts/{account_id}/invoices | List Account Invoices
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /v1/arc/accounts | List Accounts
[**list_contacts**](AccountsApi.md#list_contacts) | **GET** /v1/arc/accounts/{account_id}/contacts | List Contacts
[**opt_out_v1**](AccountsApi.md#opt_out_v1) | **POST** /v1/arc/accounts/contacts/{contact_id}/opt-out | Opt Out
[**resolve_jurisdiction_v1**](AccountsApi.md#resolve_jurisdiction_v1) | **POST** /v1/arc/accounts/{account_id}/resolve-jurisdiction | Resolve Jurisdiction
[**update_account**](AccountsApi.md#update_account) | **PATCH** /v1/arc/accounts/{account_id} | Update Account
[**update_channel_preferences**](AccountsApi.md#update_channel_preferences) | **PUT** /v1/arc/accounts/contacts/{contact_id}/preferences | Update Channel Preferences
[**update_contact**](AccountsApi.md#update_contact) | **PATCH** /v1/arc/accounts/contacts/{contact_id} | Update Contact


# **create_account**
> AccountResponse create_account(account_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Account

Create a new ARC account linked to a MooMeter customer.

### Example


```python
import moolabs
from moolabs.models.account_create import AccountCreate
from moolabs.models.account_response import AccountResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    account_create = moolabs.AccountCreate() # AccountCreate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Account
        api_response = api_instance.create_account(account_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->create_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_create** | [**AccountCreate**](AccountCreate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **create_contact**
> ContactResponse create_contact(account_id, contact_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Create Contact

Create a contact for an account.

### Example


```python
import moolabs
from moolabs.models.contact_create import ContactCreate
from moolabs.models.contact_response import ContactResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    contact_create = moolabs.ContactCreate() # ContactCreate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Create Contact
        api_response = api_instance.create_contact(account_id, contact_create, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **contact_create** | [**ContactCreate**](ContactCreate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ContactResponse**](ContactResponse.md)

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

# **get_account**
> AccountResponse get_account(account_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Get Account

Get a single account by ID.

### Example


```python
import moolabs
from moolabs.models.account_response import AccountResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Account
        api_response = api_instance.get_account(account_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **get_account_filter_options_v1**
> AccountFilterOptionsResponse get_account_filter_options_v1(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Get Account Filter Options

Return distinct account filter values needed by the Accounts list UI.

### Example


```python
import moolabs
from moolabs.models.account_filter_options_response import AccountFilterOptionsResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Account Filter Options
        api_response = api_instance.get_account_filter_options_v1(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->get_account_filter_options_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_filter_options_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountFilterOptionsResponse**](AccountFilterOptionsResponse.md)

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

# **get_account_overview**
> AccountOverviewResponse get_account_overview(account_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Get Account Overview

Return account-level aging summary for the Customer 360 overview tab.

### Example


```python
import moolabs
from moolabs.models.account_overview_response import AccountOverviewResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Account Overview
        api_response = api_instance.get_account_overview(account_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->get_account_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_overview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountOverviewResponse**](AccountOverviewResponse.md)

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

# **get_channel_preferences**
> ChannelPreferencesResponse get_channel_preferences(contact_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Get Channel Preferences

Get all channel preferences for a contact.

### Example


```python
import moolabs
from moolabs.models.channel_preferences_response import ChannelPreferencesResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Channel Preferences
        api_response = api_instance.get_channel_preferences(contact_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->get_channel_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_channel_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ChannelPreferencesResponse**](ChannelPreferencesResponse.md)

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

# **list_account_invoices**
> AccountInvoiceListResponse list_account_invoices(account_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Account Invoices

List all invoices associated with an account's collection cases.

### Example


```python
import moolabs
from moolabs.models.account_invoice_list_response import AccountInvoiceListResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Account Invoices
        api_response = api_instance.list_account_invoices(account_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->list_account_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountInvoiceListResponse**](AccountInvoiceListResponse.md)

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

# **list_accounts**
> AccountListResponse list_accounts(page=page, page_size=page_size, customer_id=customer_id, search=search, is_strategic=is_strategic, source_system=source_system, subsidiary=subsidiary, has_open_balance=has_open_balance, sort_by=sort_by, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Accounts

List accounts with pagination and optional filters.

### Example


```python
import moolabs
from moolabs.models.account_list_response import AccountListResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    customer_id = 'customer_id_example' # str |  (optional)
    search = 'search_example' # str | Search by legal name or customer ID (optional)
    is_strategic = True # bool |  (optional)
    source_system = 'source_system_example' # str |  (optional)
    subsidiary = ['subsidiary_example'] # List[str] | Filter by account subsidiary (optional)
    has_open_balance = True # bool | Filter by account open balance (optional)
    sort_by = 'sort_by_example' # str | created_desc, created_asc, open_balance_desc, open_balance_asc (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Accounts
        api_response = api_instance.list_accounts(page=page, page_size=page_size, customer_id=customer_id, search=search, is_strategic=is_strategic, source_system=source_system, subsidiary=subsidiary, has_open_balance=has_open_balance, sort_by=sort_by, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **customer_id** | **str**|  | [optional] 
 **search** | **str**| Search by legal name or customer ID | [optional] 
 **is_strategic** | **bool**|  | [optional] 
 **source_system** | **str**|  | [optional] 
 **subsidiary** | [**List[str]**](str.md)| Filter by account subsidiary | [optional] 
 **has_open_balance** | **bool**| Filter by account open balance | [optional] 
 **sort_by** | **str**| created_desc, created_asc, open_balance_desc, open_balance_asc | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountListResponse**](AccountListResponse.md)

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

# **list_contacts**
> ContactListResponse list_contacts(account_id, page=page, page_size=page_size, role=role, is_active=is_active, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

List Contacts

List contacts for an account with optional filters.

### Example


```python
import moolabs
from moolabs.models.contact_list_response import ContactListResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    role = 'role_example' # str | Filter by contact role (optional)
    is_active = True # bool | Filter by active status (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Contacts
        api_response = api_instance.list_contacts(account_id, page=page, page_size=page_size, role=role, is_active=is_active, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->list_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **role** | **str**| Filter by contact role | [optional] 
 **is_active** | **bool**| Filter by active status | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ContactListResponse**](ContactListResponse.md)

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

# **opt_out_v1**
> OptOutResponse opt_out_v1(contact_id, opt_out_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Opt Out

Process an opt-out request for a specific channel.

### Example


```python
import moolabs
from moolabs.models.opt_out_request import OptOutRequest
from moolabs.models.opt_out_response import OptOutResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    opt_out_request = moolabs.OptOutRequest() # OptOutRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Opt Out
        api_response = api_instance.opt_out_v1(contact_id, opt_out_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->opt_out_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->opt_out_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **opt_out_request** | [**OptOutRequest**](OptOutRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**OptOutResponse**](OptOutResponse.md)

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

# **resolve_jurisdiction_v1**
> JurisdictionProfileResponse resolve_jurisdiction_v1(account_id, jurisdiction_resolution_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Resolve Jurisdiction

Resolve effective jurisdiction for an account based on country/region.

### Example


```python
import moolabs
from moolabs.models.jurisdiction_profile_response import JurisdictionProfileResponse
from moolabs.models.jurisdiction_resolution_request import JurisdictionResolutionRequest
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    jurisdiction_resolution_request = moolabs.JurisdictionResolutionRequest() # JurisdictionResolutionRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Resolve Jurisdiction
        api_response = api_instance.resolve_jurisdiction_v1(account_id, jurisdiction_resolution_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->resolve_jurisdiction_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->resolve_jurisdiction_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **jurisdiction_resolution_request** | [**JurisdictionResolutionRequest**](JurisdictionResolutionRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**JurisdictionProfileResponse**](JurisdictionProfileResponse.md)

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

# **update_account**
> AccountResponse update_account(account_id, account_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Update Account

Partial update of an account.

### Example


```python
import moolabs
from moolabs.models.account_response import AccountResponse
from moolabs.models.account_update import AccountUpdate
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
    api_instance = moolabs.AccountsApi(api_client)
    account_id = 'account_id_example' # str | 
    account_update = moolabs.AccountUpdate() # AccountUpdate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update Account
        api_response = api_instance.update_account(account_id, account_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->update_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **account_update** | [**AccountUpdate**](AccountUpdate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **update_channel_preferences**
> ChannelPreferencesResponse update_channel_preferences(contact_id, channel_preference_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Update Channel Preferences

Bulk upsert channel preferences for a contact.

### Example


```python
import moolabs
from moolabs.models.channel_preference_update import ChannelPreferenceUpdate
from moolabs.models.channel_preferences_response import ChannelPreferencesResponse
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
    api_instance = moolabs.AccountsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    channel_preference_update = moolabs.ChannelPreferenceUpdate() # ChannelPreferenceUpdate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update Channel Preferences
        api_response = api_instance.update_channel_preferences(contact_id, channel_preference_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->update_channel_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_channel_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **channel_preference_update** | [**ChannelPreferenceUpdate**](ChannelPreferenceUpdate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ChannelPreferencesResponse**](ChannelPreferencesResponse.md)

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

# **update_contact**
> ContactResponse update_contact(contact_id, contact_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Update Contact

Update a contact. Setting is_active=false triggers F19 deactivation lifecycle: - Revokes portal tokens - Blocks pending communications - Creates human task for review

### Example


```python
import moolabs
from moolabs.models.contact_response import ContactResponse
from moolabs.models.contact_update import ContactUpdate
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
    api_instance = moolabs.AccountsApi(api_client)
    contact_id = 'contact_id_example' # str | 
    contact_update = moolabs.ContactUpdate() # ContactUpdate | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Update Contact
        api_response = api_instance.update_contact(contact_id, contact_update, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of AccountsApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**|  | 
 **contact_update** | [**ContactUpdate**](ContactUpdate.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ContactResponse**](ContactResponse.md)

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

