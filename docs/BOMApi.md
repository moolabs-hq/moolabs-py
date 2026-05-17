# moolabs.BOMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_bom**](BOMApi.md#approve_bom) | **POST** /api/v1/bom/{bom_id}/approve | Approve BOM (pending_approval → active)
[**auto_derive**](BOMApi.md#auto_derive) | **POST** /api/v1/bom/{bom_id}/derive | Auto-derive BOM from observed cost_events
[**create_bom**](BOMApi.md#create_bom) | **POST** /api/v1/bom | Create BOM (status&#x3D;draft)
[**create_new_version**](BOMApi.md#create_new_version) | **PUT** /api/v1/bom/{bom_id} | Create new BOM version (immutable update)
[**get_bom**](BOMApi.md#get_bom) | **GET** /api/v1/bom/{bom_id} | Get BOM with components
[**get_observation_completeness**](BOMApi.md#get_observation_completeness) | **GET** /api/v1/bom/{bom_id}/observation | Observation completeness vs BOM expected_span_count
[**list_boms**](BOMApi.md#list_boms) | **GET** /api/v1/bom | List BOMs for tenant
[**simulate_cost**](BOMApi.md#simulate_cost) | **GET** /api/v1/bom/{bom_id}/simulate | Simulate BOM cost with current rate_catalog rates
[**submit_for_approval**](BOMApi.md#submit_for_approval) | **POST** /api/v1/bom/{bom_id}/submit | Submit BOM for approval (draft → pending_approval)


# **approve_bom**
> BomOut approve_bom(bom_id, tenant_id, acute_approve_request)

Approve BOM (pending_approval → active)

Transition BOM from 'pending_approval' to 'active'. Sets approved_by + approved_at. Supersedes existing active BOM. Creates standard_costs row (period_start=now, period_end=NULL). Returns 400 if BOM is not in pending_approval status. Returns 422 if approved_by is missing.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.acute_approve_request import AcuteApproveRequest
from moolabs.models.bom_out import BomOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    acute_approve_request = moolabs.AcuteApproveRequest() # AcuteApproveRequest | 

    try:
        # Approve BOM (pending_approval → active)
        api_response = api_instance.approve_bom(bom_id, tenant_id, acute_approve_request)
        print("The response of BOMApi->approve_bom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->approve_bom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 
 **acute_approve_request** | [**AcuteApproveRequest**](AcuteApproveRequest.md)|  | 

### Return type

[**BomOut**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_derive**
> BomOut auto_derive(bom_id, derive_request)

Auto-derive BOM from observed cost_events

Derive a new BOM from observed cost_events in the given period. Creates a draft BOM with derived_from='auto_from_observed'. REQUIRES approval before activation — cannot self-activate.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_out import BomOut
from moolabs.models.derive_request import DeriveRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    derive_request = moolabs.DeriveRequest() # DeriveRequest | 

    try:
        # Auto-derive BOM from observed cost_events
        api_response = api_instance.auto_derive(bom_id, derive_request)
        print("The response of BOMApi->auto_derive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->auto_derive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **derive_request** | [**DeriveRequest**](DeriveRequest.md)|  | 

### Return type

[**BomOut**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bom**
> BomOut create_bom(bom_create_request)

Create BOM (status=draft)

Create a new BOM at version=1, status=draft. unit_cost looked up from rate_catalog if not provided in components. standard_cost computed per component: expected_quantity × unit_cost.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_create_request import BomCreateRequest
from moolabs.models.bom_out import BomOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_create_request = moolabs.BomCreateRequest() # BomCreateRequest | 

    try:
        # Create BOM (status=draft)
        api_response = api_instance.create_bom(bom_create_request)
        print("The response of BOMApi->create_bom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->create_bom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_create_request** | [**BomCreateRequest**](BomCreateRequest.md)|  | 

### Return type

[**BomOut**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_version**
> BomOut create_new_version(bom_id, tenant_id, bom_update_request)

Create new BOM version (immutable update)

Immutable update: creates a new BOM at version=old+1 with status=draft. Old version is NOT modified until new version is approved. Active BOM cannot be deleted — use this endpoint + approve flow.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_out import BomOut
from moolabs.models.bom_update_request import BomUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    bom_update_request = moolabs.BomUpdateRequest() # BomUpdateRequest | 

    try:
        # Create new BOM version (immutable update)
        api_response = api_instance.create_new_version(bom_id, tenant_id, bom_update_request)
        print("The response of BOMApi->create_new_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->create_new_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 
 **bom_update_request** | [**BomUpdateRequest**](BomUpdateRequest.md)|  | 

### Return type

[**BomOut**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bom**
> BomOut get_bom(bom_id, tenant_id)

Get BOM with components

Get a BOM by ID including all components.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_out import BomOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID

    try:
        # Get BOM with components
        api_response = api_instance.get_bom(bom_id, tenant_id)
        print("The response of BOMApi->get_bom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->get_bom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 

### Return type

[**BomOut**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_observation_completeness**
> ObservationOut get_observation_completeness(bom_id, tenant_id, period_start, period_end)

Observation completeness vs BOM expected_span_count

Compare BOM expected_span_count against observed cost_event count per billing event. Returns 404 if no active BOM or no data in period.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.observation_out import ObservationOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    period_start = '2013-10-20T19:20:30+01:00' # datetime | Period start (ISO datetime)
    period_end = '2013-10-20T19:20:30+01:00' # datetime | Period end (ISO datetime)

    try:
        # Observation completeness vs BOM expected_span_count
        api_response = api_instance.get_observation_completeness(bom_id, tenant_id, period_start, period_end)
        print("The response of BOMApi->get_observation_completeness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->get_observation_completeness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 
 **period_start** | **datetime**| Period start (ISO datetime) | 
 **period_end** | **datetime**| Period end (ISO datetime) | 

### Return type

[**ObservationOut**](ObservationOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_boms**
> List[BomOut] list_boms(tenant_id, feature_key=feature_key, status=status, limit=limit, offset=offset)

List BOMs for tenant

List BOMs for a tenant. Filterable by feature_key and status.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_out import BomOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    feature_key = 'feature_key_example' # str | Filter by feature_key (optional)
    status = 'status_example' # str | Filter by status (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List BOMs for tenant
        api_response = api_instance.list_boms(tenant_id, feature_key=feature_key, status=status, limit=limit, offset=offset)
        print("The response of BOMApi->list_boms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->list_boms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant UUID | 
 **feature_key** | **str**| Filter by feature_key | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[BomOut]**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simulate_cost**
> SimulateOut simulate_cost(bom_id, tenant_id, billing_event_count=billing_event_count)

Simulate BOM cost with current rate_catalog rates

Recalculate BOM components against CURRENT rate_catalog (not locked rates). Returns projected cost vs standard cost with rate delta per component.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.simulate_out import SimulateOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID
    billing_event_count = 1 # int | Number of billing events to project (optional) (default to 1)

    try:
        # Simulate BOM cost with current rate_catalog rates
        api_response = api_instance.simulate_cost(bom_id, tenant_id, billing_event_count=billing_event_count)
        print("The response of BOMApi->simulate_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->simulate_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 
 **billing_event_count** | **int**| Number of billing events to project | [optional] [default to 1]

### Return type

[**SimulateOut**](SimulateOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_for_approval**
> BomOut submit_for_approval(bom_id, tenant_id)

Submit BOM for approval (draft → pending_approval)

Transition BOM from 'draft' to 'pending_approval'. Returns 400 if BOM is not in draft status.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.bom_out import BomOut
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.BOMApi(api_client)
    bom_id = 'bom_id_example' # str | 
    tenant_id = 'tenant_id_example' # str | Tenant UUID

    try:
        # Submit BOM for approval (draft → pending_approval)
        api_response = api_instance.submit_for_approval(bom_id, tenant_id)
        print("The response of BOMApi->submit_for_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BOMApi->submit_for_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bom_id** | **str**|  | 
 **tenant_id** | **str**| Tenant UUID | 

### Return type

[**BomOut**](BomOut.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

