# ArcDunningTemplateAdminRevokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoke_reason** | **str** |  | [optional] [default to 'Revoked from ARC Communications Settings']

## Example

```python
from moolabs.models.arc_dunning_template_admin_revoke_request import ArcDunningTemplateAdminRevokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArcDunningTemplateAdminRevokeRequest from a JSON string
arc_dunning_template_admin_revoke_request_instance = ArcDunningTemplateAdminRevokeRequest.from_json(json)
# print the JSON string representation of the object
print(ArcDunningTemplateAdminRevokeRequest.to_json())

# convert the object into a dict
arc_dunning_template_admin_revoke_request_dict = arc_dunning_template_admin_revoke_request_instance.to_dict()
# create an instance of ArcDunningTemplateAdminRevokeRequest from a dict
arc_dunning_template_admin_revoke_request_from_dict = ArcDunningTemplateAdminRevokeRequest.from_dict(arc_dunning_template_admin_revoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


