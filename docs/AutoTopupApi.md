# moolabs.AutoTopupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_trigger_v1**](AutoTopupApi.md#check_trigger_v1) | **POST** /v1/auto-topup/rules/{rule_id}/check | Check Trigger
[**create_rule_v1**](AutoTopupApi.md#create_rule_v1) | **POST** /v1/auto-topup/rules | Create Rule
[**delete_rule_v1**](AutoTopupApi.md#delete_rule_v1) | **DELETE** /v1/auto-topup/rules/{rule_id} | Delete Rule
[**get_activity_v1**](AutoTopupApi.md#get_activity_v1) | **GET** /v1/auto-topup/activity | Get Activity
[**get_rule_v1**](AutoTopupApi.md#get_rule_v1) | **GET** /v1/auto-topup/rules/{rule_id} | Get Rule
[**list_rules_v1**](AutoTopupApi.md#list_rules_v1) | **GET** /v1/auto-topup/rules | List Rules
[**patch_rule_v1**](AutoTopupApi.md#patch_rule_v1) | **PATCH** /v1/auto-topup/rules/{rule_id} | Patch Rule
[**payment_failed_v1**](AutoTopupApi.md#payment_failed_v1) | **POST** /v1/auto-topup/payments/failed | Payment Failed
[**payment_succeeded_v1**](AutoTopupApi.md#payment_succeeded_v1) | **POST** /v1/auto-topup/payments/succeeded | Payment Succeeded
[**update_rule_v1**](AutoTopupApi.md#update_rule_v1) | **PUT** /v1/auto-topup/rules/{rule_id} | Update Rule


# **check_trigger_v1**
> AppApiV1AutoTopupRouterTriggerResponse check_trigger_v1(rule_id, check_trigger_request=check_trigger_request)

Check Trigger

Check trigger condition and trigger auto top-up if needed.  This endpoint: - Checks if trigger condition is met - Checks cooldown atomicity - Acquires trigger lock - Emits AUTO_TOPUP_REQUESTED outbox event

### Example


```python
import moolabs
from moolabs.models.app_api_v1_auto_topup_router_trigger_response import AppApiV1AutoTopupRouterTriggerResponse
from moolabs.models.check_trigger_request import CheckTriggerRequest
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
    api_instance = moolabs.AutoTopupApi(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    check_trigger_request = moolabs.CheckTriggerRequest() # CheckTriggerRequest |  (optional)

    try:
        # Check Trigger
        api_response = api_instance.check_trigger_v1(rule_id, check_trigger_request=check_trigger_request)
        print("The response of AutoTopupApi->check_trigger_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->check_trigger_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **check_trigger_request** | [**CheckTriggerRequest**](CheckTriggerRequest.md)|  | [optional] 

### Return type

[**AppApiV1AutoTopupRouterTriggerResponse**](AppApiV1AutoTopupRouterTriggerResponse.md)

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

# **create_rule_v1**
> AutoTopupRuleResponse create_rule_v1(create_auto_topup_rule_request)

Create Rule

Create an auto top-up rule.  This endpoint creates a rule that triggers automatic wallet top-up when certain conditions are met (e.g., LOW state, threshold crossed).

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.models.create_auto_topup_rule_request import CreateAutoTopupRuleRequest
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
    api_instance = moolabs.AutoTopupApi(api_client)
    create_auto_topup_rule_request = moolabs.CreateAutoTopupRuleRequest() # CreateAutoTopupRuleRequest | 

    try:
        # Create Rule
        api_response = api_instance.create_rule_v1(create_auto_topup_rule_request)
        print("The response of AutoTopupApi->create_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->create_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auto_topup_rule_request** | [**CreateAutoTopupRuleRequest**](CreateAutoTopupRuleRequest.md)|  | 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

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

# **delete_rule_v1**
> object delete_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id)

Delete Rule

Delete an auto top-up rule.

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
    api_instance = moolabs.AutoTopupApi(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier for validation (optional)

    try:
        # Delete Rule
        api_response = api_instance.delete_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id)
        print("The response of AutoTopupApi->delete_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->delete_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 
 **wallet_id** | **str**| Optional wallet identifier for validation | [optional] 

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

# **get_activity_v1**
> AutoTopupActivityResponse get_activity_v1(tenant_id, pool_id, wallet_id, limit=limit, offset=offset)

Get Activity

Get auto-topup activity/history for a wallet.  Returns history of auto-topup executions (both requested and completed).

### Example


```python
import moolabs
from moolabs.models.auto_topup_activity_response import AutoTopupActivityResponse
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
    api_instance = moolabs.AutoTopupApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Wallet identifier
    limit = 50 # int | Maximum number of items to return (optional) (default to 50)
    offset = 0 # int | Offset for pagination (optional) (default to 0)

    try:
        # Get Activity
        api_response = api_instance.get_activity_v1(tenant_id, pool_id, wallet_id, limit=limit, offset=offset)
        print("The response of AutoTopupApi->get_activity_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->get_activity_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_id** | **str**| Wallet identifier | 
 **limit** | **int**| Maximum number of items to return | [optional] [default to 50]
 **offset** | **int**| Offset for pagination | [optional] [default to 0]

### Return type

[**AutoTopupActivityResponse**](AutoTopupActivityResponse.md)

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

# **get_rule_v1**
> AutoTopupRuleResponse get_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id)

Get Rule

Get a specific auto top-up rule by ID.

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
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
    api_instance = moolabs.AutoTopupApi(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)

    try:
        # Get Rule
        api_response = api_instance.get_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id)
        print("The response of AutoTopupApi->get_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->get_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

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

# **list_rules_v1**
> ListAutoTopupRulesResponse list_rules_v1(tenant_id, pool_id, wallet_id=wallet_id)

List Rules

List auto top-up rules.  Returns all rules for a tenant/pool, optionally filtered by wallet_id.

### Example


```python
import moolabs
from moolabs.models.list_auto_topup_rules_response import ListAutoTopupRulesResponse
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
    api_instance = moolabs.AutoTopupApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier
    pool_id = 'pool_id_example' # str | Pool identifier
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier to filter by (optional)

    try:
        # List Rules
        api_response = api_instance.list_rules_v1(tenant_id, pool_id, wallet_id=wallet_id)
        print("The response of AutoTopupApi->list_rules_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->list_rules_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier | 
 **pool_id** | **str**| Pool identifier | 
 **wallet_id** | **str**| Optional wallet identifier to filter by | [optional] 

### Return type

[**ListAutoTopupRulesResponse**](ListAutoTopupRulesResponse.md)

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

# **patch_rule_v1**
> AutoTopupRuleResponse patch_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)

Patch Rule

Partially update an auto top-up rule (e.g., enable/disable).  This is an alias for PUT - updates the specified fields.

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.models.update_auto_topup_rule_request import UpdateAutoTopupRuleRequest
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
    api_instance = moolabs.AutoTopupApi(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier for validation (optional)
    update_auto_topup_rule_request = moolabs.UpdateAutoTopupRuleRequest() # UpdateAutoTopupRuleRequest |  (optional)

    try:
        # Patch Rule
        api_response = api_instance.patch_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)
        print("The response of AutoTopupApi->patch_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->patch_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 
 **wallet_id** | **str**| Optional wallet identifier for validation | [optional] 
 **update_auto_topup_rule_request** | [**UpdateAutoTopupRuleRequest**](UpdateAutoTopupRuleRequest.md)|  | [optional] 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

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

# **payment_failed_v1**
> PaymentFailedResponse payment_failed_v1(payment_failed_request)

Payment Failed

Handle payment failed callback.  This endpoint: - Emits AUTO_TOPUP_FAILED outbox event (idempotent) - Dispatches topup-failed email via centralized template renderer

### Example


```python
import moolabs
from moolabs.models.payment_failed_request import PaymentFailedRequest
from moolabs.models.payment_failed_response import PaymentFailedResponse
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
    api_instance = moolabs.AutoTopupApi(api_client)
    payment_failed_request = moolabs.PaymentFailedRequest() # PaymentFailedRequest | 

    try:
        # Payment Failed
        api_response = api_instance.payment_failed_v1(payment_failed_request)
        print("The response of AutoTopupApi->payment_failed_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->payment_failed_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_failed_request** | [**PaymentFailedRequest**](PaymentFailedRequest.md)|  | 

### Return type

[**PaymentFailedResponse**](PaymentFailedResponse.md)

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

# **payment_succeeded_v1**
> PaymentSucceededResponse payment_succeeded_v1(payment_succeeded_request)

Payment Succeeded

Handle payment succeeded callback.  This endpoint: - Mints grant with FX locking (idempotent) - Creates CREDIT_MINT journal entry - Emits AUTO_TOPUP_SUCCEEDED outbox event

### Example


```python
import moolabs
from moolabs.models.payment_succeeded_request import PaymentSucceededRequest
from moolabs.models.payment_succeeded_response import PaymentSucceededResponse
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
    api_instance = moolabs.AutoTopupApi(api_client)
    payment_succeeded_request = moolabs.PaymentSucceededRequest() # PaymentSucceededRequest | 

    try:
        # Payment Succeeded
        api_response = api_instance.payment_succeeded_v1(payment_succeeded_request)
        print("The response of AutoTopupApi->payment_succeeded_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->payment_succeeded_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_succeeded_request** | [**PaymentSucceededRequest**](PaymentSucceededRequest.md)|  | 

### Return type

[**PaymentSucceededResponse**](PaymentSucceededResponse.md)

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

# **update_rule_v1**
> AutoTopupRuleResponse update_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)

Update Rule

Update an auto top-up rule.  Updates the specified fields of an existing rule.

### Example


```python
import moolabs
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse
from moolabs.models.update_auto_topup_rule_request import UpdateAutoTopupRuleRequest
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
    api_instance = moolabs.AutoTopupApi(api_client)
    rule_id = 'rule_id_example' # str | Auto top-up rule ID
    tenant_id = 'tenant_id_example' # str | Optional tenant identifier for validation (optional)
    pool_id = 'pool_id_example' # str | Optional pool identifier for validation (optional)
    wallet_id = 'wallet_id_example' # str | Optional wallet identifier for validation (optional)
    update_auto_topup_rule_request = moolabs.UpdateAutoTopupRuleRequest() # UpdateAutoTopupRuleRequest |  (optional)

    try:
        # Update Rule
        api_response = api_instance.update_rule_v1(rule_id, tenant_id=tenant_id, pool_id=pool_id, wallet_id=wallet_id, update_auto_topup_rule_request=update_auto_topup_rule_request)
        print("The response of AutoTopupApi->update_rule_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTopupApi->update_rule_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Auto top-up rule ID | 
 **tenant_id** | **str**| Optional tenant identifier for validation | [optional] 
 **pool_id** | **str**| Optional pool identifier for validation | [optional] 
 **wallet_id** | **str**| Optional wallet identifier for validation | [optional] 
 **update_auto_topup_rule_request** | [**UpdateAutoTopupRuleRequest**](UpdateAutoTopupRuleRequest.md)|  | [optional] 

### Return type

[**AutoTopupRuleResponse**](AutoTopupRuleResponse.md)

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

