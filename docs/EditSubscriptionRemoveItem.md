# EditSubscriptionRemoveItem

Remove an item from a phase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**phase_key** | **str** |  | 
**item_key** | **str** |  | 

## Example

```python
from moolabs.models.edit_subscription_remove_item import EditSubscriptionRemoveItem

# TODO update the JSON string below
json = "{}"
# create an instance of EditSubscriptionRemoveItem from a JSON string
edit_subscription_remove_item_instance = EditSubscriptionRemoveItem.from_json(json)
# print the JSON string representation of the object
print(EditSubscriptionRemoveItem.to_json())

# convert the object into a dict
edit_subscription_remove_item_dict = edit_subscription_remove_item_instance.to_dict()
# create an instance of EditSubscriptionRemoveItem from a dict
edit_subscription_remove_item_from_dict = EditSubscriptionRemoveItem.from_dict(edit_subscription_remove_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


