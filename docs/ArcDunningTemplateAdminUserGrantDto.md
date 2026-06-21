# ArcDunningTemplateAdminUserGrantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**permission** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.arc_dunning_template_admin_user_grant_dto import ArcDunningTemplateAdminUserGrantDto

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningTemplateAdminUserGrantDto from a JSON string
arc_dunning_template_admin_user_grant_dto_instance = ArcDunningTemplateAdminUserGrantDto.from_json(json)
# print the JSON string representation of the object
print(ArcDunningTemplateAdminUserGrantDto.to_json())

# convert the object into a dict
arc_dunning_template_admin_user_grant_dto_dict = arc_dunning_template_admin_user_grant_dto_instance.to_dict()
# create an instance of ArcDunningTemplateAdminUserGrantDto from a dict
arc_dunning_template_admin_user_grant_dto_from_dict = ArcDunningTemplateAdminUserGrantDto.from_dict(arc_dunning_template_admin_user_grant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


