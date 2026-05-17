# PTPApprovalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.ptp_approval_request import PTPApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PTPApprovalRequest from a JSON string
ptp_approval_request_instance = PTPApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(PTPApprovalRequest.to_json())

# convert the object into a dict
ptp_approval_request_dict = ptp_approval_request_instance.to_dict()
# create an instance of PTPApprovalRequest from a dict
ptp_approval_request_from_dict = PTPApprovalRequest.from_dict(ptp_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


