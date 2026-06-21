# ArcDunningTemplateAdminGrantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**org_id** | **str** |  | 
**user_subject** | **str** |  | 
**permission** | **str** |  | 
**status** | **str** |  | 
**created** | **bool** |  | [optional] 
**revoked** | **bool** |  | [optional] 

## Example

```python
from moolabs.models.arc_dunning_template_admin_grant_response import ArcDunningTemplateAdminGrantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningTemplateAdminGrantResponse from a JSON string
arc_dunning_template_admin_grant_response_instance = ArcDunningTemplateAdminGrantResponse.from_json(json)
# print the JSON string representation of the object
print(ArcDunningTemplateAdminGrantResponse.to_json())

# convert the object into a dict
arc_dunning_template_admin_grant_response_dict = arc_dunning_template_admin_grant_response_instance.to_dict()
# create an instance of ArcDunningTemplateAdminGrantResponse from a dict
arc_dunning_template_admin_grant_response_from_dict = ArcDunningTemplateAdminGrantResponse.from_dict(arc_dunning_template_admin_grant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


