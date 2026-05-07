# RateCardUsageBasedPrice

The price of the usage based rate card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The price of one package. | 
**payment_term** | [**PricePaymentTerm**](PricePaymentTerm.md) | The payment term of the flat price. Defaults to in advance. | [optional] 
**minimum_amount** | **str** | The customer is committed to spend at least the amount. | [optional] 
**maximum_amount** | **str** | The customer is limited to spend at most the amount. | [optional] 
**mode** | [**TieredPriceMode**](TieredPriceMode.md) | Defines if the tiering mode is volume-based or graduated: - In &#x60;volume&#x60;-based tiering, the maximum quantity within a period determines the per unit price. - In &#x60;graduated&#x60; tiering, pricing can change as the quantity grows. | 
**tiers** | [**List[PriceTier]**](PriceTier.md) | The tiers of the tiered price. At least one price component is required in each tier. | 
**multiplier** | **str** | The multiplier to apply to the base price to get the dynamic price.  Examples: - 0.0: the price is zero - 0.5: the price is 50% of the base price - 1.0: the price is the same as the base price - 1.5: the price is 150% of the base price | [optional] 
**quantity_per_package** | **str** | The quantity per package. | 

## Example

```python
from moolabs.models.rate_card_usage_based_price import RateCardUsageBasedPrice

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardUsageBasedPrice from a JSON string
rate_card_usage_based_price_instance = RateCardUsageBasedPrice.from_json(json)
# print the JSON string representation of the object
print(RateCardUsageBasedPrice.to_json())

# convert the object into a dict
rate_card_usage_based_price_dict = rate_card_usage_based_price_instance.to_dict()
# create an instance of RateCardUsageBasedPrice from a dict
rate_card_usage_based_price_from_dict = RateCardUsageBasedPrice.from_dict(rate_card_usage_based_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


