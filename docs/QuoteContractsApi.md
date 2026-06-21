# moolabs.QuoteContractsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_quote_contract_participant_v1**](QuoteContractsApi.md#add_quote_contract_participant_v1) | **POST** /v1/quotes/{quote_id}/contract-thread/participants | Add Quote Contract Participant
[**create_quote_contract_thread_v1**](QuoteContractsApi.md#create_quote_contract_thread_v1) | **POST** /v1/quotes/{quote_id}/contract-thread | Create Quote Contract Thread
[**get_quote_contract_thread_v1**](QuoteContractsApi.md#get_quote_contract_thread_v1) | **GET** /v1/quotes/{quote_id}/contract-thread | Get Quote Contract Thread
[**list_quote_contract_quarantine_v1**](QuoteContractsApi.md#list_quote_contract_quarantine_v1) | **GET** /v1/quotes/{quote_id}/contract-thread/quarantine | List Quote Contract Quarantine
[**list_quote_contract_versions_v1**](QuoteContractsApi.md#list_quote_contract_versions_v1) | **GET** /v1/quotes/{quote_id}/contract-thread/versions | List Quote Contract Versions
[**promote_quote_contract_quarantine_sender_v1**](QuoteContractsApi.md#promote_quote_contract_quarantine_sender_v1) | **POST** /v1/quotes/{quote_id}/contract-thread/quarantine/{message_id}/promote | Promote Quote Contract Quarantine Sender
[**remove_quote_contract_participant_v1**](QuoteContractsApi.md#remove_quote_contract_participant_v1) | **DELETE** /v1/quotes/{quote_id}/contract-thread/participants/{participant_id} | Remove Quote Contract Participant
[**reprocess_quote_contract_quarantine_message_v1**](QuoteContractsApi.md#reprocess_quote_contract_quarantine_message_v1) | **POST** /v1/quotes/{quote_id}/contract-thread/quarantine/{message_id}/reprocess | Reprocess Quote Contract Quarantine Message
[**upload_quote_contract_version_v1**](QuoteContractsApi.md#upload_quote_contract_version_v1) | **POST** /v1/quotes/{quote_id}/contract-thread/versions | Upload Quote Contract Version


# **add_quote_contract_participant_v1**
> ContractParticipantResponse add_quote_contract_participant_v1(quote_id, add_contract_participant_request)

Add Quote Contract Participant

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.add_contract_participant_request import AddContractParticipantRequest
from moolabs.models.contract_participant_response import ContractParticipantResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    add_contract_participant_request = moolabs.AddContractParticipantRequest() # AddContractParticipantRequest | 

    try:
        # Add Quote Contract Participant
        api_response = api_instance.add_quote_contract_participant_v1(quote_id, add_contract_participant_request)
        print("The response of QuoteContractsApi->add_quote_contract_participant_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->add_quote_contract_participant_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **add_contract_participant_request** | [**AddContractParticipantRequest**](AddContractParticipantRequest.md)|  | 

### Return type

[**ContractParticipantResponse**](ContractParticipantResponse.md)

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

# **create_quote_contract_thread_v1**
> ContractThreadSnapshotResponse create_quote_contract_thread_v1(quote_id, create_contract_thread_request=create_contract_thread_request)

Create Quote Contract Thread

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.contract_thread_snapshot_response import ContractThreadSnapshotResponse
from moolabs.models.create_contract_thread_request import CreateContractThreadRequest
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    create_contract_thread_request = moolabs.CreateContractThreadRequest() # CreateContractThreadRequest |  (optional)

    try:
        # Create Quote Contract Thread
        api_response = api_instance.create_quote_contract_thread_v1(quote_id, create_contract_thread_request=create_contract_thread_request)
        print("The response of QuoteContractsApi->create_quote_contract_thread_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->create_quote_contract_thread_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **create_contract_thread_request** | [**CreateContractThreadRequest**](CreateContractThreadRequest.md)|  | [optional] 

### Return type

[**ContractThreadSnapshotResponse**](ContractThreadSnapshotResponse.md)

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

# **get_quote_contract_thread_v1**
> ContractThreadSnapshotResponse get_quote_contract_thread_v1(quote_id)

Get Quote Contract Thread

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.contract_thread_snapshot_response import ContractThreadSnapshotResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # Get Quote Contract Thread
        api_response = api_instance.get_quote_contract_thread_v1(quote_id)
        print("The response of QuoteContractsApi->get_quote_contract_thread_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->get_quote_contract_thread_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

### Return type

[**ContractThreadSnapshotResponse**](ContractThreadSnapshotResponse.md)

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

# **list_quote_contract_quarantine_v1**
> List[ContractInboundMessageResponse] list_quote_contract_quarantine_v1(quote_id)

List Quote Contract Quarantine

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.contract_inbound_message_response import ContractInboundMessageResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # List Quote Contract Quarantine
        api_response = api_instance.list_quote_contract_quarantine_v1(quote_id)
        print("The response of QuoteContractsApi->list_quote_contract_quarantine_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->list_quote_contract_quarantine_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

### Return type

[**List[ContractInboundMessageResponse]**](ContractInboundMessageResponse.md)

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

# **list_quote_contract_versions_v1**
> List[ContractVersionResponse] list_quote_contract_versions_v1(quote_id)

List Quote Contract Versions

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.contract_version_response import ContractVersionResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 

    try:
        # List Quote Contract Versions
        api_response = api_instance.list_quote_contract_versions_v1(quote_id)
        print("The response of QuoteContractsApi->list_quote_contract_versions_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->list_quote_contract_versions_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 

### Return type

[**List[ContractVersionResponse]**](ContractVersionResponse.md)

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

# **promote_quote_contract_quarantine_sender_v1**
> ContractParticipantResponse promote_quote_contract_quarantine_sender_v1(quote_id, message_id, add_contract_participant_request)

Promote Quote Contract Quarantine Sender

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.add_contract_participant_request import AddContractParticipantRequest
from moolabs.models.contract_participant_response import ContractParticipantResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    message_id = 'message_id_example' # str | 
    add_contract_participant_request = moolabs.AddContractParticipantRequest() # AddContractParticipantRequest | 

    try:
        # Promote Quote Contract Quarantine Sender
        api_response = api_instance.promote_quote_contract_quarantine_sender_v1(quote_id, message_id, add_contract_participant_request)
        print("The response of QuoteContractsApi->promote_quote_contract_quarantine_sender_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->promote_quote_contract_quarantine_sender_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **message_id** | **str**|  | 
 **add_contract_participant_request** | [**AddContractParticipantRequest**](AddContractParticipantRequest.md)|  | 

### Return type

[**ContractParticipantResponse**](ContractParticipantResponse.md)

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

# **remove_quote_contract_participant_v1**
> RemoveContractParticipantResponse remove_quote_contract_participant_v1(quote_id, participant_id)

Remove Quote Contract Participant

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.remove_contract_participant_response import RemoveContractParticipantResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    participant_id = 'participant_id_example' # str | 

    try:
        # Remove Quote Contract Participant
        api_response = api_instance.remove_quote_contract_participant_v1(quote_id, participant_id)
        print("The response of QuoteContractsApi->remove_quote_contract_participant_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->remove_quote_contract_participant_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **participant_id** | **str**|  | 

### Return type

[**RemoveContractParticipantResponse**](RemoveContractParticipantResponse.md)

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

# **reprocess_quote_contract_quarantine_message_v1**
> InboundEmailProcessResponse reprocess_quote_contract_quarantine_message_v1(quote_id, message_id)

Reprocess Quote Contract Quarantine Message

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.inbound_email_process_response import InboundEmailProcessResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Reprocess Quote Contract Quarantine Message
        api_response = api_instance.reprocess_quote_contract_quarantine_message_v1(quote_id, message_id)
        print("The response of QuoteContractsApi->reprocess_quote_contract_quarantine_message_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->reprocess_quote_contract_quarantine_message_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**InboundEmailProcessResponse**](InboundEmailProcessResponse.md)

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

# **upload_quote_contract_version_v1**
> ContractVersionResponse upload_quote_contract_version_v1(quote_id, file)

Upload Quote Contract Version

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.contract_version_response import ContractVersionResponse
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
    api_instance = moolabs.QuoteContractsApi(api_client)
    quote_id = 'quote_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload Quote Contract Version
        api_response = api_instance.upload_quote_contract_version_v1(quote_id, file)
        print("The response of QuoteContractsApi->upload_quote_contract_version_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteContractsApi->upload_quote_contract_version_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**ContractVersionResponse**](ContractVersionResponse.md)

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

