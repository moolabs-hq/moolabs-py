# DangerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_note** | **str** |  | 
**confirm** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.danger_request import DangerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DangerRequest from a JSON string
danger_request_instance = DangerRequest.from_json(json)
# print the JSON string representation of the object
print(DangerRequest.to_json())

# convert the object into a dict
danger_request_dict = danger_request_instance.to_dict()
# create an instance of DangerRequest from a dict
danger_request_from_dict = DangerRequest.from_dict(danger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


