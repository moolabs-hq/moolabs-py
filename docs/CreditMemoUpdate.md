# CreditMemoUpdate

PATCH /credit-memos/{id} — update (draft only).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_number** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**credit_amount_micros** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from moolabs.models.credit_memo_update import CreditMemoUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoUpdate from a JSON string
credit_memo_update_instance = CreditMemoUpdate.from_json(json)
# print the JSON string representation of the object
print(CreditMemoUpdate.to_json())

# convert the object into a dict
credit_memo_update_dict = credit_memo_update_instance.to_dict()
# create an instance of CreditMemoUpdate from a dict
credit_memo_update_from_dict = CreditMemoUpdate.from_dict(credit_memo_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


