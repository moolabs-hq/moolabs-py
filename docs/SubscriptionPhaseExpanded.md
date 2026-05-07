# SubscriptionPhaseExpanded

Expanded subscription phase

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
**key** | **str** | A locally unique identifier for the resource. | 
**discounts** | [**Discounts**](Discounts.md) | The discounts on the plan. | [optional] 
**active_from** | **datetime** | The time from which the phase is active. | 
**active_to** | **datetime** | The until which the Phase is active. | [optional] 
**items** | [**List[SubscriptionItem]**](SubscriptionItem.md) | The items of the phase. The structure is flattened to better conform to the Plan API. The timelines are flattened according to the following rules: - for the current phase, the &#x60;items&#x60; contains only the active item for each key - for past phases, the &#x60;items&#x60; contains only the last item for each key - for future phases, the &#x60;items&#x60; contains only the first version of the item for each key | 
**item_timelines** | **Dict[str, List[SubscriptionItem]]** | Includes all versions of the items on each key, including all edits, scheduled changes, etc... | 

## Example

```python
from moolabs.models.subscription_phase_expanded import SubscriptionPhaseExpanded

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPhaseExpanded from a JSON string
subscription_phase_expanded_instance = SubscriptionPhaseExpanded.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPhaseExpanded.to_json())

# convert the object into a dict
subscription_phase_expanded_dict = subscription_phase_expanded_instance.to_dict()
# create an instance of SubscriptionPhaseExpanded from a dict
subscription_phase_expanded_from_dict = SubscriptionPhaseExpanded.from_dict(subscription_phase_expanded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


