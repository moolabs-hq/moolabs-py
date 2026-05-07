# CreateAutoTopupRuleRequest

Request to create an auto top-up rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**wallet_id** | **str** | Wallet identifier | 
**trigger_type** | **str** | Trigger type (STATE or THRESHOLD) | 
**trigger_value** | **str** | Trigger value (e.g., &#39;LOW&#39;, &#39;OVERDRAFT&#39;, &#39;ABS:-100000&#39;) | 
**topup_amount_micros** | **int** | Top-up amount in micros | 
**topup_cooldown_seconds** | **int** | Cooldown period in seconds | [optional] [default to 3600]
**max_topups_per_day** | **int** | Maximum top-ups per day | [optional] [default to 5]
**payment_method_ref** | **str** |  | [optional] 
**invoice_mode** | **str** | Invoice mode | [optional] [default to 'INVOICE_NOW']

## Example

```python
from moolabs.models.create_auto_topup_rule_request import CreateAutoTopupRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutoTopupRuleRequest from a JSON string
create_auto_topup_rule_request_instance = CreateAutoTopupRuleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAutoTopupRuleRequest.to_json())

# convert the object into a dict
create_auto_topup_rule_request_dict = create_auto_topup_rule_request_instance.to_dict()
# create an instance of CreateAutoTopupRuleRequest from a dict
create_auto_topup_rule_request_from_dict = CreateAutoTopupRuleRequest.from_dict(create_auto_topup_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


