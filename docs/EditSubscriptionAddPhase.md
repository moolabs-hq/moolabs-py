# EditSubscriptionAddPhase

Add a new phase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**phase** | [**SubscriptionPhaseCreate**](SubscriptionPhaseCreate.md) |  | 

## Example

```python
from moolabs.models.edit_subscription_add_phase import EditSubscriptionAddPhase

# TODO update the JSON string below
json = "{}"
# create an instance of EditSubscriptionAddPhase from a JSON string
edit_subscription_add_phase_instance = EditSubscriptionAddPhase.from_json(json)
# print the JSON string representation of the object
print(EditSubscriptionAddPhase.to_json())

# convert the object into a dict
edit_subscription_add_phase_dict = edit_subscription_add_phase_instance.to_dict()
# create an instance of EditSubscriptionAddPhase from a dict
edit_subscription_add_phase_from_dict = EditSubscriptionAddPhase.from_dict(edit_subscription_add_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


