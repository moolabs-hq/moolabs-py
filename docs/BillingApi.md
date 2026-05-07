# moolabs.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advance_invoice_action**](BillingApi.md#advance_invoice_action) | **POST** /api/v1/billing/invoices/{invoiceId}/advance | Advance the invoice&#39;s state to the next status
[**approve_invoice_action**](BillingApi.md#approve_invoice_action) | **POST** /api/v1/billing/invoices/{invoiceId}/approve | Send the invoice to the customer
[**create_billing_profile**](BillingApi.md#create_billing_profile) | **POST** /api/v1/billing/profiles | Create a new billing profile
[**create_pending_invoice_line**](BillingApi.md#create_pending_invoice_line) | **POST** /api/v1/billing/customers/{customerId}/invoices/pending-lines | Create pending line items
[**delete_billing_profile**](BillingApi.md#delete_billing_profile) | **DELETE** /api/v1/billing/profiles/{id} | Delete a billing profile
[**delete_billing_profile_customer_override**](BillingApi.md#delete_billing_profile_customer_override) | **DELETE** /api/v1/billing/customers/{customerId} | Delete a customer override
[**delete_invoice**](BillingApi.md#delete_invoice) | **DELETE** /api/v1/billing/invoices/{invoiceId} | Delete an invoice
[**get_billing_profile**](BillingApi.md#get_billing_profile) | **GET** /api/v1/billing/profiles/{id} | Get a billing profile
[**get_billing_profile_customer_override**](BillingApi.md#get_billing_profile_customer_override) | **GET** /api/v1/billing/customers/{customerId} | Get a customer override
[**get_invoice**](BillingApi.md#get_invoice) | **GET** /api/v1/billing/invoices/{invoiceId} | Get an invoice
[**invoice_pending_lines_action**](BillingApi.md#invoice_pending_lines_action) | **POST** /api/v1/billing/invoices/invoice | Invoice a customer based on the pending line items
[**list_billing_profile_customer_overrides**](BillingApi.md#list_billing_profile_customer_overrides) | **GET** /api/v1/billing/customers | List customer overrides
[**list_billing_profiles**](BillingApi.md#list_billing_profiles) | **GET** /api/v1/billing/profiles | List billing profiles
[**list_invoices**](BillingApi.md#list_invoices) | **GET** /api/v1/billing/invoices | List invoices
[**recalculate_invoice_tax_action**](BillingApi.md#recalculate_invoice_tax_action) | **POST** /api/v1/billing/invoices/{invoiceId}/taxes/recalculate | Recalculate an invoice&#39;s tax amounts
[**retry_invoice_action**](BillingApi.md#retry_invoice_action) | **POST** /api/v1/billing/invoices/{invoiceId}/retry | Retry advancing the invoice after a failed attempt.
[**simulate_invoice**](BillingApi.md#simulate_invoice) | **POST** /api/v1/billing/customers/{customerId}/invoices/simulate | Simulate an invoice for a customer
[**snapshot_quantities_invoice_action**](BillingApi.md#snapshot_quantities_invoice_action) | **POST** /api/v1/billing/invoices/{invoiceId}/snapshot-quantities | Snapshot quantities for usage based line items
[**update_billing_profile**](BillingApi.md#update_billing_profile) | **PUT** /api/v1/billing/profiles/{id} | Update a billing profile
[**update_invoice**](BillingApi.md#update_invoice) | **PUT** /api/v1/billing/invoices/{invoiceId} | Update an invoice
[**update_invoice_payment_status**](BillingApi.md#update_invoice_payment_status) | **POST** /api/v1/billing/invoices/{invoiceId}/payment-status | Update invoice payment status
[**upsert_billing_profile_customer_override**](BillingApi.md#upsert_billing_profile_customer_override) | **PUT** /api/v1/billing/customers/{customerId} | Create a new or update a customer override
[**void_invoice_action**](BillingApi.md#void_invoice_action) | **POST** /api/v1/billing/invoices/{invoiceId}/void | Void an invoice


# **advance_invoice_action**
> Invoice advance_invoice_action(invoice_id)

Advance the invoice's state to the next status

Advance the invoice's state to the next status.  The call doesn't \"approve the invoice\", it only advances the invoice to the next status if the transition would be automatic.  The action can be called when the invoice's statusDetails' actions field contain the \"advance\" action.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Advance the invoice's state to the next status
        api_response = api_instance.advance_invoice_action(invoice_id)
        print("The response of BillingApi->advance_invoice_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->advance_invoice_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **approve_invoice_action**
> Invoice approve_invoice_action(invoice_id)

Send the invoice to the customer

Approve an invoice and start executing the payment workflow.  This call instantly sends the invoice to the customer using the configured billing profile app.  This call is valid in two invoice statuses: - `draft`: the invoice will be sent to the customer, the invluce state becomes issued - `manual_approval_needed`: the invoice will be sent to the customer, the invoice state becomes issued

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Send the invoice to the customer
        api_response = api_instance.approve_invoice_action(invoice_id)
        print("The response of BillingApi->approve_invoice_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->approve_invoice_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **create_billing_profile**
> BillingProfile create_billing_profile(billing_profile_create)

Create a new billing profile

Create a new billing profile  Billing profiles are representations of a customer's billing information. Customer overrides can be applied to a billing profile to customize the billing behavior for a specific customer.

### Example


```python
import moolabs
from moolabs.models.billing_profile import BillingProfile
from moolabs.models.billing_profile_create import BillingProfileCreate
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
    api_instance = moolabs.BillingApi(api_client)
    billing_profile_create = moolabs.BillingProfileCreate() # BillingProfileCreate | 

    try:
        # Create a new billing profile
        api_response = api_instance.create_billing_profile(billing_profile_create)
        print("The response of BillingApi->create_billing_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_billing_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_profile_create** | [**BillingProfileCreate**](BillingProfileCreate.md)|  | 

### Return type

[**BillingProfile**](BillingProfile.md)

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

# **create_pending_invoice_line**
> InvoicePendingLineCreateResponse create_pending_invoice_line(customer_id, invoice_pending_line_create_input)

Create pending line items

Create a new pending line item (charge).  This call is used to create a new pending line item for the customer if required a new gathering invoice will be created.  A new invoice will be created if: - there is no invoice in gathering state - the currency of the line item doesn't match the currency of any invoices in gathering state

### Example


```python
import moolabs
from moolabs.models.invoice_pending_line_create_input import InvoicePendingLineCreateInput
from moolabs.models.invoice_pending_line_create_response import InvoicePendingLineCreateResponse
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
    api_instance = moolabs.BillingApi(api_client)
    customer_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    invoice_pending_line_create_input = moolabs.InvoicePendingLineCreateInput() # InvoicePendingLineCreateInput | 

    try:
        # Create pending line items
        api_response = api_instance.create_pending_invoice_line(customer_id, invoice_pending_line_create_input)
        print("The response of BillingApi->create_pending_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->create_pending_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **invoice_pending_line_create_input** | [**InvoicePendingLineCreateInput**](InvoicePendingLineCreateInput.md)|  | 

### Return type

[**InvoicePendingLineCreateResponse**](InvoicePendingLineCreateResponse.md)

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

# **delete_billing_profile**
> delete_billing_profile(id)

Delete a billing profile

Delete a billing profile by id.  Only such billing profiles can be deleted that are: - not the default one - not pinned to any customer using customer overrides - only have finalized invoices

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
    api_instance = moolabs.BillingApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete a billing profile
        api_instance.delete_billing_profile(id)
    except Exception as e:
        print("Exception when calling BillingApi->delete_billing_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **delete_billing_profile_customer_override**
> delete_billing_profile_customer_override(customer_id)

Delete a customer override

Delete a customer override by customer id.  This will remove the customer override and the customer will be subject to the default billing profile's settings again.

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
    api_instance = moolabs.BillingApi(api_client)
    customer_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete a customer override
        api_instance.delete_billing_profile_customer_override(customer_id)
    except Exception as e:
        print("Exception when calling BillingApi->delete_billing_profile_customer_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 

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

# **delete_invoice**
> delete_invoice(invoice_id)

Delete an invoice

Delete an invoice  Only invoices that are in the draft (or earlier) status can be deleted.  Invoices that are post finalization can only be voided.

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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete an invoice
        api_instance.delete_invoice(invoice_id)
    except Exception as e:
        print("Exception when calling BillingApi->delete_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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

# **get_billing_profile**
> BillingProfile get_billing_profile(id, expand=expand)

Get a billing profile

Get a billing profile by id.  The expand option can be used to include additional information (besides the billing profile) in the response. For example by adding the expand=apps option the apps used by the billing profile will be included in the response.

### Example


```python
import moolabs
from moolabs.models.billing_profile import BillingProfile
from moolabs.models.billing_profile_expand import BillingProfileExpand
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
    api_instance = moolabs.BillingApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    expand = [moolabs.BillingProfileExpand()] # List[BillingProfileExpand] |  (optional)

    try:
        # Get a billing profile
        api_response = api_instance.get_billing_profile(id, expand=expand)
        print("The response of BillingApi->get_billing_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_billing_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **expand** | [**List[BillingProfileExpand]**](BillingProfileExpand.md)|  | [optional] 

### Return type

[**BillingProfile**](BillingProfile.md)

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

# **get_billing_profile_customer_override**
> BillingProfileCustomerOverrideWithDetails get_billing_profile_customer_override(customer_id, expand=expand)

Get a customer override

Get a customer override by customer id.  The response will include the customer override values and the merged billing profile values.  If the customer override is not found, the default billing profile's values are returned. This behavior allows for getting a merged profile regardless of the customer override existence.

### Example


```python
import moolabs
from moolabs.models.billing_profile_customer_override_expand import BillingProfileCustomerOverrideExpand
from moolabs.models.billing_profile_customer_override_with_details import BillingProfileCustomerOverrideWithDetails
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
    api_instance = moolabs.BillingApi(api_client)
    customer_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    expand = [moolabs.BillingProfileCustomerOverrideExpand()] # List[BillingProfileCustomerOverrideExpand] |  (optional)

    try:
        # Get a customer override
        api_response = api_instance.get_billing_profile_customer_override(customer_id, expand=expand)
        print("The response of BillingApi->get_billing_profile_customer_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_billing_profile_customer_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **expand** | [**List[BillingProfileCustomerOverrideExpand]**](BillingProfileCustomerOverrideExpand.md)|  | [optional] 

### Return type

[**BillingProfileCustomerOverrideWithDetails**](BillingProfileCustomerOverrideWithDetails.md)

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

# **get_invoice**
> Invoice get_invoice(invoice_id, expand=expand, include_deleted_lines=include_deleted_lines)

Get an invoice

Get an invoice by ID.  Gathering invoices will always show the current usage calculated on the fly.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
from moolabs.models.invoice_expand import InvoiceExpand
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    expand = [moolabs.InvoiceExpand()] # List[InvoiceExpand] |  (optional)
    include_deleted_lines = False # bool |  (optional) (default to False)

    try:
        # Get an invoice
        api_response = api_instance.get_invoice(invoice_id, expand=expand, include_deleted_lines=include_deleted_lines)
        print("The response of BillingApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **expand** | [**List[InvoiceExpand]**](InvoiceExpand.md)|  | [optional] 
 **include_deleted_lines** | **bool**|  | [optional] [default to False]

### Return type

[**Invoice**](Invoice.md)

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

# **invoice_pending_lines_action**
> List[Invoice] invoice_pending_lines_action(invoice_pending_lines_action_input)

Invoice a customer based on the pending line items

Create a new invoice from the pending line items.  This should be only called if for some reason we need to invoice a customer outside of the normal billing cycle.  When creating an invoice, the pending line items will be marked as invoiced and the invoice will be created with the total amount of the pending items.  New pending line items will be created for the period between now() and the next billing cycle's begining date for any metered item.  The call can return multiple invoices if the pending line items are in different currencies.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
from moolabs.models.invoice_pending_lines_action_input import InvoicePendingLinesActionInput
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_pending_lines_action_input = moolabs.InvoicePendingLinesActionInput() # InvoicePendingLinesActionInput | 

    try:
        # Invoice a customer based on the pending line items
        api_response = api_instance.invoice_pending_lines_action(invoice_pending_lines_action_input)
        print("The response of BillingApi->invoice_pending_lines_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->invoice_pending_lines_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_pending_lines_action_input** | [**InvoicePendingLinesActionInput**](InvoicePendingLinesActionInput.md)|  | 

### Return type

[**List[Invoice]**](Invoice.md)

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

# **list_billing_profile_customer_overrides**
> BillingProfileCustomerOverrideWithDetailsPaginatedResponse list_billing_profile_customer_overrides(billing_profile=billing_profile, customers_without_pinned_profile=customers_without_pinned_profile, include_all_customers=include_all_customers, customer_id=customer_id, customer_name=customer_name, customer_key=customer_key, customer_primary_email=customer_primary_email, expand=expand, order=order, order_by=order_by, page=page, page_size=page_size)

List customer overrides

List customer overrides using the specified filters.  The response will include the customer override values and the merged billing profile values.  If the includeAllCustomers is set to true, the list contains all customers. This mode is useful for getting the current effective billing workflow settings for all users regardless if they have customer orverrides or not.

### Example


```python
import moolabs
from moolabs.models.billing_profile_customer_override_expand import BillingProfileCustomerOverrideExpand
from moolabs.models.billing_profile_customer_override_order_by import BillingProfileCustomerOverrideOrderBy
from moolabs.models.billing_profile_customer_override_with_details_paginated_response import BillingProfileCustomerOverrideWithDetailsPaginatedResponse
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
    api_instance = moolabs.BillingApi(api_client)
    billing_profile = ['billing_profile_example'] # List[str] | Filter by billing profile. (optional)
    customers_without_pinned_profile = True # bool | Only return customers without pinned billing profiles. This implicitly sets includeAllCustomers to true. (optional)
    include_all_customers = True # bool | Include customers without customer overrides.  If set to false only the customers specifically associated with a billing profile will be returned.  If set to true, in case of the default billing profile, all customers will be returned. (optional) (default to True)
    customer_id = ['customer_id_example'] # List[str] | Filter by customer id. (optional)
    customer_name = 'customer_name_example' # str | Filter by customer name. (optional)
    customer_key = 'customer_key_example' # str | Filter by customer key (optional)
    customer_primary_email = 'customer_primary_email_example' # str | Filter by customer primary email (optional)
    expand = [moolabs.BillingProfileCustomerOverrideExpand()] # List[BillingProfileCustomerOverrideExpand] | Expand the response with additional details. (optional)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.BillingProfileCustomerOverrideOrderBy() # BillingProfileCustomerOverrideOrderBy | The order by field. (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)

    try:
        # List customer overrides
        api_response = api_instance.list_billing_profile_customer_overrides(billing_profile=billing_profile, customers_without_pinned_profile=customers_without_pinned_profile, include_all_customers=include_all_customers, customer_id=customer_id, customer_name=customer_name, customer_key=customer_key, customer_primary_email=customer_primary_email, expand=expand, order=order, order_by=order_by, page=page, page_size=page_size)
        print("The response of BillingApi->list_billing_profile_customer_overrides:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_billing_profile_customer_overrides: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_profile** | [**List[str]**](str.md)| Filter by billing profile. | [optional] 
 **customers_without_pinned_profile** | **bool**| Only return customers without pinned billing profiles. This implicitly sets includeAllCustomers to true. | [optional] 
 **include_all_customers** | **bool**| Include customers without customer overrides.  If set to false only the customers specifically associated with a billing profile will be returned.  If set to true, in case of the default billing profile, all customers will be returned. | [optional] [default to True]
 **customer_id** | [**List[str]**](str.md)| Filter by customer id. | [optional] 
 **customer_name** | **str**| Filter by customer name. | [optional] 
 **customer_key** | **str**| Filter by customer key | [optional] 
 **customer_primary_email** | **str**| Filter by customer primary email | [optional] 
 **expand** | [**List[BillingProfileCustomerOverrideExpand]**](BillingProfileCustomerOverrideExpand.md)| Expand the response with additional details. | [optional] 
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**BillingProfileCustomerOverrideOrderBy**](.md)| The order by field. | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]

### Return type

[**BillingProfileCustomerOverrideWithDetailsPaginatedResponse**](BillingProfileCustomerOverrideWithDetailsPaginatedResponse.md)

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

# **list_billing_profiles**
> BillingProfilePaginatedResponse list_billing_profiles(include_archived=include_archived, expand=expand, page=page, page_size=page_size, order=order, order_by=order_by)

List billing profiles

List all billing profiles matching the specified filters.  The expand option can be used to include additional information (besides the billing profile) in the response. For example by adding the expand=apps option the apps used by the billing profile will be included in the response.

### Example


```python
import moolabs
from moolabs.models.billing_profile_expand import BillingProfileExpand
from moolabs.models.billing_profile_order_by import BillingProfileOrderBy
from moolabs.models.billing_profile_paginated_response import BillingProfilePaginatedResponse
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
    api_instance = moolabs.BillingApi(api_client)
    include_archived = False # bool |  (optional) (default to False)
    expand = [moolabs.BillingProfileExpand()] # List[BillingProfileExpand] |  (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.BillingProfileOrderBy() # BillingProfileOrderBy | The order by field. (optional)

    try:
        # List billing profiles
        api_response = api_instance.list_billing_profiles(include_archived=include_archived, expand=expand, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of BillingApi->list_billing_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_billing_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_archived** | **bool**|  | [optional] [default to False]
 **expand** | [**List[BillingProfileExpand]**](BillingProfileExpand.md)|  | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**BillingProfileOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**BillingProfilePaginatedResponse**](BillingProfilePaginatedResponse.md)

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

# **list_invoices**
> InvoicePaginatedResponse list_invoices(statuses=statuses, extended_statuses=extended_statuses, issued_after=issued_after, issued_before=issued_before, period_start_after=period_start_after, period_start_before=period_start_before, created_after=created_after, created_before=created_before, expand=expand, customers=customers, include_deleted=include_deleted, page=page, page_size=page_size, order=order, order_by=order_by)

List invoices

List invoices based on the specified filters.  The expand option can be used to include additional information (besides the invoice header and totals) in the response. For example by adding the expand=lines option the invoice lines will be included in the response.  Gathering invoices will always show the current usage calculated on the fly.

### Example


```python
import moolabs
from moolabs.models.invoice_expand import InvoiceExpand
from moolabs.models.invoice_order_by import InvoiceOrderBy
from moolabs.models.invoice_paginated_response import InvoicePaginatedResponse
from moolabs.models.invoice_status import InvoiceStatus
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
    api_instance = moolabs.BillingApi(api_client)
    statuses = [moolabs.InvoiceStatus()] # List[InvoiceStatus] | Filter by the invoice status. (optional)
    extended_statuses = ['extended_statuses_example'] # List[str] | Filter by invoice extended statuses (optional)
    issued_after = '2023-01-01T01:01:01.001Z' # datetime | Filter by invoice issued time. Inclusive. (optional)
    issued_before = '2023-01-01T01:01:01.001Z' # datetime | Filter by invoice issued time. Inclusive. (optional)
    period_start_after = '2023-01-01T01:01:01.001Z' # datetime | Filter by period start time. Inclusive. (optional)
    period_start_before = '2023-01-01T01:01:01.001Z' # datetime | Filter by period start time. Inclusive. (optional)
    created_after = '2023-01-01T01:01:01.001Z' # datetime | Filter by invoice created time. Inclusive. (optional)
    created_before = '2023-01-01T01:01:01.001Z' # datetime | Filter by invoice created time. Inclusive. (optional)
    expand = [moolabs.InvoiceExpand()] # List[InvoiceExpand] | What parts of the list output to expand in listings (optional)
    customers = ['customers_example'] # List[str] | Filter by customer ID (optional)
    include_deleted = True # bool | Include deleted invoices (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.InvoiceOrderBy() # InvoiceOrderBy | The order by field. (optional)

    try:
        # List invoices
        api_response = api_instance.list_invoices(statuses=statuses, extended_statuses=extended_statuses, issued_after=issued_after, issued_before=issued_before, period_start_after=period_start_after, period_start_before=period_start_before, created_after=created_after, created_before=created_before, expand=expand, customers=customers, include_deleted=include_deleted, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of BillingApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statuses** | [**List[InvoiceStatus]**](InvoiceStatus.md)| Filter by the invoice status. | [optional] 
 **extended_statuses** | [**List[str]**](str.md)| Filter by invoice extended statuses | [optional] 
 **issued_after** | **datetime**| Filter by invoice issued time. Inclusive. | [optional] 
 **issued_before** | **datetime**| Filter by invoice issued time. Inclusive. | [optional] 
 **period_start_after** | **datetime**| Filter by period start time. Inclusive. | [optional] 
 **period_start_before** | **datetime**| Filter by period start time. Inclusive. | [optional] 
 **created_after** | **datetime**| Filter by invoice created time. Inclusive. | [optional] 
 **created_before** | **datetime**| Filter by invoice created time. Inclusive. | [optional] 
 **expand** | [**List[InvoiceExpand]**](InvoiceExpand.md)| What parts of the list output to expand in listings | [optional] 
 **customers** | [**List[str]**](str.md)| Filter by customer ID | [optional] 
 **include_deleted** | **bool**| Include deleted invoices | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**InvoiceOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**InvoicePaginatedResponse**](InvoicePaginatedResponse.md)

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

# **recalculate_invoice_tax_action**
> Invoice recalculate_invoice_tax_action(invoice_id)

Recalculate an invoice's tax amounts

Recalculate an invoice's tax amounts (using the app set in the customer's billing profile)  Note: charges might apply, depending on the tax provider.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Recalculate an invoice's tax amounts
        api_response = api_instance.recalculate_invoice_tax_action(invoice_id)
        print("The response of BillingApi->recalculate_invoice_tax_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->recalculate_invoice_tax_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **retry_invoice_action**
> Invoice retry_invoice_action(invoice_id)

Retry advancing the invoice after a failed attempt.

Retry advancing the invoice after a failed attempt.  The action can be called when the invoice's statusDetails' actions field contain the \"retry\" action.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Retry advancing the invoice after a failed attempt.
        api_response = api_instance.retry_invoice_action(invoice_id)
        print("The response of BillingApi->retry_invoice_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->retry_invoice_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **simulate_invoice**
> Invoice simulate_invoice(customer_id, invoice_simulation_input)

Simulate an invoice for a customer

Simulate an invoice for a customer.  This call will simulate an invoice for a customer based on the pending line items.  The call will return the total amount of the invoice and the line items that will be included in the invoice.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
from moolabs.models.invoice_simulation_input import InvoiceSimulationInput
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
    api_instance = moolabs.BillingApi(api_client)
    customer_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    invoice_simulation_input = moolabs.InvoiceSimulationInput() # InvoiceSimulationInput | 

    try:
        # Simulate an invoice for a customer
        api_response = api_instance.simulate_invoice(customer_id, invoice_simulation_input)
        print("The response of BillingApi->simulate_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->simulate_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **invoice_simulation_input** | [**InvoiceSimulationInput**](InvoiceSimulationInput.md)|  | 

### Return type

[**Invoice**](Invoice.md)

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
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_quantities_invoice_action**
> Invoice snapshot_quantities_invoice_action(invoice_id)

Snapshot quantities for usage based line items

Snapshot quantities for usage based line items.  This call will snapshot the quantities for all usage based line items in the invoice.  This call is only valid in `draft.waiting_for_collection` status, where the collection period can be skipped using this action.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Snapshot quantities for usage based line items
        api_response = api_instance.snapshot_quantities_invoice_action(invoice_id)
        print("The response of BillingApi->snapshot_quantities_invoice_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->snapshot_quantities_invoice_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **update_billing_profile**
> BillingProfile update_billing_profile(id, billing_profile_replace_update_with_workflow)

Update a billing profile

Update a billing profile by id.  The apps field cannot be updated directly, if an app change is desired a new profile should be created.

### Example


```python
import moolabs
from moolabs.models.billing_profile import BillingProfile
from moolabs.models.billing_profile_replace_update_with_workflow import BillingProfileReplaceUpdateWithWorkflow
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
    api_instance = moolabs.BillingApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    billing_profile_replace_update_with_workflow = moolabs.BillingProfileReplaceUpdateWithWorkflow() # BillingProfileReplaceUpdateWithWorkflow | 

    try:
        # Update a billing profile
        api_response = api_instance.update_billing_profile(id, billing_profile_replace_update_with_workflow)
        print("The response of BillingApi->update_billing_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_billing_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **billing_profile_replace_update_with_workflow** | [**BillingProfileReplaceUpdateWithWorkflow**](BillingProfileReplaceUpdateWithWorkflow.md)|  | 

### Return type

[**BillingProfile**](BillingProfile.md)

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

# **update_invoice**
> Invoice update_invoice(invoice_id, invoice_replace_update)

Update an invoice

Update an invoice  Only invoices in draft or earlier status can be updated.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
from moolabs.models.invoice_replace_update import InvoiceReplaceUpdate
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    invoice_replace_update = moolabs.InvoiceReplaceUpdate() # InvoiceReplaceUpdate | 

    try:
        # Update an invoice
        api_response = api_instance.update_invoice(invoice_id, invoice_replace_update)
        print("The response of BillingApi->update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **invoice_replace_update** | [**InvoiceReplaceUpdate**](InvoiceReplaceUpdate.md)|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **update_invoice_payment_status**
> Invoice update_invoice_payment_status(invoice_id, custom_invoicing_update_payment_status_request)

Update invoice payment status

Update the payment status of an invoice managed by the custom invoicing app.

### Example


```python
import moolabs
from moolabs.models.custom_invoicing_update_payment_status_request import CustomInvoicingUpdatePaymentStatusRequest
from moolabs.models.invoice import Invoice
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    custom_invoicing_update_payment_status_request = moolabs.CustomInvoicingUpdatePaymentStatusRequest() # CustomInvoicingUpdatePaymentStatusRequest | 

    try:
        # Update invoice payment status
        api_response = api_instance.update_invoice_payment_status(invoice_id, custom_invoicing_update_payment_status_request)
        print("The response of BillingApi->update_invoice_payment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->update_invoice_payment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **custom_invoicing_update_payment_status_request** | [**CustomInvoicingUpdatePaymentStatusRequest**](CustomInvoicingUpdatePaymentStatusRequest.md)|  | 

### Return type

[**Invoice**](Invoice.md)

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

# **upsert_billing_profile_customer_override**
> BillingProfileCustomerOverrideWithDetails upsert_billing_profile_customer_override(customer_id, billing_profile_customer_override_create)

Create a new or update a customer override

The customer override can be used to pin a given customer to a billing profile different from the default one.  This can be used to test the effect of different billing profiles before making them the default ones or have different workflow settings for example for enterprise customers.

### Example


```python
import moolabs
from moolabs.models.billing_profile_customer_override_create import BillingProfileCustomerOverrideCreate
from moolabs.models.billing_profile_customer_override_with_details import BillingProfileCustomerOverrideWithDetails
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
    api_instance = moolabs.BillingApi(api_client)
    customer_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    billing_profile_customer_override_create = moolabs.BillingProfileCustomerOverrideCreate() # BillingProfileCustomerOverrideCreate | 

    try:
        # Create a new or update a customer override
        api_response = api_instance.upsert_billing_profile_customer_override(customer_id, billing_profile_customer_override_create)
        print("The response of BillingApi->upsert_billing_profile_customer_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->upsert_billing_profile_customer_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**|  | 
 **billing_profile_customer_override_create** | [**BillingProfileCustomerOverrideCreate**](BillingProfileCustomerOverrideCreate.md)|  | 

### Return type

[**BillingProfileCustomerOverrideWithDetails**](BillingProfileCustomerOverrideWithDetails.md)

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

# **void_invoice_action**
> Invoice void_invoice_action(invoice_id, void_invoice_action_input)

Void an invoice

Void an invoice  Only invoices that have been alread issued can be voided.  Voiding an invoice will mark it as voided, the user can specify how to handle the voided line items.

### Example


```python
import moolabs
from moolabs.models.invoice import Invoice
from moolabs.models.void_invoice_action_input import VoidInvoiceActionInput
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
    api_instance = moolabs.BillingApi(api_client)
    invoice_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    void_invoice_action_input = moolabs.VoidInvoiceActionInput() # VoidInvoiceActionInput | 

    try:
        # Void an invoice
        api_response = api_instance.void_invoice_action(invoice_id, void_invoice_action_input)
        print("The response of BillingApi->void_invoice_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->void_invoice_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **void_invoice_action_input** | [**VoidInvoiceActionInput**](VoidInvoiceActionInput.md)|  | 

### Return type

[**Invoice**](Invoice.md)

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

