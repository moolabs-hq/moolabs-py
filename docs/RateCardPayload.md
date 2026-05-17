# RateCardPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**pricing_type** | **str** |  | 
**currency** | **str** |  | 
**amount** | [**Amount1**](Amount1.md) |  | [optional] 
**tiered_pricing** | [**TieredPricingPayload**](TieredPricingPayload.md) |  | [optional] 

## Example

```python
from moolabs.models.rate_card_payload import RateCardPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardPayload from a JSON string
rate_card_payload_instance = RateCardPayload.from_json(json)
# print the JSON string representation of the object
print(RateCardPayload.to_json())

# convert the object into a dict
rate_card_payload_dict = rate_card_payload_instance.to_dict()
# create an instance of RateCardPayload from a dict
rate_card_payload_from_dict = RateCardPayload.from_dict(rate_card_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


