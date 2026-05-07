# InvoiceLineAmountDiscount

InvoiceLineAmountDiscount represents an amount deducted from the line, and will be applied before taxes.

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
**amount** | **str** | Fixed discount amount to apply (calculated if percent present). | [readonly] 

## Example

```python
from moolabs.models.invoice_line_amount_discount import InvoiceLineAmountDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineAmountDiscount from a JSON string
invoice_line_amount_discount_instance = InvoiceLineAmountDiscount.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineAmountDiscount.to_json())

# convert the object into a dict
invoice_line_amount_discount_dict = invoice_line_amount_discount_instance.to_dict()
# create an instance of InvoiceLineAmountDiscount from a dict
invoice_line_amount_discount_from_dict = InvoiceLineAmountDiscount.from_dict(invoice_line_amount_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


