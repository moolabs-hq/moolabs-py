# MeterUsageSummaryItem

Usage summary for a single meter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meter_slug** | **str** | The meter slug. | 
**description** | **str** | Human-readable meter description. | [optional] 
**aggregation** | **str** | The meter&#39;s aggregation type (SUM, COUNT, AVG, etc). | 
**value** | **float** | Total aggregated value for the requested time range. | 
**windows** | [**List[MeterQueryRow]**](MeterQueryRow.md) | Per-window breakdown (only present when windowSize is specified). | [optional] 

## Example

```python
from moolabs.models.meter_usage_summary_item import MeterUsageSummaryItem

# TODO update the JSON string below
json = "{}"
# create an instance of MeterUsageSummaryItem from a JSON string
meter_usage_summary_item_instance = MeterUsageSummaryItem.from_json(json)
# print the JSON string representation of the object
print(MeterUsageSummaryItem.to_json())

# convert the object into a dict
meter_usage_summary_item_dict = meter_usage_summary_item_instance.to_dict()
# create an instance of MeterUsageSummaryItem from a dict
meter_usage_summary_item_from_dict = MeterUsageSummaryItem.from_dict(meter_usage_summary_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


