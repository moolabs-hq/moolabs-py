# DiscountPercentage

Percentage discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percentage** | **float** | The percentage of the discount. | 

## Example

```python
from moolabs.models.discount_percentage import DiscountPercentage

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPercentage from a JSON string
discount_percentage_instance = DiscountPercentage.from_json(json)
# print the JSON string representation of the object
print(DiscountPercentage.to_json())

# convert the object into a dict
discount_percentage_dict = discount_percentage_instance.to_dict()
# create an instance of DiscountPercentage from a dict
discount_percentage_from_dict = DiscountPercentage.from_dict(discount_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


