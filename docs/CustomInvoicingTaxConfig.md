# CustomInvoicingTaxConfig

Custom invoicing tax config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Tax code.  The tax code should be interpreted by the custom invoicing provider. | 

## Example

```python
from moolabs.models.custom_invoicing_tax_config import CustomInvoicingTaxConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingTaxConfig from a JSON string
custom_invoicing_tax_config_instance = CustomInvoicingTaxConfig.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingTaxConfig.to_json())

# convert the object into a dict
custom_invoicing_tax_config_dict = custom_invoicing_tax_config_instance.to_dict()
# create an instance of CustomInvoicingTaxConfig from a dict
custom_invoicing_tax_config_from_dict = CustomInvoicingTaxConfig.from_dict(custom_invoicing_tax_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


