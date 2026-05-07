# InvoiceReference

Reference to an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the invoice. | [readonly] 
**number** | **str** | The number of the invoice. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_reference import InvoiceReference

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReference from a JSON string
invoice_reference_instance = InvoiceReference.from_json(json)
# print the JSON string representation of the object
print(InvoiceReference.to_json())

# convert the object into a dict
invoice_reference_dict = invoice_reference_instance.to_dict()
# create an instance of InvoiceReference from a dict
invoice_reference_from_dict = InvoiceReference.from_dict(invoice_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


