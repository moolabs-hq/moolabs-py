# UpdateAutoTopupRuleRequest

Request to update an auto top-up rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_type** | **str** |  | [optional] 
**trigger_value** | **str** |  | [optional] 
**topup_amount_micros** | **int** |  | [optional] 
**topup_cooldown_seconds** | **int** |  | [optional] 
**max_topups_per_day** | **int** |  | [optional] 
**payment_method_ref** | **str** |  | [optional] 
**invoice_mode** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from moolabs.models.update_auto_topup_rule_request import UpdateAutoTopupRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutoTopupRuleRequest from a JSON string
update_auto_topup_rule_request_instance = UpdateAutoTopupRuleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAutoTopupRuleRequest.to_json())

# convert the object into a dict
update_auto_topup_rule_request_dict = update_auto_topup_rule_request_instance.to_dict()
# create an instance of UpdateAutoTopupRuleRequest from a dict
update_auto_topup_rule_request_from_dict = UpdateAutoTopupRuleRequest.from_dict(update_auto_topup_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


