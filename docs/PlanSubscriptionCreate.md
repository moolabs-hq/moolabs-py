# PlanSubscriptionCreate

Create subscription based on plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | [**Alignment**](Alignment.md) | What alignment settings the subscription should have. | [optional] 
**metadata** | **Dict[str, str]** | Arbitrary metadata associated with the subscription. | [optional] 
**commercial_overrides** | [**CommercialOverrides**](CommercialOverrides.md) | Commercial terms for this subscription (replaces prior overrides when set on change). | [optional] 
**plan** | [**PlanReferenceInput**](PlanReferenceInput.md) | The plan reference to change to. | 
**starting_phase** | **str** | The key of the phase to start the subscription in. If not provided, the subscription will start in the first phase of the plan. | [optional] 
**name** | **str** | The name of the Subscription. If not provided the plan name is used. | [optional] 
**description** | **str** | Description for the Subscription. | [optional] 
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | Timing configuration for the change, when the change should take effect. The default is immediate. | [optional] 
**customer_id** | **str** | The ID of the customer. Provide either the key or ID. Has presedence over the key. | [optional] 
**customer_key** | **str** | The key of the customer. Provide either the key or ID. | [optional] 
**billing_anchor** | **datetime** | The billing anchor of the subscription. The provided date will be normalized according to the billing cadence to the nearest recurrence before start time. If not provided, the subscription start time will be used. | [optional] 

## Example

```python
from moolabs.models.plan_subscription_create import PlanSubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlanSubscriptionCreate from a JSON string
plan_subscription_create_instance = PlanSubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print(PlanSubscriptionCreate.to_json())

# convert the object into a dict
plan_subscription_create_dict = plan_subscription_create_instance.to_dict()
# create an instance of PlanSubscriptionCreate from a dict
plan_subscription_create_from_dict = PlanSubscriptionCreate.from_dict(plan_subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


