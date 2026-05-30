# PriceSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 
**pricing_snapshot_id** | **str** |  | 
**normalized_input** | **Dict[str, object]** |  | 
**priced_output** | **Dict[str, object]** |  | 
**pricing_trace** | **Dict[str, object]** |  | 
**pricing_trace_digest** | **str** |  | 
**source_versions** | **Dict[str, object]** |  | 
**currency** | **str** |  | [optional] [default to 'USD']
**subtotal_micros** | **int** |  | 
**discount_micros** | **int** |  | 
**total_micros** | **int** |  | 

## Example

```python
from moolabs.models.price_session_response import PriceSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceSessionResponse from a JSON string
price_session_response_instance = PriceSessionResponse.from_json(json)
# print the JSON string representation of the object
print(PriceSessionResponse.to_json())

# convert the object into a dict
price_session_response_dict = price_session_response_instance.to_dict()
# create an instance of PriceSessionResponse from a dict
price_session_response_from_dict = PriceSessionResponse.from_dict(price_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


