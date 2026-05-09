# moolabs.SubjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subject**](SubjectsApi.md#delete_subject) | **DELETE** /api/v1/subjects/{subjectIdOrKey} | Delete subject
[**get_subject**](SubjectsApi.md#get_subject) | **GET** /api/v1/subjects/{subjectIdOrKey} | Get subject
[**list_subjects**](SubjectsApi.md#list_subjects) | **GET** /api/v1/subjects | List subjects
[**upsert_subject**](SubjectsApi.md#upsert_subject) | **POST** /api/v1/subjects | Upsert subject


# **delete_subject**
> delete_subject(subject_id_or_key)

Delete subject

Delete subject by ID or key.

### Example

* Bearer Authentication (CloudTokenAuth):

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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.SubjectsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 

    try:
        # Delete subject
        api_instance.delete_subject(subject_id_or_key)
    except Exception as e:
        print("Exception when calling SubjectsApi->delete_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | There is no content to send for this request, but the headers may be useful.  |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subject**
> Subject get_subject(subject_id_or_key)

Get subject

Get subject by ID or key.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subject import Subject
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.SubjectsApi(api_client)
    subject_id_or_key = 'subject_id_or_key_example' # str | 

    try:
        # Get subject
        api_response = api_instance.get_subject(subject_id_or_key)
        print("The response of SubjectsApi->get_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->get_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_id_or_key** | **str**|  | 

### Return type

[**Subject**](Subject.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subjects**
> List[Subject] list_subjects()

List subjects

List subjects.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subject import Subject
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.SubjectsApi(api_client)

    try:
        # List subjects
        api_response = api_instance.list_subjects()
        print("The response of SubjectsApi->list_subjects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->list_subjects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Subject]**](Subject.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_subject**
> List[Subject] upsert_subject(subject_upsert)

Upsert subject

Upserts a subject. Creates or updates subject.  If the subject doesn't exist, it will be created. If the subject exists, it will be partially updated with the provided fields.

### Example

* Bearer Authentication (CloudTokenAuth):

```python
import moolabs
from moolabs.models.subject import Subject
from moolabs.models.subject_upsert import SubjectUpsert
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

# Configure Bearer authorization: CloudTokenAuth
configuration = moolabs.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with moolabs.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moolabs.SubjectsApi(api_client)
    subject_upsert = [moolabs.SubjectUpsert()] # List[SubjectUpsert] | 

    try:
        # Upsert subject
        api_response = api_instance.upsert_subject(subject_upsert)
        print("The response of SubjectsApi->upsert_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsApi->upsert_subject: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_upsert** | [**List[SubjectUpsert]**](SubjectUpsert.md)|  | 

### Return type

[**List[Subject]**](Subject.md)

### Authorization

[CloudTokenAuth](../README.md#CloudTokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request has succeeded. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

