# EditSubscriptionRemovePhase

Remove a phase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**phase_key** | **str** |  | 
**shift** | [**RemovePhaseShifting**](RemovePhaseShifting.md) |  | 

## Example

```python
from moolabs.models.edit_subscription_remove_phase import EditSubscriptionRemovePhase

# TODO update the JSON string below
json = "{}"
# create an instance of EditSubscriptionRemovePhase from a JSON string
edit_subscription_remove_phase_instance = EditSubscriptionRemovePhase.from_json(json)
# print the JSON string representation of the object
print(EditSubscriptionRemovePhase.to_json())

# convert the object into a dict
edit_subscription_remove_phase_dict = edit_subscription_remove_phase_instance.to_dict()
# create an instance of EditSubscriptionRemovePhase from a dict
edit_subscription_remove_phase_from_dict = EditSubscriptionRemovePhase.from_dict(edit_subscription_remove_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


