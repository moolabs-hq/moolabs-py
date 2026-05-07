# InvoiceAppExternalIds

InvoiceAppExternalIds contains the external IDs of the invoice in other apps such as Stripe.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoicing** | **str** | The external ID of the invoice in the invoicing app if available. | [optional] [readonly] 
**tax** | **str** | The external ID of the invoice in the tax app if available. | [optional] [readonly] 
**payment** | **str** | The external ID of the invoice in the payment app if available. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_app_external_ids import InvoiceAppExternalIds

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAppExternalIds from a JSON string
invoice_app_external_ids_instance = InvoiceAppExternalIds.from_json(json)
# print the JSON string representation of the object
print(InvoiceAppExternalIds.to_json())

# convert the object into a dict
invoice_app_external_ids_dict = invoice_app_external_ids_instance.to_dict()
# create an instance of InvoiceAppExternalIds from a dict
invoice_app_external_ids_from_dict = InvoiceAppExternalIds.from_dict(invoice_app_external_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


