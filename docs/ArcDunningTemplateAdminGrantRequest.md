# ArcDunningTemplateAdminGrantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_subject** | **str** |  | 
**grant_reason** | **str** |  | [optional] [default to 'Granted from ARC Communications Settings']

## Example

```python
from moolabs.models.arc_dunning_template_admin_grant_request import ArcDunningTemplateAdminGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningTemplateAdminGrantRequest from a JSON string
arc_dunning_template_admin_grant_request_instance = ArcDunningTemplateAdminGrantRequest.from_json(json)
# print the JSON string representation of the object
print(ArcDunningTemplateAdminGrantRequest.to_json())

# convert the object into a dict
arc_dunning_template_admin_grant_request_dict = arc_dunning_template_admin_grant_request_instance.to_dict()
# create an instance of ArcDunningTemplateAdminGrantRequest from a dict
arc_dunning_template_admin_grant_request_from_dict = ArcDunningTemplateAdminGrantRequest.from_dict(arc_dunning_template_admin_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


