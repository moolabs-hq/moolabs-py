# InvoiceLineReplaceUpdate

InvoiceLineReplaceUpdate represents the update model for an UBP invoice line.  This type makes ID optional to allow for creating new lines as part of the update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**tax_config** | [**TaxConfig**](TaxConfig.md) | Tax config specify the tax configuration for this line. | [optional] 
**period** | [**Period**](Period.md) | Period of the line item applies to for revenue recognition pruposes.  Billing always treats periods as start being inclusive and end being exclusive. | 
**invoice_at** | **datetime** | The time this line item should be invoiced. | 
**price** | [**RateCardUsageBasedPrice**](RateCardUsageBasedPrice.md) | Price of the usage-based item being sold. | [optional] 
**feature_key** | **str** | The feature that the usage is based on. | [optional] 
**rate_card** | [**InvoiceUsageBasedRateCard**](InvoiceUsageBasedRateCard.md) | The rate card that is used for this line.  The rate card captures the intent of the price and discounts for the usage-based item. | [optional] 
**id** | **str** | The ID of the line. | [optional] 

## Example

```python
from moolabs.models.invoice_line_replace_update import InvoiceLineReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineReplaceUpdate from a JSON string
invoice_line_replace_update_instance = InvoiceLineReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineReplaceUpdate.to_json())

# convert the object into a dict
invoice_line_replace_update_dict = invoice_line_replace_update_instance.to_dict()
# create an instance of InvoiceLineReplaceUpdate from a dict
invoice_line_replace_update_from_dict = InvoiceLineReplaceUpdate.from_dict(invoice_line_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


