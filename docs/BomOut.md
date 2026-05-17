# BomOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**feature_key** | **str** |  | 
**version** | **int** |  | 
**status** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**workflow_type** | **str** |  | 
**derived_from** | **str** |  | 
**approved_by** | **str** |  | 
**approved_at** | **str** |  | 
**superseded_by_id** | **str** |  | 
**superseded_at** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**components** | [**List[BomComponentOut]**](BomComponentOut.md) |  | [optional] 

## Example

```python
from moolabs.models.bom_out import BomOut

# TODO update the JSON string below
json = "{}"
# create an instance of BomOut from a JSON string
bom_out_instance = BomOut.from_json(json)
# print the JSON string representation of the object
print(BomOut.to_json())

# convert the object into a dict
bom_out_dict = bom_out_instance.to_dict()
# create an instance of BomOut from a dict
bom_out_from_dict = BomOut.from_dict(bom_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


