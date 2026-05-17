# BomComponentOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**component_type** | **str** |  | 
**provider** | **str** |  | 
**model** | **str** |  | 
**metric_type** | **str** |  | 
**expected_quantity** | **float** |  | 
**expected_span_count** | **int** |  | 
**unit_cost** | **float** |  | 
**standard_cost** | **float** |  | 
**currency** | **str** |  | 
**sort_order** | **int** |  | 
**notes** | **str** |  | 

## Example

```python
from moolabs.models.bom_component_out import BomComponentOut

# TODO update the JSON string below
json = "{}"
# create an instance of BomComponentOut from a JSON string
bom_component_out_instance = BomComponentOut.from_json(json)
# print the JSON string representation of the object
print(BomComponentOut.to_json())

# convert the object into a dict
bom_component_out_dict = bom_component_out_instance.to_dict()
# create an instance of BomComponentOut from a dict
bom_component_out_from_dict = BomComponentOut.from_dict(bom_component_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


