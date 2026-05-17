# FeatureMarginItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** |  | 
**total_valued_burn** | **str** |  | 
**total_cost** | **str** |  | 
**margin** | **str** |  | 
**margin_pct** | **str** |  | 
**margin_reason** | **str** |  | 
**billing_event_count** | **int** |  | 

## Example

```python
from moolabs.models.feature_margin_item import FeatureMarginItem

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMarginItem from a JSON string
feature_margin_item_instance = FeatureMarginItem.from_json(json)
# print the JSON string representation of the object
print(FeatureMarginItem.to_json())

# convert the object into a dict
feature_margin_item_dict = feature_margin_item_instance.to_dict()
# create an instance of FeatureMarginItem from a dict
feature_margin_item_from_dict = FeatureMarginItem.from_dict(feature_margin_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


