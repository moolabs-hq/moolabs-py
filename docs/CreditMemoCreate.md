# CreditMemoCreate

POST /credit-memos — create a credit memo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**case_id** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reason** | **str** | billing_error, service_credit, commercial_concession, dispute_resolution, pricing_adjustment, other | 
**credit_amount_micros** | **int** |  | 
**currency_code** | **str** |  | 
**subsidiary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.credit_memo_create import CreditMemoCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoCreate from a JSON string
credit_memo_create_instance = CreditMemoCreate.from_json(json)
# print the JSON string representation of the object
print(CreditMemoCreate.to_json())

# convert the object into a dict
credit_memo_create_dict = credit_memo_create_instance.to_dict()
# create an instance of CreditMemoCreate from a dict
credit_memo_create_from_dict = CreditMemoCreate.from_dict(credit_memo_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


