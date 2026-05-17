# BomUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**workflow_type** | **str** |  | [optional] 
**components** | [**List[BomComponentIn]**](BomComponentIn.md) |  | [optional] 
**created_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.bom_update_request import BomUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BomUpdateRequest from a JSON string
bom_update_request_instance = BomUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BomUpdateRequest.to_json())

# convert the object into a dict
bom_update_request_dict = bom_update_request_instance.to_dict()
# create an instance of BomUpdateRequest from a dict
bom_update_request_from_dict = BomUpdateRequest.from_dict(bom_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


