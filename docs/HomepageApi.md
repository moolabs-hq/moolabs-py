# moolabs.HomepageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_homepage_insights**](HomepageApi.md#get_homepage_insights) | **GET** /v1/homepage/insights | Get Homepage Insights


# **get_homepage_insights**
> HomepageResponse get_homepage_insights(persona=persona)

Get Homepage Insights

Get personalized homepage insights and quick actions.

### Example


```python
import moolabs
from moolabs.models.homepage_response import HomepageResponse
from moolabs.models.persona import Persona
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
    api_instance = moolabs.HomepageApi(api_client)
    persona = moolabs.Persona() # Persona | User persona/role (optional)

    try:
        # Get Homepage Insights
        api_response = api_instance.get_homepage_insights(persona=persona)
        print("The response of HomepageApi->get_homepage_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HomepageApi->get_homepage_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **persona** | [**Persona**](.md)| User persona/role | [optional] 

### Return type

[**HomepageResponse**](HomepageResponse.md)

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

