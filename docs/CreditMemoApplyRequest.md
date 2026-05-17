# CreditMemoApplyRequest

POST /credit-memos/{id}/apply — apply to an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** |  | 
**amount_micros** | **int** |  | 

## Example

```python
from moolabs.models.credit_memo_apply_request import CreditMemoApplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoApplyRequest from a JSON string
credit_memo_apply_request_instance = CreditMemoApplyRequest.from_json(json)
# print the JSON string representation of the object
print(CreditMemoApplyRequest.to_json())

# convert the object into a dict
credit_memo_apply_request_dict = credit_memo_apply_request_instance.to_dict()
# create an instance of CreditMemoApplyRequest from a dict
credit_memo_apply_request_from_dict = CreditMemoApplyRequest.from_dict(credit_memo_apply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


