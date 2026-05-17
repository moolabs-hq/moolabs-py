# ApproveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_event_id** | **str** |  | 
**status** | **str** |  | 
**completion_kind** | **str** |  | 

## Example

```python
from moolabs.models.approve_response import ApproveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveResponse from a JSON string
approve_response_instance = ApproveResponse.from_json(json)
# print the JSON string representation of the object
print(ApproveResponse.to_json())

# convert the object into a dict
approve_response_dict = approve_response_instance.to_dict()
# create an instance of ApproveResponse from a dict
approve_response_from_dict = ApproveResponse.from_dict(approve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


