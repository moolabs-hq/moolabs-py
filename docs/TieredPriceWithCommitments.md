# TieredPriceWithCommitments

Tiered price with spend commitments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price.  One of: flat, unit, or tiered. | 
**mode** | [**TieredPriceMode**](TieredPriceMode.md) | Defines if the tiering mode is volume-based or graduated: - In &#x60;volume&#x60;-based tiering, the maximum quantity within a period determines the per unit price. - In &#x60;graduated&#x60; tiering, pricing can change as the quantity grows. | 
**tiers** | [**List[PriceTier]**](PriceTier.md) | The tiers of the tiered price. At least one price component is required in each tier. | 
**minimum_amount** | **str** | The customer is committed to spend at least the amount. | [optional] 
**maximum_amount** | **str** | The customer is limited to spend at most the amount. | [optional] 

## Example

```python
from moolabs.models.tiered_price_with_commitments import TieredPriceWithCommitments

# TODO update the JSON string below
json = "{}"
# create an instance of TieredPriceWithCommitments from a JSON string
tiered_price_with_commitments_instance = TieredPriceWithCommitments.from_json(json)
# print the JSON string representation of the object
print(TieredPriceWithCommitments.to_json())

# convert the object into a dict
tiered_price_with_commitments_dict = tiered_price_with_commitments_instance.to_dict()
# create an instance of TieredPriceWithCommitments from a dict
tiered_price_with_commitments_from_dict = TieredPriceWithCommitments.from_dict(tiered_price_with_commitments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


