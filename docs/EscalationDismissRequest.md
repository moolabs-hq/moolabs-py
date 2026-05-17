# EscalationDismissRequest

POST /cases/{case_id}/escalations/{id}/dismiss (Spec B Task 10).  ``hard=True`` additionally stamps ``case.escalation_no_response_fired_at = now()`` so the no-response detector won't immediately re-fire on the same case (operator said \"don't bug me about this one\").  ``hard=False`` (default) is a one-off dismissal — the next agent tick is free to re-raise if conditions persist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**hard** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.escalation_dismiss_request import EscalationDismissRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationDismissRequest from a JSON string
escalation_dismiss_request_instance = EscalationDismissRequest.from_json(json)
# print the JSON string representation of the object
print(EscalationDismissRequest.to_json())

# convert the object into a dict
escalation_dismiss_request_dict = escalation_dismiss_request_instance.to_dict()
# create an instance of EscalationDismissRequest from a dict
escalation_dismiss_request_from_dict = EscalationDismissRequest.from_dict(escalation_dismiss_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


