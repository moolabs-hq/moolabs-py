# InvoicePaymentTerms

Payment contains details as to how the invoice should be paid.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms** | [**PaymentTerms**](PaymentTerms.md) | The terms of payment for the invoice. | [optional] 

## Example

```python
from moolabs.models.invoice_payment_terms import InvoicePaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePaymentTerms from a JSON string
invoice_payment_terms_instance = InvoicePaymentTerms.from_json(json)
# print the JSON string representation of the object
print(InvoicePaymentTerms.to_json())

# convert the object into a dict
invoice_payment_terms_dict = invoice_payment_terms_instance.to_dict()
# create an instance of InvoicePaymentTerms from a dict
invoice_payment_terms_from_dict = InvoicePaymentTerms.from_dict(invoice_payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


