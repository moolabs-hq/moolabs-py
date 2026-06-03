# DraftLockResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | 
**lock_id** | **str** |  | 
**lock_token** | **str** |  | 
**lock_owner_actor_id** | **str** |  | 
**lock_owner_display** | **str** |  | [optional] 
**lock_expires_at** | **str** |  | 

## Example

```python
from moolabs.models.draft_lock_response import DraftLockResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DraftLockResponse from a JSON string
draft_lock_response_instance = DraftLockResponse.from_json(json)
# print the JSON string representation of the object
print(DraftLockResponse.to_json())

# convert the object into a dict
draft_lock_response_dict = draft_lock_response_instance.to_dict()
# create an instance of DraftLockResponse from a dict
draft_lock_response_from_dict = DraftLockResponse.from_dict(draft_lock_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


