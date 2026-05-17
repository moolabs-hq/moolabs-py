# QuickAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | 
**icon** | **str** |  | 
**icon_color** | **str** |  | 
**icon_bg** | **str** |  | 
**route** | **str** |  | 

## Example

```python
from moolabs.models.quick_action import QuickAction

# TODO update the JSON string below
json = "{}"
# create an instance of QuickAction from a JSON string
quick_action_instance = QuickAction.from_json(json)
# print the JSON string representation of the object
print(QuickAction.to_json())

# convert the object into a dict
quick_action_dict = quick_action_instance.to_dict()
# create an instance of QuickAction from a dict
quick_action_from_dict = QuickAction.from_dict(quick_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


