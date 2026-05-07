# RateCard

A rate card defines the pricing and entitlement of a feature or service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the RateCard. | 
**key** | **str** | A semi-unique identifier for the resource. | 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**feature_key** | **str** | The feature the customer is entitled to use. | [optional] 
**entitlement_template** | [**RateCardEntitlement**](RateCardEntitlement.md) | The entitlement of the rate card. Only available when featureKey is set. | [optional] 
**tax_config** | [**TaxConfig**](TaxConfig.md) | The tax config of the rate card. When undefined, the tax config of the feature or the default tax config of the plan is used. | [optional] 
**billing_cadence** | **str** | The billing cadence of the rate card. | 
**price** | [**RateCardUsageBasedPrice**](RateCardUsageBasedPrice.md) | The price of the rate card. When null, the feature or service is free. | 
**discounts** | [**Discounts**](Discounts.md) | The discounts of the rate card.  Flat fee rate cards only support percentage discounts. | [optional] 

## Example

```python
from moolabs.models.rate_card import RateCard

# TODO update the JSON string below
json = "{}"
# create an instance of RateCard from a JSON string
rate_card_instance = RateCard.from_json(json)
# print the JSON string representation of the object
print(RateCard.to_json())

# convert the object into a dict
rate_card_dict = rate_card_instance.to_dict()
# create an instance of RateCard from a dict
rate_card_from_dict = RateCard.from_dict(rate_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


