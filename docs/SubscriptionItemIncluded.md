# SubscriptionItemIncluded

Included contents like Entitlement, or the Feature.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**Feature**](Feature.md) | The feature the customer is entitled to use. | 
**entitlement** | [**Entitlement**](Entitlement.md) | The entitlement of the Subscription Item. | [optional] 

## Example

```python
from moolabs.models.subscription_item_included import SubscriptionItemIncluded

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionItemIncluded from a JSON string
subscription_item_included_instance = SubscriptionItemIncluded.from_json(json)
# print the JSON string representation of the object
print(SubscriptionItemIncluded.to_json())

# convert the object into a dict
subscription_item_included_dict = subscription_item_included_instance.to_dict()
# create an instance of SubscriptionItemIncluded from a dict
subscription_item_included_from_dict = SubscriptionItemIncluded.from_dict(subscription_item_included_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


