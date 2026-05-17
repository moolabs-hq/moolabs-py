# TieredPricingPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**tiers** | [**List[PriceTierPayload]**](PriceTierPayload.md) |  | 

## Example

```python
from moolabs.models.tiered_pricing_payload import TieredPricingPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TieredPricingPayload from a JSON string
tiered_pricing_payload_instance = TieredPricingPayload.from_json(json)
# print the JSON string representation of the object
print(TieredPricingPayload.to_json())

# convert the object into a dict
tiered_pricing_payload_dict = tiered_pricing_payload_instance.to_dict()
# create an instance of TieredPricingPayload from a dict
tiered_pricing_payload_from_dict = TieredPricingPayload.from_dict(tiered_pricing_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


