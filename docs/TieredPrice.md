# TieredPrice

Tiered price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price.  One of: flat, unit, or tiered. | 
**mode** | [**TieredPriceMode**](TieredPriceMode.md) | Defines if the tiering mode is volume-based or graduated: - In &#x60;volume&#x60;-based tiering, the maximum quantity within a period determines the per unit price. - In &#x60;graduated&#x60; tiering, pricing can change as the quantity grows. | 
**tiers** | [**List[PriceTier]**](PriceTier.md) | The tiers of the tiered price. At least one price component is required in each tier. | 

## Example

```python
from moolabs.models.tiered_price import TieredPrice

# TODO update the JSON string below
json = "{}"
# create an instance of TieredPrice from a JSON string
tiered_price_instance = TieredPrice.from_json(json)
# print the JSON string representation of the object
print(TieredPrice.to_json())

# convert the object into a dict
tiered_price_dict = tiered_price_instance.to_dict()
# create an instance of TieredPrice from a dict
tiered_price_from_dict = TieredPrice.from_dict(tiered_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


