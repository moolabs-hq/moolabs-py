# Discounts

Discount by type on a price

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | [**DiscountPercentage**](DiscountPercentage.md) | The percentage discount. | [optional] 
**usage** | [**DiscountUsage**](DiscountUsage.md) | The usage discount. | [optional] 

## Example

```python
from moolabs.models.discounts import Discounts

# TODO update the JSON string below
json = "{}"
# create an instance of Discounts from a JSON string
discounts_instance = Discounts.from_json(json)
# print the JSON string representation of the object
print(Discounts.to_json())

# convert the object into a dict
discounts_dict = discounts_instance.to_dict()
# create an instance of Discounts from a dict
discounts_from_dict = Discounts.from_dict(discounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


