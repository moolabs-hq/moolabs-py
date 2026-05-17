# CreditMemoResponse

GET /credit-memos/{id} response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**account_id** | **str** |  | 
**case_id** | **str** |  | [optional] 
**reference_number** | **str** |  | [optional] 
**reason** | **str** |  | 
**status** | **str** |  | 
**credit_amount_micros** | **int** |  | 
**applied_amount_micros** | **int** |  | 
**unapplied_amount_micros** | **int** |  | 
**currency_code** | **str** |  | 
**subsidiary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**approved_by** | **str** |  | [optional] 
**approved_at** | **datetime** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.credit_memo_response import CreditMemoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoResponse from a JSON string
credit_memo_response_instance = CreditMemoResponse.from_json(json)
# print the JSON string representation of the object
print(CreditMemoResponse.to_json())

# convert the object into a dict
credit_memo_response_dict = credit_memo_response_instance.to_dict()
# create an instance of CreditMemoResponse from a dict
credit_memo_response_from_dict = CreditMemoResponse.from_dict(credit_memo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


