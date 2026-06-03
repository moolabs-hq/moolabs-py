# EffectivePermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**org_id** | **str** |  | 
**actor_user_id** | **str** |  | 
**actor_display** | **str** |  | [optional] 
**actor_email** | **str** |  | [optional] 
**org_role** | **str** |  | [optional] 
**is_org_admin** | **bool** |  | 
**permissions** | **List[str]** |  | 
**grants** | [**List[EffectivePermissionGrantDto]**](EffectivePermissionGrantDto.md) |  | 

## Example

```python
from moolabs.models.effective_permissions_response import EffectivePermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EffectivePermissionsResponse from a JSON string
effective_permissions_response_instance = EffectivePermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(EffectivePermissionsResponse.to_json())

# convert the object into a dict
effective_permissions_response_dict = effective_permissions_response_instance.to_dict()
# create an instance of EffectivePermissionsResponse from a dict
effective_permissions_response_from_dict = EffectivePermissionsResponse.from_dict(effective_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


