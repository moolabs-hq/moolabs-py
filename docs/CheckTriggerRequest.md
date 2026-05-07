# CheckTriggerRequest

Request to check and trigger auto top-up.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.check_trigger_request import CheckTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTriggerRequest from a JSON string
check_trigger_request_instance = CheckTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(CheckTriggerRequest.to_json())

# convert the object into a dict
check_trigger_request_dict = check_trigger_request_instance.to_dict()
# create an instance of CheckTriggerRequest from a dict
check_trigger_request_from_dict = CheckTriggerRequest.from_dict(check_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


