# BillingWorkflow

BillingWorkflow represents the settings for a billing workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**BillingWorkflowCollectionSettings**](BillingWorkflowCollectionSettings.md) | The collection settings for this workflow | [optional] 
**invoicing** | [**BillingWorkflowInvoicingSettings**](BillingWorkflowInvoicingSettings.md) | The invoicing settings for this workflow | [optional] 
**payment** | [**BillingWorkflowPaymentSettings**](BillingWorkflowPaymentSettings.md) | The payment settings for this workflow | [optional] 
**tax** | [**BillingWorkflowTaxSettings**](BillingWorkflowTaxSettings.md) | The tax settings for this workflow | [optional] 

## Example

```python
from moolabs.models.billing_workflow import BillingWorkflow

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflow from a JSON string
billing_workflow_instance = BillingWorkflow.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflow.to_json())

# convert the object into a dict
billing_workflow_dict = billing_workflow_instance.to_dict()
# create an instance of BillingWorkflow from a dict
billing_workflow_from_dict = BillingWorkflow.from_dict(billing_workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


