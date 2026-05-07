# SubscriptionEdit

Subscription edit input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customizations** | [**List[SubscriptionEditOperation]**](SubscriptionEditOperation.md) | Batch processing commands for manipulating running subscriptions. The key format is &#x60;/phases/{phaseKey}&#x60; or &#x60;/phases/{phaseKey}/items/{itemKey}&#x60;. | 
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | Whether the billing period should be restarted.Timing configuration to allow for the changes to take effect at different times. | [optional] 

## Example

```python
from moolabs.models.subscription_edit import SubscriptionEdit

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEdit from a JSON string
subscription_edit_instance = SubscriptionEdit.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEdit.to_json())

# convert the object into a dict
subscription_edit_dict = subscription_edit_instance.to_dict()
# create an instance of SubscriptionEdit from a dict
subscription_edit_from_dict = SubscriptionEdit.from_dict(subscription_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


