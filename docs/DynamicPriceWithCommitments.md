# DynamicPriceWithCommitments

Dynamic price with spend commitments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**multiplier** | **str** | The multiplier to apply to the base price to get the dynamic price.  Examples: - 0.0: the price is zero - 0.5: the price is 50% of the base price - 1.0: the price is the same as the base price - 1.5: the price is 150% of the base price | [optional] 
**minimum_amount** | **str** | The customer is committed to spend at least the amount. | [optional] 
**maximum_amount** | **str** | The customer is limited to spend at most the amount. | [optional] 

## Example

```python
from moolabs.models.dynamic_price_with_commitments import DynamicPriceWithCommitments

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicPriceWithCommitments from a JSON string
dynamic_price_with_commitments_instance = DynamicPriceWithCommitments.from_json(json)
# print the JSON string representation of the object
print(DynamicPriceWithCommitments.to_json())

# convert the object into a dict
dynamic_price_with_commitments_dict = dynamic_price_with_commitments_instance.to_dict()
# create an instance of DynamicPriceWithCommitments from a dict
dynamic_price_with_commitments_from_dict = DynamicPriceWithCommitments.from_dict(dynamic_price_with_commitments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


