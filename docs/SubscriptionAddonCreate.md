# SubscriptionAddonCreate

A subscription add-on create body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**quantity** | **int** | The quantity of the add-on. Always 1 for single instance add-ons. | 
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | The timing of the operation. After the create or update, a new entry will be created in the timeline. | 
**addon** | [**Addon2**](Addon2.md) |  | 

## Example

```python
from moolabs.models.subscription_addon_create import SubscriptionAddonCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAddonCreate from a JSON string
subscription_addon_create_instance = SubscriptionAddonCreate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAddonCreate.to_json())

# convert the object into a dict
subscription_addon_create_dict = subscription_addon_create_instance.to_dict()
# create an instance of SubscriptionAddonCreate from a dict
subscription_addon_create_from_dict = SubscriptionAddonCreate.from_dict(subscription_addon_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


