# BillingWorkflowInvoicingSettings

BillingWorkflowInvoicingSettings represents the invoice settings for a billing workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_advance** | **bool** | Whether to automatically issue the invoice after the draftPeriod has passed. | [optional] [default to True]
**draft_period** | **str** | The period for the invoice to be kept in draft status for manual reviews. | [optional] [default to 'P0D']
**due_after** | **str** | The period after which the invoice is due. With some payment solutions it&#39;s only applicable for manual collection method. | [optional] [default to 'P30D']
**progressive_billing** | **bool** | Should progressive billing be allowed for this workflow? | [optional] [default to False]
**default_tax_config** | [**TaxConfig**](TaxConfig.md) | Default tax configuration to apply to the invoices. | [optional] 

## Example

```python
from moolabs.models.billing_workflow_invoicing_settings import BillingWorkflowInvoicingSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowInvoicingSettings from a JSON string
billing_workflow_invoicing_settings_instance = BillingWorkflowInvoicingSettings.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowInvoicingSettings.to_json())

# convert the object into a dict
billing_workflow_invoicing_settings_dict = billing_workflow_invoicing_settings_instance.to_dict()
# create an instance of BillingWorkflowInvoicingSettings from a dict
billing_workflow_invoicing_settings_from_dict = BillingWorkflowInvoicingSettings.from_dict(billing_workflow_invoicing_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


