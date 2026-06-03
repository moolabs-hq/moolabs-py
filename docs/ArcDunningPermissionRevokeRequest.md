# ArcDunningPermissionRevokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoke_reason** | **str** |  | 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from moolabs.models.arc_dunning_permission_revoke_request import ArcDunningPermissionRevokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningPermissionRevokeRequest from a JSON string
arc_dunning_permission_revoke_request_instance = ArcDunningPermissionRevokeRequest.from_json(json)
# print the JSON string representation of the object
print(ArcDunningPermissionRevokeRequest.to_json())

# convert the object into a dict
arc_dunning_permission_revoke_request_dict = arc_dunning_permission_revoke_request_instance.to_dict()
# create an instance of ArcDunningPermissionRevokeRequest from a dict
arc_dunning_permission_revoke_request_from_dict = ArcDunningPermissionRevokeRequest.from_dict(arc_dunning_permission_revoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


