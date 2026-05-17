# DisputeApprovalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.dispute_approval_request import DisputeApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisputeApprovalRequest from a JSON string
dispute_approval_request_instance = DisputeApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(DisputeApprovalRequest.to_json())

# convert the object into a dict
dispute_approval_request_dict = dispute_approval_request_instance.to_dict()
# create an instance of DisputeApprovalRequest from a dict
dispute_approval_request_from_dict = DisputeApprovalRequest.from_dict(dispute_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


