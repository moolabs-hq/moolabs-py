# EscalationResolveRequest

POST /cases/{case_id}/escalations/{id}/resolve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_notes** | **str** |  | [optional] 

## Example

```python
from moolabs.models.escalation_resolve_request import EscalationResolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationResolveRequest from a JSON string
escalation_resolve_request_instance = EscalationResolveRequest.from_json(json)
# print the JSON string representation of the object
print(EscalationResolveRequest.to_json())

# convert the object into a dict
escalation_resolve_request_dict = escalation_resolve_request_instance.to_dict()
# create an instance of EscalationResolveRequest from a dict
escalation_resolve_request_from_dict = EscalationResolveRequest.from_dict(escalation_resolve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


