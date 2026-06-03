# DraftLockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl_seconds** | **int** |  | [optional] [default to 900]

## Example

```python
from moolabs.models.draft_lock_request import DraftLockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DraftLockRequest from a JSON string
draft_lock_request_instance = DraftLockRequest.from_json(json)
# print the JSON string representation of the object
print(DraftLockRequest.to_json())

# convert the object into a dict
draft_lock_request_dict = draft_lock_request_instance.to_dict()
# create an instance of DraftLockRequest from a dict
draft_lock_request_from_dict = DraftLockRequest.from_dict(draft_lock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


