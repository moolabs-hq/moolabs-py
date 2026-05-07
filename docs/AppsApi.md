# moolabs.AppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app**](AppsApi.md#get_app) | **GET** /api/v1/apps/{id} | Get app
[**get_marketplace_listing**](AppsApi.md#get_marketplace_listing) | **GET** /api/v1/marketplace/listings/{type} | Get app details by type
[**list_apps**](AppsApi.md#list_apps) | **GET** /api/v1/apps | List apps
[**list_marketplace_listings**](AppsApi.md#list_marketplace_listings) | **GET** /api/v1/marketplace/listings | List available apps
[**marketplace_app_api_key_install**](AppsApi.md#marketplace_app_api_key_install) | **POST** /api/v1/marketplace/listings/{type}/install/apikey | Install app via API key
[**marketplace_app_install**](AppsApi.md#marketplace_app_install) | **POST** /api/v1/marketplace/listings/{type}/install | Install app
[**marketplace_o_auth2_install_authorize**](AppsApi.md#marketplace_o_auth2_install_authorize) | **GET** /api/v1/marketplace/listings/{type}/install/oauth2/authorize | Install app via OAuth2
[**marketplace_o_auth2_install_get_url**](AppsApi.md#marketplace_o_auth2_install_get_url) | **GET** /api/v1/marketplace/listings/{type}/install/oauth2 | Get OAuth2 install URL
[**uninstall_app**](AppsApi.md#uninstall_app) | **DELETE** /api/v1/apps/{id} | Uninstall app
[**update_app**](AppsApi.md#update_app) | **PUT** /api/v1/apps/{id} | Update app


# **get_app**
> App get_app(id)

Get app

Get the app.

### Example


```python
import moolabs
from moolabs.models.app import App
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
    api_instance = moolabs.AppsApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Get app
        api_response = api_instance.get_app(id)
        print("The response of AppsApi->get_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**App**](App.md)

### Authorization

No authorization required

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

# **get_marketplace_listing**
> MarketplaceListing get_marketplace_listing(type)

Get app details by type

Get a marketplace listing by type.

### Example


```python
import moolabs
from moolabs.models.app_type import AppType
from moolabs.models.marketplace_listing import MarketplaceListing
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
    api_instance = moolabs.AppsApi(api_client)
    type = moolabs.AppType() # AppType | 

    try:
        # Get app details by type
        api_response = api_instance.get_marketplace_listing(type)
        print("The response of AppsApi->get_marketplace_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_marketplace_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AppType**](.md)|  | 

### Return type

[**MarketplaceListing**](MarketplaceListing.md)

### Authorization

No authorization required

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

# **list_apps**
> AppPaginatedResponse list_apps(page=page, page_size=page_size)

List apps

List apps.

### Example


```python
import moolabs
from moolabs.models.app_paginated_response import AppPaginatedResponse
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
    api_instance = moolabs.AppsApi(api_client)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)

    try:
        # List apps
        api_response = api_instance.list_apps(page=page, page_size=page_size)
        print("The response of AppsApi->list_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]

### Return type

[**AppPaginatedResponse**](AppPaginatedResponse.md)

### Authorization

No authorization required

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

# **list_marketplace_listings**
> MarketplaceListingPaginatedResponse list_marketplace_listings(page=page, page_size=page_size)

List available apps

List available apps of the app marketplace.

### Example


```python
import moolabs
from moolabs.models.marketplace_listing_paginated_response import MarketplaceListingPaginatedResponse
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
    api_instance = moolabs.AppsApi(api_client)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)

    try:
        # List available apps
        api_response = api_instance.list_marketplace_listings(page=page, page_size=page_size)
        print("The response of AppsApi->list_marketplace_listings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->list_marketplace_listings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]

### Return type

[**MarketplaceListingPaginatedResponse**](MarketplaceListingPaginatedResponse.md)

### Authorization

No authorization required

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

# **marketplace_app_api_key_install**
> MarketplaceInstallResponse marketplace_app_api_key_install(type, marketplace_app_api_key_install_request)

Install app via API key

Install an marketplace app via API Key.

### Example


```python
import moolabs
from moolabs.models.app_type import AppType
from moolabs.models.marketplace_app_api_key_install_request import MarketplaceAppAPIKeyInstallRequest
from moolabs.models.marketplace_install_response import MarketplaceInstallResponse
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
    api_instance = moolabs.AppsApi(api_client)
    type = moolabs.AppType() # AppType | The type of the app to install.
    marketplace_app_api_key_install_request = moolabs.MarketplaceAppAPIKeyInstallRequest() # MarketplaceAppAPIKeyInstallRequest | 

    try:
        # Install app via API key
        api_response = api_instance.marketplace_app_api_key_install(type, marketplace_app_api_key_install_request)
        print("The response of AppsApi->marketplace_app_api_key_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->marketplace_app_api_key_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AppType**](.md)| The type of the app to install. | 
 **marketplace_app_api_key_install_request** | [**MarketplaceAppAPIKeyInstallRequest**](MarketplaceAppAPIKeyInstallRequest.md)|  | 

### Return type

[**MarketplaceInstallResponse**](MarketplaceInstallResponse.md)

### Authorization

No authorization required

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

# **marketplace_app_install**
> MarketplaceInstallResponse marketplace_app_install(type, marketplace_install_request_payload)

Install app

Install an app from the marketplace.

### Example


```python
import moolabs
from moolabs.models.app_type import AppType
from moolabs.models.marketplace_install_request_payload import MarketplaceInstallRequestPayload
from moolabs.models.marketplace_install_response import MarketplaceInstallResponse
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
    api_instance = moolabs.AppsApi(api_client)
    type = moolabs.AppType() # AppType | The type of the app to install.
    marketplace_install_request_payload = moolabs.MarketplaceInstallRequestPayload() # MarketplaceInstallRequestPayload | 

    try:
        # Install app
        api_response = api_instance.marketplace_app_install(type, marketplace_install_request_payload)
        print("The response of AppsApi->marketplace_app_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->marketplace_app_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AppType**](.md)| The type of the app to install. | 
 **marketplace_install_request_payload** | [**MarketplaceInstallRequestPayload**](MarketplaceInstallRequestPayload.md)|  | 

### Return type

[**MarketplaceInstallResponse**](MarketplaceInstallResponse.md)

### Authorization

No authorization required

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

# **marketplace_o_auth2_install_authorize**
> UnexpectedProblemResponse marketplace_o_auth2_install_authorize(type, state=state, code=code, error=error, error_description=error_description, error_uri=error_uri)

Install app via OAuth2

Authorize OAuth2 code. Verifies the OAuth code and exchanges it for a token and refresh token

### Example


```python
import moolabs
from moolabs.models.app_type import AppType
from moolabs.models.o_auth2_authorization_code_grant_error_type import OAuth2AuthorizationCodeGrantErrorType
from moolabs.models.unexpected_problem_response import UnexpectedProblemResponse
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
    api_instance = moolabs.AppsApi(api_client)
    type = moolabs.AppType() # AppType | The type of the app to install.
    state = 'state_example' # str | Required if the \"state\" parameter was present in the client authorization request. The exact value received from the client:  Unique, randomly generated, opaque, and non-guessable string that is sent when starting an authentication request and validated when processing the response. (optional)
    code = 'code_example' # str | Authorization code which the client will later exchange for an access token. Required with the success response. (optional)
    error = moolabs.OAuth2AuthorizationCodeGrantErrorType() # OAuth2AuthorizationCodeGrantErrorType | Error code. Required with the error response. (optional)
    error_description = 'error_description_example' # str | Optional human-readable text providing additional information, used to assist the client developer in understanding the error that occurred. (optional)
    error_uri = 'error_uri_example' # str | Optional uri identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error (optional)

    try:
        # Install app via OAuth2
        api_response = api_instance.marketplace_o_auth2_install_authorize(type, state=state, code=code, error=error, error_description=error_description, error_uri=error_uri)
        print("The response of AppsApi->marketplace_o_auth2_install_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->marketplace_o_auth2_install_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AppType**](.md)| The type of the app to install. | 
 **state** | **str**| Required if the \&quot;state\&quot; parameter was present in the client authorization request. The exact value received from the client:  Unique, randomly generated, opaque, and non-guessable string that is sent when starting an authentication request and validated when processing the response. | [optional] 
 **code** | **str**| Authorization code which the client will later exchange for an access token. Required with the success response. | [optional] 
 **error** | [**OAuth2AuthorizationCodeGrantErrorType**](.md)| Error code. Required with the error response. | [optional] 
 **error_description** | **str**| Optional human-readable text providing additional information, used to assist the client developer in understanding the error that occurred. | [optional] 
 **error_uri** | **str**| Optional uri identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error | [optional] 

### Return type

[**UnexpectedProblemResponse**](UnexpectedProblemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**303** | Redirection |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_o_auth2_install_get_url**
> ClientAppStartResponse marketplace_o_auth2_install_get_url(type)

Get OAuth2 install URL

Install an app via OAuth. Returns a URL to start the OAuth 2.0 flow.

### Example


```python
import moolabs
from moolabs.models.app_type import AppType
from moolabs.models.client_app_start_response import ClientAppStartResponse
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
    api_instance = moolabs.AppsApi(api_client)
    type = moolabs.AppType() # AppType | 

    try:
        # Get OAuth2 install URL
        api_response = api_instance.marketplace_o_auth2_install_get_url(type)
        print("The response of AppsApi->marketplace_o_auth2_install_get_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->marketplace_o_auth2_install_get_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**AppType**](.md)|  | 

### Return type

[**ClientAppStartResponse**](ClientAppStartResponse.md)

### Authorization

No authorization required

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

# **uninstall_app**
> uninstall_app(id)

Uninstall app

Uninstall an app.

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
    api_instance = moolabs.AppsApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Uninstall app
        api_instance.uninstall_app(id)
    except Exception as e:
        print("Exception when calling AppsApi->uninstall_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

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
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> App update_app(id, app_replace_update)

Update app

Update an app.

### Example


```python
import moolabs
from moolabs.models.app import App
from moolabs.models.app_replace_update import AppReplaceUpdate
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
    api_instance = moolabs.AppsApi(api_client)
    id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    app_replace_update = moolabs.AppReplaceUpdate() # AppReplaceUpdate | 

    try:
        # Update app
        api_response = api_instance.update_app(id, app_replace_update)
        print("The response of AppsApi->update_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->update_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **app_replace_update** | [**AppReplaceUpdate**](AppReplaceUpdate.md)|  | 

### Return type

[**App**](App.md)

### Authorization

No authorization required

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
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

