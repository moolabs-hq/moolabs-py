# moolabs.QuoteAgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_agent_evaluations_v1**](QuoteAgentsApi.md#list_agent_evaluations_v1) | **GET** /v1/quote-agents/evaluations | List Agent Evaluations
[**list_agent_runs_v1**](QuoteAgentsApi.md#list_agent_runs_v1) | **GET** /v1/quote-agents/runs | List Agent Runs
[**list_policies_v1**](QuoteAgentsApi.md#list_policies_v1) | **GET** /v1/quote-agents/policies | List Policies
[**patch_policy_v1**](QuoteAgentsApi.md#patch_policy_v1) | **PATCH** /v1/quote-agents/policies/{agent_name} | Patch Policy


# **list_agent_evaluations_v1**
> List[QuoteAgentEvaluationResponse] list_agent_evaluations_v1(limit=limit, offset=offset)

List Agent Evaluations

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_agent_evaluation_response import QuoteAgentEvaluationResponse
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
    api_instance = moolabs.QuoteAgentsApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Agent Evaluations
        api_response = api_instance.list_agent_evaluations_v1(limit=limit, offset=offset)
        print("The response of QuoteAgentsApi->list_agent_evaluations_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteAgentsApi->list_agent_evaluations_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[QuoteAgentEvaluationResponse]**](QuoteAgentEvaluationResponse.md)

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

# **list_agent_runs_v1**
> List[QuoteAgentRunResponse] list_agent_runs_v1(limit=limit, offset=offset)

List Agent Runs

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_agent_run_response import QuoteAgentRunResponse
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
    api_instance = moolabs.QuoteAgentsApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Agent Runs
        api_response = api_instance.list_agent_runs_v1(limit=limit, offset=offset)
        print("The response of QuoteAgentsApi->list_agent_runs_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteAgentsApi->list_agent_runs_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[QuoteAgentRunResponse]**](QuoteAgentRunResponse.md)

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

# **list_policies_v1**
> List[QuoteAgentPolicyResponse] list_policies_v1()

List Policies

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.quote_agent_policy_response import QuoteAgentPolicyResponse
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
    api_instance = moolabs.QuoteAgentsApi(api_client)

    try:
        # List Policies
        api_response = api_instance.list_policies_v1()
        print("The response of QuoteAgentsApi->list_policies_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteAgentsApi->list_policies_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[QuoteAgentPolicyResponse]**](QuoteAgentPolicyResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_policy_v1**
> QuoteAgentPolicyResponse patch_policy_v1(agent_name, patch_quote_agent_policy_request)

Patch Policy

### Example

* Bearer (opaque) Authentication (HTTPBearer):

```python
import moolabs
from moolabs.models.patch_quote_agent_policy_request import PatchQuoteAgentPolicyRequest
from moolabs.models.quote_agent_policy_response import QuoteAgentPolicyResponse
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
    api_instance = moolabs.QuoteAgentsApi(api_client)
    agent_name = 'agent_name_example' # str | 
    patch_quote_agent_policy_request = moolabs.PatchQuoteAgentPolicyRequest() # PatchQuoteAgentPolicyRequest | 

    try:
        # Patch Policy
        api_response = api_instance.patch_policy_v1(agent_name, patch_quote_agent_policy_request)
        print("The response of QuoteAgentsApi->patch_policy_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteAgentsApi->patch_policy_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_name** | **str**|  | 
 **patch_quote_agent_policy_request** | [**PatchQuoteAgentPolicyRequest**](PatchQuoteAgentPolicyRequest.md)|  | 

### Return type

[**QuoteAgentPolicyResponse**](QuoteAgentPolicyResponse.md)

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

