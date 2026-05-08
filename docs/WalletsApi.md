# moolabs.WalletsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allocate_credits**](WalletsApi.md#allocate_credits) | **POST** /v1/wallets/allocate | Allocate Credits
[**bind_subject_to_wallet**](WalletsApi.md#bind_subject_to_wallet) | **POST** /v1/wallets/members | Bind Subject To Wallet
[**create_wallet**](WalletsApi.md#create_wallet) | **POST** /v1/wallets | Create Wallet
[**get_wallet**](WalletsApi.md#get_wallet) | **GET** /v1/wallets/{wallet_id} | Get Wallet
[**get_wallet_activity**](WalletsApi.md#get_wallet_activity) | **GET** /v1/wallets/{wallet_id}/activity | Get Wallet Activity
[**get_wallet_members**](WalletsApi.md#get_wallet_members) | **GET** /v1/wallets/{wallet_id}/members | Get Wallet Members
[**list_wallet_members**](WalletsApi.md#list_wallet_members) | **GET** /v1/wallet_members | List Wallet Members
[**list_wallets**](WalletsApi.md#list_wallets) | **GET** /v1/wallets | List Wallets
[**resolve_tenant_and_pool**](WalletsApi.md#resolve_tenant_and_pool) | **GET** /v1/wallets/resolve | Resolve Tenant And Pool
[**update_wallet_settings**](WalletsApi.md#update_wallet_settings) | **PATCH** /v1/wallets/{wallet_id}/settings | Update Wallet Settings
[**update_wallet_thresholds**](WalletsApi.md#update_wallet_thresholds) | **PATCH** /v1/wallets/{wallet_id}/thresholds | Update Wallet Thresholds


# **allocate_credits**
> object allocate_credits(allocate_credits_request)

Allocate Credits

Allocate credits from source wallet to target wallet.  Server-side validation: - Both wallets must belong to the same tenant and pool. - Source must have sufficient transferable balance. - Creates double-entry journal entries (JournalEntry header + JournalPosting lines).

### Example

* Bearer Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.allocate_credits_request import AllocateCreditsRequest
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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.WalletsApi(api_client)
    allocate_credits_request = moolabs.AllocateCreditsRequest() # AllocateCreditsRequest | 

    try:
        # Allocate Credits
        api_response = api_instance.allocate_credits(allocate_credits_request)
        print("The response of WalletsApi->allocate_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->allocate_credits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocate_credits_request** | [**AllocateCreditsRequest**](AllocateCreditsRequest.md)|  | 

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

# **bind_subject_to_wallet**
> object bind_subject_to_wallet(tenant_id, pool_id, subject_id, wallet_id)

Bind Subject To Wallet

Bind a subject to a wallet.  Creates or updates wallet_members entry.

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
    api_instance = moolabs.WalletsApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    pool_id = 'pool_id_example' # str | 
    subject_id = 'subject_id_example' # str | 
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Bind Subject To Wallet
        api_response = api_instance.bind_subject_to_wallet(tenant_id, pool_id, subject_id, wallet_id)
        print("The response of WalletsApi->bind_subject_to_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->bind_subject_to_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **pool_id** | **str**|  | 
 **subject_id** | **str**|  | 
 **wallet_id** | **str**|  | 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wallet**
> WalletResponse create_wallet(create_wallet_request)

Create Wallet

Create or upsert a wallet.  - Validates hierarchy (depth, cycles) - Auto-creates SYSTEM wallet if needed - Returns wallet details

### Example


```python
import moolabs
from moolabs.models.create_wallet_request import CreateWalletRequest
from moolabs.models.wallet_response import WalletResponse
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
    api_instance = moolabs.WalletsApi(api_client)
    create_wallet_request = moolabs.CreateWalletRequest() # CreateWalletRequest | 

    try:
        # Create Wallet
        api_response = api_instance.create_wallet(create_wallet_request)
        print("The response of WalletsApi->create_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->create_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_wallet_request** | [**CreateWalletRequest**](CreateWalletRequest.md)|  | 

### Return type

[**WalletResponse**](WalletResponse.md)

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

# **get_wallet**
> WalletResponse get_wallet(wallet_id)

Get Wallet

Get wallet details by ID.

### Example


```python
import moolabs
from moolabs.models.wallet_response import WalletResponse
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
    api_instance = moolabs.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Get Wallet
        api_response = api_instance.get_wallet(wallet_id)
        print("The response of WalletsApi->get_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

### Return type

[**WalletResponse**](WalletResponse.md)

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

# **get_wallet_activity**
> object get_wallet_activity(wallet_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, cursor=cursor)

Get Wallet Activity

Get wallet activity (journal entries) for a specific wallet.  Returns ALL journal entry types (burns, mints, adjustments, expiry, topup, transfer, system). For entries with burn allocations, shows the burn amount as negative delta. For grant mints, shows the grant amount as positive delta. For other entry types, calculates delta based on entry type.

### Example

* Bearer Authentication (HTTPBearer):

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

# Configure Bearer authorization: HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    from_effective_at = '2013-10-20T19:20:30+01:00' # datetime | Start time for activity range (optional)
    to_effective_at = '2013-10-20T19:20:30+01:00' # datetime | End time for activity range (optional)
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency for reads (optional)
    limit = 50 # int | Maximum number of items to return (optional) (default to 50)
    cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        # Get Wallet Activity
        api_response = api_instance.get_wallet_activity(wallet_id, from_effective_at=from_effective_at, to_effective_at=to_effective_at, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, cursor=cursor)
        print("The response of WalletsApi->get_wallet_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **from_effective_at** | **datetime**| Start time for activity range | [optional] 
 **to_effective_at** | **datetime**| End time for activity range | [optional] 
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency for reads | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 50]
 **cursor** | **str**| Pagination cursor | [optional] 

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

# **get_wallet_members**
> object get_wallet_members(wallet_id)

Get Wallet Members

Get wallet members (subjects bound to a wallet).  Returns list of subjects that are bound to the specified wallet.

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
    api_instance = moolabs.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 

    try:
        # Get Wallet Members
        api_response = api_instance.get_wallet_members(wallet_id)
        print("The response of WalletsApi->get_wallet_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->get_wallet_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 

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

# **list_wallet_members**
> object list_wallet_members(tenant_id, pool_id, subject_id=subject_id, wallet_id=wallet_id)

List Wallet Members

List wallet members with optional filters.  - Filters by tenant_id and pool_id (required) - Optionally filters by subject_id or wallet_id - Returns list of wallet members matching the filters - Includes resolved tenant_id and pool_id in response headers

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
    api_instance = moolabs.WalletsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Credit pool identifier
    subject_id = 'subject_id_example' # str | Optional subject_id filter (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet_id filter (optional)

    try:
        # List Wallet Members
        api_response = api_instance.list_wallet_members(tenant_id, pool_id, subject_id=subject_id, wallet_id=wallet_id)
        print("The response of WalletsApi->list_wallet_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_wallet_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Credit pool identifier | 
 **subject_id** | **str**| Optional subject_id filter | [optional] 
 **wallet_id** | **str**| Optional wallet_id filter | [optional] 

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

# **list_wallets**
> object list_wallets(tenant_id=tenant_id, pool_id=pool_id, subject_id=subject_id, subscription_id=subscription_id, owner_type=owner_type, owner_id=owner_id, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)

List Wallets

List wallets with optional filters.  - If subscription_id is provided, finds wallets via grants (most direct, no hardcoded resolution) - If subject_id is provided, tenant_id and pool_id are automatically resolved - If neither is provided, tenant_id and pool_id are required - Optionally filters by owner_type and owner_id - Returns list of wallets matching the filters

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
    api_instance = moolabs.WalletsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier (optional if subject_id or subscription_id provided) (optional)
    pool_id = 'pool_id_example' # str | Credit pool identifier (optional if subject_id or subscription_id provided) (optional)
    subject_id = 'subject_id_example' # str | Subject identifier (if provided, tenant_id and pool_id are auto-resolved) (optional)
    subscription_id = 'subscription_id_example' # str | Subscription identifier (finds wallets via grants with this subscription_id) (optional)
    owner_type = 'owner_type_example' # str | Optional owner_type filter (optional)
    owner_id = 'owner_id_example' # str | Optional owner_id filter (optional)
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency for reads (optional)

    try:
        # List Wallets
        api_response = api_instance.list_wallets(tenant_id=tenant_id, pool_id=pool_id, subject_id=subject_id, subscription_id=subscription_id, owner_type=owner_type, owner_id=owner_id, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view)
        print("The response of WalletsApi->list_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->list_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier (optional if subject_id or subscription_id provided) | [optional] 
 **pool_id** | **str**| Credit pool identifier (optional if subject_id or subscription_id provided) | [optional] 
 **subject_id** | **str**| Subject identifier (if provided, tenant_id and pool_id are auto-resolved) | [optional] 
 **subscription_id** | **str**| Subscription identifier (finds wallets via grants with this subscription_id) | [optional] 
 **owner_type** | **str**| Optional owner_type filter | [optional] 
 **owner_id** | **str**| Optional owner_id filter | [optional] 
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency for reads | [optional] 

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

# **resolve_tenant_and_pool**
> object resolve_tenant_and_pool(subject_id)

Resolve Tenant And Pool

Resolve tenant_id and pool_id for a given subject_id.  This endpoint automatically finds the tenant_id and pool_id for a customer/subject by looking up their wallet memberships. This allows the UI to query wallets/grants without requiring the user to manually configure tenant_id and pool_id.  Returns:     {         \"tenant_id\": \"uuid\",         \"pool_id\": \"uuid\" (Global Credits pool for the tenant)     }

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
    api_instance = moolabs.WalletsApi(api_client)
    subject_id = 'subject_id_example' # str | Subject identifier (customer ID or subject key)

    try:
        # Resolve Tenant And Pool
        api_response = api_instance.resolve_tenant_and_pool(subject_id)
        print("The response of WalletsApi->resolve_tenant_and_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->resolve_tenant_and_pool: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id** | **str**| Subject identifier (customer ID or subject key) | 

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

# **update_wallet_settings**
> WalletResponse update_wallet_settings(wallet_id, update_wallet_settings_request, tenant_id=tenant_id, pool_id=pool_id)

Update Wallet Settings

Update wallet settings.  Updates parent_wallet_id, local_hard_cap_micros, and/or policy. - Setting parent_wallet_id to null detaches the wallet from hierarchy - Setting local_hard_cap_micros to null removes the override (reverts to inherited) - Policy controls at-cap behavior (SOFT_BORROW, HARD_BUDGET, NOTIFY_ONLY)

### Example


```python
import moolabs
from moolabs.models.update_wallet_settings_request import UpdateWalletSettingsRequest
from moolabs.models.wallet_response import WalletResponse
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
    api_instance = moolabs.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    update_wallet_settings_request = moolabs.UpdateWalletSettingsRequest() # UpdateWalletSettingsRequest | 
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)

    try:
        # Update Wallet Settings
        api_response = api_instance.update_wallet_settings(wallet_id, update_wallet_settings_request, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of WalletsApi->update_wallet_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->update_wallet_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **update_wallet_settings_request** | [**UpdateWalletSettingsRequest**](UpdateWalletSettingsRequest.md)|  | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 

### Return type

[**WalletResponse**](WalletResponse.md)

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

# **update_wallet_thresholds**
> WalletResponse update_wallet_thresholds(wallet_id, update_wallet_thresholds_request, tenant_id=tenant_id, pool_id=pool_id)

Update Wallet Thresholds

Update wallet thresholds.  Updates local_soft_threshold_micros and/or local_hard_cap_micros. Setting a value to null removes the wallet override (reverts to inherited).

### Example


```python
import moolabs
from moolabs.models.update_wallet_thresholds_request import UpdateWalletThresholdsRequest
from moolabs.models.wallet_response import WalletResponse
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
    api_instance = moolabs.WalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | 
    update_wallet_thresholds_request = moolabs.UpdateWalletThresholdsRequest() # UpdateWalletThresholdsRequest | 
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)

    try:
        # Update Wallet Thresholds
        api_response = api_instance.update_wallet_thresholds(wallet_id, update_wallet_thresholds_request, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of WalletsApi->update_wallet_thresholds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WalletsApi->update_wallet_thresholds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**|  | 
 **update_wallet_thresholds_request** | [**UpdateWalletThresholdsRequest**](UpdateWalletThresholdsRequest.md)|  | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 

### Return type

[**WalletResponse**](WalletResponse.md)

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

