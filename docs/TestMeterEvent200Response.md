# TestMeterEvent200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extracted_value** | **float** |  | [optional] 
**is_numeric** | **bool** |  | 
**group_by_values** | **Dict[str, Optional[str]]** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.test_meter_event200_response import TestMeterEvent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TestMeterEvent200Response from a JSON string
test_meter_event200_response_instance = TestMeterEvent200Response.from_json(json)
# print the JSON string representation of the object
print(TestMeterEvent200Response.to_json())

# convert the object into a dict
test_meter_event200_response_dict = test_meter_event200_response_instance.to_dict()
# create an instance of TestMeterEvent200Response from a dict
test_meter_event200_response_from_dict = TestMeterEvent200Response.from_dict(test_meter_event200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


