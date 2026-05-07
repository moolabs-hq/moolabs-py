# CustomInvoicingFinalizedRequest

Information to finalize the invoice.  If invoicing.invoiceNumber is not set, then a new invoice number will be generated (INV- prefix).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoicing** | [**CustomInvoicingFinalizedInvoicingRequest**](CustomInvoicingFinalizedInvoicingRequest.md) | The result of the synchronization. | [optional] 
**payment** | [**CustomInvoicingFinalizedPaymentRequest**](CustomInvoicingFinalizedPaymentRequest.md) | The result of the payment synchronization. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_finalized_request import CustomInvoicingFinalizedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingFinalizedRequest from a JSON string
custom_invoicing_finalized_request_instance = CustomInvoicingFinalizedRequest.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingFinalizedRequest.to_json())

# convert the object into a dict
custom_invoicing_finalized_request_dict = custom_invoicing_finalized_request_instance.to_dict()
# create an instance of CustomInvoicingFinalizedRequest from a dict
custom_invoicing_finalized_request_from_dict = CustomInvoicingFinalizedRequest.from_dict(custom_invoicing_finalized_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


