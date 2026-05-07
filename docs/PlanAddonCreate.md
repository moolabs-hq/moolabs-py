# PlanAddonCreate

A plan add-on assignment create request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**from_plan_phase** | **str** | The key of the plan phase from the add-on becomes available for purchase. | 
**max_quantity** | **int** | The maximum number of times the add-on can be purchased for the plan. It is not applicable for add-ons with single instance type. | [optional] 
**addon_id** | **str** | The add-on unique identifier in ULID format. | 

## Example

```python
from moolabs.models.plan_addon_create import PlanAddonCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAddonCreate from a JSON string
plan_addon_create_instance = PlanAddonCreate.from_json(json)
# print the JSON string representation of the object
print(PlanAddonCreate.to_json())

# convert the object into a dict
plan_addon_create_dict = plan_addon_create_instance.to_dict()
# create an instance of PlanAddonCreate from a dict
plan_addon_create_from_dict = PlanAddonCreate.from_dict(plan_addon_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


