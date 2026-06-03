# DraftSaveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] [default to 'email']
**subject_template** | **str** |  | 
**body_template** | **str** |  | 
**change_reason** | **str** |  | 
**prompt_summary** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**base_version_id** | **str** |  | [optional] 
**lock_id** | **str** |  | [optional] 
**lock_token** | **str** |  | [optional] 

## Example

```python
from moolabs.models.draft_save_request import DraftSaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DraftSaveRequest from a JSON string
draft_save_request_instance = DraftSaveRequest.from_json(json)
# print the JSON string representation of the object
print(DraftSaveRequest.to_json())

# convert the object into a dict
draft_save_request_dict = draft_save_request_instance.to_dict()
# create an instance of DraftSaveRequest from a dict
draft_save_request_from_dict = DraftSaveRequest.from_dict(draft_save_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


