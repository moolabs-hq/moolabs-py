# SubscriptionEditOperation

The operation to be performed on the subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**phase_key** | **str** |  | 
**rate_card** | [**RateCard**](RateCard.md) |  | 
**item_key** | **str** |  | 
**phase** | [**SubscriptionPhaseCreate**](SubscriptionPhaseCreate.md) |  | 
**shift** | [**RemovePhaseShifting**](RemovePhaseShifting.md) |  | 
**extend_by** | **str** |  | 

## Example

```python
from moolabs.models.subscription_edit_operation import SubscriptionEditOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionEditOperation from a JSON string
subscription_edit_operation_instance = SubscriptionEditOperation.from_json(json)
# print the JSON string representation of the object
print(SubscriptionEditOperation.to_json())

# convert the object into a dict
subscription_edit_operation_dict = subscription_edit_operation_instance.to_dict()
# create an instance of SubscriptionEditOperation from a dict
subscription_edit_operation_from_dict = SubscriptionEditOperation.from_dict(subscription_edit_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


