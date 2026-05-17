# EscalationActionRequest

POST /v1/arc/escalations/{escalation_id}/actions (Spec B Task 9 / I3).  Operator-clickable card actions dispatched from the EscalationCard. ``action_type`` must be one of the values in :class:`app.models.enums.EscalationActionType`; ``payload`` is the per-action argument bag (validated by the dispatcher).  SECURITY: ``tenant_id`` MUST come from the auth context (``get_tenant_id`` dep) — never from the request body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** |  | 
**payload** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.escalation_action_request import EscalationActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationActionRequest from a JSON string
escalation_action_request_instance = EscalationActionRequest.from_json(json)
# print the JSON string representation of the object
print(EscalationActionRequest.to_json())

# convert the object into a dict
escalation_action_request_dict = escalation_action_request_instance.to_dict()
# create an instance of EscalationActionRequest from a dict
escalation_action_request_from_dict = EscalationActionRequest.from_dict(escalation_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


