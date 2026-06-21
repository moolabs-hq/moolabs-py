# ArcDunningTemplateAdminUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_subject** | **str** |  | 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**org_role** | [**OrgRole**](OrgRole.md) |  | [optional] 
**eligible_for_grant** | **bool** |  | [optional] [default to False]
**grant_blocked_reason** | **str** |  | [optional] 
**grant** | [**ArcDunningTemplateAdminUserGrantDto**](ArcDunningTemplateAdminUserGrantDto.md) |  | [optional] 

## Example

```python
from moolabs.models.arc_dunning_template_admin_user_dto import ArcDunningTemplateAdminUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningTemplateAdminUserDto from a JSON string
arc_dunning_template_admin_user_dto_instance = ArcDunningTemplateAdminUserDto.from_json(json)
# print the JSON string representation of the object
print(ArcDunningTemplateAdminUserDto.to_json())

# convert the object into a dict
arc_dunning_template_admin_user_dto_dict = arc_dunning_template_admin_user_dto_instance.to_dict()
# create an instance of ArcDunningTemplateAdminUserDto from a dict
arc_dunning_template_admin_user_dto_from_dict = ArcDunningTemplateAdminUserDto.from_dict(arc_dunning_template_admin_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


