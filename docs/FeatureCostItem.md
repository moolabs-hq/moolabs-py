# FeatureCostItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**total_cost** | **float** |  | 
**total_quantity** | **float** |  | 
**event_count** | **int** |  | 
**avg_cost** | **float** |  | 

## Example

```python
from moolabs.models.feature_cost_item import FeatureCostItem

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureCostItem from a JSON string
feature_cost_item_instance = FeatureCostItem.from_json(json)
# print the JSON string representation of the object
print(FeatureCostItem.to_json())

# convert the object into a dict
feature_cost_item_dict = feature_cost_item_instance.to_dict()
# create an instance of FeatureCostItem from a dict
feature_cost_item_from_dict = FeatureCostItem.from_dict(feature_cost_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


