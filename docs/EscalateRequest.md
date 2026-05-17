# EscalateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**priority** | **str** |  | [optional] [default to 'medium']

## Example

```python
from moolabs.models.escalate_request import EscalateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EscalateRequest from a JSON string
escalate_request_instance = EscalateRequest.from_json(json)
# print the JSON string representation of the object
print(EscalateRequest.to_json())

# convert the object into a dict
escalate_request_dict = escalate_request_instance.to_dict()
# create an instance of EscalateRequest from a dict
escalate_request_from_dict = EscalateRequest.from_dict(escalate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


