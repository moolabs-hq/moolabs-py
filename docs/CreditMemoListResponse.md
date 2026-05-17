# CreditMemoListResponse

GET /credit-memos — paginated list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreditMemoResponse]**](CreditMemoResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from moolabs.models.credit_memo_list_response import CreditMemoListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoListResponse from a JSON string
credit_memo_list_response_instance = CreditMemoListResponse.from_json(json)
# print the JSON string representation of the object
print(CreditMemoListResponse.to_json())

# convert the object into a dict
credit_memo_list_response_dict = credit_memo_list_response_instance.to_dict()
# create an instance of CreditMemoListResponse from a dict
credit_memo_list_response_from_dict = CreditMemoListResponse.from_dict(credit_memo_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


