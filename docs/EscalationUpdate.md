# EscalationUpdate

PATCH /cases/{case_id}/escalations/{id} — partial update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escalated_to** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**sla_deadline** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.escalation_update import EscalationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationUpdate from a JSON string
escalation_update_instance = EscalationUpdate.from_json(json)
# print the JSON string representation of the object
print(EscalationUpdate.to_json())

# convert the object into a dict
escalation_update_dict = escalation_update_instance.to_dict()
# create an instance of EscalationUpdate from a dict
escalation_update_from_dict = EscalationUpdate.from_dict(escalation_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


