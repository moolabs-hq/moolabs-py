# InvoiceDiscountBase

InvoiceDiscountBase represents a charge or discount that can be applied to a line or the entire invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**id** | **str** | ID of the charge or discount. | [readonly] 
**reason** | [**BillingDiscountReason**](BillingDiscountReason.md) | Reason code. | [readonly] 
**description** | **str** | Text description as to why the discount was applied. | [optional] [readonly] 
**external_ids** | [**InvoiceLineAppExternalIds**](InvoiceLineAppExternalIds.md) | External IDs of the invoice in other apps such as Stripe. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_discount_base import InvoiceDiscountBase

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDiscountBase from a JSON string
invoice_discount_base_instance = InvoiceDiscountBase.from_json(json)
# print the JSON string representation of the object
print(InvoiceDiscountBase.to_json())

# convert the object into a dict
invoice_discount_base_dict = invoice_discount_base_instance.to_dict()
# create an instance of InvoiceDiscountBase from a dict
invoice_discount_base_from_dict = InvoiceDiscountBase.from_dict(invoice_discount_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


