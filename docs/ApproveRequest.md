# ApproveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.approve_request import ApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveRequest from a JSON string
approve_request_instance = ApproveRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveRequest.to_json())

# convert the object into a dict
approve_request_dict = approve_request_instance.to_dict()
# create an instance of ApproveRequest from a dict
approve_request_from_dict = ApproveRequest.from_dict(approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


