# moolabs.BatchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch**](BatchApi.md#batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch) | **POST** /v1/arc/batch/backfill-managed-portal-suppression/protection/ack | Batch Backfill Managed Portal Suppression Ack Protection
[**batch_backfill_managed_portal_suppression_cancel_v1_arc_batch**](BatchApi.md#batch_backfill_managed_portal_suppression_cancel_v1_arc_batch) | **POST** /v1/arc/batch/backfill-managed-portal-suppression/{job_id}/cancel | Batch Backfill Managed Portal Suppression Cancel
[**batch_backfill_managed_portal_suppression_run_v1_arc_batch**](BatchApi.md#batch_backfill_managed_portal_suppression_run_v1_arc_batch) | **POST** /v1/arc/batch/backfill-managed-portal-suppression/run | Batch Backfill Managed Portal Suppression Run
[**batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill**](BatchApi.md#batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill) | **POST** /v1/arc/batch/backfill-managed-portal-suppression/run-pending | Batch Backfill Managed Portal Suppression Run
[**batch_backfill_managed_portal_suppression_status_v1_arc_batch**](BatchApi.md#batch_backfill_managed_portal_suppression_status_v1_arc_batch) | **GET** /v1/arc/batch/backfill-managed-portal-suppression/{job_id} | Batch Backfill Managed Portal Suppression Status
[**batch_backfill_managed_portal_suppression_v1_arc_batch**](BatchApi.md#batch_backfill_managed_portal_suppression_v1_arc_batch) | **POST** /v1/arc/batch/backfill-managed-portal-suppression | Batch Backfill Managed Portal Suppression
[**batch_backfill_netsuite_deferred_invoices_v1_arc_batch**](BatchApi.md#batch_backfill_netsuite_deferred_invoices_v1_arc_batch) | **POST** /v1/arc/batch/backfill-netsuite-deferred-invoices | Batch Backfill Netsuite Deferred Invoices
[**batch_backfill_netsuite_identities_v1_arc**](BatchApi.md#batch_backfill_netsuite_identities_v1_arc) | **POST** /v1/arc/batch/backfill-netsuite-identities | Batch Backfill Netsuite Identities
[**batch_bootstrap_netsuite_accounts_v1_arc**](BatchApi.md#batch_bootstrap_netsuite_accounts_v1_arc) | **POST** /v1/arc/batch/bootstrap-netsuite-accounts | Batch Bootstrap Netsuite Accounts
[**batch_bulk_action_v1**](BatchApi.md#batch_bulk_action_v1) | **POST** /v1/arc/batch/bulk-action | Batch Bulk Action
[**batch_delete_netsuite_managed_portal_mapping_v1_arc_batch**](BatchApi.md#batch_delete_netsuite_managed_portal_mapping_v1_arc_batch) | **DELETE** /v1/arc/batch/netsuite-managed-portal-mapping | Batch Delete Netsuite Managed Portal Mapping
[**batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post**](BatchApi.md#batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post) | **POST** /v1/arc/batch/netsuite-managed-portal-mapping/delete | Batch Delete Netsuite Managed Portal Mapping
[**batch_link_netsuite_account_v1_arc**](BatchApi.md#batch_link_netsuite_account_v1_arc) | **POST** /v1/arc/batch/link-netsuite-account | Batch Link Netsuite Account
[**batch_recalculate_aging_v1**](BatchApi.md#batch_recalculate_aging_v1) | **POST** /v1/arc/batch/recalculate-aging | Batch Recalculate Aging
[**batch_reconcile_pending_provider_confirmations_v1_arc_batch**](BatchApi.md#batch_reconcile_pending_provider_confirmations_v1_arc_batch) | **POST** /v1/arc/batch/communications/reconcile-pending-provider-confirmations | Batch Reconcile Pending Provider Confirmations
[**batch_set_netsuite_cutover_guard_v1_arc**](BatchApi.md#batch_set_netsuite_cutover_guard_v1_arc) | **POST** /v1/arc/batch/netsuite-cutover-guard | Batch Set Netsuite Cutover Guard
[**batch_set_netsuite_managed_portal_mapping_v1_arc_batch**](BatchApi.md#batch_set_netsuite_managed_portal_mapping_v1_arc_batch) | **POST** /v1/arc/batch/netsuite-managed-portal-mapping | Batch Set Netsuite Managed Portal Mapping
[**batch_sync_invoices_v1**](BatchApi.md#batch_sync_invoices_v1) | **POST** /v1/arc/batch/sync-invoices | Batch Sync Invoices
[**batch_trigger_netsuite_sync_v1_arc**](BatchApi.md#batch_trigger_netsuite_sync_v1_arc) | **POST** /v1/arc/batch/trigger-netsuite-sync | Batch Trigger Netsuite Sync


# **batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch**
> object batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_protection_ack_request=net_suite_managed_portal_protection_ack_request)

Batch Backfill Managed Portal Suppression Ack Protection

POST /batch/backfill-managed-portal-suppression/protection/ack — acknowledge and optionally exit tenant protection mode.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_protection_ack_request import NetSuiteManagedPortalProtectionAckRequest
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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    net_suite_managed_portal_protection_ack_request = moolabs.NetSuiteManagedPortalProtectionAckRequest() # NetSuiteManagedPortalProtectionAckRequest |  (optional)

    try:
        # Batch Backfill Managed Portal Suppression Ack Protection
        api_response = api_instance.batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_protection_ack_request=net_suite_managed_portal_protection_ack_request)
        print("The response of BatchApi->batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_managed_portal_suppression_ack_protection_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **net_suite_managed_portal_protection_ack_request** | [**NetSuiteManagedPortalProtectionAckRequest**](NetSuiteManagedPortalProtectionAckRequest.md)|  | [optional] 

### Return type

**object**

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

# **batch_backfill_managed_portal_suppression_cancel_v1_arc_batch**
> object batch_backfill_managed_portal_suppression_cancel_v1_arc_batch(job_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_backfill_cancel_request=net_suite_managed_portal_backfill_cancel_request)

Batch Backfill Managed Portal Suppression Cancel

POST /batch/backfill-managed-portal-suppression/{job_id}/cancel — cancel queued/running job.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_backfill_cancel_request import NetSuiteManagedPortalBackfillCancelRequest
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
    api_instance = moolabs.BatchApi(api_client)
    job_id = 'job_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    net_suite_managed_portal_backfill_cancel_request = moolabs.NetSuiteManagedPortalBackfillCancelRequest() # NetSuiteManagedPortalBackfillCancelRequest |  (optional)

    try:
        # Batch Backfill Managed Portal Suppression Cancel
        api_response = api_instance.batch_backfill_managed_portal_suppression_cancel_v1_arc_batch(job_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_backfill_cancel_request=net_suite_managed_portal_backfill_cancel_request)
        print("The response of BatchApi->batch_backfill_managed_portal_suppression_cancel_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_managed_portal_suppression_cancel_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **net_suite_managed_portal_backfill_cancel_request** | [**NetSuiteManagedPortalBackfillCancelRequest**](NetSuiteManagedPortalBackfillCancelRequest.md)|  | [optional] 

### Return type

**object**

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

# **batch_backfill_managed_portal_suppression_run_v1_arc_batch**
> object batch_backfill_managed_portal_suppression_run_v1_arc_batch(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_backfill_run_request=net_suite_managed_portal_backfill_run_request)

Batch Backfill Managed Portal Suppression Run

POST /batch/backfill-managed-portal-suppression/run — worker trigger for queued jobs.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_backfill_run_request import NetSuiteManagedPortalBackfillRunRequest
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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    net_suite_managed_portal_backfill_run_request = moolabs.NetSuiteManagedPortalBackfillRunRequest() # NetSuiteManagedPortalBackfillRunRequest |  (optional)

    try:
        # Batch Backfill Managed Portal Suppression Run
        api_response = api_instance.batch_backfill_managed_portal_suppression_run_v1_arc_batch(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_backfill_run_request=net_suite_managed_portal_backfill_run_request)
        print("The response of BatchApi->batch_backfill_managed_portal_suppression_run_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_managed_portal_suppression_run_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **net_suite_managed_portal_backfill_run_request** | [**NetSuiteManagedPortalBackfillRunRequest**](NetSuiteManagedPortalBackfillRunRequest.md)|  | [optional] 

### Return type

**object**

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

# **batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill**
> object batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_backfill_run_request=net_suite_managed_portal_backfill_run_request)

Batch Backfill Managed Portal Suppression Run

POST /batch/backfill-managed-portal-suppression/run — worker trigger for queued jobs.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_backfill_run_request import NetSuiteManagedPortalBackfillRunRequest
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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)
    net_suite_managed_portal_backfill_run_request = moolabs.NetSuiteManagedPortalBackfillRunRequest() # NetSuiteManagedPortalBackfillRunRequest |  (optional)

    try:
        # Batch Backfill Managed Portal Suppression Run
        api_response = api_instance.batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret, net_suite_managed_portal_backfill_run_request=net_suite_managed_portal_backfill_run_request)
        print("The response of BatchApi->batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_managed_portal_suppression_run_v1_arc_batch_backfill: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 
 **net_suite_managed_portal_backfill_run_request** | [**NetSuiteManagedPortalBackfillRunRequest**](NetSuiteManagedPortalBackfillRunRequest.md)|  | [optional] 

### Return type

**object**

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

# **batch_backfill_managed_portal_suppression_status_v1_arc_batch**
> object batch_backfill_managed_portal_suppression_status_v1_arc_batch(job_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Batch Backfill Managed Portal Suppression Status

GET /batch/backfill-managed-portal-suppression/{job_id} — poll backfill job status.

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
    api_instance = moolabs.BatchApi(api_client)
    job_id = 'job_id_example' # str | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Batch Backfill Managed Portal Suppression Status
        api_response = api_instance.batch_backfill_managed_portal_suppression_status_v1_arc_batch(job_id, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of BatchApi->batch_backfill_managed_portal_suppression_status_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_managed_portal_suppression_status_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

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

# **batch_backfill_managed_portal_suppression_v1_arc_batch**
> object batch_backfill_managed_portal_suppression_v1_arc_batch(net_suite_managed_portal_backfill_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Batch Backfill Managed Portal Suppression

POST /batch/backfill-managed-portal-suppression — create a managed-portal backfill job.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_backfill_request import NetSuiteManagedPortalBackfillRequest
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
    api_instance = moolabs.BatchApi(api_client)
    net_suite_managed_portal_backfill_request = moolabs.NetSuiteManagedPortalBackfillRequest() # NetSuiteManagedPortalBackfillRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Batch Backfill Managed Portal Suppression
        api_response = api_instance.batch_backfill_managed_portal_suppression_v1_arc_batch(net_suite_managed_portal_backfill_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of BatchApi->batch_backfill_managed_portal_suppression_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_managed_portal_suppression_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_suite_managed_portal_backfill_request** | [**NetSuiteManagedPortalBackfillRequest**](NetSuiteManagedPortalBackfillRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_backfill_netsuite_deferred_invoices_v1_arc_batch**
> object batch_backfill_netsuite_deferred_invoices_v1_arc_batch(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Backfill Netsuite Deferred Invoices

POST /batch/backfill-netsuite-deferred-invoices — seed skipped pending-approval invoices.

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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Backfill Netsuite Deferred Invoices
        api_response = api_instance.batch_backfill_netsuite_deferred_invoices_v1_arc_batch(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_backfill_netsuite_deferred_invoices_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_netsuite_deferred_invoices_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **batch_backfill_netsuite_identities_v1_arc**
> object batch_backfill_netsuite_identities_v1_arc(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Backfill Netsuite Identities

POST /batch/backfill-netsuite-identities — one-time identity crosswalk backfill.

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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Backfill Netsuite Identities
        api_response = api_instance.batch_backfill_netsuite_identities_v1_arc(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_backfill_netsuite_identities_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_backfill_netsuite_identities_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **batch_bootstrap_netsuite_accounts_v1_arc**
> object batch_bootstrap_netsuite_accounts_v1_arc(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Bootstrap Netsuite Accounts

POST /batch/bootstrap-netsuite-accounts — Seed ArcAccount rows from BFF NetSuite staging.

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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Bootstrap Netsuite Accounts
        api_response = api_instance.batch_bootstrap_netsuite_accounts_v1_arc(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_bootstrap_netsuite_accounts_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_bootstrap_netsuite_accounts_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **batch_bulk_action_v1**
> object batch_bulk_action_v1(bulk_action_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Bulk Action

POST /batch/bulk-action — Bulk case operations (pause, resume, escalate, assign).

### Example


```python
import moolabs
from moolabs.models.bulk_action_request import BulkActionRequest
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
    api_instance = moolabs.BatchApi(api_client)
    bulk_action_request = moolabs.BulkActionRequest() # BulkActionRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Bulk Action
        api_response = api_instance.batch_bulk_action_v1(bulk_action_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_bulk_action_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_bulk_action_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_action_request** | [**BulkActionRequest**](BulkActionRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_delete_netsuite_managed_portal_mapping_v1_arc_batch**
> object batch_delete_netsuite_managed_portal_mapping_v1_arc_batch(net_suite_managed_portal_mapping_delete_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Batch Delete Netsuite Managed Portal Mapping

POST /batch/netsuite-managed-portal-mapping/delete — delete managed-portal mapping.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_mapping_delete_request import NetSuiteManagedPortalMappingDeleteRequest
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
    api_instance = moolabs.BatchApi(api_client)
    net_suite_managed_portal_mapping_delete_request = moolabs.NetSuiteManagedPortalMappingDeleteRequest() # NetSuiteManagedPortalMappingDeleteRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Batch Delete Netsuite Managed Portal Mapping
        api_response = api_instance.batch_delete_netsuite_managed_portal_mapping_v1_arc_batch(net_suite_managed_portal_mapping_delete_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of BatchApi->batch_delete_netsuite_managed_portal_mapping_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_delete_netsuite_managed_portal_mapping_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_suite_managed_portal_mapping_delete_request** | [**NetSuiteManagedPortalMappingDeleteRequest**](NetSuiteManagedPortalMappingDeleteRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post**
> object batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post(net_suite_managed_portal_mapping_delete_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Batch Delete Netsuite Managed Portal Mapping

POST /batch/netsuite-managed-portal-mapping/delete — delete managed-portal mapping.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_mapping_delete_request import NetSuiteManagedPortalMappingDeleteRequest
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
    api_instance = moolabs.BatchApi(api_client)
    net_suite_managed_portal_mapping_delete_request = moolabs.NetSuiteManagedPortalMappingDeleteRequest() # NetSuiteManagedPortalMappingDeleteRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Batch Delete Netsuite Managed Portal Mapping
        api_response = api_instance.batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post(net_suite_managed_portal_mapping_delete_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of BatchApi->batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_delete_netsuite_managed_portal_mapping_v1_arc_batch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_suite_managed_portal_mapping_delete_request** | [**NetSuiteManagedPortalMappingDeleteRequest**](NetSuiteManagedPortalMappingDeleteRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_link_netsuite_account_v1_arc**
> object batch_link_netsuite_account_v1_arc(link_net_suite_account_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Link Netsuite Account

POST /batch/link-netsuite-account — Link existing account to NetSuite customer id.

### Example


```python
import moolabs
from moolabs.models.link_net_suite_account_request import LinkNetSuiteAccountRequest
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
    api_instance = moolabs.BatchApi(api_client)
    link_net_suite_account_request = moolabs.LinkNetSuiteAccountRequest() # LinkNetSuiteAccountRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Link Netsuite Account
        api_response = api_instance.batch_link_netsuite_account_v1_arc(link_net_suite_account_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_link_netsuite_account_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_link_netsuite_account_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_net_suite_account_request** | [**LinkNetSuiteAccountRequest**](LinkNetSuiteAccountRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_recalculate_aging_v1**
> object batch_recalculate_aging_v1(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Recalculate Aging

POST /batch/recalculate-aging — Re-bucket all invoices by due date.

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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Recalculate Aging
        api_response = api_instance.batch_recalculate_aging_v1(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_recalculate_aging_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_recalculate_aging_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

# **batch_reconcile_pending_provider_confirmations_v1_arc_batch**
> object batch_reconcile_pending_provider_confirmations_v1_arc_batch(pending_provider_confirmation_reconcile_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Batch Reconcile Pending Provider Confirmations

POST /batch/communications/reconcile-pending-provider-confirmations — reconcile provider-unknown sends.

### Example


```python
import moolabs
from moolabs.models.pending_provider_confirmation_reconcile_request import PendingProviderConfirmationReconcileRequest
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
    api_instance = moolabs.BatchApi(api_client)
    pending_provider_confirmation_reconcile_request = moolabs.PendingProviderConfirmationReconcileRequest() # PendingProviderConfirmationReconcileRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Batch Reconcile Pending Provider Confirmations
        api_response = api_instance.batch_reconcile_pending_provider_confirmations_v1_arc_batch(pending_provider_confirmation_reconcile_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of BatchApi->batch_reconcile_pending_provider_confirmations_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_reconcile_pending_provider_confirmations_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pending_provider_confirmation_reconcile_request** | [**PendingProviderConfirmationReconcileRequest**](PendingProviderConfirmationReconcileRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_set_netsuite_cutover_guard_v1_arc**
> object batch_set_netsuite_cutover_guard_v1_arc(net_suite_cutover_guard_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Set Netsuite Cutover Guard

POST /batch/netsuite-cutover-guard — enable/disable strict unmapped-account guard.

### Example


```python
import moolabs
from moolabs.models.net_suite_cutover_guard_request import NetSuiteCutoverGuardRequest
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
    api_instance = moolabs.BatchApi(api_client)
    net_suite_cutover_guard_request = moolabs.NetSuiteCutoverGuardRequest() # NetSuiteCutoverGuardRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Set Netsuite Cutover Guard
        api_response = api_instance.batch_set_netsuite_cutover_guard_v1_arc(net_suite_cutover_guard_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_set_netsuite_cutover_guard_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_set_netsuite_cutover_guard_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_suite_cutover_guard_request** | [**NetSuiteCutoverGuardRequest**](NetSuiteCutoverGuardRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_set_netsuite_managed_portal_mapping_v1_arc_batch**
> object batch_set_netsuite_managed_portal_mapping_v1_arc_batch(net_suite_managed_portal_mapping_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)

Batch Set Netsuite Managed Portal Mapping

POST /batch/netsuite-managed-portal-mapping — configure managed-portal source field.

### Example


```python
import moolabs
from moolabs.models.net_suite_managed_portal_mapping_request import NetSuiteManagedPortalMappingRequest
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
    api_instance = moolabs.BatchApi(api_client)
    net_suite_managed_portal_mapping_request = moolabs.NetSuiteManagedPortalMappingRequest() # NetSuiteManagedPortalMappingRequest | 
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)
    x_arc_roles = 'x_arc_roles_example' # str |  (optional)
    x_arc_proxy_secret = 'x_arc_proxy_secret_example' # str |  (optional)

    try:
        # Batch Set Netsuite Managed Portal Mapping
        api_response = api_instance.batch_set_netsuite_managed_portal_mapping_v1_arc_batch(net_suite_managed_portal_mapping_request, x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, x_user_id=x_user_id, x_arc_roles=x_arc_roles, x_arc_proxy_secret=x_arc_proxy_secret)
        print("The response of BatchApi->batch_set_netsuite_managed_portal_mapping_v1_arc_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_set_netsuite_managed_portal_mapping_v1_arc_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **net_suite_managed_portal_mapping_request** | [**NetSuiteManagedPortalMappingRequest**](NetSuiteManagedPortalMappingRequest.md)|  | 
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 
 **x_arc_roles** | **str**|  | [optional] 
 **x_arc_proxy_secret** | **str**|  | [optional] 

### Return type

**object**

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

# **batch_sync_invoices_v1**
> object batch_sync_invoices_v1(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, sync_invoices_request=sync_invoices_request)

Batch Sync Invoices

POST /batch/sync-invoices — Sync invoices from MooMeter.

### Example


```python
import moolabs
from moolabs.models.sync_invoices_request import SyncInvoicesRequest
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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)
    sync_invoices_request = moolabs.SyncInvoicesRequest() # SyncInvoicesRequest |  (optional)

    try:
        # Batch Sync Invoices
        api_response = api_instance.batch_sync_invoices_v1(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization, sync_invoices_request=sync_invoices_request)
        print("The response of BatchApi->batch_sync_invoices_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_sync_invoices_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **sync_invoices_request** | [**SyncInvoicesRequest**](SyncInvoicesRequest.md)|  | [optional] 

### Return type

**object**

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

# **batch_trigger_netsuite_sync_v1_arc**
> object batch_trigger_netsuite_sync_v1_arc(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)

Batch Trigger Netsuite Sync

POST /batch/trigger-netsuite-sync — Trigger a NetSuite sync via BFF.

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
    api_instance = moolabs.BatchApi(api_client)
    x_api_key = 'x_api_key_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Batch Trigger Netsuite Sync
        api_response = api_instance.batch_trigger_netsuite_sync_v1_arc(x_api_key=x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id, authorization=authorization)
        print("The response of BatchApi->batch_trigger_netsuite_sync_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchApi->batch_trigger_netsuite_sync_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
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

