# moolabs.SdkIngestApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ingest_sdk_spans**](SdkIngestApi.md#ingest_sdk_spans) | **POST** /api/v1/ingest/batch | Ingest Sdk Batch


# **ingest_sdk_spans**
> SDKBatchIngestResponse ingest_sdk_spans(sdk_batch_ingest_request)

Ingest Sdk Batch

### Example

* Api Key Authentication (APIKeyHeader):
* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.sdk_batch_ingest_request import SDKBatchIngestRequest
from moolabs.models.sdk_batch_ingest_response import SDKBatchIngestResponse
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

# Configure Bearer authorization (opaque): HTTPBearer
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.SdkIngestApi(api_client)
    sdk_batch_ingest_request = moolabs.SDKBatchIngestRequest() # SDKBatchIngestRequest | 

    try:
        # Ingest Sdk Batch
        api_response = api_instance.ingest_sdk_spans(sdk_batch_ingest_request)
        print("The response of SdkIngestApi->ingest_sdk_spans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SdkIngestApi->ingest_sdk_spans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdk_batch_ingest_request** | [**SDKBatchIngestRequest**](SDKBatchIngestRequest.md)|  | 

### Return type

[**SDKBatchIngestResponse**](SDKBatchIngestResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

