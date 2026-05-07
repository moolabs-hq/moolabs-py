# RateCardDiscount

Discount on rate card pricing in basis points (e.g. 1500 = 15%).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_bps** | **int** |  | 

## Example

```python
from moolabs.models.rate_card_discount import RateCardDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardDiscount from a JSON string
rate_card_discount_instance = RateCardDiscount.from_json(json)
# print the JSON string representation of the object
print(RateCardDiscount.to_json())

# convert the object into a dict
rate_card_discount_dict = rate_card_discount_instance.to_dict()
# create an instance of RateCardDiscount from a dict
rate_card_discount_from_dict = RateCardDiscount.from_dict(rate_card_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


