# moolabs.SnapshotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /v1/snapshots | Create Snapshot
[**get_snapshot_at_endpoint**](SnapshotsApi.md#get_snapshot_at_endpoint) | **GET** /v1/snapshots/wallet/{wallet_id}/at | Get Snapshot At Endpoint
[**list_snapshots_endpoint**](SnapshotsApi.md#list_snapshots_endpoint) | **GET** /v1/snapshots/wallet/{wallet_id} | List Snapshots Endpoint
[**validate_snapshot_endpoint**](SnapshotsApi.md#validate_snapshot_endpoint) | **POST** /v1/snapshots/{snapshot_id}/validate | Validate Snapshot Endpoint


# **create_snapshot**
> SnapshotResponse create_snapshot(create_snapshot_request)

Create Snapshot

Create a balance snapshot using REPEATABLE READ transaction isolation.  This endpoint creates a snapshot of the wallet balance at a specific point in time. The snapshot uses REPEATABLE READ isolation to ensure a consistent view of the data.

### Example


```python
import moolabs
from moolabs.models.create_snapshot_request import CreateSnapshotRequest
from moolabs.models.snapshot_response import SnapshotResponse
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
    api_instance = moolabs.SnapshotsApi(api_client)
    create_snapshot_request = moolabs.CreateSnapshotRequest() # CreateSnapshotRequest | 

    try:
        # Create Snapshot
        api_response = api_instance.create_snapshot(create_snapshot_request)
        print("The response of SnapshotsApi->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_snapshot_request** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

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

# **get_snapshot_at_endpoint**
> object get_snapshot_at_endpoint(wallet_id, tenant_id, pool_id, as_of_recorded_at)

Get Snapshot At Endpoint

Get the most recent snapshot at or before a recorded timestamp.  Returns the snapshot with as_of_recorded_at <= provided timestamp.

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
    api_instance = moolabs.SnapshotsApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    as_of_recorded_at = '2013-10-20T19:20:30+01:00' # datetime | Recorded timestamp

    try:
        # Get Snapshot At Endpoint
        api_response = api_instance.get_snapshot_at_endpoint(wallet_id, tenant_id, pool_id, as_of_recorded_at)
        print("The response of SnapshotsApi->get_snapshot_at_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_snapshot_at_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **as_of_recorded_at** | **datetime**| Recorded timestamp | 

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

# **list_snapshots_endpoint**
> object list_snapshots_endpoint(wallet_id, tenant_id, pool_id, limit=limit)

List Snapshots Endpoint

List snapshots for a wallet.  Returns the most recent snapshots first.

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
    api_instance = moolabs.SnapshotsApi(api_client)
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    limit = 100 # int | Maximum number of snapshots (optional) (default to 100)

    try:
        # List Snapshots Endpoint
        api_response = api_instance.list_snapshots_endpoint(wallet_id, tenant_id, pool_id, limit=limit)
        print("The response of SnapshotsApi->list_snapshots_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_snapshots_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet identifier | 
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **limit** | **int**| Maximum number of snapshots | [optional] [default to 100]

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

# **validate_snapshot_endpoint**
> ValidationResponse validate_snapshot_endpoint(snapshot_id)

Validate Snapshot Endpoint

Validate a balance snapshot by recomputing the balance and fingerprint.  This recomputes the balance at the snapshot's cut times and compares the fingerprint to ensure data integrity.

### Example


```python
import moolabs
from moolabs.models.validation_response import ValidationResponse
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
    api_instance = moolabs.SnapshotsApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | Snapshot identifier

    try:
        # Validate Snapshot Endpoint
        api_response = api_instance.validate_snapshot_endpoint(snapshot_id)
        print("The response of SnapshotsApi->validate_snapshot_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->validate_snapshot_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot identifier | 

### Return type

[**ValidationResponse**](ValidationResponse.md)

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

