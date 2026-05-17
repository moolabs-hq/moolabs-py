# FeatureFlagItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**tenant_override** | **bool** |  | 
**default_value** | **bool** |  | 
**enabled** | **bool** |  | 
**last_changed** | **str** |  | 

## Example

```python
from moolabs.models.feature_flag_item import FeatureFlagItem

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagItem from a JSON string
feature_flag_item_instance = FeatureFlagItem.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagItem.to_json())

# convert the object into a dict
feature_flag_item_dict = feature_flag_item_instance.to_dict()
# create an instance of FeatureFlagItem from a dict
feature_flag_item_from_dict = FeatureFlagItem.from_dict(feature_flag_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


