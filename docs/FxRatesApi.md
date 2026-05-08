# moolabs.FxRatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fx_rate_endpoint_v1**](FxRatesApi.md#create_fx_rate_endpoint_v1) | **POST** /v1/fx-rates/rates | Create Fx Rate Endpoint
[**create_value_recognition_entry_endpoint_v1_fx**](FxRatesApi.md#create_value_recognition_entry_endpoint_v1_fx) | **POST** /v1/fx-rates/value-recognition/entry | Create Value Recognition Entry Endpoint
[**get_fx_rate_at_endpoint_v1**](FxRatesApi.md#get_fx_rate_at_endpoint_v1) | **POST** /v1/fx-rates/rates/at | Get Fx Rate At Endpoint
[**process_value_recognition_v1_fx**](FxRatesApi.md#process_value_recognition_v1_fx) | **POST** /v1/fx-rates/value-recognition/process | Process Value Recognition


# **create_fx_rate_endpoint_v1**
> FxRateResponse create_fx_rate_endpoint_v1(create_fx_rate_request)

Create Fx Rate Endpoint

Create a new FX rate version.  This endpoint creates a versioned FX rate for converting credits to USD. FX rates are effective at a specific timestamp and can be locked to grants.

### Example


```python
import moolabs
from moolabs.models.create_fx_rate_request import CreateFxRateRequest
from moolabs.models.fx_rate_response import FxRateResponse
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
    api_instance = moolabs.FxRatesApi(api_client)
    create_fx_rate_request = moolabs.CreateFxRateRequest() # CreateFxRateRequest | 

    try:
        # Create Fx Rate Endpoint
        api_response = api_instance.create_fx_rate_endpoint_v1(create_fx_rate_request)
        print("The response of FxRatesApi->create_fx_rate_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FxRatesApi->create_fx_rate_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_fx_rate_request** | [**CreateFxRateRequest**](CreateFxRateRequest.md)|  | 

### Return type

[**FxRateResponse**](FxRateResponse.md)

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

# **create_value_recognition_entry_endpoint_v1_fx**
> object create_value_recognition_entry_endpoint_v1_fx(create_value_recognition_request)

Create Value Recognition Entry Endpoint

Create a VALUE_RECOGNITION journal entry.  This endpoint creates a journal entry for revenue recognition in USD.

### Example


```python
import moolabs
from moolabs.models.create_value_recognition_request import CreateValueRecognitionRequest
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
    api_instance = moolabs.FxRatesApi(api_client)
    create_value_recognition_request = moolabs.CreateValueRecognitionRequest() # CreateValueRecognitionRequest | 

    try:
        # Create Value Recognition Entry Endpoint
        api_response = api_instance.create_value_recognition_entry_endpoint_v1_fx(create_value_recognition_request)
        print("The response of FxRatesApi->create_value_recognition_entry_endpoint_v1_fx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FxRatesApi->create_value_recognition_entry_endpoint_v1_fx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_value_recognition_request** | [**CreateValueRecognitionRequest**](CreateValueRecognitionRequest.md)|  | 

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

# **get_fx_rate_at_endpoint_v1**
> object get_fx_rate_at_endpoint_v1(get_fx_rate_request)

Get Fx Rate At Endpoint

Get FX rate effective at a specific timestamp.  Returns the FX rate that was effective at the given timestamp.

### Example


```python
import moolabs
from moolabs.models.get_fx_rate_request import GetFxRateRequest
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
    api_instance = moolabs.FxRatesApi(api_client)
    get_fx_rate_request = moolabs.GetFxRateRequest() # GetFxRateRequest | 

    try:
        # Get Fx Rate At Endpoint
        api_response = api_instance.get_fx_rate_at_endpoint_v1(get_fx_rate_request)
        print("The response of FxRatesApi->get_fx_rate_at_endpoint_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FxRatesApi->get_fx_rate_at_endpoint_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_fx_rate_request** | [**GetFxRateRequest**](GetFxRateRequest.md)|  | 

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

# **process_value_recognition_v1_fx**
> ValueRecognitionResponse process_value_recognition_v1_fx(process_value_recognition_request)

Process Value Recognition

Process burn allocations for a journal entry and create VALUE_RECOGNITION postings.  This endpoint: - Gets all burn allocations for a journal entry - Computes USD value for each allocation (using locked FX rates or effective_at rate) - Creates VALUE_RECOGNITION postings in USD

### Example


```python
import moolabs
from moolabs.models.process_value_recognition_request import ProcessValueRecognitionRequest
from moolabs.models.value_recognition_response import ValueRecognitionResponse
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
    api_instance = moolabs.FxRatesApi(api_client)
    process_value_recognition_request = moolabs.ProcessValueRecognitionRequest() # ProcessValueRecognitionRequest | 

    try:
        # Process Value Recognition
        api_response = api_instance.process_value_recognition_v1_fx(process_value_recognition_request)
        print("The response of FxRatesApi->process_value_recognition_v1_fx:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FxRatesApi->process_value_recognition_v1_fx: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_value_recognition_request** | [**ProcessValueRecognitionRequest**](ProcessValueRecognitionRequest.md)|  | 

### Return type

[**ValueRecognitionResponse**](ValueRecognitionResponse.md)

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

