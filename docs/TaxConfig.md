# TaxConfig

Set of provider specific tax configs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | [**TaxBehavior**](TaxBehavior.md) | Tax behavior.  If not specified the billing profile is used to determine the tax behavior. If not specified in the billing profile, the provider&#39;s default behavior is used. | [optional] 
**stripe** | [**StripeTaxConfig**](StripeTaxConfig.md) | Stripe tax config. | [optional] 
**custom_invoicing** | [**CustomInvoicingTaxConfig**](CustomInvoicingTaxConfig.md) | Custom invoicing tax config. | [optional] 

## Example

```python
from moolabs.models.tax_config import TaxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TaxConfig from a JSON string
tax_config_instance = TaxConfig.from_json(json)
# print the JSON string representation of the object
print(TaxConfig.to_json())

# convert the object into a dict
tax_config_dict = tax_config_instance.to_dict()
# create an instance of TaxConfig from a dict
tax_config_from_dict = TaxConfig.from_dict(tax_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


