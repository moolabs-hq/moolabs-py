# InvoiceLineTaxItem

TaxConfig stores the configuration for a tax line relative to an invoice line.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**TaxConfig**](TaxConfig.md) | Tax provider configuration. | [optional] [readonly] 
**percent** | **float** | Percent defines the percentage set manually or determined from the rate key (calculated if rate present). A nil percent implies that this tax combo is **exempt** from tax.\&quot;) | [optional] [readonly] 
**surcharge** | **str** | Some countries require an additional surcharge (calculated if rate present). | [optional] [readonly] 
**behavior** | [**InvoiceLineTaxBehavior**](InvoiceLineTaxBehavior.md) | Is the tax item inclusive or exclusive of the base amount. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_line_tax_item import InvoiceLineTaxItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineTaxItem from a JSON string
invoice_line_tax_item_instance = InvoiceLineTaxItem.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineTaxItem.to_json())

# convert the object into a dict
invoice_line_tax_item_dict = invoice_line_tax_item_instance.to_dict()
# create an instance of InvoiceLineTaxItem from a dict
invoice_line_tax_item_from_dict = InvoiceLineTaxItem.from_dict(invoice_line_tax_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


