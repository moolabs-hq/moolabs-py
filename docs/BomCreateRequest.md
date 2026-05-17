# BomCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant UUID | 
**feature_key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**workflow_type** | **str** |  | [optional] 
**components** | [**List[BomComponentIn]**](BomComponentIn.md) |  | 
**created_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.bom_create_request import BomCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BomCreateRequest from a JSON string
bom_create_request_instance = BomCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BomCreateRequest.to_json())

# convert the object into a dict
bom_create_request_dict = bom_create_request_instance.to_dict()
# create an instance of BomCreateRequest from a dict
bom_create_request_from_dict = BomCreateRequest.from_dict(bom_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


