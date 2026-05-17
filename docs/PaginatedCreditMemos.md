# PaginatedCreditMemos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreditMemoItem]**](CreditMemoItem.md) |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from moolabs.models.paginated_credit_memos import PaginatedCreditMemos

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCreditMemos from a JSON string
paginated_credit_memos_instance = PaginatedCreditMemos.from_json(json)
# print the JSON string representation of the object
print(PaginatedCreditMemos.to_json())

# convert the object into a dict
paginated_credit_memos_dict = paginated_credit_memos_instance.to_dict()
# create an instance of PaginatedCreditMemos from a dict
paginated_credit_memos_from_dict = PaginatedCreditMemos.from_dict(paginated_credit_memos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


