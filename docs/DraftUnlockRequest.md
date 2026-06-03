# DraftUnlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock_id** | **str** |  | 
**lock_token** | **str** |  | 

## Example

```python
from moolabs.models.draft_unlock_request import DraftUnlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DraftUnlockRequest from a JSON string
draft_unlock_request_instance = DraftUnlockRequest.from_json(json)
# print the JSON string representation of the object
print(DraftUnlockRequest.to_json())

# convert the object into a dict
draft_unlock_request_dict = draft_unlock_request_instance.to_dict()
# create an instance of DraftUnlockRequest from a dict
draft_unlock_request_from_dict = DraftUnlockRequest.from_dict(draft_unlock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


