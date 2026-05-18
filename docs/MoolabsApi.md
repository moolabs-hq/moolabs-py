# moolabs.MoolabsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credit**](MoolabsApi.md#create_credit) | **POST** /v1/moolabs/credits | Create Credit
[**get_credits**](MoolabsApi.md#get_credits) | **GET** /v1/moolabs/credits | Get Credits
[**get_credits_issued_aggregate_v1**](MoolabsApi.md#get_credits_issued_aggregate_v1) | **GET** /v1/moolabs/credits-issued/aggregate | Get Credits Issued Aggregate
[**get_credits_issued_v1**](MoolabsApi.md#get_credits_issued_v1) | **GET** /v1/moolabs/credits-issued | Get Credits Issued


# **create_credit**
> object create_credit(create_credit_request)

Create Credit

Create a new credit note.  This creates a journal entry with entry_type=CREDIT_NOTE that represents a credit memo or invoice adjustment.  TODO: Full implementation requires: - Resolving tenant_id/pool_id from customerId - Finding the customer's wallet - Creating journal entry and postings - Handling currency conversion if needed

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_credit_request import CreateCreditRequest
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
    api_instance = moolabs.MoolabsApi(api_client)
    create_credit_request = moolabs.CreateCreditRequest() # CreateCreditRequest | 

    try:
        # Create Credit
        api_response = api_instance.create_credit(create_credit_request)
        print("The response of MoolabsApi->create_credit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoolabsApi->create_credit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_credit_request** | [**CreateCreditRequest**](CreateCreditRequest.md)|  | 

### Return type

**object**

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

# **get_credits**
> object get_credits(customer_id=customer_id, invoice_id=invoice_id)

Get Credits

Get credit notes for a customer or invoice.  Returns credit notes (journal entries with entry_type=CREDIT_NOTE) that represent invoice adjustments or credit memos.

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
    api_instance = moolabs.MoolabsApi(api_client)
    customer_id = 'customer_id_example' # str | Customer ID to filter by (optional)
    invoice_id = 'invoice_id_example' # str | Invoice ID to filter by (optional)

    try:
        # Get Credits
        api_response = api_instance.get_credits(customer_id=customer_id, invoice_id=invoice_id)
        print("The response of MoolabsApi->get_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoolabsApi->get_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer ID to filter by | [optional] 
 **invoice_id** | **str**| Invoice ID to filter by | [optional] 

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

# **get_credits_issued_aggregate_v1**
> object get_credits_issued_aggregate_v1(from_date=from_date, to_date=to_date)

Get Credits Issued Aggregate

Get aggregated credits issued (grants/mints) for all customers.  OPTIMIZED: Uses direct SQL aggregation instead of loading entries into memory. This is much faster and scales better with large datasets.  Query Parameters: - fromDate: Start date (ISO format, optional, defaults to start of current month) - toDate: End date (ISO format, optional, defaults to now)

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
    api_instance = moolabs.MoolabsApi(api_client)
    from_date = 'from_date_example' # str | Start date (ISO format) - defaults to start of current month (optional)
    to_date = 'to_date_example' # str | End date (ISO format) - defaults to now (optional)

    try:
        # Get Credits Issued Aggregate
        api_response = api_instance.get_credits_issued_aggregate_v1(from_date=from_date, to_date=to_date)
        print("The response of MoolabsApi->get_credits_issued_aggregate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoolabsApi->get_credits_issued_aggregate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **str**| Start date (ISO format) - defaults to start of current month | [optional] 
 **to_date** | **str**| End date (ISO format) - defaults to now | [optional] 

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

# **get_credits_issued_v1**
> object get_credits_issued_v1(customer_id=customer_id, from_date=from_date, to_date=to_date)

Get Credits Issued

Get credits issued (grants/mints) for a customer.  Returns grants and credit mints (journal entries with entry_type in ['GRANT', 'CREDIT_MINT']) that represent credits issued to customers. This is different from credit notes, which are invoice adjustments.  Query Parameters: - customerId: Filter by customer ID (subject_id) - fromDate: Start date (ISO format, optional, defaults to start of current month) - toDate: End date (ISO format, optional, defaults to now)

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
    api_instance = moolabs.MoolabsApi(api_client)
    customer_id = 'customer_id_example' # str | Customer ID (subject_id) to filter by (optional)
    from_date = 'from_date_example' # str | Start date (ISO format) - defaults to start of current month (optional)
    to_date = 'to_date_example' # str | End date (ISO format) - defaults to now (optional)

    try:
        # Get Credits Issued
        api_response = api_instance.get_credits_issued_v1(customer_id=customer_id, from_date=from_date, to_date=to_date)
        print("The response of MoolabsApi->get_credits_issued_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoolabsApi->get_credits_issued_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer ID (subject_id) to filter by | [optional] 
 **from_date** | **str**| Start date (ISO format) - defaults to start of current month | [optional] 
 **to_date** | **str**| End date (ISO format) - defaults to now | [optional] 

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

