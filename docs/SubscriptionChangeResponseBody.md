# SubscriptionChangeResponseBody

Response body for subscription change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**Subscription**](Subscription.md) | The current subscription before the change. | 
**next** | [**SubscriptionExpanded**](SubscriptionExpanded.md) | The new state of the subscription after the change. | 

## Example

```python
from moolabs.models.subscription_change_response_body import SubscriptionChangeResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionChangeResponseBody from a JSON string
subscription_change_response_body_instance = SubscriptionChangeResponseBody.from_json(json)
# print the JSON string representation of the object
print(SubscriptionChangeResponseBody.to_json())

# convert the object into a dict
subscription_change_response_body_dict = subscription_change_response_body_instance.to_dict()
# create an instance of SubscriptionChangeResponseBody from a dict
subscription_change_response_body_from_dict = SubscriptionChangeResponseBody.from_dict(subscription_change_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


