# InvoiceGenericDocumentRef

Omitted fields: period: Tax period in which the referred document had an effect required by some tax regimes and formats. stamps: Seals of approval from other organisations that may need to be listed. ext:  Extensions for additional codes that may be required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**InvoiceDocumentRefType**](InvoiceDocumentRefType.md) | Type of the document referenced. | [readonly] 
**reason** | **str** | Human readable description on why this reference is here or needs to be used. | [optional] [readonly] 
**description** | **str** | Additional details about the document. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_generic_document_ref import InvoiceGenericDocumentRef

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceGenericDocumentRef from a JSON string
invoice_generic_document_ref_instance = InvoiceGenericDocumentRef.from_json(json)
# print the JSON string representation of the object
print(InvoiceGenericDocumentRef.to_json())

# convert the object into a dict
invoice_generic_document_ref_dict = invoice_generic_document_ref_instance.to_dict()
# create an instance of InvoiceGenericDocumentRef from a dict
invoice_generic_document_ref_from_dict = InvoiceGenericDocumentRef.from_dict(invoice_generic_document_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


