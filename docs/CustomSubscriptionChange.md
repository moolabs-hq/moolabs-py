# CustomSubscriptionChange

Change a custom subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | Timing configuration for the change, when the change should take effect. For changing a subscription, the accepted values depend on the subscription configuration. | 
**billing_anchor** | **datetime** | The billing anchor of the subscription. The provided date will be normalized according to the billing cadence to the nearest recurrence before start time. If not provided, the previous subscription billing anchor will be used. | [optional] 
**commercial_overrides** | [**CommercialOverrides**](CommercialOverrides.md) | Commercial terms for this subscription change. | [optional] 
**custom_plan** | [**CustomPlanInput**](CustomPlanInput.md) | The custom plan description which defines the Subscription. | 
**quote_origin_key** | **str** | Idempotency key supplied by accepted quote activation for subscription create or change requests. | [optional] 

## Example

```python
from moolabs.models.custom_subscription_change import CustomSubscriptionChange

# TODO update the JSON string below
json = "{}"
# create an instance of CustomSubscriptionChange from a JSON string
custom_subscription_change_instance = CustomSubscriptionChange.from_json(json)
# print the JSON string representation of the object
print(CustomSubscriptionChange.to_json())

# convert the object into a dict
custom_subscription_change_dict = custom_subscription_change_instance.to_dict()
# create an instance of CustomSubscriptionChange from a dict
custom_subscription_change_from_dict = CustomSubscriptionChange.from_dict(custom_subscription_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


