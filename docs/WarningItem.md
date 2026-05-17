# WarningItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**message** | **str** |  | 
**timestamp** | **str** |  | 
**severity** | **str** |  | 

## Example

```python
from moolabs.models.warning_item import WarningItem

# TODO update the JSON string below
json = "{}"
# create an instance of WarningItem from a JSON string
warning_item_instance = WarningItem.from_json(json)
# print the JSON string representation of the object
print(WarningItem.to_json())

# convert the object into a dict
warning_item_dict = warning_item_instance.to_dict()
# create an instance of WarningItem from a dict
warning_item_from_dict = WarningItem.from_dict(warning_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


