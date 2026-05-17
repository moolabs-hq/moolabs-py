# BudgetWithUtilization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**budget_name** | **str** |  | 
**scope_type** | **str** |  | 
**scope_id** | **str** |  | 
**period_type** | **str** |  | 
**budget_amount** | **str** |  | 
**currency** | **str** |  | 
**alert_thresholds** | **List[int]** |  | 
**notify_channels** | **List[object]** |  | 
**is_active** | **bool** |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**current_spend** | **str** |  | [optional] 
**utilization_pct** | **str** |  | [optional] 
**loaded_margin_available** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.budget_with_utilization import BudgetWithUtilization

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetWithUtilization from a JSON string
budget_with_utilization_instance = BudgetWithUtilization.from_json(json)
# print the JSON string representation of the object
print(BudgetWithUtilization.to_json())

# convert the object into a dict
budget_with_utilization_dict = budget_with_utilization_instance.to_dict()
# create an instance of BudgetWithUtilization from a dict
budget_with_utilization_from_dict = BudgetWithUtilization.from_dict(budget_with_utilization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


