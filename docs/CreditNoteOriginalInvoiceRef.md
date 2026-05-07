# CreditNoteOriginalInvoiceRef

CreditNoteOriginalInvoiceRef is used to reference the original invoice that a credit note is based on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the invoice. | 
**issued_at** | **datetime** | IssueAt reflects the time the document was issued. | [optional] [readonly] 
**number** | **str** | (Serial) Number of the referenced document. | [optional] [readonly] 
**url** | **str** | Link to the source document. | [readonly] 
**reason** | **str** | Human readable description on why this reference is here or needs to be used. | [optional] [readonly] 
**description** | **str** | Additional details about the document. | [optional] [readonly] 

## Example

```python
from moolabs.models.credit_note_original_invoice_ref import CreditNoteOriginalInvoiceRef

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteOriginalInvoiceRef from a JSON string
credit_note_original_invoice_ref_instance = CreditNoteOriginalInvoiceRef.from_json(json)
# print the JSON string representation of the object
print(CreditNoteOriginalInvoiceRef.to_json())

# convert the object into a dict
credit_note_original_invoice_ref_dict = credit_note_original_invoice_ref_instance.to_dict()
# create an instance of CreditNoteOriginalInvoiceRef from a dict
credit_note_original_invoice_ref_from_dict = CreditNoteOriginalInvoiceRef.from_dict(credit_note_original_invoice_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


