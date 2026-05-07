# InvoiceLine

InvoiceUsageBasedLine represents a line item that is sold to the customer based on usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**id** | **str** | ID of the line. | 
**managed_by** | [**InvoiceLineManagedBy**](InvoiceLineManagedBy.md) | managedBy specifies if the line is manually added via the api or managed by OpenMeter. | [readonly] 
**status** | [**InvoiceLineStatus**](InvoiceLineStatus.md) | Status of the line.  External calls always create valid lines, other line types are managed by the billing engine of OpenMeter. | [readonly] 
**discounts** | [**InvoiceLineDiscounts**](InvoiceLineDiscounts.md) | Discounts detailes applied to this line.  New discounts can be added via the invoice&#39;s discounts API, to facilitate discounts that are affecting multiple lines. | [optional] [readonly] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) | The invoice this item belongs to. | [optional] 
**currency** | **str** | The currency of this line. | 
**taxes** | [**List[InvoiceLineTaxItem]**](InvoiceLineTaxItem.md) | Taxes applied to the invoice totals. | [optional] 
**tax_config** | [**TaxConfig**](TaxConfig.md) | Tax config specify the tax configuration for this line. | [optional] 
**totals** | [**InvoiceTotals**](InvoiceTotals.md) | Totals for this line. | [readonly] 
**period** | [**Period**](Period.md) | Period of the line item applies to for revenue recognition pruposes.  Billing always treats periods as start being inclusive and end being exclusive. | 
**invoice_at** | **datetime** | The time this line item should be invoiced. | 
**external_ids** | [**InvoiceLineAppExternalIds**](InvoiceLineAppExternalIds.md) | External IDs of the invoice in other apps such as Stripe. | [optional] [readonly] 
**subscription** | [**InvoiceLineSubscriptionReference**](InvoiceLineSubscriptionReference.md) | Subscription are the references to the subscritpions that this line is related to. | [optional] [readonly] 
**type** | **str** | Type of the line. | [readonly] 
**price** | [**RateCardUsageBasedPrice**](RateCardUsageBasedPrice.md) | Price of the usage-based item being sold. | [optional] 
**feature_key** | **str** | The feature that the usage is based on. | [optional] 
**children** | [**List[InvoiceDetailedLine]**](InvoiceDetailedLine.md) | The lines detailing the item or service sold. | [optional] 
**rate_card** | [**InvoiceUsageBasedRateCard**](InvoiceUsageBasedRateCard.md) | The rate card that is used for this line.  The rate card captures the intent of the price and discounts for the usage-based item. | [optional] 
**quantity** | **str** | The quantity of the item being sold.  Any usage discounts applied previously are deducted from this quantity. | [optional] [readonly] 
**metered_quantity** | **str** | The quantity of the item that has been metered for the period before any discounts were applied. | [optional] [readonly] 
**pre_line_period_quantity** | **str** | The quantity of the item used before this line&#39;s period.  It is non-zero in case of progressive billing, when this shows how much of the usage was already billed.  Any usage discounts applied previously are deducted from this quantity. | [optional] [readonly] 
**metered_pre_line_period_quantity** | **str** | The metered quantity of the item used in before this line&#39;s period without any discounts applied.  It is non-zero in case of progressive billing, when this shows how much of the usage was already billed. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_line import InvoiceLine

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLine from a JSON string
invoice_line_instance = InvoiceLine.from_json(json)
# print the JSON string representation of the object
print(InvoiceLine.to_json())

# convert the object into a dict
invoice_line_dict = invoice_line_instance.to_dict()
# create an instance of InvoiceLine from a dict
invoice_line_from_dict = InvoiceLine.from_dict(invoice_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


