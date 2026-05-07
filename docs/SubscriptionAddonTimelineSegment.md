# SubscriptionAddonTimelineSegment

A subscription add-on event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**quantity** | **int** | The quantity of the add-on for the given period. | [readonly] 

## Example

```python
from moolabs.models.subscription_addon_timeline_segment import SubscriptionAddonTimelineSegment

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAddonTimelineSegment from a JSON string
subscription_addon_timeline_segment_instance = SubscriptionAddonTimelineSegment.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAddonTimelineSegment.to_json())

# convert the object into a dict
subscription_addon_timeline_segment_dict = subscription_addon_timeline_segment_instance.to_dict()
# create an instance of SubscriptionAddonTimelineSegment from a dict
subscription_addon_timeline_segment_from_dict = SubscriptionAddonTimelineSegment.from_dict(subscription_addon_timeline_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


