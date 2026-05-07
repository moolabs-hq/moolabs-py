# InvoiceWorkflowSettingsReplaceUpdate

Mutable workflow settings for an invoice.  Other fields on the invoice's workflow are not mutable, they serve as a history of the invoice's workflow at creation time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoicing** | [**InvoiceWorkflowInvoicingSettingsReplaceUpdate**](InvoiceWorkflowInvoicingSettingsReplaceUpdate.md) | The invoicing settings for this workflow | 
**payment** | [**BillingWorkflowPaymentSettings**](BillingWorkflowPaymentSettings.md) | The payment settings for this workflow | 

## Example

```python
from moolabs.models.invoice_workflow_settings_replace_update import InvoiceWorkflowSettingsReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceWorkflowSettingsReplaceUpdate from a JSON string
invoice_workflow_settings_replace_update_instance = InvoiceWorkflowSettingsReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(InvoiceWorkflowSettingsReplaceUpdate.to_json())

# convert the object into a dict
invoice_workflow_settings_replace_update_dict = invoice_workflow_settings_replace_update_instance.to_dict()
# create an instance of InvoiceWorkflowSettingsReplaceUpdate from a dict
invoice_workflow_settings_replace_update_from_dict = InvoiceWorkflowSettingsReplaceUpdate.from_dict(invoice_workflow_settings_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


