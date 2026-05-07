# CustomInvoicingUpdatePaymentStatusRequest

Update payment status request.  Can be used to manipulate invoice's payment status (when custominvoicing app is being used).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | [**CustomInvoicingPaymentTrigger**](CustomInvoicingPaymentTrigger.md) | The trigger to be executed on the invoice. | 
**external_payment_id** | **str** | If set the invoice&#39;s payment external ID will be set to this value. | [optional] 
**payment_provider** | **str** | If set the invoice&#39;s payment provider metadata will be set to this value. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_update_payment_status_request import CustomInvoicingUpdatePaymentStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingUpdatePaymentStatusRequest from a JSON string
custom_invoicing_update_payment_status_request_instance = CustomInvoicingUpdatePaymentStatusRequest.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingUpdatePaymentStatusRequest.to_json())

# convert the object into a dict
custom_invoicing_update_payment_status_request_dict = custom_invoicing_update_payment_status_request_instance.to_dict()
# create an instance of CustomInvoicingUpdatePaymentStatusRequest from a dict
custom_invoicing_update_payment_status_request_from_dict = CustomInvoicingUpdatePaymentStatusRequest.from_dict(custom_invoicing_update_payment_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


