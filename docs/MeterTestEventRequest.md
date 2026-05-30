# MeterTestEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** |  | 

## Example

```python
from moolabs.models.meter_test_event_request import MeterTestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MeterTestEventRequest from a JSON string
meter_test_event_request_instance = MeterTestEventRequest.from_json(json)
# print the JSON string representation of the object
print(MeterTestEventRequest.to_json())

# convert the object into a dict
meter_test_event_request_dict = meter_test_event_request_instance.to_dict()
# create an instance of MeterTestEventRequest from a dict
meter_test_event_request_from_dict = MeterTestEventRequest.from_dict(meter_test_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


