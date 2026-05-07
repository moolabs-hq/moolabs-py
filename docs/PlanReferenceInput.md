# PlanReferenceInput

References an exact plan defaulting to the current active version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The plan key. | 
**version** | **int** | The plan version. | [optional] 

## Example

```python
from moolabs.models.plan_reference_input import PlanReferenceInput

# TODO update the JSON string below
json = "{}"
# create an instance of PlanReferenceInput from a JSON string
plan_reference_input_instance = PlanReferenceInput.from_json(json)
# print the JSON string representation of the object
print(PlanReferenceInput.to_json())

# convert the object into a dict
plan_reference_input_dict = plan_reference_input_instance.to_dict()
# create an instance of PlanReferenceInput from a dict
plan_reference_input_from_dict = PlanReferenceInput.from_dict(plan_reference_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


