# InvoiceLineUsageDiscount

InvoiceLineUsageDiscount represents an usage-based discount applied to the line.  The deduction is done before the pricing algorithm is applied.

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
**quantity** | **str** | The usage to apply. | [readonly] 
**pre_line_period_quantity** | **str** | The usage discount already applied to the previous split lines.  Only set if progressive billing is enabled and the line is a split line. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_line_usage_discount import InvoiceLineUsageDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineUsageDiscount from a JSON string
invoice_line_usage_discount_instance = InvoiceLineUsageDiscount.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineUsageDiscount.to_json())

# convert the object into a dict
invoice_line_usage_discount_dict = invoice_line_usage_discount_instance.to_dict()
# create an instance of InvoiceLineUsageDiscount from a dict
invoice_line_usage_discount_from_dict = InvoiceLineUsageDiscount.from_dict(invoice_line_usage_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


