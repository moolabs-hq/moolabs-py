# CustomSubscriptionCreate

Create a custom subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commercial_overrides** | [**CommercialOverrides**](CommercialOverrides.md) | Commercial terms for this subscription change. | [optional] 
**custom_plan** | [**CustomPlanInput**](CustomPlanInput.md) | The custom plan description which defines the Subscription. | 
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | Timing configuration for the change, when the change should take effect. The default is immediate. | [optional] 
**customer_id** | **str** | The ID of the customer. Provide either the key or ID. Has presedence over the key. | [optional] 
**customer_key** | **str** | The key of the customer. Provide either the key or ID. | [optional] 
**billing_anchor** | **datetime** | The billing anchor of the subscription. The provided date will be normalized according to the billing cadence to the nearest recurrence before start time. If not provided, the subscription start time will be used. | [optional] 

## Example

```python
from moolabs.models.custom_subscription_create import CustomSubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomSubscriptionCreate from a JSON string
custom_subscription_create_instance = CustomSubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print(CustomSubscriptionCreate.to_json())

# convert the object into a dict
custom_subscription_create_dict = custom_subscription_create_instance.to_dict()
# create an instance of CustomSubscriptionCreate from a dict
custom_subscription_create_from_dict = CustomSubscriptionCreate.from_dict(custom_subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


