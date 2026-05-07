# SubscriptionTiming

Subscription edit timing defined when the changes should take effect. If the provided configuration is not supported by the subscription, an error will be returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from moolabs.models.subscription_timing import SubscriptionTiming

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionTiming from a JSON string
subscription_timing_instance = SubscriptionTiming.from_json(json)
# print the JSON string representation of the object
print(SubscriptionTiming.to_json())

# convert the object into a dict
subscription_timing_dict = subscription_timing_instance.to_dict()
# create an instance of SubscriptionTiming from a dict
subscription_timing_from_dict = SubscriptionTiming.from_dict(subscription_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


