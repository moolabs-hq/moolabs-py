# ModelCostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**provider** | **str** |  | 
**total_cost** | **float** |  | 
**request_count** | **int** |  | 
**pct_of_total** | **float** |  | 

## Example

```python
from moolabs.models.model_cost_item import ModelCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of ModelCostItem from a JSON string
model_cost_item_instance = ModelCostItem.from_json(json)
# print the JSON string representation of the object
print(ModelCostItem.to_json())

# convert the object into a dict
model_cost_item_dict = model_cost_item_instance.to_dict()
# create an instance of ModelCostItem from a dict
model_cost_item_from_dict = ModelCostItem.from_dict(model_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


