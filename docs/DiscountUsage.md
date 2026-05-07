# DiscountUsage

Usage discount.  Usage discount means that the first N items are free. From billing perspective this means that any usage on a specific feature is considered 0 until this discount is exhausted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **str** | The quantity of the usage discount.  Must be positive. | 

## Example

```python
from moolabs.models.discount_usage import DiscountUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountUsage from a JSON string
discount_usage_instance = DiscountUsage.from_json(json)
# print the JSON string representation of the object
print(DiscountUsage.to_json())

# convert the object into a dict
discount_usage_dict = discount_usage_instance.to_dict()
# create an instance of DiscountUsage from a dict
discount_usage_from_dict = DiscountUsage.from_dict(discount_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


