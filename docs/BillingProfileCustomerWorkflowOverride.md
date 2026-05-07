# BillingProfileCustomerWorkflowOverride

Customer specific workflow overrides.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**BillingWorkflowCollectionSettings**](BillingWorkflowCollectionSettings.md) | The collection settings for this workflow | [optional] 
**invoicing** | [**BillingWorkflowInvoicingSettings**](BillingWorkflowInvoicingSettings.md) | The invoicing settings for this workflow | [optional] 
**payment** | [**BillingWorkflowPaymentSettings**](BillingWorkflowPaymentSettings.md) | The payment settings for this workflow | [optional] 
**tax** | [**BillingWorkflowTaxSettings**](BillingWorkflowTaxSettings.md) | The tax settings for this workflow | [optional] 
**tax_app** | [**AppReadOrCreateOrUpdateOrDeleteOrQuery**](AppReadOrCreateOrUpdateOrDeleteOrQuery.md) | The tax app used for this workflow | [readonly] 
**invoicing_app** | [**AppReadOrCreateOrUpdateOrDeleteOrQuery**](AppReadOrCreateOrUpdateOrDeleteOrQuery.md) | The invoicing app used for this workflow | [readonly] 
**payment_app** | [**AppReadOrCreateOrUpdateOrDeleteOrQuery**](AppReadOrCreateOrUpdateOrDeleteOrQuery.md) | The payment app used for this workflow | [readonly] 

## Example

```python
from moolabs.models.billing_profile_customer_workflow_override import BillingProfileCustomerWorkflowOverride

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCustomerWorkflowOverride from a JSON string
billing_profile_customer_workflow_override_instance = BillingProfileCustomerWorkflowOverride.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCustomerWorkflowOverride.to_json())

# convert the object into a dict
billing_profile_customer_workflow_override_dict = billing_profile_customer_workflow_override_instance.to_dict()
# create an instance of BillingProfileCustomerWorkflowOverride from a dict
billing_profile_customer_workflow_override_from_dict = BillingProfileCustomerWorkflowOverride.from_dict(billing_profile_customer_workflow_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


