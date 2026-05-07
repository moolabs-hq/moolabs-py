# InvoiceDetailedLine

InvoiceDetailedLine represents a line item that is sold to the customer as a manually added fee.

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
**external_ids** | [**InvoiceLineAppExternalIds**](InvoiceLineAppExternalIds.md) | External IDs of the invoice in other apps such as Stripe. | [optional] [readonly] 
**subscription** | [**InvoiceLineSubscriptionReference**](InvoiceLineSubscriptionReference.md) | Subscription are the references to the subscritpions that this line is related to. | [optional] [readonly] 
**invoice_at** | **datetime** | The time this line item should be invoiced. | 
**type** | **str** | Type of the line. | [readonly] 
**per_unit_amount** | **str** | Price of the item being sold. | [optional] 
**payment_term** | [**PricePaymentTerm**](PricePaymentTerm.md) | Payment term of the line. | [optional] 
**quantity** | **str** | Quantity of the item being sold. | [optional] 
**rate_card** | [**InvoiceDetailedLineRateCard**](InvoiceDetailedLineRateCard.md) | The rate card that is used for this line. | [optional] 
**category** | [**InvoiceDetailedLineCostCategory**](InvoiceDetailedLineCostCategory.md) | Category of the flat fee. | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_detailed_line import InvoiceDetailedLine

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailedLine from a JSON string
invoice_detailed_line_instance = InvoiceDetailedLine.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailedLine.to_json())

# convert the object into a dict
invoice_detailed_line_dict = invoice_detailed_line_instance.to_dict()
# create an instance of InvoiceDetailedLine from a dict
invoice_detailed_line_from_dict = InvoiceDetailedLine.from_dict(invoice_detailed_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


