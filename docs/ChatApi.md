# moolabs.ChatApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat**](ChatApi.md#chat) | **POST** /v1/chat | Chat
[**delete_session**](ChatApi.md#delete_session) | **DELETE** /v1/chat/sessions/{session_id} | Delete Session
[**download_arc_report**](ChatApi.md#download_arc_report) | **GET** /v1/chat/reports/{report_id}/download | Download Arc Report
[**get_session**](ChatApi.md#get_session) | **GET** /v1/chat/sessions/{session_id} | Get Session
[**get_starter_prompts**](ChatApi.md#get_starter_prompts) | **GET** /v1/chat/starters | Get Starter Prompts
[**list_sessions**](ChatApi.md#list_sessions) | **GET** /v1/chat/sessions | List Sessions
[**update_session**](ChatApi.md#update_session) | **PATCH** /v1/chat/sessions/{session_id} | Update Session


# **chat**
> object chat(chat_request)

Chat

Chat with MooLabs Assistant. Persists messages to a session.

### Example


```python
import moolabs
from moolabs.models.chat_request import ChatRequest
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
    api_instance = moolabs.ChatApi(api_client)
    chat_request = moolabs.ChatRequest() # ChatRequest | 

    try:
        # Chat
        api_response = api_instance.chat(chat_request)
        print("The response of ChatApi->chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_request** | [**ChatRequest**](ChatRequest.md)|  | 

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

# **delete_session**
> object delete_session(session_id)

Delete Session

Delete a chat session and all its messages.

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
    api_instance = moolabs.ChatApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Delete Session
        api_response = api_instance.delete_session(session_id)
        print("The response of ChatApi->delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

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

# **download_arc_report**
> object download_arc_report(report_id)

Download Arc Report

Proxy ARC report downloads through BFF so UI links remain same-origin.

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
    api_instance = moolabs.ChatApi(api_client)
    report_id = 'report_id_example' # str | 

    try:
        # Download Arc Report
        api_response = api_instance.download_arc_report(report_id)
        print("The response of ChatApi->download_arc_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->download_arc_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**|  | 

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

# **get_session**
> object get_session(session_id)

Get Session

Get a session with all its messages.

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
    api_instance = moolabs.ChatApi(api_client)
    session_id = 'session_id_example' # str | 

    try:
        # Get Session
        api_response = api_instance.get_session(session_id)
        print("The response of ChatApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 

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

# **get_starter_prompts**
> object get_starter_prompts()

Get Starter Prompts

Get conversation starter prompts.

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
    api_instance = moolabs.ChatApi(api_client)

    try:
        # Get Starter Prompts
        api_response = api_instance.get_starter_prompts()
        print("The response of ChatApi->get_starter_prompts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->get_starter_prompts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> object list_sessions(limit=limit, offset=offset)

List Sessions

List chat sessions for the current tenant, newest first.

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
    api_instance = moolabs.ChatApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Sessions
        api_response = api_instance.list_sessions(limit=limit, offset=offset)
        print("The response of ChatApi->list_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->list_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

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

# **update_session**
> object update_session(session_id, request_body)

Update Session

Update session title.

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
    api_instance = moolabs.ChatApi(api_client)
    session_id = 'session_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Session
        api_response = api_instance.update_session(session_id, request_body)
        print("The response of ChatApi->update_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->update_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

