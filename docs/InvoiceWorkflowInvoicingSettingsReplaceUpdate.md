# InvoiceWorkflowInvoicingSettingsReplaceUpdate

InvoiceWorkflowInvoicingSettingsReplaceUpdate represents the update model for the invoicing settings of an invoice workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_advance** | **bool** | Whether to automatically issue the invoice after the draftPeriod has passed. | [optional] [default to True]
**draft_period** | **str** | The period for the invoice to be kept in draft status for manual reviews. | [optional] [default to 'P0D']
**due_after** | **str** | The period after which the invoice is due. With some payment solutions it&#39;s only applicable for manual collection method. | [optional] [default to 'P30D']
**default_tax_config** | [**TaxConfig**](TaxConfig.md) | Default tax configuration to apply to the invoices. | [optional] 

## Example

```python
from moolabs.models.invoice_workflow_invoicing_settings_replace_update import InvoiceWorkflowInvoicingSettingsReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceWorkflowInvoicingSettingsReplaceUpdate from a JSON string
invoice_workflow_invoicing_settings_replace_update_instance = InvoiceWorkflowInvoicingSettingsReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(InvoiceWorkflowInvoicingSettingsReplaceUpdate.to_json())

# convert the object into a dict
invoice_workflow_invoicing_settings_replace_update_dict = invoice_workflow_invoicing_settings_replace_update_instance.to_dict()
# create an instance of InvoiceWorkflowInvoicingSettingsReplaceUpdate from a dict
invoice_workflow_invoicing_settings_replace_update_from_dict = InvoiceWorkflowInvoicingSettingsReplaceUpdate.from_dict(invoice_workflow_invoicing_settings_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


