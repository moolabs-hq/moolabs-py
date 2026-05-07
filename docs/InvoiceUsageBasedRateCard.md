# InvoiceUsageBasedRateCard

InvoiceUsageBasedRateCard represents the rate card (intent) for an usage-based line.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | The feature the customer is entitled to use. | [optional] 
**tax_config** | [**TaxConfig**](TaxConfig.md) | The tax config of the rate card. When undefined, the tax config of the feature or the default tax config of the plan is used. | [optional] 
**price** | [**RateCardUsageBasedPrice**](RateCardUsageBasedPrice.md) | The price of the rate card. When null, the feature or service is free. | 
**discounts** | [**BillingDiscounts**](BillingDiscounts.md) | The discounts that are applied to the line. | [optional] 

## Example

```python
from moolabs.models.invoice_usage_based_rate_card import InvoiceUsageBasedRateCard

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceUsageBasedRateCard from a JSON string
invoice_usage_based_rate_card_instance = InvoiceUsageBasedRateCard.from_json(json)
# print the JSON string representation of the object
print(InvoiceUsageBasedRateCard.to_json())

# convert the object into a dict
invoice_usage_based_rate_card_dict = invoice_usage_based_rate_card_instance.to_dict()
# create an instance of InvoiceUsageBasedRateCard from a dict
invoice_usage_based_rate_card_from_dict = InvoiceUsageBasedRateCard.from_dict(invoice_usage_based_rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


