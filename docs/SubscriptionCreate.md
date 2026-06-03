# SubscriptionCreate

Create a subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | [**Alignment**](Alignment.md) | What alignment settings the subscription should have. | [optional] 
**metadata** | **Dict[str, str]** | Arbitrary metadata associated with the subscription. | [optional] 
**commercial_overrides** | [**CommercialOverrides**](CommercialOverrides.md) | Commercial terms for this subscription change. | [optional] 
**plan** | [**PlanReferenceInput**](PlanReferenceInput.md) | The plan reference to change to. | 
**quote_origin_key** | **str** | Idempotency key supplied by accepted quote activation for subscription create or change requests. | [optional] 
**starting_phase** | **str** | The key of the phase to start the subscription in. If not provided, the subscription will start in the first phase of the plan. | [optional] 
**name** | **str** | The name of the Subscription. If not provided the plan name is used. | [optional] 
**description** | **str** | Description for the Subscription. | [optional] 
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | Timing configuration for the change, when the change should take effect. The default is immediate. | [optional] 
**customer_id** | **str** | The ID of the customer. Provide either the key or ID. Has presedence over the key. | [optional] 
**customer_key** | **str** | The key of the customer. Provide either the key or ID. | [optional] 
**billing_anchor** | **datetime** | The billing anchor of the subscription. The provided date will be normalized according to the billing cadence to the nearest recurrence before start time. If not provided, the subscription start time will be used. | [optional] 
**custom_plan** | [**CustomPlanInput**](CustomPlanInput.md) | The custom plan description which defines the Subscription. | 

## Example

```python
from moolabs.models.subscription_create import SubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCreate from a JSON string
subscription_create_instance = SubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCreate.to_json())

# convert the object into a dict
subscription_create_dict = subscription_create_instance.to_dict()
# create an instance of SubscriptionCreate from a dict
subscription_create_from_dict = SubscriptionCreate.from_dict(subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


