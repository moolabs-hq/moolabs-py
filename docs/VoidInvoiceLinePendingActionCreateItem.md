# VoidInvoiceLinePendingActionCreateItem

VoidInvoiceLinePendingAction describes how to handle the voidied line item in the invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action to take on the line item. | 
**next_invoice_at** | **datetime** | The time at which the line item should be invoiced again.  If not provided, the line item will be re-invoiced now. | [optional] 

## Example

```python
from moolabs.models.void_invoice_line_pending_action_create_item import VoidInvoiceLinePendingActionCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInvoiceLinePendingActionCreateItem from a JSON string
void_invoice_line_pending_action_create_item_instance = VoidInvoiceLinePendingActionCreateItem.from_json(json)
# print the JSON string representation of the object
print(VoidInvoiceLinePendingActionCreateItem.to_json())

# convert the object into a dict
void_invoice_line_pending_action_create_item_dict = void_invoice_line_pending_action_create_item_instance.to_dict()
# create an instance of VoidInvoiceLinePendingActionCreateItem from a dict
void_invoice_line_pending_action_create_item_from_dict = VoidInvoiceLinePendingActionCreateItem.from_dict(void_invoice_line_pending_action_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


