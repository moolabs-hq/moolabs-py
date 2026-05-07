# InvoiceDetailedLineRateCard

InvoiceDetailedLineRateCard represents the rate card (intent) for a flat fee line.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_config** | [**TaxConfig**](TaxConfig.md) | The tax config of the rate card. When undefined, the tax config of the feature or the default tax config of the plan is used. | [optional] 
**price** | [**FlatPriceWithPaymentTerm**](FlatPriceWithPaymentTerm.md) | The price of the rate card. When null, the feature or service is free. | 
**quantity** | **str** | Quantity of the item being sold.  Default: 1 | [optional] 
**discounts** | [**BillingDiscounts**](BillingDiscounts.md) | The discounts that are applied to the line. | [optional] 

## Example

```python
from moolabs.models.invoice_detailed_line_rate_card import InvoiceDetailedLineRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailedLineRateCard from a JSON string
invoice_detailed_line_rate_card_instance = InvoiceDetailedLineRateCard.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailedLineRateCard.to_json())

# convert the object into a dict
invoice_detailed_line_rate_card_dict = invoice_detailed_line_rate_card_instance.to_dict()
# create an instance of InvoiceDetailedLineRateCard from a dict
invoice_detailed_line_rate_card_from_dict = InvoiceDetailedLineRateCard.from_dict(invoice_detailed_line_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


