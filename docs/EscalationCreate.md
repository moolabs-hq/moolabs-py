# EscalationCreate

POST /cases/{case_id}/escalations — create an escalation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**escalated_to** | **str** |  | [optional] 
**escalated_from** | **str** |  | [optional] 
**priority** | **str** | low, medium, high, critical | [optional] [default to 'medium']
**sla_deadline** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.escalation_create import EscalationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationCreate from a JSON string
escalation_create_instance = EscalationCreate.from_json(json)
# print the JSON string representation of the object
print(EscalationCreate.to_json())

# convert the object into a dict
escalation_create_dict = escalation_create_instance.to_dict()
# create an instance of EscalationCreate from a dict
escalation_create_from_dict = EscalationCreate.from_dict(escalation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


