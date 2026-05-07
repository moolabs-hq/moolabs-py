# InvoicePendingLineCreateInput

InvoicePendingLineCreate represents the create model for a pending invoice line.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the lines to be created. | 
**lines** | [**List[InvoicePendingLineCreate]**](InvoicePendingLineCreate.md) | The lines to be created. | 

## Example

```python
from moolabs.models.invoice_pending_line_create_input import InvoicePendingLineCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePendingLineCreateInput from a JSON string
invoice_pending_line_create_input_instance = InvoicePendingLineCreateInput.from_json(json)
# print the JSON string representation of the object
print(InvoicePendingLineCreateInput.to_json())

# convert the object into a dict
invoice_pending_line_create_input_dict = invoice_pending_line_create_input_instance.to_dict()
# create an instance of InvoicePendingLineCreateInput from a dict
invoice_pending_line_create_input_from_dict = InvoicePendingLineCreateInput.from_dict(invoice_pending_line_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


