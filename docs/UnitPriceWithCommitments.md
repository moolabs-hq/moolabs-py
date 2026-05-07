# UnitPriceWithCommitments

Unit price with spend commitments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The amount of the unit price. | 
**minimum_amount** | **str** | The customer is committed to spend at least the amount. | [optional] 
**maximum_amount** | **str** | The customer is limited to spend at most the amount. | [optional] 

## Example

```python
from moolabs.models.unit_price_with_commitments import UnitPriceWithCommitments

# TODO update the JSON string below
json = "{}"
# create an instance of UnitPriceWithCommitments from a JSON string
unit_price_with_commitments_instance = UnitPriceWithCommitments.from_json(json)
# print the JSON string representation of the object
print(UnitPriceWithCommitments.to_json())

# convert the object into a dict
unit_price_with_commitments_dict = unit_price_with_commitments_instance.to_dict()
# create an instance of UnitPriceWithCommitments from a dict
unit_price_with_commitments_from_dict = UnitPriceWithCommitments.from_dict(unit_price_with_commitments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


