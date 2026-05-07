# CancelSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | If not provided the subscription is canceled immediately. | [optional] 

## Example

```python
from moolabs.models.cancel_subscription_request import CancelSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelSubscriptionRequest from a JSON string
cancel_subscription_request_instance = CancelSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CancelSubscriptionRequest.to_json())

# convert the object into a dict
cancel_subscription_request_dict = cancel_subscription_request_instance.to_dict()
# create an instance of CancelSubscriptionRequest from a dict
cancel_subscription_request_from_dict = CancelSubscriptionRequest.from_dict(cancel_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


