# PriceTier

A price tier. At least one price component is required in each tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**up_to_amount** | **str** | Up to and including to this quantity will be contained in the tier. If null, the tier is open-ended. | [optional] 
**flat_price** | [**FlatPrice**](FlatPrice.md) | The flat price component of the tier. | 
**unit_price** | [**UnitPrice**](UnitPrice.md) | The unit price component of the tier. | 

## Example

```python
from moolabs.models.price_tier import PriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of PriceTier from a JSON string
price_tier_instance = PriceTier.from_json(json)
# print the JSON string representation of the object
print(PriceTier.to_json())

# convert the object into a dict
price_tier_dict = price_tier_instance.to_dict()
# create an instance of PriceTier from a dict
price_tier_from_dict = PriceTier.from_dict(price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


