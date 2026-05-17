# CaseEscalateRequest

POST /cases/{id}/escalate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**escalate_to** | **str** |  | [optional] 

## Example

```python
from moolabs.models.case_escalate_request import CaseEscalateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaseEscalateRequest from a JSON string
case_escalate_request_instance = CaseEscalateRequest.from_json(json)
# print the JSON string representation of the object
print(CaseEscalateRequest.to_json())

# convert the object into a dict
case_escalate_request_dict = case_escalate_request_instance.to_dict()
# create an instance of CaseEscalateRequest from a dict
case_escalate_request_from_dict = CaseEscalateRequest.from_dict(case_escalate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


