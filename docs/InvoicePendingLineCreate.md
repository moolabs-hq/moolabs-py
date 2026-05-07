# InvoicePendingLineCreate

InvoicePendingLineCreate represents the create model for an invoice line that is sold to the customer based on usage.

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

## Example

```python
from moolabs.models.invoice_pending_line_create import InvoicePendingLineCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePendingLineCreate from a JSON string
invoice_pending_line_create_instance = InvoicePendingLineCreate.from_json(json)
# print the JSON string representation of the object
print(InvoicePendingLineCreate.to_json())

# convert the object into a dict
invoice_pending_line_create_dict = invoice_pending_line_create_instance.to_dict()
# create an instance of InvoicePendingLineCreate from a dict
invoice_pending_line_create_from_dict = InvoicePendingLineCreate.from_dict(invoice_pending_line_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


