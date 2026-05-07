# SubscriptionPhaseCreate

Subscription phase create input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_after** | **str** | Interval after the subscription starts to transition to the phase. When null, the phase starts immediately after the subscription starts. | 
**duration** | **str** | The intended duration of the new phase. Duration is required when the phase will not be the last phase. | [optional] 
**discounts** | [**Discounts**](Discounts.md) | The discounts on the plan. | [optional] 
**key** | **str** | A locally unique identifier for the phase. | 
**name** | **str** | The name of the phase. | 
**description** | **str** | The description of the phase. | [optional] 

## Example

```python
from moolabs.models.subscription_phase_create import SubscriptionPhaseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPhaseCreate from a JSON string
subscription_phase_create_instance = SubscriptionPhaseCreate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPhaseCreate.to_json())

# convert the object into a dict
subscription_phase_create_dict = subscription_phase_create_instance.to_dict()
# create an instance of SubscriptionPhaseCreate from a dict
subscription_phase_create_from_dict = SubscriptionPhaseCreate.from_dict(subscription_phase_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


