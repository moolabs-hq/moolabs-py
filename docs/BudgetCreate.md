# BudgetCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_name** | **str** |  | 
**scope_type** | **str** | &#39;tenant&#39;, &#39;customer&#39;, &#39;feature&#39;, &#39;cloud_provider&#39; | 
**scope_id** | **str** |  | [optional] 
**period_type** | **str** |  | [optional] [default to 'monthly']
**budget_amount** | [**BudgetAmount**](BudgetAmount.md) |  | 
**currency** | **str** |  | [optional] [default to 'USD']
**alert_thresholds** | **List[int]** |  | [optional] 
**notify_channels** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**created_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.budget_create import BudgetCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetCreate from a JSON string
budget_create_instance = BudgetCreate.from_json(json)
# print the JSON string representation of the object
print(BudgetCreate.to_json())

# convert the object into a dict
budget_create_dict = budget_create_instance.to_dict()
# create an instance of BudgetCreate from a dict
budget_create_from_dict = BudgetCreate.from_dict(budget_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


