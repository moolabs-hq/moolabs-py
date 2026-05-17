# ApprovalActionResponse

Response for approve/reject action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_id** | **str** |  | 
**action** | **str** |  | 
**new_status** | **str** |  | 
**external_message_id** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from moolabs.models.approval_action_response import ApprovalActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalActionResponse from a JSON string
approval_action_response_instance = ApprovalActionResponse.from_json(json)
# print the JSON string representation of the object
print(ApprovalActionResponse.to_json())

# convert the object into a dict
approval_action_response_dict = approval_action_response_instance.to_dict()
# create an instance of ApprovalActionResponse from a dict
approval_action_response_from_dict = ApprovalActionResponse.from_dict(approval_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


