# VoidInvoiceActionCreate

InvoiceVoidAction describes how to handle the voided line items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** | How much of the total line items to be voided? (e.g. 100% means all charges are voided) | 
**action** | [**VoidInvoiceLineActionCreate**](VoidInvoiceLineActionCreate.md) | The action to take on the line items. | 

## Example

```python
from moolabs.models.void_invoice_action_create import VoidInvoiceActionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInvoiceActionCreate from a JSON string
void_invoice_action_create_instance = VoidInvoiceActionCreate.from_json(json)
# print the JSON string representation of the object
print(VoidInvoiceActionCreate.to_json())

# convert the object into a dict
void_invoice_action_create_dict = void_invoice_action_create_instance.to_dict()
# create an instance of VoidInvoiceActionCreate from a dict
void_invoice_action_create_from_dict = VoidInvoiceActionCreate.from_dict(void_invoice_action_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


