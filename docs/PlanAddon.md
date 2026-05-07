# PlanAddon

The PlanAddon describes the association between a plan and add-on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**addon** | [**Addon**](Addon.md) | Add-on object. | [readonly] 
**from_plan_phase** | **str** | The key of the plan phase from the add-on becomes available for purchase. | 
**max_quantity** | **int** | The maximum number of times the add-on can be purchased for the plan. It is not applicable for add-ons with single instance type. | [optional] 
**validation_errors** | [**List[MeterValidationError]**](MeterValidationError.md) | List of validation errors. | 

## Example

```python
from moolabs.models.plan_addon import PlanAddon

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAddon from a JSON string
plan_addon_instance = PlanAddon.from_json(json)
# print the JSON string representation of the object
print(PlanAddon.to_json())

# convert the object into a dict
plan_addon_dict = plan_addon_instance.to_dict()
# create an instance of PlanAddon from a dict
plan_addon_from_dict = PlanAddon.from_dict(plan_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


