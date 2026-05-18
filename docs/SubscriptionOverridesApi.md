# moolabs.SubscriptionOverridesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_commercial_overrides_v1**](SubscriptionOverridesApi.md#create_commercial_overrides_v1) | **POST** /v1/subscription-overrides | Create Commercial Overrides
[**get_commercial_overrides_v1**](SubscriptionOverridesApi.md#get_commercial_overrides_v1) | **GET** /v1/subscription-overrides/{subscription_id} | Get Commercial Overrides


# **create_commercial_overrides_v1**
> object create_commercial_overrides_v1(commercial_overrides_input)

Create Commercial Overrides

Create commercial overrides for a subscription.  Each call creates a new override_set_id and override_revision. Prior active rows for the same override_type(s) are superseded atomically. This makes writes retry-safe and reads deterministic.

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.commercial_overrides_input import CommercialOverridesInput
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
    api_instance = moolabs.SubscriptionOverridesApi(api_client)
    commercial_overrides_input = moolabs.CommercialOverridesInput() # CommercialOverridesInput | 

    try:
        # Create Commercial Overrides
        api_response = api_instance.create_commercial_overrides_v1(commercial_overrides_input)
        print("The response of SubscriptionOverridesApi->create_commercial_overrides_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionOverridesApi->create_commercial_overrides_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commercial_overrides_input** | [**CommercialOverridesInput**](CommercialOverridesInput.md)|  | 

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

# **get_commercial_overrides_v1**
> object get_commercial_overrides_v1(subscription_id)

Get Commercial Overrides

Get active commercial overrides for a subscription.  Only returns rows with status='active' (i.e. the latest revision). Superseded rows are excluded automatically.

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
    api_instance = moolabs.SubscriptionOverridesApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get Commercial Overrides
        api_response = api_instance.get_commercial_overrides_v1(subscription_id)
        print("The response of SubscriptionOverridesApi->get_commercial_overrides_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionOverridesApi->get_commercial_overrides_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

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

