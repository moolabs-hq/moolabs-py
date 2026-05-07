# EditSubscriptionAddItem

Add a new item to a phase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**phase_key** | **str** |  | 
**rate_card** | [**RateCard**](RateCard.md) |  | 

## Example

```python
from moolabs.models.edit_subscription_add_item import EditSubscriptionAddItem

# TODO update the JSON string below
json = "{}"
# create an instance of EditSubscriptionAddItem from a JSON string
edit_subscription_add_item_instance = EditSubscriptionAddItem.from_json(json)
# print the JSON string representation of the object
print(EditSubscriptionAddItem.to_json())

# convert the object into a dict
edit_subscription_add_item_dict = edit_subscription_add_item_instance.to_dict()
# create an instance of EditSubscriptionAddItem from a dict
edit_subscription_add_item_from_dict = EditSubscriptionAddItem.from_dict(edit_subscription_add_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


