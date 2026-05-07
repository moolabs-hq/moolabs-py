# MeterQueryResult

The result of a meter query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | The start of the period the usage is queried from. If not specified, the usage is queried from the beginning of time. | [optional] 
**to** | **datetime** | The end of the period the usage is queried to. If not specified, the usage is queried up to the current time. | [optional] 
**window_size** | [**WindowSize**](WindowSize.md) | The window size that the usage is aggregated. If not specified, the usage is aggregated over the entire period. | [optional] 
**data** | [**List[MeterQueryRow]**](MeterQueryRow.md) | The usage data. If no data is available, an empty array is returned. | 

## Example

```python
from moolabs.models.meter_query_result import MeterQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of MeterQueryResult from a JSON string
meter_query_result_instance = MeterQueryResult.from_json(json)
# print the JSON string representation of the object
print(MeterQueryResult.to_json())

# convert the object into a dict
meter_query_result_dict = meter_query_result_instance.to_dict()
# create an instance of MeterQueryResult from a dict
meter_query_result_from_dict = MeterQueryResult.from_dict(meter_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


