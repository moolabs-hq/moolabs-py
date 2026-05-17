# moolabs.ArcAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backfill_malformed_disputes_v1_arc_admin**](ArcAdminApi.md#backfill_malformed_disputes_v1_arc_admin) | **POST** /v1/arc/admin/inbound-routing/backfill-malformed-disputes | Repair AI-classified disputes the pre-T4 router mis-routed
[**bulk_replay_endpoint_v1_arc**](ArcAdminApi.md#bulk_replay_endpoint_v1_arc) | **POST** /v1/arc/admin/dead-letters/bulk-replay | Bulk Replay Endpoint
[**get_agent_run_status_v1**](ArcAdminApi.md#get_agent_run_status_v1) | **GET** /v1/arc/admin/agent-runs/{run_id} | Get agent run status
[**get_dead_letters_v1**](ArcAdminApi.md#get_dead_letters_v1) | **GET** /v1/arc/admin/dead-letters | Get Dead Letters
[**get_email_config_v1**](ArcAdminApi.md#get_email_config_v1) | **GET** /v1/arc/admin/email-config | Get Email Config
[**get_outbound_failures_v1**](ArcAdminApi.md#get_outbound_failures_v1) | **GET** /v1/arc/admin/outbound-failures | Get Outbound Failures
[**get_potential_duplicates_v1**](ArcAdminApi.md#get_potential_duplicates_v1) | **GET** /v1/arc/admin/potential-duplicates | Get Potential Duplicates
[**get_tenant_escalation_config_v1_arc**](ArcAdminApi.md#get_tenant_escalation_config_v1_arc) | **GET** /v1/arc/admin/tenant-escalation-config | Get Tenant Escalation Config
[**import_disputes_endpoint**](ArcAdminApi.md#import_disputes_endpoint) | **POST** /v1/arc/admin/import/disputes | Import Disputes Endpoint
[**import_invoices_endpoint**](ArcAdminApi.md#import_invoices_endpoint) | **POST** /v1/arc/admin/import/invoices | Import Invoices Endpoint
[**import_promises_endpoint**](ArcAdminApi.md#import_promises_endpoint) | **POST** /v1/arc/admin/import/promises | Import Promises Endpoint
[**merge_remittances_endpoint**](ArcAdminApi.md#merge_remittances_endpoint) | **POST** /v1/arc/admin/remittances/merge | Merge Remittances Endpoint
[**patch_tenant_escalation_config_v1_arc**](ArcAdminApi.md#patch_tenant_escalation_config_v1_arc) | **PATCH** /v1/arc/admin/tenant-escalation-config | Patch Tenant Escalation Config
[**reclassify_communication**](ArcAdminApi.md#reclassify_communication) | **POST** /v1/arc/admin/communications/{communication_id}/reclassify | Re-enqueue inbound classification for an existing communication
[**replay_dead_letter_endpoint_v1**](ArcAdminApi.md#replay_dead_letter_endpoint_v1) | **POST** /v1/arc/admin/dead-letters/{event_id}/replay | Replay Dead Letter Endpoint
[**retry_outbound_failure_endpoint_v1**](ArcAdminApi.md#retry_outbound_failure_endpoint_v1) | **POST** /v1/arc/admin/outbound-failures/{event_id}/retry | Retry Outbound Failure Endpoint
[**rotate_inbound_secret_v1_arc**](ArcAdminApi.md#rotate_inbound_secret_v1_arc) | **POST** /v1/arc/admin/email-config/rotate-secret | Rotate Inbound Secret
[**run_agent_sync**](ArcAdminApi.md#run_agent_sync) | **POST** /v1/arc/admin/agents/{agent_type}/run | Run Agent Synchronously
[**seed_tenant_endpoint**](ArcAdminApi.md#seed_tenant_endpoint) | **POST** /v1/arc/admin/seed | Seed Tenant Endpoint
[**upsert_email_config_v1**](ArcAdminApi.md#upsert_email_config_v1) | **PUT** /v1/arc/admin/email-config | Upsert Email Config
[**verify_email_config_v1**](ArcAdminApi.md#verify_email_config_v1) | **POST** /v1/arc/admin/email-config/verify | Verify Email Config
[**void_remittance_endpoint**](ArcAdminApi.md#void_remittance_endpoint) | **POST** /v1/arc/admin/remittances/{remittance_id}/void | Void Remittance Endpoint


# **backfill_malformed_disputes_v1_arc_admin**
> BackfillMalformedDisputesResponse backfill_malformed_disputes_v1_arc_admin(x_api_key, backfill_malformed_disputes_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Repair AI-classified disputes the pre-T4 router mis-routed

Find AI-classified disputes that landed on $0 amount or fully-paid invoices, soft-resolve them, and re-feed the source comm into the (now-fixed) router so it produces a PROPOSED dispute + operator approval task.  Tenant scope: strictly the tenant resolved by ``get_tenant_id`` from the X-API-Key header.  Operators running cleanup across multiple tenants must rotate keys; the body cannot override the auth-gated tenant.  (An earlier draft accepted ``body.tenant_id``, which let any tenant-scoped key write against another tenant.)  Defensive on real-run rerouting: if the rerun raises (LLM unavailable, anchor resolution exception, etc.) the soft-mark on the broken dispute STAYS — the operator can reclassify the source comm manually via ``POST /admin/communications/{id}/reclassify``.

### Example


```python
import moolabs
from moolabs.models.backfill_malformed_disputes_request import BackfillMalformedDisputesRequest
from moolabs.models.backfill_malformed_disputes_response import BackfillMalformedDisputesResponse
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    backfill_malformed_disputes_request = moolabs.BackfillMalformedDisputesRequest() # BackfillMalformedDisputesRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Repair AI-classified disputes the pre-T4 router mis-routed
        api_response = api_instance.backfill_malformed_disputes_v1_arc_admin(x_api_key, backfill_malformed_disputes_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->backfill_malformed_disputes_v1_arc_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->backfill_malformed_disputes_v1_arc_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **backfill_malformed_disputes_request** | [**BackfillMalformedDisputesRequest**](BackfillMalformedDisputesRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**BackfillMalformedDisputesResponse**](BackfillMalformedDisputesResponse.md)

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

# **bulk_replay_endpoint_v1_arc**
> object bulk_replay_endpoint_v1_arc(x_api_key, bulk_replay_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Bulk Replay Endpoint

POST /admin/dead-letters/bulk-replay — Replay multiple dead-lettered events.

### Example


```python
import moolabs
from moolabs.models.bulk_replay_request import BulkReplayRequest
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    bulk_replay_request = moolabs.BulkReplayRequest() # BulkReplayRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Bulk Replay Endpoint
        api_response = api_instance.bulk_replay_endpoint_v1_arc(x_api_key, bulk_replay_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->bulk_replay_endpoint_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->bulk_replay_endpoint_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **bulk_replay_request** | [**BulkReplayRequest**](BulkReplayRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_agent_run_status_v1**
> object get_agent_run_status_v1(run_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get agent run status

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
    api_instance = moolabs.ArcAdminApi(api_client)
    run_id = 'run_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get agent run status
        api_response = api_instance.get_agent_run_status_v1(run_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->get_agent_run_status_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->get_agent_run_status_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_dead_letters_v1**
> object get_dead_letters_v1(x_api_key, page=page, page_size=page_size, source=source, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Dead Letters

GET /admin/dead-letters — List dead-lettered events.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    source = 'source_example' # str |  (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Dead Letters
        api_response = api_instance.get_dead_letters_v1(x_api_key, page=page, page_size=page_size, source=source, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->get_dead_letters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->get_dead_letters_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **source** | **str**|  | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_email_config_v1**
> EmailConfigOut get_email_config_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Email Config

Return the tenant's BYO sender-domain config (or an empty row).

### Example


```python
import moolabs
from moolabs.models.email_config_out import EmailConfigOut
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Email Config
        api_response = api_instance.get_email_config_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->get_email_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->get_email_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EmailConfigOut**](EmailConfigOut.md)

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

# **get_outbound_failures_v1**
> object get_outbound_failures_v1(x_api_key, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Outbound Failures

GET /admin/outbound-failures — List failed outbound events.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Outbound Failures
        api_response = api_instance.get_outbound_failures_v1(x_api_key, page=page, page_size=page_size, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->get_outbound_failures_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->get_outbound_failures_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_potential_duplicates_v1**
> object get_potential_duplicates_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Potential Duplicates

GET /admin/potential-duplicates — Detect duplicate remittances.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Potential Duplicates
        api_response = api_instance.get_potential_duplicates_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->get_potential_duplicates_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->get_potential_duplicates_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **get_tenant_escalation_config_v1_arc**
> TenantEscalationConfigOut get_tenant_escalation_config_v1_arc(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Get Tenant Escalation Config

Return the effective escalation config for the current tenant.  Always returns a 200; absence of an override row ⇒ defaults apply.

### Example


```python
import moolabs
from moolabs.models.tenant_escalation_config_out import TenantEscalationConfigOut
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Get Tenant Escalation Config
        api_response = api_instance.get_tenant_escalation_config_v1_arc(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->get_tenant_escalation_config_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->get_tenant_escalation_config_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**TenantEscalationConfigOut**](TenantEscalationConfigOut.md)

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

# **import_disputes_endpoint**
> object import_disputes_endpoint(x_api_key, import_disputes_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Import Disputes Endpoint

POST /admin/import/disputes — Bulk create disputes for data migration.

### Example


```python
import moolabs
from moolabs.models.import_disputes_request import ImportDisputesRequest
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    import_disputes_request = moolabs.ImportDisputesRequest() # ImportDisputesRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Import Disputes Endpoint
        api_response = api_instance.import_disputes_endpoint(x_api_key, import_disputes_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->import_disputes_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->import_disputes_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **import_disputes_request** | [**ImportDisputesRequest**](ImportDisputesRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_invoices_endpoint**
> object import_invoices_endpoint(x_api_key, import_invoices_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Import Invoices Endpoint

POST /admin/import/invoices — Bulk upsert invoices for data migration.

### Example


```python
import moolabs
from moolabs.models.import_invoices_request import ImportInvoicesRequest
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    import_invoices_request = moolabs.ImportInvoicesRequest() # ImportInvoicesRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Import Invoices Endpoint
        api_response = api_instance.import_invoices_endpoint(x_api_key, import_invoices_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->import_invoices_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->import_invoices_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **import_invoices_request** | [**ImportInvoicesRequest**](ImportInvoicesRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_promises_endpoint**
> object import_promises_endpoint(x_api_key, import_promises_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Import Promises Endpoint

POST /admin/import/promises — Bulk upsert PTPs for data migration.  Upsert key is ``(tenant_id, external_ptp_id)``.  Recomputes ``case.next_promise_due_at`` for every touched case.

### Example


```python
import moolabs
from moolabs.models.import_promises_request import ImportPromisesRequest
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    import_promises_request = moolabs.ImportPromisesRequest() # ImportPromisesRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Import Promises Endpoint
        api_response = api_instance.import_promises_endpoint(x_api_key, import_promises_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->import_promises_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->import_promises_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **import_promises_request** | [**ImportPromisesRequest**](ImportPromisesRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_remittances_endpoint**
> object merge_remittances_endpoint(x_api_key, merge_remittances_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Merge Remittances Endpoint

POST /admin/remittances/merge — Merge duplicate remittances.

### Example


```python
import moolabs
from moolabs.models.merge_remittances_request import MergeRemittancesRequest
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    merge_remittances_request = moolabs.MergeRemittancesRequest() # MergeRemittancesRequest | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Merge Remittances Endpoint
        api_response = api_instance.merge_remittances_endpoint(x_api_key, merge_remittances_request, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->merge_remittances_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->merge_remittances_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **merge_remittances_request** | [**MergeRemittancesRequest**](MergeRemittancesRequest.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **patch_tenant_escalation_config_v1_arc**
> TenantEscalationConfigOut patch_tenant_escalation_config_v1_arc(x_api_key, tenant_escalation_config_patch, x_tenant_id=x_tenant_id, x_org_id=x_org_id, x_user_id=x_user_id)

Patch Tenant Escalation Config

Deep-merge ``body.config`` over the existing tenant config.  Creates the row on first PATCH.  Always appends an audit row capturing the prior + new configs.

### Example


```python
import moolabs
from moolabs.models.tenant_escalation_config_out import TenantEscalationConfigOut
from moolabs.models.tenant_escalation_config_patch import TenantEscalationConfigPatch
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    tenant_escalation_config_patch = moolabs.TenantEscalationConfigPatch() # TenantEscalationConfigPatch | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)
    x_user_id = 'x_user_id_example' # str |  (optional)

    try:
        # Patch Tenant Escalation Config
        api_response = api_instance.patch_tenant_escalation_config_v1_arc(x_api_key, tenant_escalation_config_patch, x_tenant_id=x_tenant_id, x_org_id=x_org_id, x_user_id=x_user_id)
        print("The response of ArcAdminApi->patch_tenant_escalation_config_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->patch_tenant_escalation_config_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **tenant_escalation_config_patch** | [**TenantEscalationConfigPatch**](TenantEscalationConfigPatch.md)|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 
 **x_user_id** | **str**|  | [optional] 

### Return type

[**TenantEscalationConfigOut**](TenantEscalationConfigOut.md)

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

# **reclassify_communication**
> object reclassify_communication(communication_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Re-enqueue inbound classification for an existing communication

Force the classifier to re-run on a stored communication.  Used by the (future) learning-loop UI to bulk-reclassify after a pattern correction.  Dedupes by ``inbound_classify:<comm_id>`` so the row is queued at most once per comm — re-posting is safe.  Tenant-scoped: looks up the comm by ``(id, tenant_id)`` so an operator authenticated against tenant A cannot force a reclassify on tenant B's inbound email.  Missing comm — or comm belonging to a different tenant — returns 404 without distinguishing the two.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    communication_id = 'communication_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Re-enqueue inbound classification for an existing communication
        api_response = api_instance.reclassify_communication(communication_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->reclassify_communication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->reclassify_communication: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **communication_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replay_dead_letter_endpoint_v1**
> object replay_dead_letter_endpoint_v1(event_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Replay Dead Letter Endpoint

POST /admin/dead-letters/{id}/replay — Replay a single dead-lettered event.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    event_id = 'event_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Replay Dead Letter Endpoint
        api_response = api_instance.replay_dead_letter_endpoint_v1(event_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->replay_dead_letter_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->replay_dead_letter_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **retry_outbound_failure_endpoint_v1**
> object retry_outbound_failure_endpoint_v1(event_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Retry Outbound Failure Endpoint

POST /admin/outbound-failures/{id}/retry — Retry a failed outbound event.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    event_id = 'event_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Retry Outbound Failure Endpoint
        api_response = api_instance.retry_outbound_failure_endpoint_v1(event_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->retry_outbound_failure_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->retry_outbound_failure_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **rotate_inbound_secret_v1_arc**
> EmailConfigOut rotate_inbound_secret_v1_arc(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Rotate Inbound Secret

Rotate the inbound-webhook HMAC secret.  The new secret must be copied into the Resend inbound webhook dashboard; the UI will display it once after rotation.

### Example


```python
import moolabs
from moolabs.models.email_config_out import EmailConfigOut
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Rotate Inbound Secret
        api_response = api_instance.rotate_inbound_secret_v1_arc(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->rotate_inbound_secret_v1_arc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->rotate_inbound_secret_v1_arc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EmailConfigOut**](EmailConfigOut.md)

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

# **run_agent_sync**
> object run_agent_sync(agent_type, x_api_key, case_id=case_id, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Run Agent Synchronously

Run a single batch of the specified agent. Admin/E2E testing only.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    agent_type = 'agent_type_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    case_id = 'case_id_example' # str | Optional: run only for this case (optional)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Run Agent Synchronously
        api_response = api_instance.run_agent_sync(agent_type, x_api_key, case_id=case_id, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->run_agent_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->run_agent_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_type** | **str**|  | 
 **x_api_key** | **str**|  | 
 **case_id** | **str**| Optional: run only for this case | [optional] 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **seed_tenant_endpoint**
> object seed_tenant_endpoint(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Seed Tenant Endpoint

POST /admin/seed — Seed dunning strategies and agent policies.  Idempotent: skips any data that already exists.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Seed Tenant Endpoint
        api_response = api_instance.seed_tenant_endpoint(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->seed_tenant_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->seed_tenant_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

# **upsert_email_config_v1**
> EmailConfigOut upsert_email_config_v1(x_api_key, email_config_upsert, force_secret_overwrite=force_secret_overwrite, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Upsert Email Config

Create or update the tenant's sender-domain config.  If the Resend API key is configured we also provision the domain with Resend and return the DNS records the operator needs to set.

### Example


```python
import moolabs
from moolabs.models.email_config_out import EmailConfigOut
from moolabs.models.email_config_upsert import EmailConfigUpsert
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    email_config_upsert = moolabs.EmailConfigUpsert() # EmailConfigUpsert | 
    force_secret_overwrite = False # bool | Break-glass: allow this PUT to overwrite an existing non-empty ``inbound_secret`` with a different value. Without this flag the server returns 409 to prevent the smoke-harness drift that silently breaks inbound webhooks for real tenants. Use POST /email-config/rotate-secret for the production rotation flow. (optional) (default to False)
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Upsert Email Config
        api_response = api_instance.upsert_email_config_v1(x_api_key, email_config_upsert, force_secret_overwrite=force_secret_overwrite, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->upsert_email_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->upsert_email_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **email_config_upsert** | [**EmailConfigUpsert**](EmailConfigUpsert.md)|  | 
 **force_secret_overwrite** | **bool**| Break-glass: allow this PUT to overwrite an existing non-empty &#x60;&#x60;inbound_secret&#x60;&#x60; with a different value. Without this flag the server returns 409 to prevent the smoke-harness drift that silently breaks inbound webhooks for real tenants. Use POST /email-config/rotate-secret for the production rotation flow. | [optional] [default to False]
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EmailConfigOut**](EmailConfigOut.md)

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

# **verify_email_config_v1**
> EmailConfigOut verify_email_config_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Verify Email Config

Ask Resend to re-check DNS and update verification status.

### Example


```python
import moolabs
from moolabs.models.email_config_out import EmailConfigOut
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
    api_instance = moolabs.ArcAdminApi(api_client)
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Verify Email Config
        api_response = api_instance.verify_email_config_v1(x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->verify_email_config_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->verify_email_config_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

### Return type

[**EmailConfigOut**](EmailConfigOut.md)

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

# **void_remittance_endpoint**
> object void_remittance_endpoint(remittance_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)

Void Remittance Endpoint

POST /admin/remittances/{id}/void — Void a remittance.

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
    api_instance = moolabs.ArcAdminApi(api_client)
    remittance_id = 'remittance_id_example' # str | 
    x_api_key = 'x_api_key_example' # str | 
    x_tenant_id = 'x_tenant_id_example' # str |  (optional)
    x_org_id = 'x_org_id_example' # str |  (optional)

    try:
        # Void Remittance Endpoint
        api_response = api_instance.void_remittance_endpoint(remittance_id, x_api_key, x_tenant_id=x_tenant_id, x_org_id=x_org_id)
        print("The response of ArcAdminApi->void_remittance_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArcAdminApi->void_remittance_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remittance_id** | **str**|  | 
 **x_api_key** | **str**|  | 
 **x_tenant_id** | **str**|  | [optional] 
 **x_org_id** | **str**|  | [optional] 

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

