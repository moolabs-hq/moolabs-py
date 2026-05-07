# StripeTaxConfig

The tax config for Stripe.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Product tax code.  See: https://docs.stripe.com/tax/tax-codes | 

## Example

```python
from moolabs.models.stripe_tax_config import StripeTaxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StripeTaxConfig from a JSON string
stripe_tax_config_instance = StripeTaxConfig.from_json(json)
# print the JSON string representation of the object
print(StripeTaxConfig.to_json())

# convert the object into a dict
stripe_tax_config_dict = stripe_tax_config_instance.to_dict()
# create an instance of StripeTaxConfig from a dict
stripe_tax_config_from_dict = StripeTaxConfig.from_dict(stripe_tax_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


