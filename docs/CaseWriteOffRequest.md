# CaseWriteOffRequest

POST /cases/{id}/write-off — requires approval (D5).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**amount_micros** | **int** | Partial write-off amount; null &#x3D; full | [optional] 

## Example

```python
from moolabs.models.case_write_off_request import CaseWriteOffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaseWriteOffRequest from a JSON string
case_write_off_request_instance = CaseWriteOffRequest.from_json(json)
# print the JSON string representation of the object
print(CaseWriteOffRequest.to_json())

# convert the object into a dict
case_write_off_request_dict = case_write_off_request_instance.to_dict()
# create an instance of CaseWriteOffRequest from a dict
case_write_off_request_from_dict = CaseWriteOffRequest.from_dict(case_write_off_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


