# ContractSegmentResponse

A single parsed document segment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**page** | **int** |  | 
**ordinal** | **int** |  | 
**char_start** | **int** |  | 
**char_end** | **int** |  | 

## Example

```python
from moolabs.models.contract_segment_response import ContractSegmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractSegmentResponse from a JSON string
contract_segment_response_instance = ContractSegmentResponse.from_json(json)
# print the JSON string representation of the object
print(ContractSegmentResponse.to_json())

# convert the object into a dict
contract_segment_response_dict = contract_segment_response_instance.to_dict()
# create an instance of ContractSegmentResponse from a dict
contract_segment_response_from_dict = ContractSegmentResponse.from_dict(contract_segment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


