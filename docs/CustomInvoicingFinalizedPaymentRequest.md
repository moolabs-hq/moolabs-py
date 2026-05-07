# CustomInvoicingFinalizedPaymentRequest

Information to finalize the payment details of an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | If set the invoice&#39;s payment external ID will be set to this value. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_finalized_payment_request import CustomInvoicingFinalizedPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingFinalizedPaymentRequest from a JSON string
custom_invoicing_finalized_payment_request_instance = CustomInvoicingFinalizedPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingFinalizedPaymentRequest.to_json())

# convert the object into a dict
custom_invoicing_finalized_payment_request_dict = custom_invoicing_finalized_payment_request_instance.to_dict()
# create an instance of CustomInvoicingFinalizedPaymentRequest from a dict
custom_invoicing_finalized_payment_request_from_dict = CustomInvoicingFinalizedPaymentRequest.from_dict(custom_invoicing_finalized_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


