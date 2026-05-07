# TestMeterEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 

## Example

```python
from moolabs.models.test_meter_event_request import TestMeterEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestMeterEventRequest from a JSON string
test_meter_event_request_instance = TestMeterEventRequest.from_json(json)
# print the JSON string representation of the object
print(TestMeterEventRequest.to_json())

# convert the object into a dict
test_meter_event_request_dict = test_meter_event_request_instance.to_dict()
# create an instance of TestMeterEventRequest from a dict
test_meter_event_request_from_dict = TestMeterEventRequest.from_dict(test_meter_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


