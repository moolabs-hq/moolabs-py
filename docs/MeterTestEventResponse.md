# MeterTestEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted_value** | **float** |  | [optional] 
**is_numeric** | **bool** |  | 
**group_by_values** | **Dict[str, str]** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.meter_test_event_response import MeterTestEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MeterTestEventResponse from a JSON string
meter_test_event_response_instance = MeterTestEventResponse.from_json(json)
# print the JSON string representation of the object
print(MeterTestEventResponse.to_json())

# convert the object into a dict
meter_test_event_response_dict = meter_test_event_response_instance.to_dict()
# create an instance of MeterTestEventResponse from a dict
meter_test_event_response_from_dict = MeterTestEventResponse.from_dict(meter_test_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


