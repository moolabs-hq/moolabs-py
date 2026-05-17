# ReallocateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** |  | 
**tenant_id** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**allocations_created** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from moolabs.models.reallocate_response import ReallocateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReallocateResponse from a JSON string
reallocate_response_instance = ReallocateResponse.from_json(json)
# print the JSON string representation of the object
print(ReallocateResponse.to_json())

# convert the object into a dict
reallocate_response_dict = reallocate_response_instance.to_dict()
# create an instance of ReallocateResponse from a dict
reallocate_response_from_dict = ReallocateResponse.from_dict(reallocate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


