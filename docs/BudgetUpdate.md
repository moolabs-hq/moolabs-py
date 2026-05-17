# BudgetUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_name** | **str** |  | [optional] 
**scope_type** | **str** |  | [optional] 
**scope_id** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] 
**budget_amount** | [**BudgetAmount1**](BudgetAmount1.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**alert_thresholds** | **List[int]** |  | [optional] 
**notify_channels** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from moolabs.models.budget_update import BudgetUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUpdate from a JSON string
budget_update_instance = BudgetUpdate.from_json(json)
# print the JSON string representation of the object
print(BudgetUpdate.to_json())

# convert the object into a dict
budget_update_dict = budget_update_instance.to_dict()
# create an instance of BudgetUpdate from a dict
budget_update_from_dict = BudgetUpdate.from_dict(budget_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


