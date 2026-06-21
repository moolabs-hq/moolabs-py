# ApprovalPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | 
**policy_version_stamp** | **str** |  | 
**config** | **Dict[str, object]** |  | 

## Example

```python
from moolabs.models.approval_policy_response import ApprovalPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalPolicyResponse from a JSON string
approval_policy_response_instance = ApprovalPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(ApprovalPolicyResponse.to_json())

# convert the object into a dict
approval_policy_response_dict = approval_policy_response_instance.to_dict()
# create an instance of ApprovalPolicyResponse from a dict
approval_policy_response_from_dict = ApprovalPolicyResponse.from_dict(approval_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


