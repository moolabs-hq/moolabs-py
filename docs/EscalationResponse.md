# EscalationResponse

GET /cases/{case_id}/escalations/{id} response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | 
**reason** | **str** |  | 
**escalated_to** | **str** |  | [optional] 
**escalated_from** | **str** |  | [optional] 
**status** | **str** |  | 
**priority** | **str** |  | 
**sla_deadline** | **datetime** |  | [optional] 
**resolved_at** | **datetime** |  | [optional] 
**resolution_notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.escalation_response import EscalationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationResponse from a JSON string
escalation_response_instance = EscalationResponse.from_json(json)
# print the JSON string representation of the object
print(EscalationResponse.to_json())

# convert the object into a dict
escalation_response_dict = escalation_response_instance.to_dict()
# create an instance of EscalationResponse from a dict
escalation_response_from_dict = EscalationResponse.from_dict(escalation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


