# AutoTopupRuleResponse

Response from creating an auto top-up rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**pool_id** | **str** |  | 
**wallet_id** | **str** |  | 
**trigger_type** | **str** |  | 
**trigger_value** | **str** |  | 
**topup_amount_micros** | **int** |  | 
**topup_cooldown_seconds** | **int** |  | 
**max_topups_per_day** | **int** |  | 
**payment_method_ref** | **str** |  | 
**invoice_mode** | **str** |  | 
**enabled** | **bool** |  | [optional] [default to True]
**last_triggered_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.auto_topup_rule_response import AutoTopupRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTopupRuleResponse from a JSON string
auto_topup_rule_response_instance = AutoTopupRuleResponse.from_json(json)
# print the JSON string representation of the object
print(AutoTopupRuleResponse.to_json())

# convert the object into a dict
auto_topup_rule_response_dict = auto_topup_rule_response_instance.to_dict()
# create an instance of AutoTopupRuleResponse from a dict
auto_topup_rule_response_from_dict = AutoTopupRuleResponse.from_dict(auto_topup_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


