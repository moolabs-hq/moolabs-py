# CasePauseRequest

POST /cases/{id}/pause

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**resume_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.case_pause_request import CasePauseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CasePauseRequest from a JSON string
case_pause_request_instance = CasePauseRequest.from_json(json)
# print the JSON string representation of the object
print(CasePauseRequest.to_json())

# convert the object into a dict
case_pause_request_dict = case_pause_request_instance.to_dict()
# create an instance of CasePauseRequest from a dict
case_pause_request_from_dict = CasePauseRequest.from_dict(case_pause_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


