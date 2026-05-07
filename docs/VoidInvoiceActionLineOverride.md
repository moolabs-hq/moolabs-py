# VoidInvoiceActionLineOverride

VoidInvoiceLineOverride describes how to handle a specific line item in the invoice when voiding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **str** | The line item ID to override. | 
**action** | [**VoidInvoiceActionCreateItem**](VoidInvoiceActionCreateItem.md) | The action to take on the line item. | 

## Example

```python
from moolabs.models.void_invoice_action_line_override import VoidInvoiceActionLineOverride

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInvoiceActionLineOverride from a JSON string
void_invoice_action_line_override_instance = VoidInvoiceActionLineOverride.from_json(json)
# print the JSON string representation of the object
print(VoidInvoiceActionLineOverride.to_json())

# convert the object into a dict
void_invoice_action_line_override_dict = void_invoice_action_line_override_instance.to_dict()
# create an instance of VoidInvoiceActionLineOverride from a dict
void_invoice_action_line_override_from_dict = VoidInvoiceActionLineOverride.from_dict(void_invoice_action_line_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


