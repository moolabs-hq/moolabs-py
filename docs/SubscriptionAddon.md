# SubscriptionAddon

A subscription add-on, represents concrete instances of an add-on for a given subscription.

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
**active_from** | **datetime** | The cadence start of the resource. | [readonly] 
**active_to** | **datetime** | The cadence end of the resource. | [optional] [readonly] 
**addon** | [**Addon1**](Addon1.md) |  | 
**quantity_at** | **datetime** | For which point in time the quantity was resolved to. | [readonly] 
**quantity** | **int** | The quantity of the add-on. Always 1 for single instance add-ons. | 
**timeline** | [**List[SubscriptionAddonTimelineSegment]**](SubscriptionAddonTimelineSegment.md) | The timeline of the add-on. The returned periods are sorted and continuous. | 
**subscription_id** | **str** | The ID of the subscription. | [readonly] 
**rate_cards** | [**List[SubscriptionAddonRateCard]**](SubscriptionAddonRateCard.md) | The rate cards of the add-on. | 

## Example

```python
from moolabs.models.subscription_addon import SubscriptionAddon

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAddon from a JSON string
subscription_addon_instance = SubscriptionAddon.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAddon.to_json())

# convert the object into a dict
subscription_addon_dict = subscription_addon_instance.to_dict()
# create an instance of SubscriptionAddon from a dict
subscription_addon_from_dict = SubscriptionAddon.from_dict(subscription_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


