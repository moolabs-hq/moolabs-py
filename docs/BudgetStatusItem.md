# BudgetStatusItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_id** | **str** |  | 
**budget_name** | **str** |  | 
**scope_type** | **str** |  | 
**scope_id** | **str** |  | 
**budget_amount** | **str** |  | 
**currency** | **str** |  | 
**current_spend** | **str** |  | 
**utilization_pct** | **str** |  | 
**is_active** | **bool** |  | 
**active_alerts** | **int** |  | 

## Example

```python
from moolabs.models.budget_status_item import BudgetStatusItem

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetStatusItem from a JSON string
budget_status_item_instance = BudgetStatusItem.from_json(json)
# print the JSON string representation of the object
print(BudgetStatusItem.to_json())

# convert the object into a dict
budget_status_item_dict = budget_status_item_instance.to_dict()
# create an instance of BudgetStatusItem from a dict
budget_status_item_from_dict = BudgetStatusItem.from_dict(budget_status_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


