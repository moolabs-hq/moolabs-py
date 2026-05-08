# moolabs.GrantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_grant**](GrantsApi.md#get_grant) | **GET** /v1/grants/{grant_id} | Get Grant
[**list_grants**](GrantsApi.md#list_grants) | **GET** /v1/grants | List Grants
[**mint_grant**](GrantsApi.md#mint_grant) | **POST** /v1/grants/mint | Mint Grant
[**void_grant**](GrantsApi.md#void_grant) | **POST** /v1/grants/{grant_id}/void | Void Grant


# **get_grant**
> GrantResponse get_grant(grant_id)

Get Grant

Get grant details by ID.

### Example


```python
import moolabs
from moolabs.models.grant_response import GrantResponse
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
    api_instance = moolabs.GrantsApi(api_client)
    grant_id = 'grant_id_example' # str | 

    try:
        # Get Grant
        api_response = api_instance.get_grant(grant_id)
        print("The response of GrantsApi->get_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->get_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  | 

### Return type

[**GrantResponse**](GrantResponse.md)

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

# **list_grants**
> GrantsListResponse list_grants(tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, subject_id=subject_id, subscription_id=subscription_id, feature_key=feature_key, meter_slug=meter_slug, as_of=as_of, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, offset=offset)

List Grants

List grants.  Returns grants for a tenant/pool, optionally filtered by wallet_id, subject_id, subscription_id, feature_key, meter_slug, or as_of timestamp.  If subject_id or subscription_id is provided but tenant_id/pool_id are not, they will be auto-resolved.

### Example


```python
import moolabs
from moolabs.models.grants_list_response import GrantsListResponse
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
    api_instance = moolabs.GrantsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier (optional if subject_id or subscription_id provided) (optional)
    pool_id = 'pool_id_example' # str | Pool identifier (optional if subject_id or subscription_id provided) (optional)
    wallet_id = 'wallet_id_example' # str | Wallet identifier to filter by (optional)
    subject_id = 'subject_id_example' # str | Subject identifier (for finding wallet, auto-resolves tenant_id/pool_id) (optional)
    subscription_id = 'subscription_id_example' # str | Subscription identifier (filters grants by subscription, auto-resolves tenant_id/pool_id) (optional)
    feature_key = 'feature_key_example' # str | Feature key for scope filtering (optional)
    meter_slug = 'meter_slug_example' # str | Meter slug for scope filtering (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime | As-of timestamp for time travel (legacy, use effective_as_of instead) (optional)
    effective_as_of = '2013-10-20T19:20:30+01:00' # datetime | Effective as-of timestamp (business time) for time travel (optional)
    recorded_as_of = '2013-10-20T19:20:30+01:00' # datetime | Recorded as-of timestamp (system time) for time travel (optional)
    consistent_view = True # bool | Use strong consistency for reads (optional)
    limit = 100 # int | Maximum number of grants to return (optional) (default to 100)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # List Grants
        api_response = api_instance.list_grants(tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, subject_id=subject_id, subscription_id=subscription_id, feature_key=feature_key, meter_slug=meter_slug, as_of=as_of, effective_as_of=effective_as_of, recorded_as_of=recorded_as_of, consistent_view=consistent_view, limit=limit, offset=offset)
        print("The response of GrantsApi->list_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->list_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier (optional if subject_id or subscription_id provided) | [optional] 
 **pool_id** | **str**| Pool identifier (optional if subject_id or subscription_id provided) | [optional] 
 **wallet_id** | **str**| Wallet identifier to filter by | [optional] 
 **subject_id** | **str**| Subject identifier (for finding wallet, auto-resolves tenant_id/pool_id) | [optional] 
 **subscription_id** | **str**| Subscription identifier (filters grants by subscription, auto-resolves tenant_id/pool_id) | [optional] 
 **feature_key** | **str**| Feature key for scope filtering | [optional] 
 **meter_slug** | **str**| Meter slug for scope filtering | [optional] 
 **as_of** | **datetime**| As-of timestamp for time travel (legacy, use effective_as_of instead) | [optional] 
 **effective_as_of** | **datetime**| Effective as-of timestamp (business time) for time travel | [optional] 
 **recorded_as_of** | **datetime**| Recorded as-of timestamp (system time) for time travel | [optional] 
 **consistent_view** | **bool**| Use strong consistency for reads | [optional] 
 **limit** | **int**| Maximum number of grants to return | [optional] [default to 100]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

[**GrantsListResponse**](GrantsListResponse.md)

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

# **mint_grant**
> GrantResponse mint_grant(create_grant_request)

Mint Grant

Mint a new credit grant.  Features: - Idempotent minting (UNIQUE constraint on tenant_id, source_id, shard_index) - Scope support (ALL, FEATURE_LIST, METER_LIST) - Rollover configuration - Cost basis (FX locking for paid grants) - Sharding support (for large TOPUP grants)  Returns:     Created or existing grant

### Example


```python
import moolabs
from moolabs.models.create_grant_request import CreateGrantRequest
from moolabs.models.grant_response import GrantResponse
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
    api_instance = moolabs.GrantsApi(api_client)
    create_grant_request = moolabs.CreateGrantRequest() # CreateGrantRequest | 

    try:
        # Mint Grant
        api_response = api_instance.mint_grant(create_grant_request)
        print("The response of GrantsApi->mint_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->mint_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_grant_request** | [**CreateGrantRequest**](CreateGrantRequest.md)|  | 

### Return type

[**GrantResponse**](GrantResponse.md)

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

# **void_grant**
> GrantResponse void_grant(grant_id, void_grant_request)

Void Grant

Void a grant.  This marks the grant as voided, making the remaining credits unavailable. The grant cannot be un-voided.

### Example


```python
import moolabs
from moolabs.models.grant_response import GrantResponse
from moolabs.models.void_grant_request import VoidGrantRequest
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
    api_instance = moolabs.GrantsApi(api_client)
    grant_id = 'grant_id_example' # str | 
    void_grant_request = moolabs.VoidGrantRequest() # VoidGrantRequest | 

    try:
        # Void Grant
        api_response = api_instance.void_grant(grant_id, void_grant_request)
        print("The response of GrantsApi->void_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GrantsApi->void_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  | 
 **void_grant_request** | [**VoidGrantRequest**](VoidGrantRequest.md)|  | 

### Return type

[**GrantResponse**](GrantResponse.md)

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

