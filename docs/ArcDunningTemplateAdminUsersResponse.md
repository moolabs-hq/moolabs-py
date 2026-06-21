# ArcDunningTemplateAdminUsersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**org_id** | **str** |  | 
**permission** | **str** |  | 
**can_manage** | **bool** |  | 
**users** | [**List[ArcDunningTemplateAdminUserDto]**](ArcDunningTemplateAdminUserDto.md) |  | 

## Example

```python
from moolabs.models.arc_dunning_template_admin_users_response import ArcDunningTemplateAdminUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningTemplateAdminUsersResponse from a JSON string
arc_dunning_template_admin_users_response_instance = ArcDunningTemplateAdminUsersResponse.from_json(json)
# print the JSON string representation of the object
print(ArcDunningTemplateAdminUsersResponse.to_json())

# convert the object into a dict
arc_dunning_template_admin_users_response_dict = arc_dunning_template_admin_users_response_instance.to_dict()
# create an instance of ArcDunningTemplateAdminUsersResponse from a dict
arc_dunning_template_admin_users_response_from_dict = ArcDunningTemplateAdminUsersResponse.from_dict(arc_dunning_template_admin_users_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


