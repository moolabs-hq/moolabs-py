# InvoiceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**netsuite_id** | **str** |  | 
**tran_id** | **str** |  | [optional] 
**tran_date** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**customer_internal_id** | **str** |  | 
**foreign_total** | **str** |  | [optional] 
**foreign_amount_unpaid** | **str** |  | [optional] 
**status_label** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**ns_last_modified** | **datetime** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.invoice_item import InvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItem from a JSON string
invoice_item_instance = InvoiceItem.from_json(json)
# print the JSON string representation of the object
print(InvoiceItem.to_json())

# convert the object into a dict
invoice_item_dict = invoice_item_instance.to_dict()
# create an instance of InvoiceItem from a dict
invoice_item_from_dict = InvoiceItem.from_dict(invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


