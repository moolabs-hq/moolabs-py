# InvoiceSimulationLine

InvoiceSimulationLine represents a usage-based line item that can be input to the simulation endpoint.

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
**quantity** | **str** | The quantity of the item being sold. | 
**pre_line_period_quantity** | **str** | The quantity of the item used before this line&#39;s period, if the line is billed progressively. | [optional] 
**id** | **str** | ID of the line. If not specified it will be auto-generated.  When discounts are specified, this must be provided, so that the discount can reference it. | [optional] 

## Example

```python
from moolabs.models.invoice_simulation_line import InvoiceSimulationLine

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSimulationLine from a JSON string
invoice_simulation_line_instance = InvoiceSimulationLine.from_json(json)
# print the JSON string representation of the object
print(InvoiceSimulationLine.to_json())

# convert the object into a dict
invoice_simulation_line_dict = invoice_simulation_line_instance.to_dict()
# create an instance of InvoiceSimulationLine from a dict
invoice_simulation_line_from_dict = InvoiceSimulationLine.from_dict(invoice_simulation_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


