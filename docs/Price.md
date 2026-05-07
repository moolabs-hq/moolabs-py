# Price

Price. One of: flat, unit, or tiered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The price of one package. | 
**mode** | [**TieredPriceMode**](TieredPriceMode.md) | Defines if the tiering mode is volume-based or graduated: - In &#x60;volume&#x60;-based tiering, the maximum quantity within a period determines the per unit price. - In &#x60;graduated&#x60; tiering, pricing can change as the quantity grows. | 
**tiers** | [**List[PriceTier]**](PriceTier.md) | The tiers of the tiered price. At least one price component is required in each tier. | 
**multiplier** | **str** | The multiplier to apply to the base price to get the dynamic price.  Examples: - 0.0: the price is zero - 0.5: the price is 50% of the base price - 1.0: the price is the same as the base price - 1.5: the price is 150% of the base price | [optional] 
**quantity_per_package** | **str** | The quantity per package. | 

## Example

```python
from moolabs.models.price import Price

# TODO update the JSON string below
json = "{}"
# create an instance of Price from a JSON string
price_instance = Price.from_json(json)
# print the JSON string representation of the object
print(Price.to_json())

# convert the object into a dict
price_dict = price_instance.to_dict()
# create an instance of Price from a dict
price_from_dict = Price.from_dict(price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


