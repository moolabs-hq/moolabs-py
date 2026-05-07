# BillingWorkflowTaxSettings

BillingWorkflowTaxSettings represents the tax settings for a billing workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable automatic tax calculation when tax is supported by the app. For example, with Stripe Invoicing when enabled, tax is calculated via Stripe Tax. | [optional] [default to True]
**enforced** | **bool** | Enforce tax calculation when tax is supported by the app. When enabled, OpenMeter will not allow to create an invoice without tax calculation. Enforcement is different per apps, for example, Stripe app requires customer to have a tax location when starting a paid subscription. | [optional] [default to False]

## Example

```python
from moolabs.models.billing_workflow_tax_settings import BillingWorkflowTaxSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowTaxSettings from a JSON string
billing_workflow_tax_settings_instance = BillingWorkflowTaxSettings.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowTaxSettings.to_json())

# convert the object into a dict
billing_workflow_tax_settings_dict = billing_workflow_tax_settings_instance.to_dict()
# create an instance of BillingWorkflowTaxSettings from a dict
billing_workflow_tax_settings_from_dict = BillingWorkflowTaxSettings.from_dict(billing_workflow_tax_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


