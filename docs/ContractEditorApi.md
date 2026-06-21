# moolabs.ContractEditorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_redline_contract_v1**](ContractEditorApi.md#ai_redline_contract_v1) | **POST** /v1/quotes/{quote_id}/contract/editor/ai-redline | Ai Redline Contract
[**apply_contract_edits_v1**](ContractEditorApi.md#apply_contract_edits_v1) | **POST** /v1/quotes/{quote_id}/contract/editor/apply-edits | Apply Contract Edits
[**ask_moo_redline_v1**](ContractEditorApi.md#ask_moo_redline_v1) | **POST** /v1/quotes/{quote_id}/contract/editor/redline/ask-moo | Ask Moo Redline
[**editor_callback**](ContractEditorApi.md#editor_callback) | **POST** /v1/quotes/{quote_id}/contract/editor/callback | Editor Callback
[**fetch_document**](ContractEditorApi.md#fetch_document) | **GET** /v1/quotes/{quote_id}/contract/editor/document/{doc_key} | Fetch Document
[**get_document_html_v1**](ContractEditorApi.md#get_document_html_v1) | **GET** /v1/quotes/{quote_id}/contract/editor/document-html/{doc_key} | Get Document Html
[**get_editor_config**](ContractEditorApi.md#get_editor_config) | **GET** /v1/quotes/{quote_id}/contract/editor/config | Get Editor Config
[**get_latest_redline_job_v1**](ContractEditorApi.md#get_latest_redline_job_v1) | **GET** /v1/quotes/{quote_id}/contract/editor/ai-redline/latest | Get Latest Redline Job
[**get_redline_edits**](ContractEditorApi.md#get_redline_edits) | **GET** /v1/quotes/{quote_id}/contract/editor/edits/{doc_key} | Get Redline Edits
[**get_redline_job_v1**](ContractEditorApi.md#get_redline_job_v1) | **GET** /v1/quotes/{quote_id}/contract/editor/ai-redline/jobs/{job_id} | Get Redline Job
[**save_redline_edit**](ContractEditorApi.md#save_redline_edit) | **POST** /v1/quotes/{quote_id}/contract/editor/edits | Save Redline Edit
[**upload_contract_for_editor**](ContractEditorApi.md#upload_contract_for_editor) | **POST** /v1/quotes/{quote_id}/contract/editor/upload | Upload Contract For Editor


# **ai_redline_contract_v1**
> object ai_redline_contract_v1(quote_id)

Ai Redline Contract

Enqueue an async AI redline pipeline run for the latest editor doc.  Creates a ``redline_jobs`` row (status=queued) and returns 202 ``{\"job_id\": \"<uuid>\"}``.  The ``redline-job`` worker picks up the row, runs ``build_ai_redline_docx``, and writes the result back.  Poll ``GET .../ai-redline/jobs/{job_id}`` for status.  Returns 404 when no document has been uploaded.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Ai Redline Contract
        api_response = api_instance.ai_redline_contract_v1(quote_id)
        print("The response of ContractEditorApi->ai_redline_contract_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->ai_redline_contract_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

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
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_contract_edits_v1**
> object apply_contract_edits_v1(quote_id)

Apply Contract Edits

Apply saved redline ops and store a new .docx version.  S2 — idempotent base-doc application ---------------------------------------- Ops are always applied against the **base document** (version_no=1 — the first uploaded version for this quote/tenant).  This makes apply-edits idempotent: applying twice with the same ops yields the same output.  New accepts saved after a previous apply (which are recorded under the latest doc_key) are included because ALL ops across ALL doc_keys for this quote are collected and applied in one shot against the base.  This avoids the \"orphaned ops\" bug: previously, after the first apply the latest doc got a new doc_key and any ops saved against the old doc_key were silently missed on subsequent applies.  S4 — AI comment preservation ------------------------------------------- When a completed redline job exists that recorded a ``redlined_doc_key`` (the commented .docx produced by the worker), ops are applied against THAT commented version instead of the bare original.  python-docx preserves ``word/comments.xml`` and the ``w:commentRangeStart/End`` markers in non-edited paragraphs across an open→save round-trip, so AI comments survive in all clauses that were not edited.  Edited paragraphs lose their own inline comment reference (expected — the clause text changed), but all other AI comments remain intact.  Falls back to the original (version_no=1) base when no redline has run.  If no ops exist the latest doc is returned unchanged (no new version created). Returns 404 when no document has been uploaded for this quote.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Apply Contract Edits
        api_response = api_instance.apply_contract_edits_v1(quote_id)
        print("The response of ContractEditorApi->apply_contract_edits_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->apply_contract_edits_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

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

# **ask_moo_redline_v1**
> object ask_moo_redline_v1(quote_id, ask_moo_redline_request)

Ask Moo Redline

Re-review the clause at the given anchor with a human reviewer's instruction.  Logic: 1. Load the latest editor doc + parse + chunk. 2. Find the chunk whose [char_start, char_end) range contains    ``anchor_char_start`` (fallback: nearest by overlap). 3. Re-run ``review_clause`` with the ``instruction`` param. 4. Build an updated ``RedlineFinding`` keeping the original finding_id and anchor. 5. If the chunk maps to a playbook family, write a ``redline_feedback`` row. 6. Return ``{ finding: <RedlineFinding>, feedback_recorded: bool }``.  Returns 404 when no document has been uploaded for this quote.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.ask_moo_redline_request import AskMooRedlineRequest
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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    ask_moo_redline_request = moolabs.AskMooRedlineRequest() # AskMooRedlineRequest | 

    try:
        # Ask Moo Redline
        api_response = api_instance.ask_moo_redline_v1(quote_id, ask_moo_redline_request)
        print("The response of ContractEditorApi->ask_moo_redline_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->ask_moo_redline_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **ask_moo_redline_request** | [**AskMooRedlineRequest**](AskMooRedlineRequest.md)|  | 

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

# **editor_callback**
> object editor_callback(quote_id, t)

Editor Callback

OnlyOffice save callback.  Receives the callback JSON body from the doc-server.  On ``status == 2`` (or 6), downloads the edited .docx from ``payload.url`` and stores it as a new version with a new ``doc_key``.  Always returns ``{\"error\": 0}`` — any other response code causes the doc-server to surface an error to the editor user.  The ``t`` query-parameter is the BFF URL token.  We also verify the OnlyOffice JWT ``token`` field when present in the callback body.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    t = 't_example' # str | BFF URL token

    try:
        # Editor Callback
        api_response = api_instance.editor_callback(quote_id, t)
        print("The response of ContractEditorApi->editor_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->editor_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **t** | **str**| BFF URL token | 

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

# **fetch_document**
> object fetch_document(quote_id, doc_key, t)

Fetch Document

Serve the raw .docx bytes for a specific doc_key.  This endpoint is called by the OnlyOffice doc-server (no user session). Auth is via the ``?t=`` BFF URL token embedded in the ``document.url`` returned by ``GET /contract/editor/config``.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    doc_key = 'doc_key_example' # str | 
    t = 't_example' # str | BFF URL token

    try:
        # Fetch Document
        api_response = api_instance.fetch_document(quote_id, doc_key, t)
        print("The response of ContractEditorApi->fetch_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->fetch_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **doc_key** | **str**|  | 
 **t** | **str**| BFF URL token | 

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

# **get_document_html_v1**
> object get_document_html_v1(quote_id, doc_key)

Get Document Html

Return the sanitized HTML + block map for a specific doc_key.  This is the **browser/session-auth** path for the RedlineWorkspace viewer. It does NOT accept the ``?t=`` short-lived token used by the OnlyOffice doc-server (which fetches server-to-server with no session).  Auth: ``require_quotes_enabled`` (portal/API-key) + ``get_doc_by_key`` (tenant + quote scoped).  A cross-tenant or cross-quote ``doc_key`` returns 404.  Returns 422 when the stored document cannot be rendered (corrupt/unparseable zip). Returns:     ``{ html: str, blocks: [{ block_id, char_start, char_end, text }] }``

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    doc_key = 'doc_key_example' # str | 

    try:
        # Get Document Html
        api_response = api_instance.get_document_html_v1(quote_id, doc_key)
        print("The response of ContractEditorApi->get_document_html_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->get_document_html_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **doc_key** | **str**|  | 

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

# **get_editor_config**
> object get_editor_config(quote_id)

Get Editor Config

Return the OnlyOffice DocEditor configuration for the latest doc version.  Returns 503 when ``ONLYOFFICE_JWT_SECRET`` is not set. Returns 404 when no document has been uploaded for this quote yet.  The ``token`` field in the response signs the entire ``config`` payload with the shared OnlyOffice HS256 secret per the OnlyOffice JWT integration specification.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Editor Config
        api_response = api_instance.get_editor_config(quote_id)
        print("The response of ContractEditorApi->get_editor_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->get_editor_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

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

# **get_latest_redline_job_v1**
> object get_latest_redline_job_v1(quote_id)

Get Latest Redline Job

Return the most recent completed (status='done') redline job for a quote.  Used by the RedlineWorkspace on open so it can show prior findings without kicking a new job.  Returns 204 No Content when no completed job exists yet — the workspace will auto-run a new one in that case.  Returns the same shape as GET .../jobs/{job_id} so the frontend can reuse the same types: ``{job_id, doc_key, status, reviewed, total, findings, result}``.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Latest Redline Job
        api_response = api_instance.get_latest_redline_job_v1(quote_id)
        print("The response of ContractEditorApi->get_latest_redline_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->get_latest_redline_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

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

# **get_redline_edits**
> object get_redline_edits(quote_id, doc_key)

Get Redline Edits

Return the saved edit ops for a (tenant, quote, doc_key) triple.  Returns ``{ doc_key, ops }`` — an empty ``ops`` list when no row exists (not 404, because an empty edit set is a valid state).

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    doc_key = 'doc_key_example' # str | 

    try:
        # Get Redline Edits
        api_response = api_instance.get_redline_edits(quote_id, doc_key)
        print("The response of ContractEditorApi->get_redline_edits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->get_redline_edits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **doc_key** | **str**|  | 

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

# **get_redline_job_v1**
> object get_redline_job_v1(quote_id, job_id)

Get Redline Job

Poll the status of an async AI redline job.  Returns ``{status, reviewed, total, findings, result}`` scoped to the authenticated tenant.  Returns 404 for cross-tenant or unknown job IDs.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    job_id = 'job_id_example' # str | 

    try:
        # Get Redline Job
        api_response = api_instance.get_redline_job_v1(quote_id, job_id)
        print("The response of ContractEditorApi->get_redline_job_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->get_redline_job_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **job_id** | **str**|  | 

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

# **save_redline_edit**
> object save_redline_edit(quote_id, save_redline_edit_request)

Save Redline Edit

Append a targeted edit op for a contract doc.  Upserts a ``redline_edits`` row keyed on (tenant_id, quote_id, doc_key) and appends the new op to the ``ops`` list.  Idempotent across restarts — the caller may re-POST the same op list; duplicates are the caller's concern.  Returns ``{ doc_key, op_count }`` on success.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.save_redline_edit_request import SaveRedlineEditRequest
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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    save_redline_edit_request = moolabs.SaveRedlineEditRequest() # SaveRedlineEditRequest | 

    try:
        # Save Redline Edit
        api_response = api_instance.save_redline_edit(quote_id, save_redline_edit_request)
        print("The response of ContractEditorApi->save_redline_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->save_redline_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **save_redline_edit_request** | [**SaveRedlineEditRequest**](SaveRedlineEditRequest.md)|  | 

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

# **upload_contract_for_editor**
> object upload_contract_for_editor(quote_id, file)

Upload Contract For Editor

Upload a .docx for inline OnlyOffice editing.  Stores the bytes and creates a new ``contract_editor_docs`` row with a fresh ``doc_key``.  Returns 201 ``{\"doc_key\": ..., \"version_no\": ...}``.

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
    api_instance = moolabs.ContractEditorApi(api_client)
    quote_id = 'quote_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload Contract For Editor
        api_response = api_instance.upload_contract_for_editor(quote_id, file)
        print("The response of ContractEditorApi->upload_contract_for_editor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractEditorApi->upload_contract_for_editor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
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

