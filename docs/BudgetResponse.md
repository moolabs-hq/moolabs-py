# BudgetResponse


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

## Example

```python
from moolabs.models.budget_response import BudgetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetResponse from a JSON string
budget_response_instance = BudgetResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetResponse.to_json())

# convert the object into a dict
budget_response_dict = budget_response_instance.to_dict()
# create an instance of BudgetResponse from a dict
budget_response_from_dict = BudgetResponse.from_dict(budget_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


