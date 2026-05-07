# PlanPhase

The plan phase or pricing ramp allows changing a plan's rate cards over time as a subscription progresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A semi-unique identifier for the resource. | 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**duration** | **str** | The duration of the phase. | 
**rate_cards** | [**List[RateCard]**](RateCard.md) | The rate cards of the plan. | 

## Example

```python
from moolabs.models.plan_phase import PlanPhase

# TODO update the JSON string below
json = "{}"
# create an instance of PlanPhase from a JSON string
plan_phase_instance = PlanPhase.from_json(json)
# print the JSON string representation of the object
print(PlanPhase.to_json())

# convert the object into a dict
plan_phase_dict = plan_phase_instance.to_dict()
# create an instance of PlanPhase from a dict
plan_phase_from_dict = PlanPhase.from_dict(plan_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


