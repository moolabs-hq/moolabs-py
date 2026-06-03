# moolabs.DunningTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_disclosure_policy_v1_arc_dunning**](DunningTemplatesApi.md#get_disclosure_policy_v1_arc_dunning) | **GET** /v1/arc/dunning-template-disclosure-policy | Get Disclosure Policy
[**get_dunning_template_registry_v1_arc**](DunningTemplatesApi.md#get_dunning_template_registry_v1_arc) | **GET** /v1/arc/dunning-template-registry | Get Dunning Template Registry
[**get_dunning_template_version_v1**](DunningTemplatesApi.md#get_dunning_template_version_v1) | **GET** /v1/arc/dunning-templates/{template_key}/versions/{version_id} | Get Dunning Template Version
[**get_payment_instructions_v1_arc_dunning**](DunningTemplatesApi.md#get_payment_instructions_v1_arc_dunning) | **GET** /v1/arc/dunning-template-payment-instructions | Get Payment Instructions
[**get_provider_readiness_v1_arc_dunning**](DunningTemplatesApi.md#get_provider_readiness_v1_arc_dunning) | **GET** /v1/arc/dunning-template-provider-readiness | Get Provider Readiness
[**get_template_keys_v1_arc**](DunningTemplatesApi.md#get_template_keys_v1_arc) | **GET** /v1/arc/dunning-template-keys | Get Template Keys
[**list_dunning_template_versions_v1**](DunningTemplatesApi.md#list_dunning_template_versions_v1) | **GET** /v1/arc/dunning-templates/{template_key}/versions | List Dunning Template Versions
[**lock_dunning_template_draft_v1**](DunningTemplatesApi.md#lock_dunning_template_draft_v1) | **POST** /v1/arc/dunning-templates/{template_key}/drafts/{version_id}/lock | Lock Dunning Template Draft
[**post_archive_template_key_v1_arc**](DunningTemplatesApi.md#post_archive_template_key_v1_arc) | **POST** /v1/arc/dunning-template-keys/{template_key}/archive | Post Archive Template Key
[**post_template_key_v1_arc**](DunningTemplatesApi.md#post_template_key_v1_arc) | **POST** /v1/arc/dunning-template-keys | Post Template Key
[**post_template_test_send_v1_arc_dunning**](DunningTemplatesApi.md#post_template_test_send_v1_arc_dunning) | **POST** /v1/arc/dunning-template-test-sends | Post Template Test Send
[**preview_dunning_template_v1**](DunningTemplatesApi.md#preview_dunning_template_v1) | **POST** /v1/arc/dunning-templates/{template_key}/preview | Preview Dunning Template
[**publish_dunning_template_v1**](DunningTemplatesApi.md#publish_dunning_template_v1) | **POST** /v1/arc/dunning-templates/{template_key}/publish | Publish Dunning Template
[**put_disclosure_policy_v1_arc_dunning**](DunningTemplatesApi.md#put_disclosure_policy_v1_arc_dunning) | **PUT** /v1/arc/dunning-template-disclosure-policy | Put Disclosure Policy
[**put_payment_instructions_v1_arc_dunning**](DunningTemplatesApi.md#put_payment_instructions_v1_arc_dunning) | **PUT** /v1/arc/dunning-template-payment-instructions | Put Payment Instructions
[**save_dunning_template_draft_v1**](DunningTemplatesApi.md#save_dunning_template_draft_v1) | **POST** /v1/arc/dunning-templates/{template_key}/drafts | Save Dunning Template Draft
[**unlock_dunning_template_draft_v1**](DunningTemplatesApi.md#unlock_dunning_template_draft_v1) | **POST** /v1/arc/dunning-templates/{template_key}/drafts/{version_id}/unlock | Unlock Dunning Template Draft
[**validate_dunning_template_v1**](DunningTemplatesApi.md#validate_dunning_template_v1) | **POST** /v1/arc/dunning-templates/{template_key}/validate | Validate Dunning Template


# **get_disclosure_policy_v1_arc_dunning**
> DisclosurePolicyResponse get_disclosure_policy_v1_arc_dunning(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Get Disclosure Policy

### Example


```python
import moolabs
from moolabs.models.disclosure_policy_response import DisclosurePolicyResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Disclosure Policy
        api_response = api_instance.get_disclosure_policy_v1_arc_dunning(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->get_disclosure_policy_v1_arc_dunning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->get_disclosure_policy_v1_arc_dunning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DisclosurePolicyResponse**](DisclosurePolicyResponse.md)

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

# **get_dunning_template_registry_v1_arc**
> object get_dunning_template_registry_v1_arc(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Get Dunning Template Registry

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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Dunning Template Registry
        api_response = api_instance.get_dunning_template_registry_v1_arc(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->get_dunning_template_registry_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->get_dunning_template_registry_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

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

# **get_dunning_template_version_v1**
> TemplateVersionResponse get_dunning_template_version_v1(template_key, version_id, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Get Dunning Template Version

### Example


```python
import moolabs
from moolabs.models.template_version_response import TemplateVersionResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    version_id = 'version_id_example' # str | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Dunning Template Version
        api_response = api_instance.get_dunning_template_version_v1(template_key, version_id, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->get_dunning_template_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->get_dunning_template_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **version_id** | **str**|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateVersionResponse**](TemplateVersionResponse.md)

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

# **get_payment_instructions_v1_arc_dunning**
> PaymentInstructionsResponse get_payment_instructions_v1_arc_dunning(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Get Payment Instructions

### Example


```python
import moolabs
from moolabs.models.payment_instructions_response import PaymentInstructionsResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Payment Instructions
        api_response = api_instance.get_payment_instructions_v1_arc_dunning(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->get_payment_instructions_v1_arc_dunning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->get_payment_instructions_v1_arc_dunning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PaymentInstructionsResponse**](PaymentInstructionsResponse.md)

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

# **get_provider_readiness_v1_arc_dunning**
> ProviderReadinessResponse get_provider_readiness_v1_arc_dunning(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Get Provider Readiness

### Example


```python
import moolabs
from moolabs.models.provider_readiness_response import ProviderReadinessResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Provider Readiness
        api_response = api_instance.get_provider_readiness_v1_arc_dunning(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->get_provider_readiness_v1_arc_dunning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->get_provider_readiness_v1_arc_dunning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ProviderReadinessResponse**](ProviderReadinessResponse.md)

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

# **get_template_keys_v1_arc**
> TemplateKeyListResponse get_template_keys_v1_arc(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Get Template Keys

### Example


```python
import moolabs
from moolabs.models.template_key_list_response import TemplateKeyListResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Get Template Keys
        api_response = api_instance.get_template_keys_v1_arc(x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->get_template_keys_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->get_template_keys_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateKeyListResponse**](TemplateKeyListResponse.md)

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

# **list_dunning_template_versions_v1**
> TemplateVersionListResponse list_dunning_template_versions_v1(template_key, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

List Dunning Template Versions

### Example


```python
import moolabs
from moolabs.models.template_version_list_response import TemplateVersionListResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # List Dunning Template Versions
        api_response = api_instance.list_dunning_template_versions_v1(template_key, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->list_dunning_template_versions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->list_dunning_template_versions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateVersionListResponse**](TemplateVersionListResponse.md)

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

# **lock_dunning_template_draft_v1**
> DraftLockResponse lock_dunning_template_draft_v1(template_key, version_id, draft_lock_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Lock Dunning Template Draft

### Example


```python
import moolabs
from moolabs.models.draft_lock_request import DraftLockRequest
from moolabs.models.draft_lock_response import DraftLockResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    version_id = 'version_id_example' # str | 
    draft_lock_request = moolabs.DraftLockRequest() # DraftLockRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Lock Dunning Template Draft
        api_response = api_instance.lock_dunning_template_draft_v1(template_key, version_id, draft_lock_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->lock_dunning_template_draft_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->lock_dunning_template_draft_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **version_id** | **str**|  | 
 **draft_lock_request** | [**DraftLockRequest**](DraftLockRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DraftLockResponse**](DraftLockResponse.md)

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

# **post_archive_template_key_v1_arc**
> TemplateKeyResponse post_archive_template_key_v1_arc(template_key, template_archive_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Post Archive Template Key

### Example


```python
import moolabs
from moolabs.models.template_archive_request import TemplateArchiveRequest
from moolabs.models.template_key_response import TemplateKeyResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    template_archive_request = moolabs.TemplateArchiveRequest() # TemplateArchiveRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Post Archive Template Key
        api_response = api_instance.post_archive_template_key_v1_arc(template_key, template_archive_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->post_archive_template_key_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->post_archive_template_key_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **template_archive_request** | [**TemplateArchiveRequest**](TemplateArchiveRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateKeyResponse**](TemplateKeyResponse.md)

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

# **post_template_key_v1_arc**
> TemplateKeyResponse post_template_key_v1_arc(template_key_create_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Post Template Key

### Example


```python
import moolabs
from moolabs.models.template_key_create_request import TemplateKeyCreateRequest
from moolabs.models.template_key_response import TemplateKeyResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key_create_request = moolabs.TemplateKeyCreateRequest() # TemplateKeyCreateRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Post Template Key
        api_response = api_instance.post_template_key_v1_arc(template_key_create_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->post_template_key_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->post_template_key_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key_create_request** | [**TemplateKeyCreateRequest**](TemplateKeyCreateRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateKeyResponse**](TemplateKeyResponse.md)

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

# **post_template_test_send_v1_arc_dunning**
> TestSendResponse post_template_test_send_v1_arc_dunning(test_send_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Post Template Test Send

### Example


```python
import moolabs
from moolabs.models.test_send_request import TestSendRequest
from moolabs.models.test_send_response import TestSendResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    test_send_request = moolabs.TestSendRequest() # TestSendRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Post Template Test Send
        api_response = api_instance.post_template_test_send_v1_arc_dunning(test_send_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->post_template_test_send_v1_arc_dunning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->post_template_test_send_v1_arc_dunning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_send_request** | [**TestSendRequest**](TestSendRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TestSendResponse**](TestSendResponse.md)

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

# **preview_dunning_template_v1**
> PreviewTemplateResponse preview_dunning_template_v1(template_key, preview_template_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Preview Dunning Template

### Example


```python
import moolabs
from moolabs.models.preview_template_request import PreviewTemplateRequest
from moolabs.models.preview_template_response import PreviewTemplateResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    preview_template_request = moolabs.PreviewTemplateRequest() # PreviewTemplateRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Preview Dunning Template
        api_response = api_instance.preview_dunning_template_v1(template_key, preview_template_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->preview_dunning_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->preview_dunning_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **preview_template_request** | [**PreviewTemplateRequest**](PreviewTemplateRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PreviewTemplateResponse**](PreviewTemplateResponse.md)

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

# **publish_dunning_template_v1**
> TemplateVersionResponse publish_dunning_template_v1(template_key, publish_template_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Publish Dunning Template

### Example


```python
import moolabs
from moolabs.models.publish_template_request import PublishTemplateRequest
from moolabs.models.template_version_response import TemplateVersionResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    publish_template_request = moolabs.PublishTemplateRequest() # PublishTemplateRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Publish Dunning Template
        api_response = api_instance.publish_dunning_template_v1(template_key, publish_template_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->publish_dunning_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->publish_dunning_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **publish_template_request** | [**PublishTemplateRequest**](PublishTemplateRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateVersionResponse**](TemplateVersionResponse.md)

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

# **put_disclosure_policy_v1_arc_dunning**
> DisclosurePolicyResponse put_disclosure_policy_v1_arc_dunning(disclosure_policy_update_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Put Disclosure Policy

### Example


```python
import moolabs
from moolabs.models.disclosure_policy_response import DisclosurePolicyResponse
from moolabs.models.disclosure_policy_update_request import DisclosurePolicyUpdateRequest
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    disclosure_policy_update_request = moolabs.DisclosurePolicyUpdateRequest() # DisclosurePolicyUpdateRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Put Disclosure Policy
        api_response = api_instance.put_disclosure_policy_v1_arc_dunning(disclosure_policy_update_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->put_disclosure_policy_v1_arc_dunning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->put_disclosure_policy_v1_arc_dunning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disclosure_policy_update_request** | [**DisclosurePolicyUpdateRequest**](DisclosurePolicyUpdateRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**DisclosurePolicyResponse**](DisclosurePolicyResponse.md)

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

# **put_payment_instructions_v1_arc_dunning**
> PaymentInstructionsResponse put_payment_instructions_v1_arc_dunning(payment_instructions_update_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Put Payment Instructions

### Example


```python
import moolabs
from moolabs.models.payment_instructions_response import PaymentInstructionsResponse
from moolabs.models.payment_instructions_update_request import PaymentInstructionsUpdateRequest
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    payment_instructions_update_request = moolabs.PaymentInstructionsUpdateRequest() # PaymentInstructionsUpdateRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Put Payment Instructions
        api_response = api_instance.put_payment_instructions_v1_arc_dunning(payment_instructions_update_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->put_payment_instructions_v1_arc_dunning:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->put_payment_instructions_v1_arc_dunning: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_instructions_update_request** | [**PaymentInstructionsUpdateRequest**](PaymentInstructionsUpdateRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**PaymentInstructionsResponse**](PaymentInstructionsResponse.md)

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

# **save_dunning_template_draft_v1**
> TemplateVersionResponse save_dunning_template_draft_v1(template_key, draft_save_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Save Dunning Template Draft

### Example


```python
import moolabs
from moolabs.models.draft_save_request import DraftSaveRequest
from moolabs.models.template_version_response import TemplateVersionResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    draft_save_request = moolabs.DraftSaveRequest() # DraftSaveRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Save Dunning Template Draft
        api_response = api_instance.save_dunning_template_draft_v1(template_key, draft_save_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->save_dunning_template_draft_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->save_dunning_template_draft_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **draft_save_request** | [**DraftSaveRequest**](DraftSaveRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateVersionResponse**](TemplateVersionResponse.md)

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

# **unlock_dunning_template_draft_v1**
> TemplateVersionResponse unlock_dunning_template_draft_v1(template_key, version_id, draft_unlock_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Unlock Dunning Template Draft

### Example


```python
import moolabs
from moolabs.models.draft_unlock_request import DraftUnlockRequest
from moolabs.models.template_version_response import TemplateVersionResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    version_id = 'version_id_example' # str | 
    draft_unlock_request = moolabs.DraftUnlockRequest() # DraftUnlockRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Unlock Dunning Template Draft
        api_response = api_instance.unlock_dunning_template_draft_v1(template_key, version_id, draft_unlock_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->unlock_dunning_template_draft_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->unlock_dunning_template_draft_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **version_id** | **str**|  | 
 **draft_unlock_request** | [**DraftUnlockRequest**](DraftUnlockRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**TemplateVersionResponse**](TemplateVersionResponse.md)

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

# **validate_dunning_template_v1**
> ValidateTemplateResponse validate_dunning_template_v1(template_key, validate_template_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)

Validate Dunning Template

### Example


```python
import moolabs
from moolabs.models.validate_template_request import ValidateTemplateRequest
from moolabs.models.validate_template_response import ValidateTemplateResponse
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
    api_instance = moolabs.DunningTemplatesApi(api_client)
    template_key = 'template_key_example' # str | 
    validate_template_request = moolabs.ValidateTemplateRequest() # ValidateTemplateRequest | 
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    x_arc_feature_flags = 'x_arc_feature_flags_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_actor_user_id = 'x_arc_actor_user_id_example' # str |  (optional)
    x_arc_actor_display = 'x_arc_actor_display_example' # str |  (optional)
    x_arc_actor_email = 'x_arc_actor_email_example' # str |  (optional)
    x_arc_source = 'x_arc_source_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_chat_session_id = 'x_chat_session_id_example' # str |  (optional)
    x_request_id = 'x_request_id_example' # str |  (optional)
    x_correlation_id = 'x_correlation_id_example' # str |  (optional)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Validate Dunning Template
        api_response = api_instance.validate_dunning_template_v1(template_key, validate_template_request, x_arc_proxy_secret=x_arc_proxy_secret, x_arc_feature_flags=x_arc_feature_flags, x_arc_roles=x_arc_roles, x_arc_actor_user_id=x_arc_actor_user_id, x_arc_actor_display=x_arc_actor_display, x_arc_actor_email=x_arc_actor_email, x_arc_source=x_arc_source, x_org_id=x_org_id, x_chat_session_id=x_chat_session_id, x_request_id=x_request_id, x_correlation_id=x_correlation_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, authorization=authorization)
        print("The response of DunningTemplatesApi->validate_dunning_template_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DunningTemplatesApi->validate_dunning_template_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_key** | **str**|  | 
 **validate_template_request** | [**ValidateTemplateRequest**](ValidateTemplateRequest.md)|  | 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **x_arc_feature_flags** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_actor_user_id** | **str**|  | [optional] 
 **x_arc_actor_display** | **str**|  | [optional] 
 **x_arc_actor_email** | **str**|  | [optional] 
 **x_arc_source** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_chat_session_id** | **str**|  | [optional] 
 **x_request_id** | **str**|  | [optional] 
 **x_correlation_id** | **str**|  | [optional] 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ValidateTemplateResponse**](ValidateTemplateResponse.md)

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

