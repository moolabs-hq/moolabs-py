# moolabs.WordAddinApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**word_open**](WordAddinApi.md#word_open) | **GET** /v1/quotes/{quote_id}/contract/editor/word/open | Word Open
[**word_sync**](WordAddinApi.md#word_sync) | **POST** /v1/quotes/{quote_id}/contract/editor/word/sync | Word Sync


# **word_open**
> object word_open(quote_id)

Word Open

Serve the latest master .docx stamped with a Moolabs bind custom-XML part.  The bind part is a ZIP-embedded XML element (namespace urn:moolabs:bind) whose text content is a JSON object:   {tenant_id, quote_id, doc_key, base_version, bind_token}  The bind_token is a short-TTL (30 min) HS256 JWT scoped to (tenant_id, quote_id, doc_key) with purpose=\"bind\".  It expires so a forwarded copy of the file cannot be replayed after the TTL.  The custom-XML part is NOT visible in Word's standard UI but IS readable by any party who unzips the file — ids only, no long-lived secrets.  Returns 404 when no document has been uploaded for this quote. Returns 503 when WORD_ADDIN_JWT_SECRET is not configured.

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
    api_instance = moolabs.WordAddinApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Word Open
        api_response = api_instance.word_open(quote_id)
        print("The response of WordAddinApi->word_open:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordAddinApi->word_open: %s\n" % e)
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

# **word_sync**
> object word_sync(quote_id, file, base_version, x_bind_token=x_bind_token)

Word Sync

Accept the add-in's current .docx and store it as a new master version.  Auth (SPIKE — see PRODUCTION NOTE in module docstring):   The caller must supply the bind_token in the X-Bind-Token header.   The token is verified (signature + expiry + scope) to prove the caller   holds the file that was served by /word/open.   PRODUCTION: replace bind-token auth with durable session token +   require_quotes_enabled dependency per spec §9.  Version-fence:   base_version must equal the current head version_no for this quote's   contract.  If not (someone else pushed a new version, or the doc is   stale) → 409 Conflict.  The add-in must reconcile (re-open the new   master) before pushing again.  Validation:   - File must start with PK\\x03\\x04 (OOXML/ZIP magic).   - File size must be <= 30 MiB.  Returns:   200 {doc_key, version_no, status: \"stored\"} on success.   409 {detail: \"Version conflict...\"} on stale base_version.   422 on invalid bytes.   401/403 on bad/missing token.

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
    api_instance = moolabs.WordAddinApi(api_client)
    quote_id = 'quote_id_example' # str | 
    file = None # bytearray | The current .docx from the add-in
    base_version = 56 # int | The version_no the add-in derived this doc from
    x_bind_token = '' # str |  (optional) (default to '')

    try:
        # Word Sync
        api_response = api_instance.word_sync(quote_id, file, base_version, x_bind_token=x_bind_token)
        print("The response of WordAddinApi->word_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WordAddinApi->word_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **file** | **bytearray**| The current .docx from the add-in | 
 **base_version** | **int**| The version_no the add-in derived this doc from | 
 **x_bind_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

