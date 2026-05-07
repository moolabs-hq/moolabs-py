# MeterQueryRow

A row in the result of a meter query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The aggregated value. | 
**window_start** | **datetime** | The start of the window the value is aggregated over. | 
**window_end** | **datetime** | The end of the window the value is aggregated over. | 
**subject** | **str** | The subject the value is aggregated over. If not specified, the value is aggregated over all subjects. | 
**customer_id** | **str** | The customer ID the value is aggregated over. | [optional] 
**group_by** | **Dict[str, str]** | The group by values the value is aggregated over. | 

## Example

```python
from moolabs.models.meter_query_row import MeterQueryRow

# TODO update the JSON string below
json = "{}"
# create an instance of MeterQueryRow from a JSON string
meter_query_row_instance = MeterQueryRow.from_json(json)
# print the JSON string representation of the object
print(MeterQueryRow.to_json())

# convert the object into a dict
meter_query_row_dict = meter_query_row_instance.to_dict()
# create an instance of MeterQueryRow from a dict
meter_query_row_from_dict = MeterQueryRow.from_dict(meter_query_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


