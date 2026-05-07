# RateCardFlatFee

A flat fee rate card defines a one-time purchase or a recurring fee.

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
**billing_cadence** | **str** | The billing cadence of the rate card. When null it means it is a one time fee. | 
**price** | [**FlatPriceWithPaymentTerm**](FlatPriceWithPaymentTerm.md) | The price of the rate card. When null, the feature or service is free. | 
**discounts** | [**Discounts**](Discounts.md) | The discount of the rate card. For flat fee rate cards only percentage discounts are supported. Only available when price is set. | [optional] 

## Example

```python
from moolabs.models.rate_card_flat_fee import RateCardFlatFee

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardFlatFee from a JSON string
rate_card_flat_fee_instance = RateCardFlatFee.from_json(json)
# print the JSON string representation of the object
print(RateCardFlatFee.to_json())

# convert the object into a dict
rate_card_flat_fee_dict = rate_card_flat_fee_instance.to_dict()
# create an instance of RateCardFlatFee from a dict
rate_card_flat_fee_from_dict = RateCardFlatFee.from_dict(rate_card_flat_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


