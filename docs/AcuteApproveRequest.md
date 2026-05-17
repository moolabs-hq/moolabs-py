# AcuteApproveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_by** | **str** | Identity of approver (required) | 

## Example

```python
from moolabs.models.acute_approve_request import AcuteApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcuteApproveRequest from a JSON string
acute_approve_request_instance = AcuteApproveRequest.from_json(json)
# print the JSON string representation of the object
print(AcuteApproveRequest.to_json())

# convert the object into a dict
acute_approve_request_dict = acute_approve_request_instance.to_dict()
# create an instance of AcuteApproveRequest from a dict
acute_approve_request_from_dict = AcuteApproveRequest.from_dict(acute_approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


