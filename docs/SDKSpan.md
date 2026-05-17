# SDKSpan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**span_id** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | 
**operation_type** | **str** |  | 
**input_tokens** | **int** |  | [optional] 
**output_tokens** | **int** |  | [optional] 
**tool_calls** | **int** |  | [optional] 
**latency_ms** | **int** |  | [optional] 
**cache_hit** | **bool** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.sdk_span import SDKSpan

# TODO update the JSON string below
json = "{}"
# create an instance of SDKSpan from a JSON string
sdk_span_instance = SDKSpan.from_json(json)
# print the JSON string representation of the object
print(SDKSpan.to_json())

# convert the object into a dict
sdk_span_dict = sdk_span_instance.to_dict()
# create an instance of SDKSpan from a dict
sdk_span_from_dict = SDKSpan.from_dict(sdk_span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


