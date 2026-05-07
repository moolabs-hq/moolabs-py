# FlatPrice

Flat price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The amount of the flat price. | 

## Example

```python
from moolabs.models.flat_price import FlatPrice

# TODO update the JSON string below
json = "{}"
# create an instance of FlatPrice from a JSON string
flat_price_instance = FlatPrice.from_json(json)
# print the JSON string representation of the object
print(FlatPrice.to_json())

# convert the object into a dict
flat_price_dict = flat_price_instance.to_dict()
# create an instance of FlatPrice from a dict
flat_price_from_dict = FlatPrice.from_dict(flat_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


