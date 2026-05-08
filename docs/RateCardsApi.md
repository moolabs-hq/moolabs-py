# moolabs.RateCardsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate_card**](RateCardsApi.md#create_rate_card) | **POST** /v1/rate_cards | Create Rate Card
[**get_rate_card**](RateCardsApi.md#get_rate_card) | **GET** /v1/rate_cards/{rate_card_id} | Get Rate Card


# **create_rate_card**
> RateCardResponse create_rate_card(create_rate_card_request)

Create Rate Card

Create a new rate card.  Features: - Non-overlap constraint enforcement (no overlapping time ranges) - Rate card versioning - Pricing model fingerprinting  Returns:     Created rate card

### Example


```python
import moolabs
from moolabs.models.create_rate_card_request import CreateRateCardRequest
from moolabs.models.rate_card_response import RateCardResponse
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
    api_instance = moolabs.RateCardsApi(api_client)
    create_rate_card_request = moolabs.CreateRateCardRequest() # CreateRateCardRequest | 

    try:
        # Create Rate Card
        api_response = api_instance.create_rate_card(create_rate_card_request)
        print("The response of RateCardsApi->create_rate_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCardsApi->create_rate_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_rate_card_request** | [**CreateRateCardRequest**](CreateRateCardRequest.md)|  | 

### Return type

[**RateCardResponse**](RateCardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_card**
> RateCardResponse get_rate_card(rate_card_id)

Get Rate Card

Get rate card details by ID.

### Example


```python
import moolabs
from moolabs.models.rate_card_response import RateCardResponse
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
    api_instance = moolabs.RateCardsApi(api_client)
    rate_card_id = 'rate_card_id_example' # str | 

    try:
        # Get Rate Card
        api_response = api_instance.get_rate_card(rate_card_id)
        print("The response of RateCardsApi->get_rate_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateCardsApi->get_rate_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_card_id** | **str**|  | 

### Return type

[**RateCardResponse**](RateCardResponse.md)

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

