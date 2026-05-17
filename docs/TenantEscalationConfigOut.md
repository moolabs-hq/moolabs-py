# TenantEscalationConfigOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**config** | **Dict[str, object]** |  | 
**effective_config** | **Dict[str, object]** |  | 
**updated_by_user_id** | **str** |  | 
**change_reason** | **str** |  | 
**has_overrides** | **bool** |  | 

## Example

```python
from moolabs.models.tenant_escalation_config_out import TenantEscalationConfigOut

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEscalationConfigOut from a JSON string
tenant_escalation_config_out_instance = TenantEscalationConfigOut.from_json(json)
# print the JSON string representation of the object
print(TenantEscalationConfigOut.to_json())

# convert the object into a dict
tenant_escalation_config_out_dict = tenant_escalation_config_out_instance.to_dict()
# create an instance of TenantEscalationConfigOut from a dict
tenant_escalation_config_out_from_dict = TenantEscalationConfigOut.from_dict(tenant_escalation_config_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


