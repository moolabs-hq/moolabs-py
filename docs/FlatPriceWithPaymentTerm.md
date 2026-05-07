# FlatPriceWithPaymentTerm

Flat price with payment term.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the price. | 
**amount** | **str** | The amount of the flat price. | 
**payment_term** | [**PricePaymentTerm**](PricePaymentTerm.md) | The payment term of the flat price. Defaults to in advance. | [optional] 

## Example

```python
from moolabs.models.flat_price_with_payment_term import FlatPriceWithPaymentTerm

# TODO update the JSON string below
json = "{}"
# create an instance of FlatPriceWithPaymentTerm from a JSON string
flat_price_with_payment_term_instance = FlatPriceWithPaymentTerm.from_json(json)
# print the JSON string representation of the object
print(FlatPriceWithPaymentTerm.to_json())

# convert the object into a dict
flat_price_with_payment_term_dict = flat_price_with_payment_term_instance.to_dict()
# create an instance of FlatPriceWithPaymentTerm from a dict
flat_price_with_payment_term_from_dict = FlatPriceWithPaymentTerm.from_dict(flat_price_with_payment_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


