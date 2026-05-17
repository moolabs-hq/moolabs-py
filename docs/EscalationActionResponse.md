# EscalationActionResponse

POST /v1/arc/escalations/{escalation_id}/actions response.  Mirrors the ``escalation_actions.dispatch_action`` shape so the UI can render success / failure inline on the card without a 500.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**result** | **Dict[str, object]** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from moolabs.models.escalation_action_response import EscalationActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationActionResponse from a JSON string
escalation_action_response_instance = EscalationActionResponse.from_json(json)
# print the JSON string representation of the object
print(EscalationActionResponse.to_json())

# convert the object into a dict
escalation_action_response_dict = escalation_action_response_instance.to_dict()
# create an instance of EscalationActionResponse from a dict
escalation_action_response_from_dict = EscalationActionResponse.from_dict(escalation_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


