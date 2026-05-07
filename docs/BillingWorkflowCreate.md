# BillingWorkflowCreate

Resource create operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**BillingWorkflowCollectionSettings**](BillingWorkflowCollectionSettings.md) | The collection settings for this workflow | [optional] 
**invoicing** | [**BillingWorkflowInvoicingSettings**](BillingWorkflowInvoicingSettings.md) | The invoicing settings for this workflow | [optional] 
**payment** | [**BillingWorkflowPaymentSettings**](BillingWorkflowPaymentSettings.md) | The payment settings for this workflow | [optional] 
**tax** | [**BillingWorkflowTaxSettings**](BillingWorkflowTaxSettings.md) | The tax settings for this workflow | [optional] 

## Example

```python
from moolabs.models.billing_workflow_create import BillingWorkflowCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowCreate from a JSON string
billing_workflow_create_instance = BillingWorkflowCreate.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowCreate.to_json())

# convert the object into a dict
billing_workflow_create_dict = billing_workflow_create_instance.to_dict()
# create an instance of BillingWorkflowCreate from a dict
billing_workflow_create_from_dict = BillingWorkflowCreate.from_dict(billing_workflow_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


