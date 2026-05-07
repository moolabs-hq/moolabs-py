# MeterCreate

A meter create model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. Defaults to the slug if not specified. | [optional] 
**slug** | **str** | A unique, human-readable identifier for the meter. Must consist only alphanumeric and underscore characters. | 
**aggregation** | [**MeterAggregation**](MeterAggregation.md) | The aggregation type to use for the meter. | 
**event_type** | **str** | The event type to aggregate. | 
**event_from** | **datetime** | The date since the meter should include events. Useful to skip old events. If not specified, all historical events are included. | [optional] 
**value_property** | **str** | JSONPath expression to extract the value from the ingested event&#39;s data property.  The ingested value for SUM, AVG, MIN, and MAX aggregations is a number or a string that can be parsed to a number.  For UNIQUE_COUNT aggregation, the ingested value must be a string. For COUNT aggregation the valueProperty is ignored. | [optional] 
**group_by** | **Dict[str, str]** | Named JSONPath expressions to extract the group by values from the event data.  Keys must be unique and consist only alphanumeric and underscore characters. | [optional] 

## Example

```python
from moolabs.models.meter_create import MeterCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MeterCreate from a JSON string
meter_create_instance = MeterCreate.from_json(json)
# print the JSON string representation of the object
print(MeterCreate.to_json())

# convert the object into a dict
meter_create_dict = meter_create_instance.to_dict()
# create an instance of MeterCreate from a dict
meter_create_from_dict = MeterCreate.from_dict(meter_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


