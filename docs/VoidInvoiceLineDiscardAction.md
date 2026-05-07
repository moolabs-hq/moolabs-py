# VoidInvoiceLineDiscardAction

VoidInvoiceLineDiscardAction describes how to handle the voidied line item in the invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action to take on the line item. | 

## Example

```python
from moolabs.models.void_invoice_line_discard_action import VoidInvoiceLineDiscardAction

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInvoiceLineDiscardAction from a JSON string
void_invoice_line_discard_action_instance = VoidInvoiceLineDiscardAction.from_json(json)
# print the JSON string representation of the object
print(VoidInvoiceLineDiscardAction.to_json())

# convert the object into a dict
void_invoice_line_discard_action_dict = void_invoice_line_discard_action_instance.to_dict()
# create an instance of VoidInvoiceLineDiscardAction from a dict
void_invoice_line_discard_action_from_dict = VoidInvoiceLineDiscardAction.from_dict(void_invoice_line_discard_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


