# CreditMemoItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**netsuite_id** | **str** |  | 
**customer_internal_id** | **str** |  | 
**foreign_total** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**tran_date** | **str** |  | [optional] 
**ns_last_modified** | **datetime** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.credit_memo_item import CreditMemoItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreditMemoItem from a JSON string
credit_memo_item_instance = CreditMemoItem.from_json(json)
# print the JSON string representation of the object
print(CreditMemoItem.to_json())

# convert the object into a dict
credit_memo_item_dict = credit_memo_item_instance.to_dict()
# create an instance of CreditMemoItem from a dict
credit_memo_item_from_dict = CreditMemoItem.from_dict(credit_memo_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


