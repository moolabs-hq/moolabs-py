# Invoice

Invoice represents an invoice in the system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**type** | [**InvoiceType**](InvoiceType.md) | Type of the invoice.  The type of invoice determines the purpose of the invoice and how it should be handled.  Supported types: - standard: A regular commercial invoice document between a supplier and customer. - credit_note: Reflects a refund either partial or complete of the preceding document. A credit note effectively *extends* the previous document. | [readonly] 
**supplier** | [**BillingParty**](BillingParty.md) | The taxable entity supplying the goods or services. | 
**customer** | [**BillingInvoiceCustomerExtendedDetails**](BillingInvoiceCustomerExtendedDetails.md) | Legal entity receiving the goods or services. | 
**number** | **str** | Number specifies the human readable key used to reference this Invoice.  The invoice number can change in the draft phases, as we are allocating temporary draft invoice numbers, but it&#39;s final as soon as the invoice gets finalized (issued state).  Please note that the number is (depending on the upstream settings) either unique for the whole organization or unique for the customer, or in multi (stripe) account setups unique for the account. | [readonly] 
**currency** | **str** | Currency for all invoice line items.  Multi currency invoices are not supported yet. | 
**preceding** | [**List[CreditNoteOriginalInvoiceRef]**](CreditNoteOriginalInvoiceRef.md) | Key information regarding previous invoices and potentially details as to why they were corrected. | [optional] 
**totals** | [**InvoiceTotals**](InvoiceTotals.md) | Summary of all the invoice totals, including taxes (calculated). | [readonly] 
**status** | [**InvoiceStatus**](InvoiceStatus.md) | The status of the invoice.  This field only conatins a simplified status, for more detailed information use the statusDetails field. | [readonly] 
**status_details** | [**InvoiceStatusDetails**](InvoiceStatusDetails.md) | The details of the current invoice status. | [readonly] 
**issued_at** | **datetime** | The time the invoice was issued.  Depending on the status of the invoice this can mean multiple things: - draft, gathering: The time the invoice will be issued based on the workflow settings. - issued: The time the invoice was issued. | [optional] [readonly] 
**draft_until** | **datetime** | The time until the invoice is in draft status.  On draft invoice creation it is calculated from the workflow settings.  If manual approval is required, the draftUntil time is set. | [optional] 
**quantity_snapshoted_at** | **datetime** | The time when the quantity snapshots on the invoice lines were taken. | [optional] [readonly] 
**collection_at** | **datetime** | The time when the invoice will be/has been collected. | [optional] [readonly] 
**due_at** | **datetime** | Due time of the fulfillment of the invoice (if available). | [optional] [readonly] 
**period** | [**Period**](Period.md) | The period the invoice covers. If the invoice has no line items, it&#39;s not set. | [optional] 
**voided_at** | **datetime** | The time the invoice was voided.  If the invoice was voided, this field will be set to the time the invoice was voided. | [optional] [readonly] 
**sent_to_customer_at** | **datetime** | The time the invoice was sent to customer. | [optional] [readonly] 
**workflow** | [**InvoiceWorkflowSettings**](InvoiceWorkflowSettings.md) | The workflow associated with the invoice.  It is always a snapshot of the workflow settings at the time of invoice creation. The field is optional as it should be explicitly requested with expand options. | 
**lines** | [**List[InvoiceLine]**](InvoiceLine.md) | List of invoice lines representing each of the items sold to the customer. | [optional] 
**payment** | [**InvoicePaymentTerms**](InvoicePaymentTerms.md) | Information on when, how, and to whom the invoice should be paid. | [optional] [readonly] 
**validation_issues** | [**List[ValidationIssue]**](ValidationIssue.md) | Validation issues reported by the invoice workflow. | [optional] 
**external_ids** | [**InvoiceAppExternalIds**](InvoiceAppExternalIds.md) | External IDs of the invoice in other apps such as Stripe. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print(Invoice.to_json())

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_from_dict = Invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


