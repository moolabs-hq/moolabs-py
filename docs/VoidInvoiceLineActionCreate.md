# VoidInvoiceLineActionCreate

VoidInvoiceLineAction describes how to handle a specific line item in the invoice when voiding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action to take on the line item. | 
**next_invoice_at** | **datetime** | The time at which the line item should be invoiced again.  If not provided, the line item will be re-invoiced now. | [optional] 

## Example

```python
from moolabs.models.void_invoice_line_action_create import VoidInvoiceLineActionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInvoiceLineActionCreate from a JSON string
void_invoice_line_action_create_instance = VoidInvoiceLineActionCreate.from_json(json)
# print the JSON string representation of the object
print(VoidInvoiceLineActionCreate.to_json())

# convert the object into a dict
void_invoice_line_action_create_dict = void_invoice_line_action_create_instance.to_dict()
# create an instance of VoidInvoiceLineActionCreate from a dict
void_invoice_line_action_create_from_dict = VoidInvoiceLineActionCreate.from_dict(void_invoice_line_action_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


