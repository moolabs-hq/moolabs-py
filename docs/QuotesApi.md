# moolabs.QuotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_approver_v1**](QuotesApi.md#delete_approver_v1) | **DELETE** /v1/quotes/approver-directory/{user_ref} | Delete Approver
[**delete_territory**](QuotesApi.md#delete_territory) | **DELETE** /v1/quotes/territories/{key} | Delete Territory
[**get_approval_levels_v1**](QuotesApi.md#get_approval_levels_v1) | **GET** /v1/quotes/approval-levels | Get Approval Levels
[**get_approver_directory_v1**](QuotesApi.md#get_approver_directory_v1) | **GET** /v1/quotes/approver-directory | Get Approver Directory
[**get_latest_quote_contract_upload_v1**](QuotesApi.md#get_latest_quote_contract_upload_v1) | **GET** /v1/quotes/{quote_id}/contract-uploads/latest | Get Latest Quote Contract Upload
[**get_pricing_snapshot_v1**](QuotesApi.md#get_pricing_snapshot_v1) | **GET** /v1/quotes/pricing-snapshots/{snapshot_id} | Get Pricing Snapshot
[**get_quote**](QuotesApi.md#get_quote) | **GET** /v1/quotes/{quote_id} | Get Quote
[**get_quote_contract_pdf_v1**](QuotesApi.md#get_quote_contract_pdf_v1) | **GET** /v1/quotes/{quote_id}/contract.pdf | Get Quote Contract Pdf
[**get_quote_settings**](QuotesApi.md#get_quote_settings) | **GET** /v1/quotes/settings | Get Quote Settings
[**get_quote_version**](QuotesApi.md#get_quote_version) | **GET** /v1/quotes/{quote_id}/versions/{version} | Get Quote Version
[**get_rate_cards_v1**](QuotesApi.md#get_rate_cards_v1) | **GET** /v1/rate-cards | Get Rate Cards
[**get_territories**](QuotesApi.md#get_territories) | **GET** /v1/quotes/territories | Get Territories
[**list_quote_activation_failures_v1**](QuotesApi.md#list_quote_activation_failures_v1) | **GET** /v1/quotes/activation-failures | List Quote Activation Failures
[**list_quote_agent_cards_v1**](QuotesApi.md#list_quote_agent_cards_v1) | **GET** /v1/quotes/{quote_id}/agent-cards | List Quote Agent Cards
[**list_quote_agent_runs_v1**](QuotesApi.md#list_quote_agent_runs_v1) | **GET** /v1/quotes/{quote_id}/agent-runs | List Quote Agent Runs
[**list_quote_redlines**](QuotesApi.md#list_quote_redlines) | **GET** /v1/quotes/{quote_id}/redlines | List Quote Redlines
[**list_quotes**](QuotesApi.md#list_quotes) | **GET** /v1/quotes | List Quotes
[**patch_rate_card_cost_v1**](QuotesApi.md#patch_rate_card_cost_v1) | **PATCH** /v1/rate-cards/{rate_card_id}/cost | Patch Rate Card Cost
[**post_quote**](QuotesApi.md#post_quote) | **POST** /v1/quotes | Post Quote
[**post_quote_accept**](QuotesApi.md#post_quote_accept) | **POST** /v1/quotes/{quote_id}/accept | Post Quote Accept
[**post_quote_activate**](QuotesApi.md#post_quote_activate) | **POST** /v1/quotes/{quote_id}/activate | Post Quote Activate
[**post_quote_approve**](QuotesApi.md#post_quote_approve) | **POST** /v1/quotes/{quote_id}/approve | Post Quote Approve
[**post_quote_contract_upload_v1**](QuotesApi.md#post_quote_contract_upload_v1) | **POST** /v1/quotes/{quote_id}/contract-uploads | Post Quote Contract Upload
[**post_quote_lock**](QuotesApi.md#post_quote_lock) | **POST** /v1/quotes/{quote_id}/lock | Post Quote Lock
[**post_quote_redline**](QuotesApi.md#post_quote_redline) | **POST** /v1/quotes/{quote_id}/redlines | Post Quote Redline
[**post_quote_redline_accept**](QuotesApi.md#post_quote_redline_accept) | **POST** /v1/quotes/{quote_id}/redlines/{redline_id}/accept | Post Quote Redline Accept
[**post_quote_redline_reject**](QuotesApi.md#post_quote_redline_reject) | **POST** /v1/quotes/{quote_id}/redlines/{redline_id}/reject | Post Quote Redline Reject
[**post_quote_redlines_first_pass_v1**](QuotesApi.md#post_quote_redlines_first_pass_v1) | **POST** /v1/quotes/{quote_id}/redlines/first-pass | Post Quote Redlines First Pass
[**post_quote_reject**](QuotesApi.md#post_quote_reject) | **POST** /v1/quotes/{quote_id}/reject | Post Quote Reject
[**post_quote_send**](QuotesApi.md#post_quote_send) | **POST** /v1/quotes/{quote_id}/send | Post Quote Send
[**post_quote_session**](QuotesApi.md#post_quote_session) | **POST** /v1/quotes/{quote_id}/sessions | Post Quote Session
[**post_quote_signing_webhook**](QuotesApi.md#post_quote_signing_webhook) | **POST** /v1/quotes/signing/webhooks/{provider} | Post Quote Signing Webhook
[**post_quote_submit_approval_v1**](QuotesApi.md#post_quote_submit_approval_v1) | **POST** /v1/quotes/{quote_id}/submit-approval | Post Quote Submit Approval
[**post_quote_unlock**](QuotesApi.md#post_quote_unlock) | **POST** /v1/quotes/{quote_id}/unlock | Post Quote Unlock
[**put_approval_levels_v1**](QuotesApi.md#put_approval_levels_v1) | **PUT** /v1/quotes/approval-levels | Put Approval Levels
[**put_approver_v1**](QuotesApi.md#put_approver_v1) | **PUT** /v1/quotes/approver-directory/{user_ref} | Put Approver
[**put_quote_settings**](QuotesApi.md#put_quote_settings) | **PUT** /v1/quotes/settings | Put Quote Settings
[**put_territory**](QuotesApi.md#put_territory) | **PUT** /v1/quotes/territories/{key} | Put Territory
[**sync_approver_directory_v1**](QuotesApi.md#sync_approver_directory_v1) | **POST** /v1/quotes/approver-directory/sync | Sync Approver Directory


# **delete_approver_v1**
> object delete_approver_v1(user_ref)

Delete Approver

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
    api_instance = moolabs.QuotesApi(api_client)
    user_ref = 'user_ref_example' # str | 

    try:
        # Delete Approver
        api_response = api_instance.delete_approver_v1(user_ref)
        print("The response of QuotesApi->delete_approver_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->delete_approver_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ref** | **str**|  | 

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

# **delete_territory**
> object delete_territory(key)

Delete Territory

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
    api_instance = moolabs.QuotesApi(api_client)
    key = 'key_example' # str | 

    try:
        # Delete Territory
        api_response = api_instance.delete_territory(key)
        print("The response of QuotesApi->delete_territory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->delete_territory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

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

# **get_approval_levels_v1**
> object get_approval_levels_v1()

Get Approval Levels

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
    api_instance = moolabs.QuotesApi(api_client)

    try:
        # Get Approval Levels
        api_response = api_instance.get_approval_levels_v1()
        print("The response of QuotesApi->get_approval_levels_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_approval_levels_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approver_directory_v1**
> object get_approver_directory_v1(level_key=level_key, territory_key=territory_key)

Get Approver Directory

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
    api_instance = moolabs.QuotesApi(api_client)
    level_key = 'level_key_example' # str |  (optional)
    territory_key = 'territory_key_example' # str |  (optional)

    try:
        # Get Approver Directory
        api_response = api_instance.get_approver_directory_v1(level_key=level_key, territory_key=territory_key)
        print("The response of QuotesApi->get_approver_directory_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_approver_directory_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level_key** | **str**|  | [optional] 
 **territory_key** | **str**|  | [optional] 

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

# **get_latest_quote_contract_upload_v1**
> ContractUploadDetailResponse get_latest_quote_contract_upload_v1(quote_id)

Get Latest Quote Contract Upload

Return the most-recent contract upload for a quote.  Returns the full extracted_text and segments so the UI can render an inline document-review view with clause highlights.  Gated by require_quotes_enabled (same as every other /quotes route) and validates quote ownership via service.get_quote (raises 404 if the quote doesn't exist or belongs to a different tenant).  Returns 404 ``{\"detail\": \"no contract uploaded for this quote\"}`` when no upload row exists.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.contract_upload_detail_response import ContractUploadDetailResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Latest Quote Contract Upload
        api_response = api_instance.get_latest_quote_contract_upload_v1(quote_id)
        print("The response of QuotesApi->get_latest_quote_contract_upload_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_latest_quote_contract_upload_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

### Return type

[**ContractUploadDetailResponse**](ContractUploadDetailResponse.md)

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

# **get_pricing_snapshot_v1**
> PricingSnapshotResponse get_pricing_snapshot_v1(snapshot_id)

Get Pricing Snapshot

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.pricing_snapshot_response import PricingSnapshotResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | 

    try:
        # Get Pricing Snapshot
        api_response = api_instance.get_pricing_snapshot_v1(snapshot_id)
        print("The response of QuotesApi->get_pricing_snapshot_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_pricing_snapshot_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**|  | 

### Return type

[**PricingSnapshotResponse**](PricingSnapshotResponse.md)

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

# **get_quote**
> QuoteResponse get_quote(quote_id)

Get Quote

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_response import QuoteResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Quote
        api_response = api_instance.get_quote(quote_id)
        print("The response of QuotesApi->get_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

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

# **get_quote_contract_pdf_v1**
> object get_quote_contract_pdf_v1(quote_id)

Get Quote Contract Pdf

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Quote Contract Pdf
        api_response = api_instance.get_quote_contract_pdf_v1(quote_id)
        print("The response of QuotesApi->get_quote_contract_pdf_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_contract_pdf_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

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

# **get_quote_settings**
> QuoteSettingsResponse get_quote_settings()

Get Quote Settings

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_settings_response import QuoteSettingsResponse
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
    api_instance = moolabs.QuotesApi(api_client)

    try:
        # Get Quote Settings
        api_response = api_instance.get_quote_settings()
        print("The response of QuotesApi->get_quote_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**QuoteSettingsResponse**](QuoteSettingsResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quote_version**
> QuoteVersionResponse get_quote_version(quote_id, version)

Get Quote Version

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    version = 56 # int | 

    try:
        # Get Quote Version
        api_response = api_instance.get_quote_version(quote_id, version)
        print("The response of QuotesApi->get_quote_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_quote_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **version** | **int**|  | 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

# **get_rate_cards_v1**
> RateCardCostListResponse get_rate_cards_v1()

Get Rate Cards

List the tenant's current rate cards with cost + per-unit margin (rep+).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_card_cost_list_response import RateCardCostListResponse
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
    api_instance = moolabs.QuotesApi(api_client)

    try:
        # Get Rate Cards
        api_response = api_instance.get_rate_cards_v1()
        print("The response of QuotesApi->get_rate_cards_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_rate_cards_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RateCardCostListResponse**](RateCardCostListResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_territories**
> object get_territories()

Get Territories

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
    api_instance = moolabs.QuotesApi(api_client)

    try:
        # Get Territories
        api_response = api_instance.get_territories()
        print("The response of QuotesApi->get_territories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->get_territories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quote_activation_failures_v1**
> object list_quote_activation_failures_v1(limit=limit, offset=offset)

List Quote Activation Failures

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
    api_instance = moolabs.QuotesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Quote Activation Failures
        api_response = api_instance.list_quote_activation_failures_v1(limit=limit, offset=offset)
        print("The response of QuotesApi->list_quote_activation_failures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quote_activation_failures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

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

# **list_quote_agent_cards_v1**
> object list_quote_agent_cards_v1(quote_id, quote_version=quote_version, limit=limit, offset=offset)

List Quote Agent Cards

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    quote_version = 56 # int |  (optional)
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Quote Agent Cards
        api_response = api_instance.list_quote_agent_cards_v1(quote_id, quote_version=quote_version, limit=limit, offset=offset)
        print("The response of QuotesApi->list_quote_agent_cards_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quote_agent_cards_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **quote_version** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

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

# **list_quote_agent_runs_v1**
> List[QuoteAgentProvenanceRunResponse] list_quote_agent_runs_v1(quote_id, quote_version=quote_version, limit=limit, offset=offset)

List Quote Agent Runs

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_agent_provenance_run_response import QuoteAgentProvenanceRunResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    quote_version = 56 # int |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Quote Agent Runs
        api_response = api_instance.list_quote_agent_runs_v1(quote_id, quote_version=quote_version, limit=limit, offset=offset)
        print("The response of QuotesApi->list_quote_agent_runs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quote_agent_runs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **quote_version** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[QuoteAgentProvenanceRunResponse]**](QuoteAgentProvenanceRunResponse.md)

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

# **list_quote_redlines**
> List[QuoteRedlineResponse] list_quote_redlines(quote_id, status=status, limit=limit, offset=offset)

List Quote Redlines

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_redline_response import QuoteRedlineResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    status = 'status_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Quote Redlines
        api_response = api_instance.list_quote_redlines(quote_id, status=status, limit=limit, offset=offset)
        print("The response of QuotesApi->list_quote_redlines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quote_redlines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[QuoteRedlineResponse]**](QuoteRedlineResponse.md)

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

# **list_quotes**
> QuoteListResponse list_quotes(limit=limit, offset=offset, state=state)

List Quotes

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_list_response import QuoteListResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    state = 'state_example' # str |  (optional)

    try:
        # List Quotes
        api_response = api_instance.list_quotes(limit=limit, offset=offset, state=state)
        print("The response of QuotesApi->list_quotes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->list_quotes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **state** | **str**|  | [optional] 

### Return type

[**QuoteListResponse**](QuoteListResponse.md)

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

# **patch_rate_card_cost_v1**
> RateCardCostRow patch_rate_card_cost_v1(rate_card_id, set_rate_card_cost_request)

Patch Rate Card Cost

Set per-unit cost + provenance on a rate card. Finance-gated, audited.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.rate_card_cost_row import RateCardCostRow
from moolabs.models.set_rate_card_cost_request import SetRateCardCostRequest
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
    api_instance = moolabs.QuotesApi(api_client)
    rate_card_id = 'rate_card_id_example' # str | 
    set_rate_card_cost_request = moolabs.SetRateCardCostRequest() # SetRateCardCostRequest | 

    try:
        # Patch Rate Card Cost
        api_response = api_instance.patch_rate_card_cost_v1(rate_card_id, set_rate_card_cost_request)
        print("The response of QuotesApi->patch_rate_card_cost_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->patch_rate_card_cost_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **str**|  | 
 **set_rate_card_cost_request** | [**SetRateCardCostRequest**](SetRateCardCostRequest.md)|  | 

### Return type

[**RateCardCostRow**](RateCardCostRow.md)

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

# **post_quote**
> QuoteResponse post_quote(create_quote_request, idempotency_key=idempotency_key)

Post Quote

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_quote_request import CreateQuoteRequest
from moolabs.models.quote_response import QuoteResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    create_quote_request = moolabs.CreateQuoteRequest() # CreateQuoteRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote
        api_response = api_instance.post_quote(create_quote_request, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_quote_request** | [**CreateQuoteRequest**](CreateQuoteRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_accept**
> object post_quote_accept(quote_id, idempotency_key=idempotency_key, signed_document=signed_document, buyer_signer_ref=buyer_signer_ref, verified_by_ref=verified_by_ref, seller_signer_ref=seller_signer_ref)

Post Quote Accept

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    signed_document = None # bytearray |  (optional)
    buyer_signer_ref = 'buyer_signer_ref_example' # str |  (optional)
    verified_by_ref = 'verified_by_ref_example' # str |  (optional)
    seller_signer_ref = 'seller_signer_ref_example' # str |  (optional)

    try:
        # Post Quote Accept
        api_response = api_instance.post_quote_accept(quote_id, idempotency_key=idempotency_key, signed_document=signed_document, buyer_signer_ref=buyer_signer_ref, verified_by_ref=verified_by_ref, seller_signer_ref=seller_signer_ref)
        print("The response of QuotesApi->post_quote_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_accept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **signed_document** | **bytearray**|  | [optional] 
 **buyer_signer_ref** | **str**|  | [optional] 
 **verified_by_ref** | **str**|  | [optional] 
 **seller_signer_ref** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_activate**
> object post_quote_activate(quote_id, idempotency_key=idempotency_key)

Post Quote Activate

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Activate
        api_response = api_instance.post_quote_activate(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

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

# **post_quote_approve**
> QuoteApprovalResponse post_quote_approve(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)

Post Quote Approve

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_approval_decision_request import QuoteApprovalDecisionRequest
from moolabs.models.quote_approval_response import QuoteApprovalResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    quote_approval_decision_request = moolabs.QuoteApprovalDecisionRequest() # QuoteApprovalDecisionRequest |  (optional)

    try:
        # Post Quote Approve
        api_response = api_instance.post_quote_approve(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)
        print("The response of QuotesApi->post_quote_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_approve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **quote_approval_decision_request** | [**QuoteApprovalDecisionRequest**](QuoteApprovalDecisionRequest.md)|  | [optional] 

### Return type

[**QuoteApprovalResponse**](QuoteApprovalResponse.md)

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

# **post_quote_contract_upload_v1**
> object post_quote_contract_upload_v1(quote_id, file)

Post Quote Contract Upload

Upload a contract document scoped to a specific quote.  Requires the quotes feature flag (via require_quotes_enabled) and validates that the quote belongs to the authenticated tenant before ingesting.

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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    file = None # bytearray | 

    try:
        # Post Quote Contract Upload
        api_response = api_instance.post_quote_contract_upload_v1(quote_id, file)
        print("The response of QuotesApi->post_quote_contract_upload_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_contract_upload_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_lock**
> QuoteVersionResponse post_quote_lock(quote_id, idempotency_key=idempotency_key)

Post Quote Lock

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Lock
        api_response = api_instance.post_quote_lock(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_lock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

# **post_quote_redline**
> QuoteRedlineResponse post_quote_redline(quote_id, create_quote_redline_request, idempotency_key=idempotency_key)

Post Quote Redline

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_quote_redline_request import CreateQuoteRedlineRequest
from moolabs.models.quote_redline_response import QuoteRedlineResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    create_quote_redline_request = moolabs.CreateQuoteRedlineRequest() # CreateQuoteRedlineRequest | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Redline
        api_response = api_instance.post_quote_redline(quote_id, create_quote_redline_request, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_redline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_redline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **create_quote_redline_request** | [**CreateQuoteRedlineRequest**](CreateQuoteRedlineRequest.md)|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteRedlineResponse**](QuoteRedlineResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_redline_accept**
> QuoteVersionResponse post_quote_redline_accept(quote_id, redline_id, idempotency_key=idempotency_key)

Post Quote Redline Accept

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    redline_id = 'redline_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Redline Accept
        api_response = api_instance.post_quote_redline_accept(quote_id, redline_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_redline_accept:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_redline_accept: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **redline_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

# **post_quote_redline_reject**
> QuoteRedlineResponse post_quote_redline_reject(quote_id, redline_id, idempotency_key=idempotency_key, quote_redline_decision_request=quote_redline_decision_request)

Post Quote Redline Reject

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_redline_decision_request import QuoteRedlineDecisionRequest
from moolabs.models.quote_redline_response import QuoteRedlineResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    redline_id = 'redline_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    quote_redline_decision_request = moolabs.QuoteRedlineDecisionRequest() # QuoteRedlineDecisionRequest |  (optional)

    try:
        # Post Quote Redline Reject
        api_response = api_instance.post_quote_redline_reject(quote_id, redline_id, idempotency_key=idempotency_key, quote_redline_decision_request=quote_redline_decision_request)
        print("The response of QuotesApi->post_quote_redline_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_redline_reject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **redline_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **quote_redline_decision_request** | [**QuoteRedlineDecisionRequest**](QuoteRedlineDecisionRequest.md)|  | [optional] 

### Return type

[**QuoteRedlineResponse**](QuoteRedlineResponse.md)

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

# **post_quote_redlines_first_pass_v1**
> FirstPassRedlineResponse post_quote_redlines_first_pass_v1(quote_id, first_pass_redline_request=first_pass_redline_request)

Post Quote Redlines First Pass

Run the first-pass clause-anchored redline agent against the uploaded contract.  Idempotent: calling twice for the same (quote, version) returns the same redlines without duplicating rows.  Returns 201 with the count and IDs of the redlines that were created (or already existed from a prior first-pass).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.first_pass_redline_request import FirstPassRedlineRequest
from moolabs.models.first_pass_redline_response import FirstPassRedlineResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    first_pass_redline_request = moolabs.FirstPassRedlineRequest() # FirstPassRedlineRequest |  (optional)

    try:
        # Post Quote Redlines First Pass
        api_response = api_instance.post_quote_redlines_first_pass_v1(quote_id, first_pass_redline_request=first_pass_redline_request)
        print("The response of QuotesApi->post_quote_redlines_first_pass_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_redlines_first_pass_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **first_pass_redline_request** | [**FirstPassRedlineRequest**](FirstPassRedlineRequest.md)|  | [optional] 

### Return type

[**FirstPassRedlineResponse**](FirstPassRedlineResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_reject**
> QuoteApprovalResponse post_quote_reject(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)

Post Quote Reject

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_approval_decision_request import QuoteApprovalDecisionRequest
from moolabs.models.quote_approval_response import QuoteApprovalResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)
    quote_approval_decision_request = moolabs.QuoteApprovalDecisionRequest() # QuoteApprovalDecisionRequest |  (optional)

    try:
        # Post Quote Reject
        api_response = api_instance.post_quote_reject(quote_id, idempotency_key=idempotency_key, quote_approval_decision_request=quote_approval_decision_request)
        print("The response of QuotesApi->post_quote_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_reject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 
 **quote_approval_decision_request** | [**QuoteApprovalDecisionRequest**](QuoteApprovalDecisionRequest.md)|  | [optional] 

### Return type

[**QuoteApprovalResponse**](QuoteApprovalResponse.md)

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

# **post_quote_send**
> QuoteResponse post_quote_send(quote_id, idempotency_key=idempotency_key)

Post Quote Send

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_response import QuoteResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Send
        api_response = api_instance.post_quote_send(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_send:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_send: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteResponse**](QuoteResponse.md)

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

# **post_quote_session**
> CreateSessionResponse post_quote_session(quote_id, idempotency_key=idempotency_key)

Post Quote Session

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_session_response import CreateSessionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Session
        api_response = api_instance.post_quote_session(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**CreateSessionResponse**](CreateSessionResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quote_signing_webhook**
> object post_quote_signing_webhook(provider, x_quote_signature=x_quote_signature)

Post Quote Signing Webhook

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
    api_instance = moolabs.QuotesApi(api_client)
    provider = 'provider_example' # str | 
    x_quote_signature = 'x_quote_signature_example' # str |  (optional)

    try:
        # Post Quote Signing Webhook
        api_response = api_instance.post_quote_signing_webhook(provider, x_quote_signature=x_quote_signature)
        print("The response of QuotesApi->post_quote_signing_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_signing_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **x_quote_signature** | **str**|  | [optional] 

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

# **post_quote_submit_approval_v1**
> QuoteApprovalResponse post_quote_submit_approval_v1(quote_id, idempotency_key=idempotency_key)

Post Quote Submit Approval

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_approval_response import QuoteApprovalResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Submit Approval
        api_response = api_instance.post_quote_submit_approval_v1(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_submit_approval_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_submit_approval_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteApprovalResponse**](QuoteApprovalResponse.md)

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

# **post_quote_unlock**
> QuoteVersionResponse post_quote_unlock(quote_id, idempotency_key=idempotency_key)

Post Quote Unlock

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_version_response import QuoteVersionResponse
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
    api_instance = moolabs.QuotesApi(api_client)
    quote_id = 'quote_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str |  (optional)

    try:
        # Post Quote Unlock
        api_response = api_instance.post_quote_unlock(quote_id, idempotency_key=idempotency_key)
        print("The response of QuotesApi->post_quote_unlock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->post_quote_unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **idempotency_key** | **str**|  | [optional] 

### Return type

[**QuoteVersionResponse**](QuoteVersionResponse.md)

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

# **put_approval_levels_v1**
> object put_approval_levels_v1(replace_levels_request)

Put Approval Levels

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.replace_levels_request import ReplaceLevelsRequest
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
    api_instance = moolabs.QuotesApi(api_client)
    replace_levels_request = moolabs.ReplaceLevelsRequest() # ReplaceLevelsRequest | 

    try:
        # Put Approval Levels
        api_response = api_instance.put_approval_levels_v1(replace_levels_request)
        print("The response of QuotesApi->put_approval_levels_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->put_approval_levels_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replace_levels_request** | [**ReplaceLevelsRequest**](ReplaceLevelsRequest.md)|  | 

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

# **put_approver_v1**
> object put_approver_v1(user_ref, approver_in)

Put Approver

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.approver_in import ApproverIn
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
    api_instance = moolabs.QuotesApi(api_client)
    user_ref = 'user_ref_example' # str | 
    approver_in = moolabs.ApproverIn() # ApproverIn | 

    try:
        # Put Approver
        api_response = api_instance.put_approver_v1(user_ref, approver_in)
        print("The response of QuotesApi->put_approver_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->put_approver_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ref** | **str**|  | 
 **approver_in** | [**ApproverIn**](ApproverIn.md)|  | 

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

# **put_quote_settings**
> QuoteSettingsResponse put_quote_settings(update_quote_settings_request)

Put Quote Settings

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_settings_response import QuoteSettingsResponse
from moolabs.models.update_quote_settings_request import UpdateQuoteSettingsRequest
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
    api_instance = moolabs.QuotesApi(api_client)
    update_quote_settings_request = moolabs.UpdateQuoteSettingsRequest() # UpdateQuoteSettingsRequest | 

    try:
        # Put Quote Settings
        api_response = api_instance.put_quote_settings(update_quote_settings_request)
        print("The response of QuotesApi->put_quote_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->put_quote_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_quote_settings_request** | [**UpdateQuoteSettingsRequest**](UpdateQuoteSettingsRequest.md)|  | 

### Return type

[**QuoteSettingsResponse**](QuoteSettingsResponse.md)

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

# **put_territory**
> object put_territory(key, territory_in)

Put Territory

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.territory_in import TerritoryIn
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
    api_instance = moolabs.QuotesApi(api_client)
    key = 'key_example' # str | 
    territory_in = moolabs.TerritoryIn() # TerritoryIn | 

    try:
        # Put Territory
        api_response = api_instance.put_territory(key, territory_in)
        print("The response of QuotesApi->put_territory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->put_territory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **territory_in** | [**TerritoryIn**](TerritoryIn.md)|  | 

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

# **sync_approver_directory_v1**
> object sync_approver_directory_v1()

Sync Approver Directory

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
    api_instance = moolabs.QuotesApi(api_client)

    try:
        # Sync Approver Directory
        api_response = api_instance.sync_approver_directory_v1()
        print("The response of QuotesApi->sync_approver_directory_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotesApi->sync_approver_directory_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

