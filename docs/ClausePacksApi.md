# moolabs.ClausePacksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dismiss_refinement_endpoint_v1_clause**](ClausePacksApi.md#dismiss_refinement_endpoint_v1_clause) | **POST** /v1/clause-packs/dismiss-refinement | Dismiss Refinement Endpoint
[**fork_pack_endpoint_v1**](ClausePacksApi.md#fork_pack_endpoint_v1) | **POST** /v1/clause-packs/fork | Fork Pack Endpoint
[**get_audit_v1**](ClausePacksApi.md#get_audit_v1) | **GET** /v1/clause-packs/audit/{audit_id} | Get Audit
[**get_effective_pack_endpoint_v1**](ClausePacksApi.md#get_effective_pack_endpoint_v1) | **GET** /v1/clause-packs/effective | Get Effective Pack Endpoint
[**get_proposed_refinements_v1_clause**](ClausePacksApi.md#get_proposed_refinements_v1_clause) | **GET** /v1/clause-packs/proposed-refinements | Get Proposed Refinements
[**post_audit_v1**](ClausePacksApi.md#post_audit_v1) | **POST** /v1/clause-packs/audit | Post Audit
[**post_quick_redline_v1_clause**](ClausePacksApi.md#post_quick_redline_v1_clause) | **POST** /v1/clause-packs/quick-redline | Post Quick Redline
[**post_training_upload_v1_clause**](ClausePacksApi.md#post_training_upload_v1_clause) | **POST** /v1/clause-packs/training-uploads | Post Training Upload
[**ratify_family_endpoint_v1_clause**](ClausePacksApi.md#ratify_family_endpoint_v1_clause) | **POST** /v1/clause-packs/ratify-family | Ratify Family Endpoint
[**ratify_refinement_endpoint_v1_clause**](ClausePacksApi.md#ratify_refinement_endpoint_v1_clause) | **POST** /v1/clause-packs/ratify-refinement | Ratify Refinement Endpoint


# **dismiss_refinement_endpoint_v1_clause**
> object dismiss_refinement_endpoint_v1_clause(dismiss_refinement_request)

Dismiss Refinement Endpoint

Mark a proposed refinement as 'dismissed' (tenant-scoped; 404 if not found).  Returns 204 No Content on success.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.dismiss_refinement_request import DismissRefinementRequest
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
    api_instance = moolabs.ClausePacksApi(api_client)
    dismiss_refinement_request = moolabs.DismissRefinementRequest() # DismissRefinementRequest | 

    try:
        # Dismiss Refinement Endpoint
        api_response = api_instance.dismiss_refinement_endpoint_v1_clause(dismiss_refinement_request)
        print("The response of ClausePacksApi->dismiss_refinement_endpoint_v1_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->dismiss_refinement_endpoint_v1_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dismiss_refinement_request** | [**DismissRefinementRequest**](DismissRefinementRequest.md)|  | 

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

# **fork_pack_endpoint_v1**
> ClausePack fork_pack_endpoint_v1(industry_vertical)

Fork Pack Endpoint

Fork the industry pack into a tenant draft playbook (idempotent).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.clause_pack import ClausePack
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
    api_instance = moolabs.ClausePacksApi(api_client)
    industry_vertical = 'industry_vertical_example' # str | Industry vertical to fork

    try:
        # Fork Pack Endpoint
        api_response = api_instance.fork_pack_endpoint_v1(industry_vertical)
        print("The response of ClausePacksApi->fork_pack_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->fork_pack_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **industry_vertical** | **str**| Industry vertical to fork | 

### Return type

[**ClausePack**](ClausePack.md)

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

# **get_audit_v1**
> Dict[str, object] get_audit_v1(audit_id)

Get Audit

Fetch a previously-run audit by id (scoped to tenant).

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
    api_instance = moolabs.ClausePacksApi(api_client)
    audit_id = 'audit_id_example' # str | 

    try:
        # Get Audit
        api_response = api_instance.get_audit_v1(audit_id)
        print("The response of ClausePacksApi->get_audit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->get_audit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_id** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **get_effective_pack_endpoint_v1**
> ClausePack get_effective_pack_endpoint_v1(industry_vertical)

Get Effective Pack Endpoint

Return the effective clause pack for the authenticated tenant.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.clause_pack import ClausePack
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
    api_instance = moolabs.ClausePacksApi(api_client)
    industry_vertical = 'industry_vertical_example' # str | Industry vertical, e.g. 'ai-saas'

    try:
        # Get Effective Pack Endpoint
        api_response = api_instance.get_effective_pack_endpoint_v1(industry_vertical)
        print("The response of ClausePacksApi->get_effective_pack_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->get_effective_pack_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **industry_vertical** | **str**| Industry vertical, e.g. &#39;ai-saas&#39; | 

### Return type

[**ClausePack**](ClausePack.md)

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

# **get_proposed_refinements_v1_clause**
> List[Dict[str, object]] get_proposed_refinements_v1_clause(industry_vertical=industry_vertical)

Get Proposed Refinements

Return all 'proposed' redline feedback rows for the authenticated tenant.  Rows are newest-first. The optional industry_vertical param is accepted for API symmetry; the query always scopes strictly to the authed tenant.

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
    api_instance = moolabs.ClausePacksApi(api_client)
    industry_vertical = 'industry_vertical_example' # str | Filter by vertical (optional) (optional)

    try:
        # Get Proposed Refinements
        api_response = api_instance.get_proposed_refinements_v1_clause(industry_vertical=industry_vertical)
        print("The response of ClausePacksApi->get_proposed_refinements_v1_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->get_proposed_refinements_v1_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **industry_vertical** | **str**| Filter by vertical (optional) | [optional] 

### Return type

**List[Dict[str, object]]**

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

# **post_audit_v1**
> object post_audit_v1(audit_request)

Post Audit

Run a clause-pack diagnostic audit on one or more uploaded contracts.  Returns 201 with {id, findings, divergences}.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.audit_request import AuditRequest
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
    api_instance = moolabs.ClausePacksApi(api_client)
    audit_request = moolabs.AuditRequest() # AuditRequest | 

    try:
        # Post Audit
        api_response = api_instance.post_audit_v1(audit_request)
        print("The response of ClausePacksApi->post_audit_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->post_audit_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_request** | [**AuditRequest**](AuditRequest.md)|  | 

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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_quick_redline_v1_clause**
> QuickRedlineResponse post_quick_redline_v1_clause(file, industry_vertical=industry_vertical)

Post Quick Redline

Upload a contract and get an instant clause-by-clause redline without creating a quote.  - Accepts multipart/form-data with a `file` field (.txt, .docx, .pdf). - Derives tenant_id from auth context; no quote is created or referenced. - Returns extracted text, document segments, clause findings, and a verdict summary. - 413 if the file exceeds the configured size limit. - 415 if the file type is unsupported (propagated from the parser).

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quick_redline_response import QuickRedlineResponse
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
    api_instance = moolabs.ClausePacksApi(api_client)
    file = None # bytearray | 
    industry_vertical = 'ai-saas' # str | Industry vertical, e.g. 'ai-saas' (optional) (default to 'ai-saas')

    try:
        # Post Quick Redline
        api_response = api_instance.post_quick_redline_v1_clause(file, industry_vertical=industry_vertical)
        print("The response of ClausePacksApi->post_quick_redline_v1_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->post_quick_redline_v1_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **industry_vertical** | **str**| Industry vertical, e.g. &#39;ai-saas&#39; | [optional] [default to &#39;ai-saas&#39;]

### Return type

[**QuickRedlineResponse**](QuickRedlineResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_training_upload_v1_clause**
> object post_training_upload_v1_clause(file)

Post Training Upload

Upload a contract document to the tenant's training corpus (quote_id=NULL).

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
    api_instance = moolabs.ClausePacksApi(api_client)
    file = None # bytearray | 

    try:
        # Post Training Upload
        api_response = api_instance.post_training_upload_v1_clause(file)
        print("The response of ClausePacksApi->post_training_upload_v1_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->post_training_upload_v1_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ratify_family_endpoint_v1_clause**
> ClausePack ratify_family_endpoint_v1_clause(ratify_family_request)

Ratify Family Endpoint

Append a signoff for a clause family in the tenant draft playbook.  actor_id is derived from the authenticated context (portal token subject or api_key fingerprint) — never from the request body.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.clause_pack import ClausePack
from moolabs.models.ratify_family_request import RatifyFamilyRequest
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
    api_instance = moolabs.ClausePacksApi(api_client)
    ratify_family_request = moolabs.RatifyFamilyRequest() # RatifyFamilyRequest | 

    try:
        # Ratify Family Endpoint
        api_response = api_instance.ratify_family_endpoint_v1_clause(ratify_family_request)
        print("The response of ClausePacksApi->ratify_family_endpoint_v1_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->ratify_family_endpoint_v1_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ratify_family_request** | [**RatifyFamilyRequest**](RatifyFamilyRequest.md)|  | 

### Return type

[**ClausePack**](ClausePack.md)

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

# **ratify_refinement_endpoint_v1_clause**
> ClausePack ratify_refinement_endpoint_v1_clause(ratify_refinement_request)

Ratify Refinement Endpoint

Ratify a proposed refinement into the tenant's draft playbook.  Merges proposed_position into the draft family's position criteria, appends a signoff (same mechanism as ratify-family), marks the feedback row 'ratified', and returns the updated ClausePack.  actor_id is derived from the authenticated context — never from the client.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.clause_pack import ClausePack
from moolabs.models.ratify_refinement_request import RatifyRefinementRequest
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
    api_instance = moolabs.ClausePacksApi(api_client)
    ratify_refinement_request = moolabs.RatifyRefinementRequest() # RatifyRefinementRequest | 

    try:
        # Ratify Refinement Endpoint
        api_response = api_instance.ratify_refinement_endpoint_v1_clause(ratify_refinement_request)
        print("The response of ClausePacksApi->ratify_refinement_endpoint_v1_clause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClausePacksApi->ratify_refinement_endpoint_v1_clause: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ratify_refinement_request** | [**RatifyRefinementRequest**](RatifyRefinementRequest.md)|  | 

### Return type

[**ClausePack**](ClausePack.md)

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

