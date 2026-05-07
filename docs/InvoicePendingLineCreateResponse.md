# InvoicePendingLineCreateResponse

InvoicePendingLineCreateResponse represents the response from the create pending line endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[InvoiceLine]**](InvoiceLine.md) | The lines that were created. | 
**invoice** | [**Invoice**](Invoice.md) | The invoice containing the created lines. | [readonly] 
**is_invoice_new** | **bool** | Whether the invoice was newly created. | [readonly] 

## Example

```python
from moolabs.models.invoice_pending_line_create_response import InvoicePendingLineCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePendingLineCreateResponse from a JSON string
invoice_pending_line_create_response_instance = InvoicePendingLineCreateResponse.from_json(json)
# print the JSON string representation of the object
print(InvoicePendingLineCreateResponse.to_json())

# convert the object into a dict
invoice_pending_line_create_response_dict = invoice_pending_line_create_response_instance.to_dict()
# create an instance of InvoicePendingLineCreateResponse from a dict
invoice_pending_line_create_response_from_dict = InvoicePendingLineCreateResponse.from_dict(invoice_pending_line_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


