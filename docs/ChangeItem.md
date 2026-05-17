# ChangeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**what_changed** | **str** |  | 
**section** | **str** |  | 
**actor** | **str** |  | 
**when** | **str** |  | 
**before** | **str** |  | 
**after** | **str** |  | 

## Example

```python
from moolabs.models.change_item import ChangeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeItem from a JSON string
change_item_instance = ChangeItem.from_json(json)
# print the JSON string representation of the object
print(ChangeItem.to_json())

# convert the object into a dict
change_item_dict = change_item_instance.to_dict()
# create an instance of ChangeItem from a dict
change_item_from_dict = ChangeItem.from_dict(change_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


