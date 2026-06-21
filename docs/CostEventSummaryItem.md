# CostEventSummaryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_event_id** | **str** |  | 
**status** | **str** |  | 
**reporting_total_cost** | **str** |  | [optional] 
**reporting_currency** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**line_item_count** | **int** |  | [optional] [default to 0]
**priced_line_item_count** | **int** |  | [optional] [default to 0]
**cost_event_count** | **int** |  | [optional] [default to 0]

## Example

```python
from moolabs.models.cost_event_summary_item import CostEventSummaryItem

# TODO update the JSON string below
json = "{}"
# create an instance of CostEventSummaryItem from a JSON string
cost_event_summary_item_instance = CostEventSummaryItem.from_json(json)
# print the JSON string representation of the object
print(CostEventSummaryItem.to_json())

# convert the object into a dict
cost_event_summary_item_dict = cost_event_summary_item_instance.to_dict()
# create an instance of CostEventSummaryItem from a dict
cost_event_summary_item_from_dict = CostEventSummaryItem.from_dict(cost_event_summary_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


