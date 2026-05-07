# DynamicPrice

Dynamic price.  The underlying meter's value is considered the base price in the customer's currency.  The rate specifies the markup over the price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**multiplier** | **str** | The multiplier to apply to the base price to get the dynamic price.  Examples: - 0.0: the price is zero - 0.5: the price is 50% of the base price - 1.0: the price is the same as the base price - 1.5: the price is 150% of the base price | [optional] 

## Example

```python
from moolabs.models.dynamic_price import DynamicPrice

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPrice from a JSON string
dynamic_price_instance = DynamicPrice.from_json(json)
# print the JSON string representation of the object
print(DynamicPrice.to_json())

# convert the object into a dict
dynamic_price_dict = dynamic_price_instance.to_dict()
# create an instance of DynamicPrice from a dict
dynamic_price_from_dict = DynamicPrice.from_dict(dynamic_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


