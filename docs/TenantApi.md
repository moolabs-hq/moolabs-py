# moolabs.TenantApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_portal_token_v1**](TenantApi.md#delete_portal_token_v1) | **DELETE** /v1/tenant/portal-tokens/{token_id} | Delete Portal Token
[**get_api_keys_v1**](TenantApi.md#get_api_keys_v1) | **GET** /v1/tenant/api-keys | Get Api Keys
[**get_audit_changes**](TenantApi.md#get_audit_changes) | **GET** /v1/tenant/audit/changes | Get Audit Changes
[**get_audit_evidence**](TenantApi.md#get_audit_evidence) | **GET** /v1/tenant/audit/evidence | Get Audit Evidence
[**get_audit_traces**](TenantApi.md#get_audit_traces) | **GET** /v1/tenant/audit/traces | Get Audit Traces
[**get_audit_warnings**](TenantApi.md#get_audit_warnings) | **GET** /v1/tenant/audit/warnings | Get Audit Warnings
[**get_domain**](TenantApi.md#get_domain) | **GET** /v1/tenant/communications/domain | Get Domain
[**get_effective_permissions_endpoint**](TenantApi.md#get_effective_permissions_endpoint) | **GET** /v1/tenant/permissions/effective | Get Effective Permissions Endpoint
[**get_feature_flags_v1**](TenantApi.md#get_feature_flags_v1) | **GET** /v1/tenant/audit/feature-flags | Get Feature Flags
[**get_integrations**](TenantApi.md#get_integrations) | **GET** /v1/tenant/integrations | Get Integrations
[**get_integrations_health**](TenantApi.md#get_integrations_health) | **GET** /v1/tenant/integrations/health | Get Integrations Health
[**get_integrations_mapping**](TenantApi.md#get_integrations_mapping) | **GET** /v1/tenant/integrations/mapping | Get Integrations Mapping
[**get_moometer_namespace_id_v1**](TenantApi.md#get_moometer_namespace_id_v1) | **GET** /v1/tenant/moometer-namespace | Get Moometer Namespace Id
[**get_portal_tokens_v1**](TenantApi.md#get_portal_tokens_v1) | **GET** /v1/tenant/portal-tokens | Get Portal Tokens
[**get_quote_settings_v1**](TenantApi.md#get_quote_settings_v1) | **GET** /v1/tenant/quote-settings | Get Quote Settings
[**get_revenue_recognition_v1**](TenantApi.md#get_revenue_recognition_v1) | **GET** /v1/tenant/revenue-recognition | Get Revenue Recognition
[**get_sender**](TenantApi.md#get_sender) | **GET** /v1/tenant/communications/sender | Get Sender
[**get_template**](TenantApi.md#get_template) | **GET** /v1/tenant/communications/templates/{template_id} | Get Template
[**get_templates_meta**](TenantApi.md#get_templates_meta) | **GET** /v1/tenant/communications/templates/meta | Get Templates Meta
[**get_tenant_context**](TenantApi.md#get_tenant_context) | **GET** /v1/tenant/context | Get Tenant Context
[**get_webhook**](TenantApi.md#get_webhook) | **GET** /v1/tenant/communications/webhook | Get Webhook
[**get_webhook_logs**](TenantApi.md#get_webhook_logs) | **GET** /v1/tenant/webhook/logs | Get Webhook Logs
[**get_webhook_metrics**](TenantApi.md#get_webhook_metrics) | **GET** /v1/tenant/webhook/metrics | Get Webhook Metrics
[**hubspot_connect**](TenantApi.md#hubspot_connect) | **POST** /v1/tenant/integrations/hubspot/connect | Hubspot Connect
[**hubspot_disconnect**](TenantApi.md#hubspot_disconnect) | **POST** /v1/tenant/integrations/hubspot/disconnect | Hubspot Disconnect
[**hubspot_oauth_callback**](TenantApi.md#hubspot_oauth_callback) | **GET** /v1/tenant/integrations/hubspot/oauth/callback | Hubspot Oauth Callback
[**hubspot_test_connection**](TenantApi.md#hubspot_test_connection) | **POST** /v1/tenant/integrations/hubspot/test | Hubspot Test Connection
[**issue_integration_key**](TenantApi.md#issue_integration_key) | **POST** /v1/tenant/integrations/{provider}/keys | Issue Integration Key
[**list_templates**](TenantApi.md#list_templates) | **GET** /v1/tenant/communications/templates | List Templates
[**netsuite_connect**](TenantApi.md#netsuite_connect) | **POST** /v1/tenant/integrations/netsuite/connect | Netsuite Connect
[**netsuite_disconnect**](TenantApi.md#netsuite_disconnect) | **POST** /v1/tenant/integrations/netsuite/disconnect | Netsuite Disconnect
[**netsuite_oauth_callback**](TenantApi.md#netsuite_oauth_callback) | **GET** /v1/tenant/integrations/netsuite/oauth/callback | Netsuite Oauth Callback
[**netsuite_test_connection**](TenantApi.md#netsuite_test_connection) | **POST** /v1/tenant/integrations/netsuite/test | Netsuite Test Connection
[**post_api_key_v1**](TenantApi.md#post_api_key_v1) | **POST** /v1/tenant/api-keys | Post Api Key
[**post_domain_verify**](TenantApi.md#post_domain_verify) | **POST** /v1/tenant/communications/domain/verify | Post Domain Verify
[**post_portal_token_v1**](TenantApi.md#post_portal_token_v1) | **POST** /v1/tenant/portal-tokens | Post Portal Token
[**post_revoke_api_key_v1**](TenantApi.md#post_revoke_api_key_v1) | **POST** /v1/tenant/api-keys/{key_id}/revoke | Post Revoke Api Key
[**preview_template**](TenantApi.md#preview_template) | **POST** /v1/tenant/communications/templates/{template_id}/preview | Preview Template
[**put_domain**](TenantApi.md#put_domain) | **PUT** /v1/tenant/communications/domain | Put Domain
[**put_feature_flag_v1**](TenantApi.md#put_feature_flag_v1) | **PUT** /v1/tenant/audit/feature-flags/{flag_id} | Put Feature Flag
[**put_integration**](TenantApi.md#put_integration) | **PUT** /v1/tenant/integrations/{provider} | Put Integration
[**put_quote_settings_v1**](TenantApi.md#put_quote_settings_v1) | **PUT** /v1/tenant/quote-settings | Put Quote Settings
[**put_sender**](TenantApi.md#put_sender) | **PUT** /v1/tenant/communications/sender | Put Sender
[**put_template**](TenantApi.md#put_template) | **PUT** /v1/tenant/communications/templates/{template_id} | Put Template
[**put_webhook**](TenantApi.md#put_webhook) | **PUT** /v1/tenant/communications/webhook | Put Webhook
[**quickbooks_connect**](TenantApi.md#quickbooks_connect) | **POST** /v1/tenant/integrations/quickbooks/connect | Quickbooks Connect
[**quickbooks_disconnect**](TenantApi.md#quickbooks_disconnect) | **POST** /v1/tenant/integrations/quickbooks/disconnect | Quickbooks Disconnect
[**quickbooks_oauth_callback**](TenantApi.md#quickbooks_oauth_callback) | **GET** /v1/tenant/integrations/quickbooks/oauth/callback | Quickbooks Oauth Callback
[**quickbooks_test_connection**](TenantApi.md#quickbooks_test_connection) | **POST** /v1/tenant/integrations/quickbooks/test | Quickbooks Test Connection
[**retry_failed_deliveries**](TenantApi.md#retry_failed_deliveries) | **POST** /v1/tenant/webhook/retry | Retry Failed Deliveries
[**revoke_all_api_keys_v1_tenant_danger**](TenantApi.md#revoke_all_api_keys_v1_tenant_danger) | **POST** /v1/tenant/danger/revoke-all-api-keys | Revoke All Api Keys
[**revoke_all_portal_tokens_v1_tenant_danger**](TenantApi.md#revoke_all_portal_tokens_v1_tenant_danger) | **POST** /v1/tenant/danger/revoke-all-portal-tokens | Revoke All Portal Tokens
[**salesforce_connect**](TenantApi.md#salesforce_connect) | **POST** /v1/tenant/integrations/salesforce/connect | Salesforce Connect
[**salesforce_disconnect**](TenantApi.md#salesforce_disconnect) | **POST** /v1/tenant/integrations/salesforce/disconnect | Salesforce Disconnect
[**salesforce_oauth_callback**](TenantApi.md#salesforce_oauth_callback) | **GET** /v1/tenant/integrations/salesforce/oauth/callback | Salesforce Oauth Callback
[**salesforce_test_connection**](TenantApi.md#salesforce_test_connection) | **POST** /v1/tenant/integrations/salesforce/test | Salesforce Test Connection
[**test_send_template_v1**](TenantApi.md#test_send_template_v1) | **POST** /v1/tenant/communications/templates/{template_id}/test-send | Test Send Template
[**test_webhook**](TenantApi.md#test_webhook) | **POST** /v1/tenant/communications/webhook/test | Test Webhook
[**update_revenue_recognition_v1**](TenantApi.md#update_revenue_recognition_v1) | **PUT** /v1/tenant/revenue-recognition | Update Revenue Recognition
[**xero_connect**](TenantApi.md#xero_connect) | **POST** /v1/tenant/integrations/xero/connect | Xero Connect
[**xero_disconnect**](TenantApi.md#xero_disconnect) | **POST** /v1/tenant/integrations/xero/disconnect | Xero Disconnect
[**xero_oauth_callback**](TenantApi.md#xero_oauth_callback) | **GET** /v1/tenant/integrations/xero/oauth/callback | Xero Oauth Callback
[**xero_test_connection**](TenantApi.md#xero_test_connection) | **POST** /v1/tenant/integrations/xero/test | Xero Test Connection


# **delete_portal_token_v1**
> object delete_portal_token_v1(token_id, revoke_portal_token_request=revoke_portal_token_request)

Delete Portal Token

Revoke a single portal token by ID.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.revoke_portal_token_request import RevokePortalTokenRequest
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
    api_instance = moolabs.TenantApi(api_client)
    token_id = 'token_id_example' # str | 
    revoke_portal_token_request = moolabs.RevokePortalTokenRequest() # RevokePortalTokenRequest |  (optional)

    try:
        # Delete Portal Token
        api_response = api_instance.delete_portal_token_v1(token_id, revoke_portal_token_request=revoke_portal_token_request)
        print("The response of TenantApi->delete_portal_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->delete_portal_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 
 **revoke_portal_token_request** | [**RevokePortalTokenRequest**](RevokePortalTokenRequest.md)|  | [optional] 

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

# **get_api_keys_v1**
> List[ApiKeyItem] get_api_keys_v1()

Get Api Keys

List API keys for the authenticated tenant (no plaintext).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.api_key_item import ApiKeyItem
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Api Keys
        api_response = api_instance.get_api_keys_v1()
        print("The response of TenantApi->get_api_keys_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_api_keys_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKeyItem]**](ApiKeyItem.md)

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

# **get_audit_changes**
> List[ChangeItem] get_audit_changes(limit=limit, section=section)

Get Audit Changes

List recent audit events for the tenant, optionally filtered by section.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.change_item import ChangeItem
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
    api_instance = moolabs.TenantApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    section = 'section_example' # str |  (optional)

    try:
        # Get Audit Changes
        api_response = api_instance.get_audit_changes(limit=limit, section=section)
        print("The response of TenantApi->get_audit_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_audit_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **section** | **str**|  | [optional] 

### Return type

[**List[ChangeItem]**](ChangeItem.md)

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

# **get_audit_evidence**
> object get_audit_evidence(limit=limit)

Get Audit Evidence

Return a downloadable JSON evidence package of recent audit events.  Response is returned as application/json with Content-Disposition: attachment so browsers download it directly.

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
    api_instance = moolabs.TenantApi(api_client)
    limit = 500 # int |  (optional) (default to 500)

    try:
        # Get Audit Evidence
        api_response = api_instance.get_audit_evidence(limit=limit)
        print("The response of TenantApi->get_audit_evidence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_audit_evidence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 500]

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

# **get_audit_traces**
> TracesResponse get_audit_traces()

Get Audit Traces

Get counts for ledger, outbox, DLQ, unpriced, warnings.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.traces_response import TracesResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Audit Traces
        api_response = api_instance.get_audit_traces()
        print("The response of TenantApi->get_audit_traces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_audit_traces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TracesResponse**](TracesResponse.md)

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

# **get_audit_warnings**
> List[WarningItem] get_audit_warnings(limit=limit)

Get Audit Warnings

List recent warnings (e.g. outbox delivery failures).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.warning_item import WarningItem
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
    api_instance = moolabs.TenantApi(api_client)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # Get Audit Warnings
        api_response = api_instance.get_audit_warnings(limit=limit)
        print("The response of TenantApi->get_audit_warnings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_audit_warnings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**List[WarningItem]**](WarningItem.md)

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

# **get_domain**
> DomainResponse get_domain()

Get Domain

Get domain and verification status.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.domain_response import DomainResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Domain
        api_response = api_instance.get_domain()
        print("The response of TenantApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_domain: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **get_effective_permissions_endpoint**
> EffectivePermissionsResponse get_effective_permissions_endpoint()

Get Effective Permissions Endpoint

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.effective_permissions_response import EffectivePermissionsResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Effective Permissions Endpoint
        api_response = api_instance.get_effective_permissions_endpoint()
        print("The response of TenantApi->get_effective_permissions_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_effective_permissions_endpoint: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EffectivePermissionsResponse**](EffectivePermissionsResponse.md)

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

# **get_feature_flags_v1**
> List[FeatureFlagItem] get_feature_flags_v1()

Get Feature Flags

List feature flags with tenant override and default merged.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.feature_flag_item import FeatureFlagItem
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Feature Flags
        api_response = api_instance.get_feature_flags_v1()
        print("The response of TenantApi->get_feature_flags_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_feature_flags_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FeatureFlagItem]**](FeatureFlagItem.md)

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

# **get_integrations**
> List[ConnectorItem] get_integrations()

Get Integrations

List integration connectors with tenant status.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.connector_item import ConnectorItem
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Integrations
        api_response = api_instance.get_integrations()
        print("The response of TenantApi->get_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConnectorItem]**](ConnectorItem.md)

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

# **get_integrations_health**
> object get_integrations_health()

Get Integrations Health

Return integration health summary: connected count, failed syncs, webhook health, mapping coverage.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Integrations Health
        api_response = api_instance.get_integrations_health()
        print("The response of TenantApi->get_integrations_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_integrations_health: %s\n" % e)
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

# **get_integrations_mapping**
> List[MeterMappingItem] get_integrations_mapping()

Get Integrations Mapping

Return meter-to-feature key mappings for this tenant.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.meter_mapping_item import MeterMappingItem
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Integrations Mapping
        api_response = api_instance.get_integrations_mapping()
        print("The response of TenantApi->get_integrations_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_integrations_mapping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MeterMappingItem]**](MeterMappingItem.md)

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

# **get_moometer_namespace_id_v1**
> object get_moometer_namespace_id_v1()

Get Moometer Namespace Id

MooMeter namespace for the authenticated tenant.  Clerk/org-backed tenants are stored internally by UUID, but their MooMeter namespace is the external org ID. The UI uses this value for direct OpenMeter proxy calls such as customer subscriptions.  Response shape:   - ``namespace`` (preferred): the MooMeter namespace string.   - ``internal_tenant_id``: the BFF tenant UUID (for debugging/correlation).   - ``tenant_id`` (DEPRECATED — same as ``namespace``): kept for one     rolling deploy window so the UI keeps working during the BFF→UI     upgrade. The UI already prefers ``namespace``; remove this field     once all UI deploys are on the new helper. Do not use this field     from any new caller — it does NOT contain the internal UUID.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Moometer Namespace Id
        api_response = api_instance.get_moometer_namespace_id_v1()
        print("The response of TenantApi->get_moometer_namespace_id_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_moometer_namespace_id_v1: %s\n" % e)
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

# **get_portal_tokens_v1**
> List[PortalTokenItem] get_portal_tokens_v1()

Get Portal Tokens

List active portal tokens for the authenticated tenant.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.portal_token_item import PortalTokenItem
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Portal Tokens
        api_response = api_instance.get_portal_tokens_v1()
        print("The response of TenantApi->get_portal_tokens_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_portal_tokens_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortalTokenItem]**](PortalTokenItem.md)

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

# **get_quote_settings_v1**
> QuoteSettingsResponse get_quote_settings_v1()

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Quote Settings
        api_response = api_instance.get_quote_settings_v1()
        print("The response of TenantApi->get_quote_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_quote_settings_v1: %s\n" % e)
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

# **get_revenue_recognition_v1**
> object get_revenue_recognition_v1()

Get Revenue Recognition

Get tenant revenue recognition config. Returns defaults if not yet configured.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Revenue Recognition
        api_response = api_instance.get_revenue_recognition_v1()
        print("The response of TenantApi->get_revenue_recognition_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_revenue_recognition_v1: %s\n" % e)
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

# **get_sender**
> SenderResponse get_sender()

Get Sender

Get sender identity for the authenticated tenant.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.sender_response import SenderResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Sender
        api_response = api_instance.get_sender()
        print("The response of TenantApi->get_sender:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_sender: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SenderResponse**](SenderResponse.md)

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

# **get_template**
> TemplateItem get_template(template_id)

Get Template

Get one template by id.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.template_item import TemplateItem
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
    api_instance = moolabs.TenantApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Get Template
        api_response = api_instance.get_template(template_id)
        print("The response of TenantApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**TemplateItem**](TemplateItem.md)

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

# **get_templates_meta**
> TemplateMetaResponse get_templates_meta()

Get Templates Meta

Get canonical template metadata and variable contract.

### Example


```python
import moolabs
from moolabs.models.template_meta_response import TemplateMetaResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Templates Meta
        api_response = api_instance.get_templates_meta()
        print("The response of TenantApi->get_templates_meta:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_templates_meta: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TemplateMetaResponse**](TemplateMetaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_context**
> object get_tenant_context()

Get Tenant Context

Return tenant info, pools, and current credit economics for the authenticated tenant.  Used by the Settings overview and billing pages. Requires portal token or API key.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Tenant Context
        api_response = api_instance.get_tenant_context()
        print("The response of TenantApi->get_tenant_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_context: %s\n" % e)
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

# **get_webhook**
> WebhookResponse get_webhook()

Get Webhook

Get webhook config for the authenticated tenant (no secret).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.webhook_response import WebhookResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Webhook
        api_response = api_instance.get_webhook()
        print("The response of TenantApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_webhook: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookResponse**](WebhookResponse.md)

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

# **get_webhook_logs**
> object get_webhook_logs(limit=limit)

Get Webhook Logs

Return recent outbox delivery log entries, newest first.

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
    api_instance = moolabs.TenantApi(api_client)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # Get Webhook Logs
        api_response = api_instance.get_webhook_logs(limit=limit)
        print("The response of TenantApi->get_webhook_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_webhook_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]

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

# **get_webhook_metrics**
> object get_webhook_metrics()

Get Webhook Metrics

Return aggregated delivery metrics for the tenant's webhook from LedgerOutbox.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Get Webhook Metrics
        api_response = api_instance.get_webhook_metrics()
        print("The response of TenantApi->get_webhook_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_webhook_metrics: %s\n" % e)
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

# **hubspot_connect**
> object hubspot_connect(hub_spot_connect_request)

Hubspot Connect

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.hub_spot_connect_request import HubSpotConnectRequest
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
    api_instance = moolabs.TenantApi(api_client)
    hub_spot_connect_request = moolabs.HubSpotConnectRequest() # HubSpotConnectRequest | 

    try:
        # Hubspot Connect
        api_response = api_instance.hubspot_connect(hub_spot_connect_request)
        print("The response of TenantApi->hubspot_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->hubspot_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_spot_connect_request** | [**HubSpotConnectRequest**](HubSpotConnectRequest.md)|  | 

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

# **hubspot_disconnect**
> object hubspot_disconnect()

Hubspot Disconnect

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Hubspot Disconnect
        api_response = api_instance.hubspot_disconnect()
        print("The response of TenantApi->hubspot_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->hubspot_disconnect: %s\n" % e)
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

# **hubspot_oauth_callback**
> object hubspot_oauth_callback(code, state)

Hubspot Oauth Callback

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
    api_instance = moolabs.TenantApi(api_client)
    code = 'code_example' # str | 
    state = 'state_example' # str | 

    try:
        # Hubspot Oauth Callback
        api_response = api_instance.hubspot_oauth_callback(code, state)
        print("The response of TenantApi->hubspot_oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->hubspot_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | 

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

# **hubspot_test_connection**
> object hubspot_test_connection()

Hubspot Test Connection

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Hubspot Test Connection
        api_response = api_instance.hubspot_test_connection()
        print("The response of TenantApi->hubspot_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->hubspot_test_connection: %s\n" % e)
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

# **issue_integration_key**
> object issue_integration_key(provider)

Issue Integration Key

Issue an API key for an integration provider (e.g. NetSuite).  Returns the plaintext key once — store it immediately. Revokes any existing key for this tenant+provider. Calling again is safe if the key was not received (single-active-key policy).

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
    api_instance = moolabs.TenantApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Issue Integration Key
        api_response = api_instance.issue_integration_key(provider)
        print("The response of TenantApi->issue_integration_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->issue_integration_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

# **list_templates**
> List[TemplateItem] list_templates()

List Templates

List email templates with tenant overrides merged.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.template_item import TemplateItem
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # List Templates
        api_response = api_instance.list_templates()
        print("The response of TenantApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->list_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TemplateItem]**](TemplateItem.md)

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

# **netsuite_connect**
> object netsuite_connect(net_suite_connect_request)

Netsuite Connect

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.net_suite_connect_request import NetSuiteConnectRequest
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
    api_instance = moolabs.TenantApi(api_client)
    net_suite_connect_request = moolabs.NetSuiteConnectRequest() # NetSuiteConnectRequest | 

    try:
        # Netsuite Connect
        api_response = api_instance.netsuite_connect(net_suite_connect_request)
        print("The response of TenantApi->netsuite_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->netsuite_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_suite_connect_request** | [**NetSuiteConnectRequest**](NetSuiteConnectRequest.md)|  | 

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

# **netsuite_disconnect**
> object netsuite_disconnect()

Netsuite Disconnect

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Netsuite Disconnect
        api_response = api_instance.netsuite_disconnect()
        print("The response of TenantApi->netsuite_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->netsuite_disconnect: %s\n" % e)
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

# **netsuite_oauth_callback**
> object netsuite_oauth_callback(code, state)

Netsuite Oauth Callback

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
    api_instance = moolabs.TenantApi(api_client)
    code = 'code_example' # str | 
    state = 'state_example' # str | 

    try:
        # Netsuite Oauth Callback
        api_response = api_instance.netsuite_oauth_callback(code, state)
        print("The response of TenantApi->netsuite_oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->netsuite_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | 

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

# **netsuite_test_connection**
> object netsuite_test_connection()

Netsuite Test Connection

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Netsuite Test Connection
        api_response = api_instance.netsuite_test_connection()
        print("The response of TenantApi->netsuite_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->netsuite_test_connection: %s\n" % e)
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

# **post_api_key_v1**
> CreateApiKeyResponse post_api_key_v1(create_api_key_request)

Post Api Key

Create an API key. Plaintext returned only in this response.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.create_api_key_request import CreateApiKeyRequest
from moolabs.models.create_api_key_response import CreateApiKeyResponse
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
    api_instance = moolabs.TenantApi(api_client)
    create_api_key_request = moolabs.CreateApiKeyRequest() # CreateApiKeyRequest | 

    try:
        # Post Api Key
        api_response = api_instance.post_api_key_v1(create_api_key_request)
        print("The response of TenantApi->post_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->post_api_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_request** | [**CreateApiKeyRequest**](CreateApiKeyRequest.md)|  | 

### Return type

[**CreateApiKeyResponse**](CreateApiKeyResponse.md)

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

# **post_domain_verify**
> DomainResponse post_domain_verify()

Post Domain Verify

Trigger domain verification via Resend and persist status.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.domain_response import DomainResponse
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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Post Domain Verify
        api_response = api_instance.post_domain_verify()
        print("The response of TenantApi->post_domain_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->post_domain_verify: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **post_portal_token_v1**
> CreatePortalTokenResponse post_portal_token_v1(app_api_v1_tenant_access_router_create_portal_token_request)

Post Portal Token

Create a portal token for the given subject. Subject must have wallet membership in this tenant. Token returned only once.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.app_api_v1_tenant_access_router_create_portal_token_request import AppApiV1TenantAccessRouterCreatePortalTokenRequest
from moolabs.models.create_portal_token_response import CreatePortalTokenResponse
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
    api_instance = moolabs.TenantApi(api_client)
    app_api_v1_tenant_access_router_create_portal_token_request = moolabs.AppApiV1TenantAccessRouterCreatePortalTokenRequest() # AppApiV1TenantAccessRouterCreatePortalTokenRequest | 

    try:
        # Post Portal Token
        api_response = api_instance.post_portal_token_v1(app_api_v1_tenant_access_router_create_portal_token_request)
        print("The response of TenantApi->post_portal_token_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->post_portal_token_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_api_v1_tenant_access_router_create_portal_token_request** | [**AppApiV1TenantAccessRouterCreatePortalTokenRequest**](AppApiV1TenantAccessRouterCreatePortalTokenRequest.md)|  | 

### Return type

[**CreatePortalTokenResponse**](CreatePortalTokenResponse.md)

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

# **post_revoke_api_key_v1**
> object post_revoke_api_key_v1(key_id, revoke_api_key_request)

Post Revoke Api Key

Revoke an API key.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.revoke_api_key_request import RevokeApiKeyRequest
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
    api_instance = moolabs.TenantApi(api_client)
    key_id = 'key_id_example' # str | 
    revoke_api_key_request = moolabs.RevokeApiKeyRequest() # RevokeApiKeyRequest | 

    try:
        # Post Revoke Api Key
        api_response = api_instance.post_revoke_api_key_v1(key_id, revoke_api_key_request)
        print("The response of TenantApi->post_revoke_api_key_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->post_revoke_api_key_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 
 **revoke_api_key_request** | [**RevokeApiKeyRequest**](RevokeApiKeyRequest.md)|  | 

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

# **preview_template**
> TemplatePreviewResponse preview_template(template_id, template_preview_request)

Preview Template

Render template preview with sample context values.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.template_preview_request import TemplatePreviewRequest
from moolabs.models.template_preview_response import TemplatePreviewResponse
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
    api_instance = moolabs.TenantApi(api_client)
    template_id = 'template_id_example' # str | 
    template_preview_request = moolabs.TemplatePreviewRequest() # TemplatePreviewRequest | 

    try:
        # Preview Template
        api_response = api_instance.preview_template(template_id, template_preview_request)
        print("The response of TenantApi->preview_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->preview_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **template_preview_request** | [**TemplatePreviewRequest**](TemplatePreviewRequest.md)|  | 

### Return type

[**TemplatePreviewResponse**](TemplatePreviewResponse.md)

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

# **put_domain**
> DomainResponse put_domain(domain_update)

Put Domain

Set branded domain (status becomes pending).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.domain_response import DomainResponse
from moolabs.models.domain_update import DomainUpdate
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
    api_instance = moolabs.TenantApi(api_client)
    domain_update = moolabs.DomainUpdate() # DomainUpdate | 

    try:
        # Put Domain
        api_response = api_instance.put_domain(domain_update)
        print("The response of TenantApi->put_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_update** | [**DomainUpdate**](DomainUpdate.md)|  | 

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **put_feature_flag_v1**
> FeatureFlagItem put_feature_flag_v1(flag_id, feature_flag_update)

Put Feature Flag

Set tenant override for a feature flag.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.feature_flag_item import FeatureFlagItem
from moolabs.models.feature_flag_update import FeatureFlagUpdate
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
    api_instance = moolabs.TenantApi(api_client)
    flag_id = 'flag_id_example' # str | 
    feature_flag_update = moolabs.FeatureFlagUpdate() # FeatureFlagUpdate | 

    try:
        # Put Feature Flag
        api_response = api_instance.put_feature_flag_v1(flag_id, feature_flag_update)
        print("The response of TenantApi->put_feature_flag_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_feature_flag_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag_id** | **str**|  | 
 **feature_flag_update** | [**FeatureFlagUpdate**](FeatureFlagUpdate.md)|  | 

### Return type

[**FeatureFlagItem**](FeatureFlagItem.md)

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

# **put_integration**
> ConnectorItem put_integration(provider, integration_update)

Put Integration

Set connector status and/or config.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.connector_item import ConnectorItem
from moolabs.models.integration_update import IntegrationUpdate
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
    api_instance = moolabs.TenantApi(api_client)
    provider = 'provider_example' # str | 
    integration_update = moolabs.IntegrationUpdate() # IntegrationUpdate | 

    try:
        # Put Integration
        api_response = api_instance.put_integration(provider, integration_update)
        print("The response of TenantApi->put_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **integration_update** | [**IntegrationUpdate**](IntegrationUpdate.md)|  | 

### Return type

[**ConnectorItem**](ConnectorItem.md)

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

# **put_quote_settings_v1**
> QuoteSettingsResponse put_quote_settings_v1(update_quote_settings_request)

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
    api_instance = moolabs.TenantApi(api_client)
    update_quote_settings_request = moolabs.UpdateQuoteSettingsRequest() # UpdateQuoteSettingsRequest | 

    try:
        # Put Quote Settings
        api_response = api_instance.put_quote_settings_v1(update_quote_settings_request)
        print("The response of TenantApi->put_quote_settings_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_quote_settings_v1: %s\n" % e)
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

# **put_sender**
> SenderResponse put_sender(sender_update)

Put Sender

Update sender identity.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.sender_response import SenderResponse
from moolabs.models.sender_update import SenderUpdate
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
    api_instance = moolabs.TenantApi(api_client)
    sender_update = moolabs.SenderUpdate() # SenderUpdate | 

    try:
        # Put Sender
        api_response = api_instance.put_sender(sender_update)
        print("The response of TenantApi->put_sender:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_sender: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_update** | [**SenderUpdate**](SenderUpdate.md)|  | 

### Return type

[**SenderResponse**](SenderResponse.md)

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

# **put_template**
> TemplateItem put_template(template_id, template_update)

Put Template

Update template override.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.template_item import TemplateItem
from moolabs.models.template_update import TemplateUpdate
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
    api_instance = moolabs.TenantApi(api_client)
    template_id = 'template_id_example' # str | 
    template_update = moolabs.TemplateUpdate() # TemplateUpdate | 

    try:
        # Put Template
        api_response = api_instance.put_template(template_id, template_update)
        print("The response of TenantApi->put_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **template_update** | [**TemplateUpdate**](TemplateUpdate.md)|  | 

### Return type

[**TemplateItem**](TemplateItem.md)

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

# **put_webhook**
> WebhookResponse put_webhook(webhook_update)

Put Webhook

Set webhook URL and auth. Secret only sent when changing.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.webhook_response import WebhookResponse
from moolabs.models.webhook_update import WebhookUpdate
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
    api_instance = moolabs.TenantApi(api_client)
    webhook_update = moolabs.WebhookUpdate() # WebhookUpdate | 

    try:
        # Put Webhook
        api_response = api_instance.put_webhook(webhook_update)
        print("The response of TenantApi->put_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->put_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_update** | [**WebhookUpdate**](WebhookUpdate.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

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

# **quickbooks_connect**
> object quickbooks_connect(quick_books_connect_request)

Quickbooks Connect

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quick_books_connect_request import QuickBooksConnectRequest
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
    api_instance = moolabs.TenantApi(api_client)
    quick_books_connect_request = moolabs.QuickBooksConnectRequest() # QuickBooksConnectRequest | 

    try:
        # Quickbooks Connect
        api_response = api_instance.quickbooks_connect(quick_books_connect_request)
        print("The response of TenantApi->quickbooks_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->quickbooks_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_books_connect_request** | [**QuickBooksConnectRequest**](QuickBooksConnectRequest.md)|  | 

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

# **quickbooks_disconnect**
> object quickbooks_disconnect()

Quickbooks Disconnect

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Quickbooks Disconnect
        api_response = api_instance.quickbooks_disconnect()
        print("The response of TenantApi->quickbooks_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->quickbooks_disconnect: %s\n" % e)
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

# **quickbooks_oauth_callback**
> object quickbooks_oauth_callback(code, state, realm_id=realm_id)

Quickbooks Oauth Callback

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
    api_instance = moolabs.TenantApi(api_client)
    code = 'code_example' # str | 
    state = 'state_example' # str | 
    realm_id = 'realm_id_example' # str |  (optional)

    try:
        # Quickbooks Oauth Callback
        api_response = api_instance.quickbooks_oauth_callback(code, state, realm_id=realm_id)
        print("The response of TenantApi->quickbooks_oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->quickbooks_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | 
 **realm_id** | **str**|  | [optional] 

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

# **quickbooks_test_connection**
> object quickbooks_test_connection()

Quickbooks Test Connection

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Quickbooks Test Connection
        api_response = api_instance.quickbooks_test_connection()
        print("The response of TenantApi->quickbooks_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->quickbooks_test_connection: %s\n" % e)
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

# **retry_failed_deliveries**
> object retry_failed_deliveries()

Retry Failed Deliveries

Reset failed outbox events so the delivery worker retries them.  Resets attempts to 0 for all events with delivered_at IS NULL and attempts > 0, making them eligible for the next delivery worker pass.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Retry Failed Deliveries
        api_response = api_instance.retry_failed_deliveries()
        print("The response of TenantApi->retry_failed_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->retry_failed_deliveries: %s\n" % e)
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

# **revoke_all_api_keys_v1_tenant_danger**
> object revoke_all_api_keys_v1_tenant_danger(danger_request)

Revoke All Api Keys

Revoke all active API keys for this tenant, disabling all machine access.  Requires audit_note and confirm=true. All API-key authenticated calls will fail after this operation. This action is logged with full audit trail.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.danger_request import DangerRequest
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
    api_instance = moolabs.TenantApi(api_client)
    danger_request = moolabs.DangerRequest() # DangerRequest | 

    try:
        # Revoke All Api Keys
        api_response = api_instance.revoke_all_api_keys_v1_tenant_danger(danger_request)
        print("The response of TenantApi->revoke_all_api_keys_v1_tenant_danger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->revoke_all_api_keys_v1_tenant_danger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **danger_request** | [**DangerRequest**](DangerRequest.md)|  | 

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

# **revoke_all_portal_tokens_v1_tenant_danger**
> object revoke_all_portal_tokens_v1_tenant_danger(danger_request)

Revoke All Portal Tokens

Revoke all active portal tokens for this tenant immediately.  Requires audit_note and confirm=true. All active customer portal sessions will be invalidated. This action is logged with full audit trail.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.danger_request import DangerRequest
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
    api_instance = moolabs.TenantApi(api_client)
    danger_request = moolabs.DangerRequest() # DangerRequest | 

    try:
        # Revoke All Portal Tokens
        api_response = api_instance.revoke_all_portal_tokens_v1_tenant_danger(danger_request)
        print("The response of TenantApi->revoke_all_portal_tokens_v1_tenant_danger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->revoke_all_portal_tokens_v1_tenant_danger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **danger_request** | [**DangerRequest**](DangerRequest.md)|  | 

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

# **salesforce_connect**
> object salesforce_connect(salesforce_connect_request)

Salesforce Connect

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.salesforce_connect_request import SalesforceConnectRequest
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
    api_instance = moolabs.TenantApi(api_client)
    salesforce_connect_request = moolabs.SalesforceConnectRequest() # SalesforceConnectRequest | 

    try:
        # Salesforce Connect
        api_response = api_instance.salesforce_connect(salesforce_connect_request)
        print("The response of TenantApi->salesforce_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->salesforce_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_connect_request** | [**SalesforceConnectRequest**](SalesforceConnectRequest.md)|  | 

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

# **salesforce_disconnect**
> object salesforce_disconnect()

Salesforce Disconnect

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Salesforce Disconnect
        api_response = api_instance.salesforce_disconnect()
        print("The response of TenantApi->salesforce_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->salesforce_disconnect: %s\n" % e)
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

# **salesforce_oauth_callback**
> object salesforce_oauth_callback(code, state)

Salesforce Oauth Callback

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
    api_instance = moolabs.TenantApi(api_client)
    code = 'code_example' # str | 
    state = 'state_example' # str | 

    try:
        # Salesforce Oauth Callback
        api_response = api_instance.salesforce_oauth_callback(code, state)
        print("The response of TenantApi->salesforce_oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->salesforce_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | 

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

# **salesforce_test_connection**
> object salesforce_test_connection()

Salesforce Test Connection

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Salesforce Test Connection
        api_response = api_instance.salesforce_test_connection()
        print("The response of TenantApi->salesforce_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->salesforce_test_connection: %s\n" % e)
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

# **test_send_template_v1**
> TemplateTestSendResponse test_send_template_v1(template_id, template_test_send_request)

Test Send Template

Send a test email for a template.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.template_test_send_request import TemplateTestSendRequest
from moolabs.models.template_test_send_response import TemplateTestSendResponse
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
    api_instance = moolabs.TenantApi(api_client)
    template_id = 'template_id_example' # str | 
    template_test_send_request = moolabs.TemplateTestSendRequest() # TemplateTestSendRequest | 

    try:
        # Test Send Template
        api_response = api_instance.test_send_template_v1(template_id, template_test_send_request)
        print("The response of TenantApi->test_send_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->test_send_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **template_test_send_request** | [**TemplateTestSendRequest**](TemplateTestSendRequest.md)|  | 

### Return type

[**TemplateTestSendResponse**](TemplateTestSendResponse.md)

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

# **test_webhook**
> object test_webhook()

Test Webhook

Send a test delivery to the configured webhook URL.

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Test Webhook
        api_response = api_instance.test_webhook()
        print("The response of TenantApi->test_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->test_webhook: %s\n" % e)
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

# **update_revenue_recognition_v1**
> object update_revenue_recognition_v1(revenue_recognition_request)

Update Revenue Recognition

Update tenant revenue recognition config. Creates on first PUT (lazy upsert).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.revenue_recognition_request import RevenueRecognitionRequest
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
    api_instance = moolabs.TenantApi(api_client)
    revenue_recognition_request = moolabs.RevenueRecognitionRequest() # RevenueRecognitionRequest | 

    try:
        # Update Revenue Recognition
        api_response = api_instance.update_revenue_recognition_v1(revenue_recognition_request)
        print("The response of TenantApi->update_revenue_recognition_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->update_revenue_recognition_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revenue_recognition_request** | [**RevenueRecognitionRequest**](RevenueRecognitionRequest.md)|  | 

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

# **xero_connect**
> object xero_connect(xero_connect_request)

Xero Connect

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.xero_connect_request import XeroConnectRequest
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
    api_instance = moolabs.TenantApi(api_client)
    xero_connect_request = moolabs.XeroConnectRequest() # XeroConnectRequest | 

    try:
        # Xero Connect
        api_response = api_instance.xero_connect(xero_connect_request)
        print("The response of TenantApi->xero_connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->xero_connect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xero_connect_request** | [**XeroConnectRequest**](XeroConnectRequest.md)|  | 

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

# **xero_disconnect**
> object xero_disconnect()

Xero Disconnect

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Xero Disconnect
        api_response = api_instance.xero_disconnect()
        print("The response of TenantApi->xero_disconnect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->xero_disconnect: %s\n" % e)
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

# **xero_oauth_callback**
> object xero_oauth_callback(code, state)

Xero Oauth Callback

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
    api_instance = moolabs.TenantApi(api_client)
    code = 'code_example' # str | 
    state = 'state_example' # str | 

    try:
        # Xero Oauth Callback
        api_response = api_instance.xero_oauth_callback(code, state)
        print("The response of TenantApi->xero_oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->xero_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **state** | **str**|  | 

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

# **xero_test_connection**
> object xero_test_connection()

Xero Test Connection

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
    api_instance = moolabs.TenantApi(api_client)

    try:
        # Xero Test Connection
        api_response = api_instance.xero_test_connection()
        print("The response of TenantApi->xero_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->xero_test_connection: %s\n" % e)
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

