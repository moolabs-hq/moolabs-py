# InvoiceLineDiscounts

InvoiceLineDiscounts represents the discounts applied to the invoice line by type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**List[InvoiceLineAmountDiscount]**](InvoiceLineAmountDiscount.md) | Amount based discounts applied to the line.  Amount based discounts are deduced from the total price of the line. | [optional] 
**usage** | [**List[InvoiceLineUsageDiscount]**](InvoiceLineUsageDiscount.md) | Usage based discounts applied to the line.  Usage based discounts are deduced from the usage of the line before price calculations are applied. | [optional] 

## Example

```python
from moolabs.models.invoice_line_discounts import InvoiceLineDiscounts

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineDiscounts from a JSON string
invoice_line_discounts_instance = InvoiceLineDiscounts.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineDiscounts.to_json())

# convert the object into a dict
invoice_line_discounts_dict = invoice_line_discounts_instance.to_dict()
# create an instance of InvoiceLineDiscounts from a dict
invoice_line_discounts_from_dict = InvoiceLineDiscounts.from_dict(invoice_line_discounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


