# BudgetAlertResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**budget_id** | **str** |  | 
**threshold_pct** | **int** |  | 
**current_spend** | **str** |  | 
**utilization_pct** | **str** |  | 
**alert_action** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**fired_at** | **str** |  | 
**acknowledged_at** | **str** |  | 

## Example

```python
from moolabs.models.budget_alert_response import BudgetAlertResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetAlertResponse from a JSON string
budget_alert_response_instance = BudgetAlertResponse.from_json(json)
# print the JSON string representation of the object
print(BudgetAlertResponse.to_json())

# convert the object into a dict
budget_alert_response_dict = budget_alert_response_instance.to_dict()
# create an instance of BudgetAlertResponse from a dict
budget_alert_response_from_dict = BudgetAlertResponse.from_dict(budget_alert_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


