# BomComponentIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_type** | **str** | &#39;llm_call&#39;, &#39;embedding&#39;, etc. | [optional] [default to 'llm_call']
**provider** | **str** |  | 
**model** | **str** |  | 
**metric_type** | **str** |  | 
**expected_quantity** | **float** | Expected units per billing event | 
**expected_span_count** | **int** | Expected cost_event spans per billing event | [optional] [default to 1]
**unit_cost** | **float** | Override from rate_catalog if provided | [optional] 
**currency** | **str** |  | [optional] [default to 'USD']
**sort_order** | **int** |  | [optional] [default to 0]
**notes** | **str** |  | [optional] 

## Example

```python
from moolabs.models.bom_component_in import BomComponentIn

# TODO update the JSON string below
json = "{}"
# create an instance of BomComponentIn from a JSON string
bom_component_in_instance = BomComponentIn.from_json(json)
# print the JSON string representation of the object
print(BomComponentIn.to_json())

# convert the object into a dict
bom_component_in_dict = bom_component_in_instance.to_dict()
# create an instance of BomComponentIn from a dict
bom_component_in_from_dict = BomComponentIn.from_dict(bom_component_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


