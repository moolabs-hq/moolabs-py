# moolabs.EntitlementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_entitlement_grant_v2**](EntitlementsApi.md#create_customer_entitlement_grant_v2) | **POST** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/grants | Create customer entitlement grant
[**create_customer_entitlement_v2**](EntitlementsApi.md#create_customer_entitlement_v2) | **POST** /api/v2/customers/{customerIdOrKey}/entitlements | Create a customer entitlement
[**create_entitlement**](EntitlementsApi.md#create_entitlement) | **POST** /api/v1/subjects/{subjectIdOrKey}/entitlements | Create a subject entitlement
[**create_grant**](EntitlementsApi.md#create_grant) | **POST** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/grants | Create subject entitlement grant
[**delete_customer_entitlement_v2**](EntitlementsApi.md#delete_customer_entitlement_v2) | **DELETE** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey} | Delete customer entitlement
[**delete_entitlement**](EntitlementsApi.md#delete_entitlement) | **DELETE** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementId} | Delete subject entitlement
[**get_customer_access**](EntitlementsApi.md#get_customer_access) | **GET** /api/v1/customers/{customerIdOrKey}/access | Get customer access
[**get_customer_entitlement_history_v2**](EntitlementsApi.md#get_customer_entitlement_history_v2) | **GET** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/history | Get customer entitlement history
[**get_customer_entitlement_v2**](EntitlementsApi.md#get_customer_entitlement_v2) | **GET** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey} | Get customer entitlement
[**get_customer_entitlement_value**](EntitlementsApi.md#get_customer_entitlement_value) | **GET** /api/v1/customers/{customerIdOrKey}/entitlements/{featureKey}/value | Get customer entitlement value
[**get_customer_entitlement_value_v2**](EntitlementsApi.md#get_customer_entitlement_value_v2) | **GET** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/value | Get customer entitlement value
[**get_entitlement**](EntitlementsApi.md#get_entitlement) | **GET** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementId} | Get subject entitlement
[**get_entitlement_by_id**](EntitlementsApi.md#get_entitlement_by_id) | **GET** /api/v1/entitlements/{entitlementId} | Get entitlement by id
[**get_entitlement_by_id_v2**](EntitlementsApi.md#get_entitlement_by_id_v2) | **GET** /api/v2/entitlements/{entitlementId} | Get entitlement by id
[**get_entitlement_history**](EntitlementsApi.md#get_entitlement_history) | **GET** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementId}/history | Get subject entitlement history
[**get_entitlement_value**](EntitlementsApi.md#get_entitlement_value) | **GET** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/value | Get subject entitlement value
[**list_customer_entitlement_grants_v2**](EntitlementsApi.md#list_customer_entitlement_grants_v2) | **GET** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/grants | List customer entitlement grants
[**list_customer_entitlements_v2**](EntitlementsApi.md#list_customer_entitlements_v2) | **GET** /api/v2/customers/{customerIdOrKey}/entitlements | List customer entitlements
[**list_entitlement_grants**](EntitlementsApi.md#list_entitlement_grants) | **GET** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/grants | List subject entitlement grants
[**list_entitlements**](EntitlementsApi.md#list_entitlements) | **GET** /api/v1/entitlements | List all entitlements
[**list_entitlements_v2**](EntitlementsApi.md#list_entitlements_v2) | **GET** /api/v2/entitlements | List all entitlements
[**list_grants_get**](EntitlementsApi.md#list_grants_get) | **GET** /api/v1/grants | List grants
[**list_grants_v2**](EntitlementsApi.md#list_grants_v2) | **GET** /api/v2/grants | List grants
[**list_subject_entitlements**](EntitlementsApi.md#list_subject_entitlements) | **GET** /api/v1/subjects/{subjectIdOrKey}/entitlements | List subject entitlements
[**override_customer_entitlement_v2**](EntitlementsApi.md#override_customer_entitlement_v2) | **PUT** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/override | Override customer entitlement
[**override_entitlement**](EntitlementsApi.md#override_entitlement) | **PUT** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/override | Override subject entitlement
[**reset_customer_entitlement_usage_v2**](EntitlementsApi.md#reset_customer_entitlement_usage_v2) | **POST** /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/reset | Reset customer entitlement
[**reset_entitlement_usage**](EntitlementsApi.md#reset_entitlement_usage) | **POST** /api/v1/subjects/{subjectIdOrKey}/entitlements/{entitlementId}/reset | Reset subject entitlement
[**void_grant_delete**](EntitlementsApi.md#void_grant_delete) | **DELETE** /api/v1/grants/{grantId} | Void grant


# **create_customer_entitlement_grant_v2**
> EntitlementGrantV2 create_customer_entitlement_grant_v2(customer_id_or_key, entitlement_id_or_feature_key, entitlement_grant_create_input_v2)

Create customer entitlement grant

Grants define a behavior of granting usage for a metered entitlement. They can have complicated recurrence and rollover rules, thanks to which you can define a wide range of access patterns with a single grant, in most cases you don't have to periodically create new grants. You can only issue grants for active metered entitlements.  A grant defines a given amount of usage that can be consumed for the entitlement. The grant is in effect between its effective date and its expiration date. Specifying both is mandatory for new grants.  Grants have a priority setting that determines their order of use. Lower numbers have higher priority, with 0 being the highest priority.  Grants can have a recurrence setting intended to automate the manual reissuing of grants. For example, a daily recurrence is equal to reissuing that same grant every day (ignoring rollover settings).  Rollover settings define what happens to the remaining balance of a grant at a reset. Balance_After_Reset = MIN(MaxRolloverAmount, MAX(Balance_Before_Reset, MinRolloverAmount))  Grants cannot be changed once created, only deleted. This is to ensure that balance is deterministic regardless of when it is queried.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_grant_create_input_v2 import EntitlementGrantCreateInputV2
from moolabs.models.entitlement_grant_v2 import EntitlementGrantV2
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    entitlement_grant_create_input_v2 = moolabs.EntitlementGrantCreateInputV2() # EntitlementGrantCreateInputV2 | 

    try:
        # Create customer entitlement grant
        api_response = api_instance.create_customer_entitlement_grant_v2(customer_id_or_key, entitlement_id_or_feature_key, entitlement_grant_create_input_v2)
        print("The response of EntitlementsApi->create_customer_entitlement_grant_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->create_customer_entitlement_grant_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **entitlement_grant_create_input_v2** | [**EntitlementGrantCreateInputV2**](EntitlementGrantCreateInputV2.md)|  | 

### Return type

[**EntitlementGrantV2**](EntitlementGrantV2.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_entitlement_v2**
> EntitlementV2 create_customer_entitlement_v2(customer_id_or_key, entitlement_v2_create_inputs)

Create a customer entitlement

OpenMeter has three types of entitlements: metered, boolean, and static. The type property determines the type of entitlement. The underlying feature has to be compatible with the entitlement type specified in the request (e.g., a metered entitlement needs a feature associated with a meter).  - Boolean entitlements define static feature access, e.g. \"Can use SSO authentication\". - Static entitlements let you pass along a configuration while granting access, e.g. \"Using this feature with X Y settings\" (passed in the config). - Metered entitlements have many use cases, from setting up usage-based access to implementing complex credit systems.  Example: The customer can use 10000 AI tokens during the usage period of the entitlement.  A given customer can only have one active (non-deleted) entitlement per featureKey. If you try to create a new entitlement for a featureKey that already has an active entitlement, the request will fail with a 409 error.  Once an entitlement is created you cannot modify it, only delete it.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_v2 import EntitlementV2
from moolabs.models.entitlement_v2_create_inputs import EntitlementV2CreateInputs
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_v2_create_inputs = moolabs.EntitlementV2CreateInputs() # EntitlementV2CreateInputs | 

    try:
        # Create a customer entitlement
        api_response = api_instance.create_customer_entitlement_v2(customer_id_or_key, entitlement_v2_create_inputs)
        print("The response of EntitlementsApi->create_customer_entitlement_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->create_customer_entitlement_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_v2_create_inputs** | [**EntitlementV2CreateInputs**](EntitlementV2CreateInputs.md)|  | 

### Return type

[**EntitlementV2**](EntitlementV2.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_entitlement**
> Entitlement create_entitlement(subject_id_or_key, entitlement_create_inputs)

Create a subject entitlement

OpenMeter has three types of entitlements: metered, boolean, and static. The type property determines the type of entitlement. The underlying feature has to be compatible with the entitlement type specified in the request (e.g., a metered entitlement needs a feature associated with a meter).  - Boolean entitlements define static feature access, e.g. \"Can use SSO authentication\". - Static entitlements let you pass along a configuration while granting access, e.g. \"Using this feature with X Y settings\" (passed in the config). - Metered entitlements have many use cases, from setting up usage-based access to implementing complex credit systems.  Example: The customer can use 10000 AI tokens during the usage period of the entitlement.  A given subject can only have one active (non-deleted) entitlement per featureKey. If you try to create a new entitlement for a featureKey that already has an active entitlement, the request will fail with a 409 error.  Once an entitlement is created you cannot modify it, only delete it.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement import Entitlement
from moolabs.models.entitlement_create_inputs import EntitlementCreateInputs
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_create_inputs = moolabs.EntitlementCreateInputs() # EntitlementCreateInputs | 

    try:
        # Create a subject entitlement
        api_response = api_instance.create_entitlement(subject_id_or_key, entitlement_create_inputs)
        print("The response of EntitlementsApi->create_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->create_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_create_inputs** | [**EntitlementCreateInputs**](EntitlementCreateInputs.md)|  | 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_grant**
> EntitlementGrant create_grant(subject_id_or_key, entitlement_id_or_feature_key, entitlement_grant_create_input)

Create subject entitlement grant

Grants define a behavior of granting usage for a metered entitlement. They can have complicated recurrence and rollover rules, thanks to which you can define a wide range of access patterns with a single grant, in most cases you don't have to periodically create new grants. You can only issue grants for active metered entitlements.  A grant defines a given amount of usage that can be consumed for the entitlement. The grant is in effect between its effective date and its expiration date. Specifying both is mandatory for new grants.  Grants have a priority setting that determines their order of use. Lower numbers have higher priority, with 0 being the highest priority.  Grants can have a recurrence setting intended to automate the manual reissuing of grants. For example, a daily recurrence is equal to reissuing that same grant every day (ignoring rollover settings).  Rollover settings define what happens to the remaining balance of a grant at a reset. Balance_After_Reset = MIN(MaxRolloverAmount, MAX(Balance_Before_Reset, MinRolloverAmount))  Grants cannot be changed once created, only deleted. This is to ensure that balance is deterministic regardless of when it is queried.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_grant import EntitlementGrant
from moolabs.models.entitlement_grant_create_input import EntitlementGrantCreateInput
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    entitlement_grant_create_input = moolabs.EntitlementGrantCreateInput() # EntitlementGrantCreateInput | 

    try:
        # Create subject entitlement grant
        api_response = api_instance.create_grant(subject_id_or_key, entitlement_id_or_feature_key, entitlement_grant_create_input)
        print("The response of EntitlementsApi->create_grant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->create_grant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **entitlement_grant_create_input** | [**EntitlementGrantCreateInput**](EntitlementGrantCreateInput.md)|  | 

### Return type

[**EntitlementGrant**](EntitlementGrant.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_entitlement_v2**
> delete_customer_entitlement_v2(customer_id_or_key, entitlement_id_or_feature_key)

Delete customer entitlement

Deleting an entitlement revokes access to the associated feature. As a single customer can only have one entitlement per featureKey, when \"migrating\" features you have to delete the old entitlements as well. As access and status checks can be historical queries, deleting an entitlement populates the deletedAt timestamp. When queried for a time before that, the entitlement is still considered active, you cannot have retroactive changes to access, which is important for, among other things, auditing.

### Example

* Bearer Authentication (CloudTokenAuth):

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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 

    try:
        # Delete customer entitlement
        api_instance.delete_customer_entitlement_v2(customer_id_or_key, entitlement_id_or_feature_key)
    except Exception as e:
        print("Exception when calling EntitlementsApi->delete_customer_entitlement_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **delete_entitlement**
> delete_entitlement(subject_id_or_key, entitlement_id)

Delete subject entitlement

Deleting an entitlement revokes access to the associated feature. As a single subject can only have one entitlement per featureKey, when \"migrating\" features you have to delete the old entitlements as well. As access and status checks can be historical queries, deleting an entitlement populates the deletedAt timestamp. When queried for a time before that, the entitlement is still considered active, you cannot have retroactive changes to access, which is important for, among other things, auditing.

### Example

* Bearer Authentication (CloudTokenAuth):

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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 

    try:
        # Delete subject entitlement
        api_instance.delete_entitlement(subject_id_or_key, entitlement_id)
    except Exception as e:
        print("Exception when calling EntitlementsApi->delete_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_customer_access**
> CustomerAccess get_customer_access(customer_id_or_key)

Get customer access

Get the overall access of a customer.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.customer_access import CustomerAccess
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 

    try:
        # Get customer access
        api_response = api_instance.get_customer_access(customer_id_or_key)
        print("The response of EntitlementsApi->get_customer_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_customer_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 

### Return type

[**CustomerAccess**](CustomerAccess.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_customer_entitlement_history_v2**
> WindowedBalanceHistory get_customer_entitlement_history_v2(customer_id_or_key, entitlement_id_or_feature_key, window_size, var_from=var_from, to=to, window_time_zone=window_time_zone)

Get customer entitlement history

Returns historical balance and usage data for the entitlement. The queried history can span accross multiple reset events.  BurndownHistory returns a continous history of segments, where the segments are seperated by events that changed either the grant burndown priority or the usage period.  WindowedHistory returns windowed usage data for the period enriched with balance information and the list of grants that were being burnt down in that window.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.window_size import WindowSize
from moolabs.models.windowed_balance_history import WindowedBalanceHistory
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    window_size = moolabs.WindowSize() # WindowSize | Windowsize
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start of time range to query entitlement: date-time in RFC 3339 format. Defaults to the last reset. Gets truncated to the granularity of the underlying meter. (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End of time range to query entitlement: date-time in RFC 3339 format. Defaults to now. If not now then gets truncated to the granularity of the underlying meter. (optional)
    window_time_zone = 'UTC' # str | The timezone used when calculating the windows. (optional) (default to 'UTC')

    try:
        # Get customer entitlement history
        api_response = api_instance.get_customer_entitlement_history_v2(customer_id_or_key, entitlement_id_or_feature_key, window_size, var_from=var_from, to=to, window_time_zone=window_time_zone)
        print("The response of EntitlementsApi->get_customer_entitlement_history_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_customer_entitlement_history_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **window_size** | [**WindowSize**](.md)| Windowsize | 
 **var_from** | **datetime**| Start of time range to query entitlement: date-time in RFC 3339 format. Defaults to the last reset. Gets truncated to the granularity of the underlying meter. | [optional] 
 **to** | **datetime**| End of time range to query entitlement: date-time in RFC 3339 format. Defaults to now. If not now then gets truncated to the granularity of the underlying meter. | [optional] 
 **window_time_zone** | **str**| The timezone used when calculating the windows. | [optional] [default to &#39;UTC&#39;]

### Return type

[**WindowedBalanceHistory**](WindowedBalanceHistory.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_customer_entitlement_v2**
> EntitlementV2 get_customer_entitlement_v2(customer_id_or_key, entitlement_id_or_feature_key)

Get customer entitlement

Get entitlement by feature key. For checking entitlement access, use the /value endpoint instead. If featureKey is used, the entitlement is resolved for the current timestamp.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_v2 import EntitlementV2
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 

    try:
        # Get customer entitlement
        api_response = api_instance.get_customer_entitlement_v2(customer_id_or_key, entitlement_id_or_feature_key)
        print("The response of EntitlementsApi->get_customer_entitlement_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_customer_entitlement_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 

### Return type

[**EntitlementV2**](EntitlementV2.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_customer_entitlement_value**
> EntitlementValue get_customer_entitlement_value(customer_id_or_key, feature_key, time=time)

Get customer entitlement value

Checks customer access to a given feature (by key). All entitlement types share the hasAccess property in their value response, but multiple other properties are returned based on the entitlement type.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_value import EntitlementValue
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    feature_key = 'feature_key_example' # str | 
    time = '2023-01-01T01:01:01.001Z' # datetime |  (optional)

    try:
        # Get customer entitlement value
        api_response = api_instance.get_customer_entitlement_value(customer_id_or_key, feature_key, time=time)
        print("The response of EntitlementsApi->get_customer_entitlement_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_customer_entitlement_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **feature_key** | **str**|  | 
 **time** | **datetime**|  | [optional] 

### Return type

[**EntitlementValue**](EntitlementValue.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_customer_entitlement_value_v2**
> EntitlementValue get_customer_entitlement_value_v2(customer_id_or_key, entitlement_id_or_feature_key, time=time)

Get customer entitlement value

Checks customer access to a given feature (by key). All entitlement types share the hasAccess property in their value response, but multiple other properties are returned based on the entitlement type.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_value import EntitlementValue
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    time = '2023-01-01T01:01:01.001Z' # datetime |  (optional)

    try:
        # Get customer entitlement value
        api_response = api_instance.get_customer_entitlement_value_v2(customer_id_or_key, entitlement_id_or_feature_key, time=time)
        print("The response of EntitlementsApi->get_customer_entitlement_value_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_customer_entitlement_value_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **time** | **datetime**|  | [optional] 

### Return type

[**EntitlementValue**](EntitlementValue.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_entitlement**
> Entitlement get_entitlement(subject_id_or_key, entitlement_id)

Get subject entitlement

Get entitlement by id. For checking entitlement access, use the /value endpoint instead.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement import Entitlement
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 

    try:
        # Get subject entitlement
        api_response = api_instance.get_entitlement(subject_id_or_key, entitlement_id)
        print("The response of EntitlementsApi->get_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id** | **str**|  | 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_entitlement_by_id**
> Entitlement get_entitlement_by_id(entitlement_id)

Get entitlement by id

Get entitlement by id.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement import Entitlement
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    entitlement_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Get entitlement by id
        api_response = api_instance.get_entitlement_by_id(entitlement_id)
        print("The response of EntitlementsApi->get_entitlement_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_id** | **str**|  | 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_entitlement_by_id_v2**
> EntitlementV2 get_entitlement_by_id_v2(entitlement_id)

Get entitlement by id

Get entitlement by id.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_v2 import EntitlementV2
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    entitlement_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Get entitlement by id
        api_response = api_instance.get_entitlement_by_id_v2(entitlement_id)
        print("The response of EntitlementsApi->get_entitlement_by_id_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement_by_id_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_id** | **str**|  | 

### Return type

[**EntitlementV2**](EntitlementV2.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_entitlement_history**
> WindowedBalanceHistory get_entitlement_history(subject_id_or_key, entitlement_id, window_size, var_from=var_from, to=to, window_time_zone=window_time_zone)

Get subject entitlement history

Returns historical balance and usage data for the entitlement. The queried history can span accross multiple reset events.  BurndownHistory returns a continous history of segments, where the segments are seperated by events that changed either the grant burndown priority or the usage period.  WindowedHistory returns windowed usage data for the period enriched with balance information and the list of grants that were being burnt down in that window.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.window_size import WindowSize
from moolabs.models.windowed_balance_history import WindowedBalanceHistory
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 
    window_size = moolabs.WindowSize() # WindowSize | Windowsize
    var_from = '2023-01-01T01:01:01.001Z' # datetime | Start of time range to query entitlement: date-time in RFC 3339 format. Defaults to the last reset. Gets truncated to the granularity of the underlying meter. (optional)
    to = '2023-01-01T01:01:01.001Z' # datetime | End of time range to query entitlement: date-time in RFC 3339 format. Defaults to now. If not now then gets truncated to the granularity of the underlying meter. (optional)
    window_time_zone = 'UTC' # str | The timezone used when calculating the windows. (optional) (default to 'UTC')

    try:
        # Get subject entitlement history
        api_response = api_instance.get_entitlement_history(subject_id_or_key, entitlement_id, window_size, var_from=var_from, to=to, window_time_zone=window_time_zone)
        print("The response of EntitlementsApi->get_entitlement_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id** | **str**|  | 
 **window_size** | [**WindowSize**](.md)| Windowsize | 
 **var_from** | **datetime**| Start of time range to query entitlement: date-time in RFC 3339 format. Defaults to the last reset. Gets truncated to the granularity of the underlying meter. | [optional] 
 **to** | **datetime**| End of time range to query entitlement: date-time in RFC 3339 format. Defaults to now. If not now then gets truncated to the granularity of the underlying meter. | [optional] 
 **window_time_zone** | **str**| The timezone used when calculating the windows. | [optional] [default to &#39;UTC&#39;]

### Return type

[**WindowedBalanceHistory**](WindowedBalanceHistory.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **get_entitlement_value**
> EntitlementValue get_entitlement_value(subject_id_or_key, entitlement_id_or_feature_key, time=time)

Get subject entitlement value

This endpoint should be used for access checks and enforcement. All entitlement types share the hasAccess property in their value response, but multiple other properties are returned based on the entitlement type.  For convenience reasons, /value works with both entitlementId and featureKey.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_value import EntitlementValue
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    time = '2023-01-01T01:01:01.001Z' # datetime |  (optional)

    try:
        # Get subject entitlement value
        api_response = api_instance.get_entitlement_value(subject_id_or_key, entitlement_id_or_feature_key, time=time)
        print("The response of EntitlementsApi->get_entitlement_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->get_entitlement_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **time** | **datetime**|  | [optional] 

### Return type

[**EntitlementValue**](EntitlementValue.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_customer_entitlement_grants_v2**
> GrantV2PaginatedResponse list_customer_entitlement_grants_v2(customer_id_or_key, entitlement_id_or_feature_key, include_deleted=include_deleted, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)

List customer entitlement grants

List all grants issued for an entitlement. The entitlement can be defined either by its id or featureKey.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.grant_order_by import GrantOrderBy
from moolabs.models.grant_v2_paginated_response import GrantV2PaginatedResponse
from moolabs.models.sort_order import SortOrder
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    include_deleted = False # bool |  (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    offset = 0 # int | Number of items to skip.  Default is 0. (optional) (default to 0)
    limit = 100 # int | Number of items to return.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.GrantOrderBy() # GrantOrderBy | The order by field. (optional)

    try:
        # List customer entitlement grants
        api_response = api_instance.list_customer_entitlement_grants_v2(customer_id_or_key, entitlement_id_or_feature_key, include_deleted=include_deleted, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)
        print("The response of EntitlementsApi->list_customer_entitlement_grants_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_customer_entitlement_grants_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip.  Default is 0. | [optional] [default to 0]
 **limit** | **int**| Number of items to return.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**GrantOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**GrantV2PaginatedResponse**](GrantV2PaginatedResponse.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_customer_entitlements_v2**
> EntitlementV2PaginatedResponse list_customer_entitlements_v2(customer_id_or_key, include_deleted=include_deleted, page=page, page_size=page_size, order=order, order_by=order_by)

List customer entitlements

List all entitlements for a customer. For checking entitlement access, use the /value endpoint instead.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_order_by import EntitlementOrderBy
from moolabs.models.entitlement_v2_paginated_response import EntitlementV2PaginatedResponse
from moolabs.models.sort_order import SortOrder
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    include_deleted = False # bool |  (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.EntitlementOrderBy() # EntitlementOrderBy | The order by field. (optional)

    try:
        # List customer entitlements
        api_response = api_instance.list_customer_entitlements_v2(customer_id_or_key, include_deleted=include_deleted, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of EntitlementsApi->list_customer_entitlements_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_customer_entitlements_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **include_deleted** | **bool**|  | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**EntitlementOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**EntitlementV2PaginatedResponse**](EntitlementV2PaginatedResponse.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_entitlement_grants**
> List[EntitlementGrant] list_entitlement_grants(subject_id_or_key, entitlement_id_or_feature_key, include_deleted=include_deleted, order_by=order_by)

List subject entitlement grants

List all grants issued for an entitlement. The entitlement can be defined either by its id or featureKey.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_grant import EntitlementGrant
from moolabs.models.grant_order_by import GrantOrderBy
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    include_deleted = False # bool |  (optional) (default to False)
    order_by = moolabs.GrantOrderBy() # GrantOrderBy |  (optional)

    try:
        # List subject entitlement grants
        api_response = api_instance.list_entitlement_grants(subject_id_or_key, entitlement_id_or_feature_key, include_deleted=include_deleted, order_by=order_by)
        print("The response of EntitlementsApi->list_entitlement_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_entitlement_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to False]
 **order_by** | [**GrantOrderBy**](.md)|  | [optional] 

### Return type

[**List[EntitlementGrant]**](EntitlementGrant.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_entitlements**
> ListEntitlementsResult list_entitlements(feature=feature, subject=subject, entitlement_type=entitlement_type, exclude_inactive=exclude_inactive, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)

List all entitlements

List all entitlements for all the subjects and features. This endpoint is intended for administrative purposes only. To fetch the entitlements of a specific subject please use the /api/v1/subjects/{subjectKeyOrID}/entitlements endpoint. If page is provided that takes precedence and the paginated response is returned.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_order_by import EntitlementOrderBy
from moolabs.models.entitlement_type import EntitlementType
from moolabs.models.list_entitlements_result import ListEntitlementsResult
from moolabs.models.sort_order import SortOrder
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    feature = ['feature_example'] # List[str] | Filtering by multiple features.  Usage: `?feature=feature-1&feature=feature-2` (optional)
    subject = ['subject_example'] # List[str] | Filtering by multiple subjects.  Usage: `?subject=customer-1&subject=customer-2` (optional)
    entitlement_type = [moolabs.EntitlementType()] # List[EntitlementType] | Filtering by multiple entitlement types.  Usage: `?entitlementType=metered&entitlementType=boolean` (optional)
    exclude_inactive = False # bool | Exclude inactive entitlements in the response (those scheduled for later or earlier) (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    offset = 0 # int | Number of items to skip.  Default is 0. (optional) (default to 0)
    limit = 100 # int | Number of items to return.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.EntitlementOrderBy() # EntitlementOrderBy | The order by field. (optional)

    try:
        # List all entitlements
        api_response = api_instance.list_entitlements(feature=feature, subject=subject, entitlement_type=entitlement_type, exclude_inactive=exclude_inactive, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)
        print("The response of EntitlementsApi->list_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | [**List[str]**](str.md)| Filtering by multiple features.  Usage: &#x60;?feature&#x3D;feature-1&amp;feature&#x3D;feature-2&#x60; | [optional] 
 **subject** | [**List[str]**](str.md)| Filtering by multiple subjects.  Usage: &#x60;?subject&#x3D;customer-1&amp;subject&#x3D;customer-2&#x60; | [optional] 
 **entitlement_type** | [**List[EntitlementType]**](EntitlementType.md)| Filtering by multiple entitlement types.  Usage: &#x60;?entitlementType&#x3D;metered&amp;entitlementType&#x3D;boolean&#x60; | [optional] 
 **exclude_inactive** | **bool**| Exclude inactive entitlements in the response (those scheduled for later or earlier) | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip.  Default is 0. | [optional] [default to 0]
 **limit** | **int**| Number of items to return.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**EntitlementOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**ListEntitlementsResult**](ListEntitlementsResult.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_entitlements_v2**
> EntitlementV2PaginatedResponse list_entitlements_v2(feature=feature, customer_keys=customer_keys, customer_ids=customer_ids, entitlement_type=entitlement_type, exclude_inactive=exclude_inactive, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)

List all entitlements

List all entitlements for all the customers and features. This endpoint is intended for administrative purposes only. To fetch the entitlements of a specific subject please use the /api/v2/customers/{customerIdOrKey}/entitlements endpoint.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_order_by import EntitlementOrderBy
from moolabs.models.entitlement_type import EntitlementType
from moolabs.models.entitlement_v2_paginated_response import EntitlementV2PaginatedResponse
from moolabs.models.sort_order import SortOrder
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    feature = ['feature_example'] # List[str] | Filtering by multiple features.  Usage: `?feature=feature-1&feature=feature-2` (optional)
    customer_keys = ['customer_keys_example'] # List[str] | Filtering by multiple customers.  Usage: `?customerKeys=customer-1&customerKeys=customer-3` (optional)
    customer_ids = ['customer_ids_example'] # List[str] | Filtering by multiple customers.  Usage: `?customerIds=01K4WAQ0J99ZZ0MD75HXR112H8&customerIds=01K4WAQ0J99ZZ0MD75HXR112H9` (optional)
    entitlement_type = [moolabs.EntitlementType()] # List[EntitlementType] | Filtering by multiple entitlement types.  Usage: `?entitlementType=metered&entitlementType=boolean` (optional)
    exclude_inactive = False # bool | Exclude inactive entitlements in the response (those scheduled for later or earlier) (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    offset = 0 # int | Number of items to skip.  Default is 0. (optional) (default to 0)
    limit = 100 # int | Number of items to return.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.EntitlementOrderBy() # EntitlementOrderBy | The order by field. (optional)

    try:
        # List all entitlements
        api_response = api_instance.list_entitlements_v2(feature=feature, customer_keys=customer_keys, customer_ids=customer_ids, entitlement_type=entitlement_type, exclude_inactive=exclude_inactive, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)
        print("The response of EntitlementsApi->list_entitlements_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_entitlements_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | [**List[str]**](str.md)| Filtering by multiple features.  Usage: &#x60;?feature&#x3D;feature-1&amp;feature&#x3D;feature-2&#x60; | [optional] 
 **customer_keys** | [**List[str]**](str.md)| Filtering by multiple customers.  Usage: &#x60;?customerKeys&#x3D;customer-1&amp;customerKeys&#x3D;customer-3&#x60; | [optional] 
 **customer_ids** | [**List[str]**](str.md)| Filtering by multiple customers.  Usage: &#x60;?customerIds&#x3D;01K4WAQ0J99ZZ0MD75HXR112H8&amp;customerIds&#x3D;01K4WAQ0J99ZZ0MD75HXR112H9&#x60; | [optional] 
 **entitlement_type** | [**List[EntitlementType]**](EntitlementType.md)| Filtering by multiple entitlement types.  Usage: &#x60;?entitlementType&#x3D;metered&amp;entitlementType&#x3D;boolean&#x60; | [optional] 
 **exclude_inactive** | **bool**| Exclude inactive entitlements in the response (those scheduled for later or earlier) | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip.  Default is 0. | [optional] [default to 0]
 **limit** | **int**| Number of items to return.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**EntitlementOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**EntitlementV2PaginatedResponse**](EntitlementV2PaginatedResponse.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_grants_get**
> ListGrantsGet200Response list_grants_get(feature=feature, subject=subject, include_deleted=include_deleted, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)

List grants

List all grants for all the subjects and entitlements. This endpoint is intended for administrative purposes only. To fetch the grants of a specific entitlement please use the /api/v1/subjects/{subjectKeyOrID}/entitlements/{entitlementOrFeatureID}/grants endpoint. If page is provided that takes precedence and the paginated response is returned.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.grant_order_by import GrantOrderBy
from moolabs.models.list_grants_get200_response import ListGrantsGet200Response
from moolabs.models.sort_order import SortOrder
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    feature = ['feature_example'] # List[str] | Filtering by multiple features.  Usage: `?feature=feature-1&feature=feature-2` (optional)
    subject = ['subject_example'] # List[str] | Filtering by multiple subjects.  Usage: `?subject=customer-1&subject=customer-2` (optional)
    include_deleted = False # bool | Include deleted (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    offset = 0 # int | Number of items to skip.  Default is 0. (optional) (default to 0)
    limit = 100 # int | Number of items to return.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.GrantOrderBy() # GrantOrderBy | The order by field. (optional)

    try:
        # List grants
        api_response = api_instance.list_grants_get(feature=feature, subject=subject, include_deleted=include_deleted, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)
        print("The response of EntitlementsApi->list_grants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_grants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | [**List[str]**](str.md)| Filtering by multiple features.  Usage: &#x60;?feature&#x3D;feature-1&amp;feature&#x3D;feature-2&#x60; | [optional] 
 **subject** | [**List[str]**](str.md)| Filtering by multiple subjects.  Usage: &#x60;?subject&#x3D;customer-1&amp;subject&#x3D;customer-2&#x60; | [optional] 
 **include_deleted** | **bool**| Include deleted | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip.  Default is 0. | [optional] [default to 0]
 **limit** | **int**| Number of items to return.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**GrantOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**ListGrantsGet200Response**](ListGrantsGet200Response.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_grants_v2**
> GrantV2PaginatedResponse list_grants_v2(feature=feature, customer=customer, include_deleted=include_deleted, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)

List grants

List all grants for all the customers and entitlements. This endpoint is intended for administrative purposes only. To fetch the grants of a specific entitlement please use the /api/v2/customers/{customerIdOrKey}/entitlements/{entitlementIdOrFeatureKey}/grants endpoint. If page is provided that takes precedence and the paginated response is returned.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.grant_order_by import GrantOrderBy
from moolabs.models.grant_v2_paginated_response import GrantV2PaginatedResponse
from moolabs.models.sort_order import SortOrder
from moolabs.models.ulidor_external_key import ULIDOrExternalKey
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    feature = ['feature_example'] # List[str] | Filtering by multiple features.  Usage: `?feature=feature-1&feature=feature-2` (optional)
    customer = [moolabs.ULIDOrExternalKey()] # List[ULIDOrExternalKey] | Filtering by multiple customers (either by ID or key).  Usage: `?customer=customer-1&customer=customer-2` (optional)
    include_deleted = False # bool | Include deleted (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    offset = 0 # int | Number of items to skip.  Default is 0. (optional) (default to 0)
    limit = 100 # int | Number of items to return.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.GrantOrderBy() # GrantOrderBy | The order by field. (optional)

    try:
        # List grants
        api_response = api_instance.list_grants_v2(feature=feature, customer=customer, include_deleted=include_deleted, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)
        print("The response of EntitlementsApi->list_grants_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_grants_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature** | [**List[str]**](str.md)| Filtering by multiple features.  Usage: &#x60;?feature&#x3D;feature-1&amp;feature&#x3D;feature-2&#x60; | [optional] 
 **customer** | [**List[ULIDOrExternalKey]**](ULIDOrExternalKey.md)| Filtering by multiple customers (either by ID or key).  Usage: &#x60;?customer&#x3D;customer-1&amp;customer&#x3D;customer-2&#x60; | [optional] 
 **include_deleted** | **bool**| Include deleted | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip.  Default is 0. | [optional] [default to 0]
 **limit** | **int**| Number of items to return.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**GrantOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**GrantV2PaginatedResponse**](GrantV2PaginatedResponse.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **list_subject_entitlements**
> List[Entitlement] list_subject_entitlements(subject_id_or_key, include_deleted=include_deleted)

List subject entitlements

List all entitlements for a subject. For checking entitlement access, use the /value endpoint instead.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement import Entitlement
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    include_deleted = False # bool |  (optional) (default to False)

    try:
        # List subject entitlements
        api_response = api_instance.list_subject_entitlements(subject_id_or_key, include_deleted=include_deleted)
        print("The response of EntitlementsApi->list_subject_entitlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->list_subject_entitlements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to False]

### Return type

[**List[Entitlement]**](Entitlement.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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

# **override_customer_entitlement_v2**
> EntitlementV2 override_customer_entitlement_v2(customer_id_or_key, entitlement_id_or_feature_key, entitlement_v2_create_inputs)

Override customer entitlement

Overriding an entitlement creates a new entitlement from the provided inputs and soft deletes the previous entitlement for the provided customer-feature pair. If the previous entitlement is already deleted or otherwise doesnt exist, the override will fail.  This endpoint is useful for upgrades, downgrades, or other changes to entitlements that require a new entitlement to be created with zero downtime.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement_v2 import EntitlementV2
from moolabs.models.entitlement_v2_create_inputs import EntitlementV2CreateInputs
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_v2_create_inputs = moolabs.EntitlementV2CreateInputs() # EntitlementV2CreateInputs | 

    try:
        # Override customer entitlement
        api_response = api_instance.override_customer_entitlement_v2(customer_id_or_key, entitlement_id_or_feature_key, entitlement_v2_create_inputs)
        print("The response of EntitlementsApi->override_customer_entitlement_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->override_customer_entitlement_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_v2_create_inputs** | [**EntitlementV2CreateInputs**](EntitlementV2CreateInputs.md)|  | 

### Return type

[**EntitlementV2**](EntitlementV2.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **override_entitlement**
> Entitlement override_entitlement(subject_id_or_key, entitlement_id_or_feature_key, entitlement_create_inputs)

Override subject entitlement

Overriding an entitlement creates a new entitlement from the provided inputs and soft deletes the previous entitlement for the provided subject-feature pair. If the previous entitlement is already deleted or otherwise doesnt exist, the override will fail.  This endpoint is useful for upgrades, downgrades, or other changes to entitlements that require a new entitlement to be created with zero downtime.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.entitlement import Entitlement
from moolabs.models.entitlement_create_inputs import EntitlementCreateInputs
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    entitlement_create_inputs = moolabs.EntitlementCreateInputs() # EntitlementCreateInputs | 

    try:
        # Override subject entitlement
        api_response = api_instance.override_entitlement(subject_id_or_key, entitlement_id_or_feature_key, entitlement_create_inputs)
        print("The response of EntitlementsApi->override_entitlement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->override_entitlement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **entitlement_create_inputs** | [**EntitlementCreateInputs**](EntitlementCreateInputs.md)|  | 

### Return type

[**Entitlement**](Entitlement.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_customer_entitlement_usage_v2**
> reset_customer_entitlement_usage_v2(customer_id_or_key, entitlement_id_or_feature_key, reset_entitlement_usage_input)

Reset customer entitlement

Reset marks the start of a new usage period for the entitlement and initiates grant rollover. At the start of a period usage is zerod out and grants are rolled over based on their rollover settings. It would typically be synced with the customers billing period to enforce usage based on their subscription.  Usage is automatically reset for metered entitlements based on their usage period, but this endpoint allows to manually reset it at any time. When doing so the period anchor of the entitlement can be changed if needed.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.reset_entitlement_usage_input import ResetEntitlementUsageInput
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    customer_id_or_key = moolabs.ULIDOrExternalKey() # ULIDOrExternalKey | 
    entitlement_id_or_feature_key = 'entitlement_id_or_feature_key_example' # str | 
    reset_entitlement_usage_input = moolabs.ResetEntitlementUsageInput() # ResetEntitlementUsageInput | 

    try:
        # Reset customer entitlement
        api_instance.reset_customer_entitlement_usage_v2(customer_id_or_key, entitlement_id_or_feature_key, reset_entitlement_usage_input)
    except Exception as e:
        print("Exception when calling EntitlementsApi->reset_customer_entitlement_usage_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id_or_key** | [**ULIDOrExternalKey**](.md)|  | 
 **entitlement_id_or_feature_key** | **str**|  | 
 **reset_entitlement_usage_input** | [**ResetEntitlementUsageInput**](ResetEntitlementUsageInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **reset_entitlement_usage**
> reset_entitlement_usage(subject_id_or_key, entitlement_id, reset_entitlement_usage_input)

Reset subject entitlement

Reset marks the start of a new usage period for the entitlement and initiates grant rollover. At the start of a period usage is zerod out and grants are rolled over based on their rollover settings. It would typically be synced with the subjects billing period to enforce usage based on their subscription.  Usage is automatically reset for metered entitlements based on their usage period, but this endpoint allows to manually reset it at any time. When doing so the period anchor of the entitlement can be changed if needed.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.reset_entitlement_usage_input import ResetEntitlementUsageInput
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 
    entitlement_id = 'entitlement_id_example' # str | 
    reset_entitlement_usage_input = moolabs.ResetEntitlementUsageInput() # ResetEntitlementUsageInput | 

    try:
        # Reset subject entitlement
        api_instance.reset_entitlement_usage(subject_id_or_key, entitlement_id, reset_entitlement_usage_input)
    except Exception as e:
        print("Exception when calling EntitlementsApi->reset_entitlement_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 
 **entitlement_id** | **str**|  | 
 **reset_entitlement_usage_input** | [**ResetEntitlementUsageInput**](ResetEntitlementUsageInput.md)|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **void_grant_delete**
> void_grant_delete(grant_id)

Void grant

Voiding a grant means it is no longer valid, it doesn't take part in further balance calculations. Voiding a grant does not retroactively take effect, meaning any usage that has already been attributed to the grant will remain, but future usage cannot be burnt down from the grant. For example, if you have a single grant for your metered entitlement with an initial amount of 100, and so far 60 usage has been metered, the grant (and the entitlement itself) would have a balance of 40. If you then void that grant, balance becomes 0, but the 60 previous usage will not be affected.

### Example

* Bearer Authentication (CloudTokenAuth):

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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.EntitlementsApi(api_client)
    grant_id = 'grant_id_example' # str | 

    try:
        # Void grant
        api_instance.void_grant_delete(grant_id)
    except Exception as e:
        print("Exception when calling EntitlementsApi->void_grant_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

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
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

