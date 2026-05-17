# TenantEscalationConfigPatch

Sparse partial config to deep-merge over the existing row.  ``change_reason`` is required so the audit history is meaningful.  Note: ``updated_by_user_id`` is intentionally NOT a body field — it's resolved server-side from the authenticated request context (``X-User-Id`` header / future JWT claim) to prevent forgery of audit attribution (Issue C3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** | Sparse partial config | 
**change_reason** | **str** |  | 
**change_label** | **str** |  | [optional] 

## Example

```python
from moolabs.models.tenant_escalation_config_patch import TenantEscalationConfigPatch

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEscalationConfigPatch from a JSON string
tenant_escalation_config_patch_instance = TenantEscalationConfigPatch.from_json(json)
# print the JSON string representation of the object
print(TenantEscalationConfigPatch.to_json())

# convert the object into a dict
tenant_escalation_config_patch_dict = tenant_escalation_config_patch_instance.to_dict()
# create an instance of TenantEscalationConfigPatch from a dict
tenant_escalation_config_patch_from_dict = TenantEscalationConfigPatch.from_dict(tenant_escalation_config_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


