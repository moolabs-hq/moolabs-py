# ApprovalActionRequest

POST approve/reject — optional note.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.approval_action_request import ApprovalActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalActionRequest from a JSON string
approval_action_request_instance = ApprovalActionRequest.from_json(json)
# print the JSON string representation of the object
print(ApprovalActionRequest.to_json())

# convert the object into a dict
approval_action_request_dict = approval_action_request_instance.to_dict()
# create an instance of ApprovalActionRequest from a dict
approval_action_request_from_dict = ApprovalActionRequest.from_dict(approval_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


