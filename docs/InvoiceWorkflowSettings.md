# InvoiceWorkflowSettings

InvoiceWorkflowSettings represents the workflow settings used by the invoice.  This is a clone of the billing profile's workflow settings at the time of invoice creation with customer overrides considered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**BillingProfileAppsOrReference**](BillingProfileAppsOrReference.md) | The apps that will be used to orchestrate the invoice&#39;s workflow. | [optional] [readonly] 
**source_billing_profile_id** | **str** | sourceBillingProfileID is the billing profile on which the workflow was based on.  The profile is snapshotted on invoice creation, after which it can be altered independently of the profile itself. | [readonly] 
**workflow** | [**BillingWorkflow**](BillingWorkflow.md) | The workflow details used by this invoice. | 

## Example

```python
from moolabs.models.invoice_workflow_settings import InvoiceWorkflowSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceWorkflowSettings from a JSON string
invoice_workflow_settings_instance = InvoiceWorkflowSettings.from_json(json)
# print the JSON string representation of the object
print(InvoiceWorkflowSettings.to_json())

# convert the object into a dict
invoice_workflow_settings_dict = invoice_workflow_settings_instance.to_dict()
# create an instance of InvoiceWorkflowSettings from a dict
invoice_workflow_settings_from_dict = InvoiceWorkflowSettings.from_dict(invoice_workflow_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


