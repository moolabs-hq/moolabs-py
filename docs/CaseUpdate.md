# CaseUpdate

PATCH /cases/{id} — partial update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_tier** | **str** |  | [optional] 
**assigned_agent** | **str** |  | [optional] 
**assigned_human** | **str** |  | [optional] 
**case_owner_team** | **str** |  | [optional] 
**autonomy_level** | **int** | Per-case autonomy override (1&#x3D;inform-only, 5&#x3D;fully autonomous). Capped by the orchestrator agent policy&#39;s max_autonomy. | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**status** | **str** | Target case status. Goes through the FSM in case_state.transition_case so an invalid transition (e.g. closed → open without a reason) returns 422. | [optional] 
**status_reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.case_update import CaseUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CaseUpdate from a JSON string
case_update_instance = CaseUpdate.from_json(json)
# print the JSON string representation of the object
print(CaseUpdate.to_json())

# convert the object into a dict
case_update_dict = case_update_instance.to_dict()
# create an instance of CaseUpdate from a dict
case_update_from_dict = CaseUpdate.from_dict(case_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


