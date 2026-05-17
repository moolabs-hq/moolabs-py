# UpdateCreditPoolRequest

Request to update a credit pool (partial; only provided fields are updated).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pool name | [optional] 
**currency** | **str** | Currency code (ISO 4217) | [optional] 
**notification_emails** | **List[str]** | Email addresses for pool-level alerts | [optional] 
**at_cap_behavior** | **str** | Default wallet policy when balance hits cap: SOFT_BORROW | HARD_BUDGET | NOTIFY_ONLY | [optional] 
**threshold_policy** | **str** | Named alert-threshold preset (e.g. Conservative, Standard, Aggressive) | [optional] 
**credit_label** | **str** | Credit unit label (e.g. credits, tokens, points) | [optional] 

## Example

```python
from moolabs.models.update_credit_pool_request import UpdateCreditPoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCreditPoolRequest from a JSON string
update_credit_pool_request_instance = UpdateCreditPoolRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCreditPoolRequest.to_json())

# convert the object into a dict
update_credit_pool_request_dict = update_credit_pool_request_instance.to_dict()
# create an instance of UpdateCreditPoolRequest from a dict
update_credit_pool_request_from_dict = UpdateCreditPoolRequest.from_dict(update_credit_pool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


