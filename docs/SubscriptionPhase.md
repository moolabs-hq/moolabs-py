# SubscriptionPhase

Subscription phase, analogous to plan phases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**key** | **str** | A locally unique identifier for the resource. | 
**discounts** | [**Discounts**](Discounts.md) | The discounts on the plan. | [optional] 
**active_from** | **datetime** | The time from which the phase is active. | 
**active_to** | **datetime** | The until which the Phase is active. | [optional] 

## Example

```python
from moolabs.models.subscription_phase import SubscriptionPhase

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPhase from a JSON string
subscription_phase_instance = SubscriptionPhase.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPhase.to_json())

# convert the object into a dict
subscription_phase_dict = subscription_phase_instance.to_dict()
# create an instance of SubscriptionPhase from a dict
subscription_phase_from_dict = SubscriptionPhase.from_dict(subscription_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


