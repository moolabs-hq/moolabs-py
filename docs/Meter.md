# Meter

A meter is a configuration that defines how to match and aggregate events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. Defaults to the slug if not specified. | [optional] 
**projection_status** | **str** | Async ClickHouse parser reconciliation status for this meter. | [optional] [readonly] 
**projection_error** | **str** | Last projection reconciliation error, if projectionStatus is failed. | [optional] [readonly] 
**data_health** | **str** | Raw-event extraction health for this meter. | [optional] [readonly] 
**data_health_reason** | **str** | Last data-health transition reason. | [optional] [readonly] 
**slug** | **str** | A unique, human-readable identifier for the meter. Must consist only alphanumeric and underscore characters. | 
**aggregation** | [**MeterAggregation**](MeterAggregation.md) | The aggregation type to use for the meter. | 
**event_type** | **str** | The event type to aggregate. | 
**event_from** | **datetime** | The date since the meter should include events. Useful to skip old events. If not specified, all historical events are included. | [optional] 
**value_property** | **str** | JSONPath expression to extract the value from the ingested event&#39;s data property.  The ingested value for SUM, AVG, MIN, and MAX aggregations is a number or a string that can be parsed to a number.  For UNIQUE_COUNT aggregation, the ingested value must be a string. For COUNT aggregation the valueProperty is ignored. | [optional] 
**group_by** | **Dict[str, str]** | Named JSONPath expressions to extract the group by values from the event data.  Keys must be unique and consist only alphanumeric and underscore characters. | [optional] 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 

## Example

```python
from moolabs.models.meter import Meter

# TODO update the JSON string below
json = "{}"
# create an instance of Meter from a JSON string
meter_instance = Meter.from_json(json)
# print the JSON string representation of the object
print(Meter.to_json())

# convert the object into a dict
meter_dict = meter_instance.to_dict()
# create an instance of Meter from a dict
meter_from_dict = Meter.from_dict(meter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


