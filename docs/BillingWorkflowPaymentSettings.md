# BillingWorkflowPaymentSettings

BillingWorkflowPaymentSettings represents the payment settings for a billing workflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_method** | [**CollectionMethod**](CollectionMethod.md) | The payment method for the invoice. | [optional] 

## Example

```python
from moolabs.models.billing_workflow_payment_settings import BillingWorkflowPaymentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BillingWorkflowPaymentSettings from a JSON string
billing_workflow_payment_settings_instance = BillingWorkflowPaymentSettings.from_json(json)
# print the JSON string representation of the object
print(BillingWorkflowPaymentSettings.to_json())

# convert the object into a dict
billing_workflow_payment_settings_dict = billing_workflow_payment_settings_instance.to_dict()
# create an instance of BillingWorkflowPaymentSettings from a dict
billing_workflow_payment_settings_from_dict = BillingWorkflowPaymentSettings.from_dict(billing_workflow_payment_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


