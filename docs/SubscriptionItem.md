# SubscriptionItem

The actual contents of the Subscription, what the user gets, what they pay, etc...

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
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**key** | **str** | The identifier of the RateCard. SubscriptionItem/RateCard can be identified, it has a reference:  1. If a Feature is associated with the SubscriptionItem, it is identified by the Feature 1.1 It can be an ID reference, for an exact version of the Feature (Features can change across versions) 1.2 It can be a Key reference, which always refers to the latest (active or inactive) version of a Feature  2. If a Feature is not associated with the SubscriptionItem, it is referenced by the Price  We say \&quot;referenced by the Price\&quot; regardless of how a price itself is referenced, it colloquially makes sense to say \&quot;paying the same price for the same thing\&quot;. In practice this should be derived from what&#39;s printed on the invoice line-item. | 
**feature_key** | **str** | The feature&#39;s key (if present). | [optional] 
**billing_cadence** | **str** | The billing cadence of the rate card. When null, the rate card is a one-time purchase. | 
**price** | [**RateCardUsageBasedPrice**](RateCardUsageBasedPrice.md) | The price of the rate card. When null, the feature or service is free. | 
**discounts** | [**Discounts**](Discounts.md) | The discounts applied to the rate card. | [optional] 
**included** | [**SubscriptionItemIncluded**](SubscriptionItemIncluded.md) | Describes what access is gained via the SubscriptionItem | [optional] 
**tax_config** | [**TaxConfig**](TaxConfig.md) | The tax config of the Subscription Item. When undefined, the tax config of the feature or the default tax config of the plan is used. | [optional] 

## Example

```python
from moolabs.models.subscription_item import SubscriptionItem

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionItem from a JSON string
subscription_item_instance = SubscriptionItem.from_json(json)
# print the JSON string representation of the object
print(SubscriptionItem.to_json())

# convert the object into a dict
subscription_item_dict = subscription_item_instance.to_dict()
# create an instance of SubscriptionItem from a dict
subscription_item_from_dict = SubscriptionItem.from_dict(subscription_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


