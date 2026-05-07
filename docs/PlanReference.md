# PlanReference

References an exact plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The plan ID. | 
**key** | **str** | The plan key. | 
**version** | **int** | The plan version. | 

## Example

```python
from moolabs.models.plan_reference import PlanReference

# TODO update the JSON string below
json = "{}"
# create an instance of PlanReference from a JSON string
plan_reference_instance = PlanReference.from_json(json)
# print the JSON string representation of the object
print(PlanReference.to_json())

# convert the object into a dict
plan_reference_dict = plan_reference_instance.to_dict()
# create an instance of PlanReference from a dict
plan_reference_from_dict = PlanReference.from_dict(plan_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


