# moolabs.MappingRulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rule_api**](MappingRulesApi.md#create_rule_api) | **POST** /api/v1/mapping-rules | Create Rule
[**disable_rule_api**](MappingRulesApi.md#disable_rule_api) | **DELETE** /api/v1/mapping-rules/{rule_id} | Disable Rule
[**dry_run_api_v1**](MappingRulesApi.md#dry_run_api_v1) | **POST** /api/v1/mapping-rules/dry-run | Dry Run
[**enable_tier3_api_v1**](MappingRulesApi.md#enable_tier3_api_v1) | **POST** /api/v1/mapping-rules/enable-tier3 | Enable Tier3
[**list_rules_api**](MappingRulesApi.md#list_rules_api) | **GET** /api/v1/mapping-rules | List Rules
[**update_rule_api**](MappingRulesApi.md#update_rule_api) | **PUT** /api/v1/mapping-rules/{rule_id} | Update Rule


# **create_rule_api**
> MappingRuleResponse create_rule_api(x_tenant_id, mapping_rule_create)

Create Rule

Create a new ingestion mapping rule for the tenant.  Validation: - source_field matching PII patterns is blocked for http_header source_type - target_field must be in VALID_TARGET_FIELDS

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.mapping_rule_create import MappingRuleCreate
from moolabs.models.mapping_rule_response import MappingRuleResponse
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
    api_instance = moolabs.MappingRulesApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | 
    mapping_rule_create = moolabs.MappingRuleCreate() # MappingRuleCreate | 

    try:
        # Create Rule
        api_response = api_instance.create_rule_api(x_tenant_id, mapping_rule_create)
        print("The response of MappingRulesApi->create_rule_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingRulesApi->create_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | 
 **mapping_rule_create** | [**MappingRuleCreate**](MappingRuleCreate.md)|  | 

### Return type

[**MappingRuleResponse**](MappingRuleResponse.md)

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

# **disable_rule_api**
> MappingRuleResponse disable_rule_api(rule_id, x_tenant_id)

Disable Rule

Soft-disable a mapping rule (sets is_enabled=False). Never hard-deletes rows. Writes audit log entry.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.mapping_rule_response import MappingRuleResponse
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
    api_instance = moolabs.MappingRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | 

    try:
        # Disable Rule
        api_response = api_instance.disable_rule_api(rule_id, x_tenant_id)
        print("The response of MappingRulesApi->disable_rule_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingRulesApi->disable_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **x_tenant_id** | **str**|  | 

### Return type

[**MappingRuleResponse**](MappingRuleResponse.md)

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

# **dry_run_api_v1**
> DryRunResponse dry_run_api_v1(x_tenant_id, dry_run_request)

Dry Run

Evaluate active mapping rules against a sample span without persisting anything.  Returns:   - derived_fields: fields that would be derived by the rule engine   - rules_applied: rules that successfully matched   - rules_skipped: rules that were skipped and why   - match_grade: always 'operational' for Tier 3   - note: reminder that Tier 3 data is operational-grade only

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.dry_run_request import DryRunRequest
from moolabs.models.dry_run_response import DryRunResponse
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
    api_instance = moolabs.MappingRulesApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | 
    dry_run_request = moolabs.DryRunRequest() # DryRunRequest | 

    try:
        # Dry Run
        api_response = api_instance.dry_run_api_v1(x_tenant_id, dry_run_request)
        print("The response of MappingRulesApi->dry_run_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingRulesApi->dry_run_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | 
 **dry_run_request** | [**DryRunRequest**](DryRunRequest.md)|  | 

### Return type

[**DryRunResponse**](DryRunResponse.md)

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

# **enable_tier3_api_v1**
> EnableTier3Response enable_tier3_api_v1(x_tenant_id)

Enable Tier3

Enable Tier 3 zero-code mapping for this tenant.  Upserts a connector_state row with connector_type='tier3_mapping', status='active'. Returns a warning that all attributed cost events will be operational-grade only.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.enable_tier3_response import EnableTier3Response
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
    api_instance = moolabs.MappingRulesApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | 

    try:
        # Enable Tier3
        api_response = api_instance.enable_tier3_api_v1(x_tenant_id)
        print("The response of MappingRulesApi->enable_tier3_api_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingRulesApi->enable_tier3_api_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | 

### Return type

[**EnableTier3Response**](EnableTier3Response.md)

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

# **list_rules_api**
> List[MappingRuleResponse] list_rules_api(x_tenant_id, enabled_only=enabled_only, include_audit=include_audit)

List Rules

List all mapping rules for the tenant ordered by priority ASC. Use ?enabled_only=false to include disabled rules. Use ?include_audit=true to include last 5 audit entries per rule.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.mapping_rule_response import MappingRuleResponse
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
    api_instance = moolabs.MappingRulesApi(api_client)
    x_tenant_id = 'x_tenant_id_example' # str | 
    enabled_only = True # bool | Return only enabled rules (optional) (default to True)
    include_audit = False # bool | Include last 5 audit entries per rule (optional) (default to False)

    try:
        # List Rules
        api_response = api_instance.list_rules_api(x_tenant_id, enabled_only=enabled_only, include_audit=include_audit)
        print("The response of MappingRulesApi->list_rules_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingRulesApi->list_rules_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant_id** | **str**|  | 
 **enabled_only** | **bool**| Return only enabled rules | [optional] [default to True]
 **include_audit** | **bool**| Include last 5 audit entries per rule | [optional] [default to False]

### Return type

[**List[MappingRuleResponse]**](MappingRuleResponse.md)

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

# **update_rule_api**
> MappingRuleResponse update_rule_api(rule_id, x_tenant_id, mapping_rule_update)

Update Rule

Update an existing mapping rule. Writes old values to audit log. Invalidates the Redis rules cache for the tenant.

### Example

* Api Key Authentication (APIKeyHeader):

```python
import moolabs
from moolabs.models.mapping_rule_response import MappingRuleResponse
from moolabs.models.mapping_rule_update import MappingRuleUpdate
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
    api_instance = moolabs.MappingRulesApi(api_client)
    rule_id = 'rule_id_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str | 
    mapping_rule_update = moolabs.MappingRuleUpdate() # MappingRuleUpdate | 

    try:
        # Update Rule
        api_response = api_instance.update_rule_api(rule_id, x_tenant_id, mapping_rule_update)
        print("The response of MappingRulesApi->update_rule_api:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingRulesApi->update_rule_api: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **x_tenant_id** | **str**|  | 
 **mapping_rule_update** | [**MappingRuleUpdate**](MappingRuleUpdate.md)|  | 

### Return type

[**MappingRuleResponse**](MappingRuleResponse.md)

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

