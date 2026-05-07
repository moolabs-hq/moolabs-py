# CustomInvoicingFinalizedInvoicingRequest

Information to finalize the invoicing details of an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** | If set the invoice&#39;s number will be set to this value. | [optional] 
**sent_to_customer_at** | **datetime** | If set the invoice&#39;s sent to customer at will be set to this value. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_finalized_invoicing_request import CustomInvoicingFinalizedInvoicingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingFinalizedInvoicingRequest from a JSON string
custom_invoicing_finalized_invoicing_request_instance = CustomInvoicingFinalizedInvoicingRequest.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingFinalizedInvoicingRequest.to_json())

# convert the object into a dict
custom_invoicing_finalized_invoicing_request_dict = custom_invoicing_finalized_invoicing_request_instance.to_dict()
# create an instance of CustomInvoicingFinalizedInvoicingRequest from a dict
custom_invoicing_finalized_invoicing_request_from_dict = CustomInvoicingFinalizedInvoicingRequest.from_dict(custom_invoicing_finalized_invoicing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


