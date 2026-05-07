# moolabs.ProductCatalogApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_addon**](ProductCatalogApi.md#archive_addon) | **POST** /api/v1/addons/{addonId}/archive | Archive add-on version
[**archive_plan**](ProductCatalogApi.md#archive_plan) | **POST** /api/v1/plans/{planId}/archive | Archive plan version
[**create_addon**](ProductCatalogApi.md#create_addon) | **POST** /api/v1/addons | Create an add-on
[**create_feature**](ProductCatalogApi.md#create_feature) | **POST** /api/v1/features | Create feature
[**create_plan**](ProductCatalogApi.md#create_plan) | **POST** /api/v1/plans | Create a plan
[**create_plan_addon**](ProductCatalogApi.md#create_plan_addon) | **POST** /api/v1/plans/{planId}/addons | Create new add-on assignment for plan
[**delete_addon**](ProductCatalogApi.md#delete_addon) | **DELETE** /api/v1/addons/{addonId} | Delete add-on
[**delete_feature**](ProductCatalogApi.md#delete_feature) | **DELETE** /api/v1/features/{featureId} | Delete feature
[**delete_plan**](ProductCatalogApi.md#delete_plan) | **DELETE** /api/v1/plans/{planId} | Delete plan
[**delete_plan_addon**](ProductCatalogApi.md#delete_plan_addon) | **DELETE** /api/v1/plans/{planId}/addons/{planAddonId} | Delete add-on assignment for plan
[**get_addon**](ProductCatalogApi.md#get_addon) | **GET** /api/v1/addons/{addonId} | Get add-on
[**get_feature**](ProductCatalogApi.md#get_feature) | **GET** /api/v1/features/{featureId} | Get feature
[**get_plan**](ProductCatalogApi.md#get_plan) | **GET** /api/v1/plans/{planId} | Get plan
[**get_plan_addon**](ProductCatalogApi.md#get_plan_addon) | **GET** /api/v1/plans/{planId}/addons/{planAddonId} | Get add-on assignment for plan
[**list_addons**](ProductCatalogApi.md#list_addons) | **GET** /api/v1/addons | List add-ons
[**list_features**](ProductCatalogApi.md#list_features) | **GET** /api/v1/features | List features
[**list_plan_addons**](ProductCatalogApi.md#list_plan_addons) | **GET** /api/v1/plans/{planId}/addons | List all available add-ons for plan
[**list_plans**](ProductCatalogApi.md#list_plans) | **GET** /api/v1/plans | List plans
[**next_plan**](ProductCatalogApi.md#next_plan) | **POST** /api/v1/plans/{planIdOrKey}/next | New draft plan
[**publish_addon**](ProductCatalogApi.md#publish_addon) | **POST** /api/v1/addons/{addonId}/publish | Publish add-on
[**publish_plan**](ProductCatalogApi.md#publish_plan) | **POST** /api/v1/plans/{planId}/publish | Publish plan
[**update_addon**](ProductCatalogApi.md#update_addon) | **PUT** /api/v1/addons/{addonId} | Update add-on
[**update_plan**](ProductCatalogApi.md#update_plan) | **PUT** /api/v1/plans/{planId} | Update a plan
[**update_plan_addon**](ProductCatalogApi.md#update_plan_addon) | **PUT** /api/v1/plans/{planId}/addons/{planAddonId} | Update add-on assignment for plan


# **archive_addon**
> Addon archive_addon(addon_id)

Archive add-on version

Archive a add-on version.

### Example


```python
import moolabs
from moolabs.models.addon import Addon
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Archive add-on version
        api_response = api_instance.archive_addon(addon_id)
        print("The response of ProductCatalogApi->archive_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->archive_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  | 

### Return type

[**Addon**](Addon.md)

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

# **archive_plan**
> Plan archive_plan(plan_id)

Archive plan version

Archive a plan version.

### Example


```python
import moolabs
from moolabs.models.plan import Plan
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Archive plan version
        api_response = api_instance.archive_plan(plan_id)
        print("The response of ProductCatalogApi->archive_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->archive_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

### Return type

[**Plan**](Plan.md)

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

# **create_addon**
> Addon create_addon(addon_create)

Create an add-on

Create a new add-on.

### Example


```python
import moolabs
from moolabs.models.addon import Addon
from moolabs.models.addon_create import AddonCreate
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    addon_create = moolabs.AddonCreate() # AddonCreate | 

    try:
        # Create an add-on
        api_response = api_instance.create_addon(addon_create)
        print("The response of ProductCatalogApi->create_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->create_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_create** | [**AddonCreate**](AddonCreate.md)|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_feature**
> Feature create_feature(feature_create_inputs)

Create feature

Features are either metered or static. A feature is metered if meterSlug is provided at creation. For metered features you can pass additional filters that will be applied when calculating feature usage, based on the meter's groupBy fields. Only meters with SUM and COUNT aggregation are supported for features. Features cannot be updated later, only archived.

### Example


```python
import moolabs
from moolabs.models.feature import Feature
from moolabs.models.feature_create_inputs import FeatureCreateInputs
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    feature_create_inputs = moolabs.FeatureCreateInputs() # FeatureCreateInputs | 

    try:
        # Create feature
        api_response = api_instance.create_feature(feature_create_inputs)
        print("The response of ProductCatalogApi->create_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->create_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_create_inputs** | [**FeatureCreateInputs**](FeatureCreateInputs.md)|  | 

### Return type

[**Feature**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plan**
> Plan create_plan(plan_create)

Create a plan

Create a new plan.

### Example


```python
import moolabs
from moolabs.models.plan import Plan
from moolabs.models.plan_create import PlanCreate
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_create = moolabs.PlanCreate() # PlanCreate | 

    try:
        # Create a plan
        api_response = api_instance.create_plan(plan_create)
        print("The response of ProductCatalogApi->create_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->create_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_create** | [**PlanCreate**](PlanCreate.md)|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plan_addon**
> PlanAddon create_plan_addon(plan_id, plan_addon_create)

Create new add-on assignment for plan

Create new add-on assignment for plan.

### Example


```python
import moolabs
from moolabs.models.plan_addon import PlanAddon
from moolabs.models.plan_addon_create import PlanAddonCreate
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    plan_addon_create = moolabs.PlanAddonCreate() # PlanAddonCreate | 

    try:
        # Create new add-on assignment for plan
        api_response = api_instance.create_plan_addon(plan_id, plan_addon_create)
        print("The response of ProductCatalogApi->create_plan_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->create_plan_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **plan_addon_create** | [**PlanAddonCreate**](PlanAddonCreate.md)|  | 

### Return type

[**PlanAddon**](PlanAddon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**409** | The request could not be completed due to a conflict with the current state of the target resource. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_addon**
> delete_addon(addon_id)

Delete add-on

Soft delete add-on by id.  Once a add-on is deleted it cannot be undeleted.

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
    api_instance = moolabs.ProductCatalogApi(api_client)
    addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete add-on
        api_instance.delete_addon(addon_id)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->delete_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  | 

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

# **delete_feature**
> delete_feature(feature_id)

Delete feature

Archive a feature by ID.  Once a feature is archived it cannot be unarchived. If a feature is archived, new entitlements cannot be created for it, but archiving the feature does not affect existing entitlements. This means, if you want to create a new feature with the same key, and then create entitlements for it, the previous entitlements have to be deleted first on a per subject basis.

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
    api_instance = moolabs.ProductCatalogApi(api_client)
    feature_id = 'feature_id_example' # str | 

    try:
        # Delete feature
        api_instance.delete_feature(feature_id)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->delete_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 

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

# **delete_plan**
> delete_plan(plan_id)

Delete plan

Soft delete plan by plan.id.  Once a plan is deleted it cannot be undeleted.

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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete plan
        api_instance.delete_plan(plan_id)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->delete_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

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

# **delete_plan_addon**
> delete_plan_addon(plan_id, plan_addon_id)

Delete add-on assignment for plan

Delete add-on assignment for plan.  Once a plan is deleted it cannot be undeleted.

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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    plan_addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Delete add-on assignment for plan
        api_instance.delete_plan_addon(plan_id, plan_addon_id)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->delete_plan_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **plan_addon_id** | **str**|  | 

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

# **get_addon**
> Addon get_addon(addon_id, include_latest=include_latest)

Get add-on

Get add-on by id or key. The latest published version is returned if latter is used.

### Example


```python
import moolabs
from moolabs.models.addon import Addon
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    addon_id = 'addon_id_example' # str | 
    include_latest = False # bool | Include latest version of the add-on instead of the version in active state.  Usage: `?includeLatest=true` (optional) (default to False)

    try:
        # Get add-on
        api_response = api_instance.get_addon(addon_id, include_latest=include_latest)
        print("The response of ProductCatalogApi->get_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  | 
 **include_latest** | **bool**| Include latest version of the add-on instead of the version in active state.  Usage: &#x60;?includeLatest&#x3D;true&#x60; | [optional] [default to False]

### Return type

[**Addon**](Addon.md)

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

# **get_feature**
> Feature get_feature(feature_id)

Get feature

Get a feature by ID.

### Example


```python
import moolabs
from moolabs.models.feature import Feature
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    feature_id = 'feature_id_example' # str | 

    try:
        # Get feature
        api_response = api_instance.get_feature(feature_id)
        print("The response of ProductCatalogApi->get_feature:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_feature: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **feature_id** | **str**|  | 

### Return type

[**Feature**](Feature.md)

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

# **get_plan**
> Plan get_plan(plan_id, include_latest=include_latest)

Get plan

Get a plan by id or key. The latest published version is returned if latter is used.

### Example


```python
import moolabs
from moolabs.models.plan import Plan
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = 'plan_id_example' # str | 
    include_latest = False # bool | Include latest version of the Plan instead of the version in active state.  Usage: `?includeLatest=true` (optional) (default to False)

    try:
        # Get plan
        api_response = api_instance.get_plan(plan_id, include_latest=include_latest)
        print("The response of ProductCatalogApi->get_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **include_latest** | **bool**| Include latest version of the Plan instead of the version in active state.  Usage: &#x60;?includeLatest&#x3D;true&#x60; | [optional] [default to False]

### Return type

[**Plan**](Plan.md)

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

# **get_plan_addon**
> PlanAddon get_plan_addon(plan_id, plan_addon_id)

Get add-on assignment for plan

Get add-on assignment for plan by id.

### Example


```python
import moolabs
from moolabs.models.plan_addon import PlanAddon
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = 'plan_id_example' # str | 
    plan_addon_id = 'plan_addon_id_example' # str | 

    try:
        # Get add-on assignment for plan
        api_response = api_instance.get_plan_addon(plan_id, plan_addon_id)
        print("The response of ProductCatalogApi->get_plan_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->get_plan_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **plan_addon_id** | **str**|  | 

### Return type

[**PlanAddon**](PlanAddon.md)

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

# **list_addons**
> AddonPaginatedResponse list_addons(include_deleted=include_deleted, id=id, key=key, key_version=key_version, status=status, currency=currency, page=page, page_size=page_size, order=order, order_by=order_by)

List add-ons

List all add-ons.

### Example


```python
import moolabs
from moolabs.models.addon_order_by import AddonOrderBy
from moolabs.models.addon_paginated_response import AddonPaginatedResponse
from moolabs.models.addon_status import AddonStatus
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    include_deleted = False # bool | Include deleted add-ons in response.  Usage: `?includeDeleted=true` (optional) (default to False)
    id = ['id_example'] # List[str] | Filter by addon.id attribute (optional)
    key = ['key_example'] # List[str] | Filter by addon.key attribute (optional)
    key_version = {'key': moolabs.List[int]()} # Dict[str, List[int]] | Filter by addon.key and addon.version attributes (optional)
    status = [moolabs.AddonStatus()] # List[AddonStatus] | Only return add-ons with the given status.  Usage: - `?status=active`: return only the currently active add-ons - `?status=draft`: return only the draft add-ons - `?status=archived`: return only the archived add-ons (optional)
    currency = ['currency_example'] # List[str] | Filter by addon.currency attribute (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.AddonOrderBy() # AddonOrderBy | The order by field. (optional)

    try:
        # List add-ons
        api_response = api_instance.list_addons(include_deleted=include_deleted, id=id, key=key, key_version=key_version, status=status, currency=currency, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of ProductCatalogApi->list_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->list_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| Include deleted add-ons in response.  Usage: &#x60;?includeDeleted&#x3D;true&#x60; | [optional] [default to False]
 **id** | [**List[str]**](str.md)| Filter by addon.id attribute | [optional] 
 **key** | [**List[str]**](str.md)| Filter by addon.key attribute | [optional] 
 **key_version** | [**Dict[str, List[int]]**](List[int].md)| Filter by addon.key and addon.version attributes | [optional] 
 **status** | [**List[AddonStatus]**](AddonStatus.md)| Only return add-ons with the given status.  Usage: - &#x60;?status&#x3D;active&#x60;: return only the currently active add-ons - &#x60;?status&#x3D;draft&#x60;: return only the draft add-ons - &#x60;?status&#x3D;archived&#x60;: return only the archived add-ons | [optional] 
 **currency** | [**List[str]**](str.md)| Filter by addon.currency attribute | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**AddonOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**AddonPaginatedResponse**](AddonPaginatedResponse.md)

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

# **list_features**
> ListFeaturesResult list_features(meter_slug=meter_slug, include_archived=include_archived, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)

List features

List features.

### Example


```python
import moolabs
from moolabs.models.feature_order_by import FeatureOrderBy
from moolabs.models.list_features_result import ListFeaturesResult
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    meter_slug = ['meter_slug_example'] # List[str] | Filter by meterSlug (optional)
    include_archived = False # bool | Include archived features in response. (optional) (default to False)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    offset = 0 # int | Number of items to skip.  Default is 0. (optional) (default to 0)
    limit = 100 # int | Number of items to return.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.FeatureOrderBy() # FeatureOrderBy | The order by field. (optional)

    try:
        # List features
        api_response = api_instance.list_features(meter_slug=meter_slug, include_archived=include_archived, page=page, page_size=page_size, offset=offset, limit=limit, order=order, order_by=order_by)
        print("The response of ProductCatalogApi->list_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->list_features: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_slug** | [**List[str]**](str.md)| Filter by meterSlug | [optional] 
 **include_archived** | **bool**| Include archived features in response. | [optional] [default to False]
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **offset** | **int**| Number of items to skip.  Default is 0. | [optional] [default to 0]
 **limit** | **int**| Number of items to return.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**FeatureOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**ListFeaturesResult**](ListFeaturesResult.md)

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

# **list_plan_addons**
> PlanAddonPaginatedResponse list_plan_addons(plan_id, include_deleted=include_deleted, id=id, key=key, key_version=key_version, page=page, page_size=page_size, order=order, order_by=order_by)

List all available add-ons for plan

List all available add-ons for plan.

### Example


```python
import moolabs
from moolabs.models.plan_addon_order_by import PlanAddonOrderBy
from moolabs.models.plan_addon_paginated_response import PlanAddonPaginatedResponse
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = 'plan_id_example' # str | 
    include_deleted = False # bool | Include deleted plan add-on assignments.  Usage: `?includeDeleted=true` (optional) (default to False)
    id = ['id_example'] # List[str] | Filter by addon.id attribute. (optional)
    key = ['key_example'] # List[str] | Filter by addon.key attribute. (optional)
    key_version = {'key': moolabs.List[int]()} # Dict[str, List[int]] | Filter by addon.key and addon.version attributes. (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.PlanAddonOrderBy() # PlanAddonOrderBy | The order by field. (optional)

    try:
        # List all available add-ons for plan
        api_response = api_instance.list_plan_addons(plan_id, include_deleted=include_deleted, id=id, key=key, key_version=key_version, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of ProductCatalogApi->list_plan_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->list_plan_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **include_deleted** | **bool**| Include deleted plan add-on assignments.  Usage: &#x60;?includeDeleted&#x3D;true&#x60; | [optional] [default to False]
 **id** | [**List[str]**](str.md)| Filter by addon.id attribute. | [optional] 
 **key** | [**List[str]**](str.md)| Filter by addon.key attribute. | [optional] 
 **key_version** | [**Dict[str, List[int]]**](List[int].md)| Filter by addon.key and addon.version attributes. | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**PlanAddonOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**PlanAddonPaginatedResponse**](PlanAddonPaginatedResponse.md)

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

# **list_plans**
> PlanPaginatedResponse list_plans(include_deleted=include_deleted, id=id, key=key, key_version=key_version, status=status, currency=currency, page=page, page_size=page_size, order=order, order_by=order_by)

List plans

List all plans.

### Example


```python
import moolabs
from moolabs.models.plan_order_by import PlanOrderBy
from moolabs.models.plan_paginated_response import PlanPaginatedResponse
from moolabs.models.plan_status import PlanStatus
from moolabs.models.sort_order import SortOrder
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    include_deleted = False # bool | Include deleted plans in response.  Usage: `?includeDeleted=true` (optional) (default to False)
    id = ['id_example'] # List[str] | Filter by plan.id attribute (optional)
    key = ['key_example'] # List[str] | Filter by plan.key attribute (optional)
    key_version = {'key': moolabs.List[int]()} # Dict[str, List[int]] | Filter by plan.key and plan.version attributes (optional)
    status = [moolabs.PlanStatus()] # List[PlanStatus] | Only return plans with the given status.  Usage: - `?status=active`: return only the currently active plan - `?status=draft`: return only the draft plan - `?status=archived`: return only the archived plans (optional)
    currency = ['currency_example'] # List[str] | Filter by plan.currency attribute (optional)
    page = 1 # int | Page index.  Default is 1. (optional) (default to 1)
    page_size = 100 # int | The maximum number of items per page.  Default is 100. (optional) (default to 100)
    order = moolabs.SortOrder() # SortOrder | The order direction. (optional)
    order_by = moolabs.PlanOrderBy() # PlanOrderBy | The order by field. (optional)

    try:
        # List plans
        api_response = api_instance.list_plans(include_deleted=include_deleted, id=id, key=key, key_version=key_version, status=status, currency=currency, page=page, page_size=page_size, order=order, order_by=order_by)
        print("The response of ProductCatalogApi->list_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->list_plans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| Include deleted plans in response.  Usage: &#x60;?includeDeleted&#x3D;true&#x60; | [optional] [default to False]
 **id** | [**List[str]**](str.md)| Filter by plan.id attribute | [optional] 
 **key** | [**List[str]**](str.md)| Filter by plan.key attribute | [optional] 
 **key_version** | [**Dict[str, List[int]]**](List[int].md)| Filter by plan.key and plan.version attributes | [optional] 
 **status** | [**List[PlanStatus]**](PlanStatus.md)| Only return plans with the given status.  Usage: - &#x60;?status&#x3D;active&#x60;: return only the currently active plan - &#x60;?status&#x3D;draft&#x60;: return only the draft plan - &#x60;?status&#x3D;archived&#x60;: return only the archived plans | [optional] 
 **currency** | [**List[str]**](str.md)| Filter by plan.currency attribute | [optional] 
 **page** | **int**| Page index.  Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page.  Default is 100. | [optional] [default to 100]
 **order** | [**SortOrder**](.md)| The order direction. | [optional] 
 **order_by** | [**PlanOrderBy**](.md)| The order by field. | [optional] 

### Return type

[**PlanPaginatedResponse**](PlanPaginatedResponse.md)

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

# **next_plan**
> Plan next_plan(plan_id_or_key)

New draft plan

Create a new draft version from plan. It returns error if there is already a plan in draft or planId does not reference the latest published version.

### Example


```python
import moolabs
from moolabs.models.plan import Plan
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id_or_key = 'plan_id_or_key_example' # str | 

    try:
        # New draft plan
        api_response = api_instance.next_plan(plan_id_or_key)
        print("The response of ProductCatalogApi->next_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->next_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id_or_key** | **str**|  | 

### Return type

[**Plan**](Plan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The request has succeeded and a new resource has been created as a result. |  -  |
**400** | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). |  -  |
**401** | The request has not been applied because it lacks valid authentication credentials for the target resource. |  -  |
**403** | The server understood the request but refuses to authorize it. |  -  |
**404** | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists. |  -  |
**412** | One or more conditions given in the request header fields evaluated to false when tested on the server. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The server is currently unable to handle the request due to a temporary overload or scheduled maintenance, which will likely be alleviated after some delay. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_addon**
> Addon publish_addon(addon_id)

Publish add-on

Publish a add-on version.

### Example


```python
import moolabs
from moolabs.models.addon import Addon
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Publish add-on
        api_response = api_instance.publish_addon(addon_id)
        print("The response of ProductCatalogApi->publish_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->publish_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  | 

### Return type

[**Addon**](Addon.md)

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

# **publish_plan**
> Plan publish_plan(plan_id)

Publish plan

Publish a plan version.

### Example


```python
import moolabs
from moolabs.models.plan import Plan
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 

    try:
        # Publish plan
        api_response = api_instance.publish_plan(plan_id)
        print("The response of ProductCatalogApi->publish_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->publish_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 

### Return type

[**Plan**](Plan.md)

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

# **update_addon**
> Addon update_addon(addon_id, addon_replace_update)

Update add-on

Update add-on by id.

### Example


```python
import moolabs
from moolabs.models.addon import Addon
from moolabs.models.addon_replace_update import AddonReplaceUpdate
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    addon_replace_update = moolabs.AddonReplaceUpdate() # AddonReplaceUpdate | 

    try:
        # Update add-on
        api_response = api_instance.update_addon(addon_id, addon_replace_update)
        print("The response of ProductCatalogApi->update_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->update_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_id** | **str**|  | 
 **addon_replace_update** | [**AddonReplaceUpdate**](AddonReplaceUpdate.md)|  | 

### Return type

[**Addon**](Addon.md)

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

# **update_plan**
> Plan update_plan(plan_id, plan_replace_update)

Update a plan

Update plan by id.

### Example


```python
import moolabs
from moolabs.models.plan import Plan
from moolabs.models.plan_replace_update import PlanReplaceUpdate
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    plan_replace_update = moolabs.PlanReplaceUpdate() # PlanReplaceUpdate | 

    try:
        # Update a plan
        api_response = api_instance.update_plan(plan_id, plan_replace_update)
        print("The response of ProductCatalogApi->update_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->update_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **plan_replace_update** | [**PlanReplaceUpdate**](PlanReplaceUpdate.md)|  | 

### Return type

[**Plan**](Plan.md)

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

# **update_plan_addon**
> PlanAddon update_plan_addon(plan_id, plan_addon_id, plan_addon_replace_update)

Update add-on assignment for plan

Update add-on assignment for plan.

### Example


```python
import moolabs
from moolabs.models.plan_addon import PlanAddon
from moolabs.models.plan_addon_replace_update import PlanAddonReplaceUpdate
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
    api_instance = moolabs.ProductCatalogApi(api_client)
    plan_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    plan_addon_id = '01G65Z755AFWAKHE12NY0CQ9FH' # str | 
    plan_addon_replace_update = moolabs.PlanAddonReplaceUpdate() # PlanAddonReplaceUpdate | 

    try:
        # Update add-on assignment for plan
        api_response = api_instance.update_plan_addon(plan_id, plan_addon_id, plan_addon_replace_update)
        print("The response of ProductCatalogApi->update_plan_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductCatalogApi->update_plan_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **str**|  | 
 **plan_addon_id** | **str**|  | 
 **plan_addon_replace_update** | [**PlanAddonReplaceUpdate**](PlanAddonReplaceUpdate.md)|  | 

### Return type

[**PlanAddon**](PlanAddon.md)

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

