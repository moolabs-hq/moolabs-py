# SubscriptionAddonUpdate

Resource create or update operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | [optional] 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**quantity** | **int** | The quantity of the add-on. Always 1 for single instance add-ons. | [optional] 
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | The timing of the operation. After the create or update, a new entry will be created in the timeline. | [optional] 

## Example

```python
from moolabs.models.subscription_addon_update import SubscriptionAddonUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAddonUpdate from a JSON string
subscription_addon_update_instance = SubscriptionAddonUpdate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAddonUpdate.to_json())

# convert the object into a dict
subscription_addon_update_dict = subscription_addon_update_instance.to_dict()
# create an instance of SubscriptionAddonUpdate from a dict
subscription_addon_update_from_dict = SubscriptionAddonUpdate.from_dict(subscription_addon_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


