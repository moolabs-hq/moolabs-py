# TemplateVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**canonical_template_key** | **str** |  | 
**channel** | **str** |  | [optional] [default to 'email']
**version** | **int** |  | 
**status** | **str** |  | 
**draft_group_id** | **str** |  | [optional] 
**draft_state** | **str** |  | [optional] 
**stale_reason** | **str** |  | [optional] 
**base_published_version_id** | **str** |  | [optional] 
**subject_template** | **str** |  | 
**body_template** | **str** |  | 
**content_hash** | **str** |  | 
**validation_snapshot** | **Dict[str, object]** |  | 
**disclosure_policy_hash** | **str** |  | 
**provider_readiness_hash** | **str** |  | 
**payment_instructions_hash** | **str** |  | 
**created_by_actor_id** | **str** |  | 
**created_by_actor_display** | **str** |  | [optional] 
**published_by_actor_id** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] [default to False]
**lock_owner_actor_id** | **str** |  | [optional] 
**lock_owner_display** | **str** |  | [optional] 
**lock_expires_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.template_version_response import TemplateVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionResponse from a JSON string
template_version_response_instance = TemplateVersionResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionResponse.to_json())

# convert the object into a dict
template_version_response_dict = template_version_response_instance.to_dict()
# create an instance of TemplateVersionResponse from a dict
template_version_response_from_dict = TemplateVersionResponse.from_dict(template_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


