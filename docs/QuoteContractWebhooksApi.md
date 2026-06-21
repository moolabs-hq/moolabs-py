# moolabs.QuoteContractWebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_quote_contract_inbound_email_v1**](QuoteContractWebhooksApi.md#post_quote_contract_inbound_email_v1) | **POST** /v1/webhooks/quote-contracts/email | Post Quote Contract Inbound Email


# **post_quote_contract_inbound_email_v1**
> InboundEmailProcessResponse post_quote_contract_inbound_email_v1(inbound_email_payload, x_moolabs_signature=x_moolabs_signature)

Post Quote Contract Inbound Email

### Example


```python
import moolabs
from moolabs.models.inbound_email_payload import InboundEmailPayload
from moolabs.models.inbound_email_process_response import InboundEmailProcessResponse
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
    api_instance = moolabs.QuoteContractWebhooksApi(api_client)
    inbound_email_payload = moolabs.InboundEmailPayload() # InboundEmailPayload | 
    x_moolabs_signature = 'x_moolabs_signature_example' # str |  (optional)

    try:
        # Post Quote Contract Inbound Email
        api_response = api_instance.post_quote_contract_inbound_email_v1(inbound_email_payload, x_moolabs_signature=x_moolabs_signature)
        print("The response of QuoteContractWebhooksApi->post_quote_contract_inbound_email_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractWebhooksApi->post_quote_contract_inbound_email_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_email_payload** | [**InboundEmailPayload**](InboundEmailPayload.md)|  | 
 **x_moolabs_signature** | **str**|  | [optional] 

### Return type

[**InboundEmailProcessResponse**](InboundEmailProcessResponse.md)

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

