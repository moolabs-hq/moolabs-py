# SubscriptionAddonRateCard

A rate card for a subscription add-on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_card** | [**RateCard**](RateCard.md) | The rate card. | 
**affected_subscription_item_ids** | **List[str]** | The IDs of the subscription items that this rate card belongs to. | 

## Example

```python
from moolabs.models.subscription_addon_rate_card import SubscriptionAddonRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAddonRateCard from a JSON string
subscription_addon_rate_card_instance = SubscriptionAddonRateCard.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAddonRateCard.to_json())

# convert the object into a dict
subscription_addon_rate_card_dict = subscription_addon_rate_card_instance.to_dict()
# create an instance of SubscriptionAddonRateCard from a dict
subscription_addon_rate_card_from_dict = SubscriptionAddonRateCard.from_dict(subscription_addon_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


