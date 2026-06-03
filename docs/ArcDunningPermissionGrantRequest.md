# ArcDunningPermissionGrantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**org_id** | **str** |  | 
**user_subject** | **str** |  | 
**grant_reason** | **str** |  | 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from moolabs.models.arc_dunning_permission_grant_request import ArcDunningPermissionGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningPermissionGrantRequest from a JSON string
arc_dunning_permission_grant_request_instance = ArcDunningPermissionGrantRequest.from_json(json)
# print the JSON string representation of the object
print(ArcDunningPermissionGrantRequest.to_json())

# convert the object into a dict
arc_dunning_permission_grant_request_dict = arc_dunning_permission_grant_request_instance.to_dict()
# create an instance of ArcDunningPermissionGrantRequest from a dict
arc_dunning_permission_grant_request_from_dict = ArcDunningPermissionGrantRequest.from_dict(arc_dunning_permission_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


