# RescheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_due_date** | **date** |  | 

## Example

```python
from moolabs.models.reschedule_request import RescheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RescheduleRequest from a JSON string
reschedule_request_instance = RescheduleRequest.from_json(json)
# print the JSON string representation of the object
print(RescheduleRequest.to_json())

# convert the object into a dict
reschedule_request_dict = reschedule_request_instance.to_dict()
# create an instance of RescheduleRequest from a dict
reschedule_request_from_dict = RescheduleRequest.from_dict(reschedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


