# InvoiceTotals

Totals contains the summaries of all calculations for the invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The total value of the line before taxes, discounts and commitments. | [readonly] 
**charges_total** | **str** | The amount of value of the line that are due to additional charges. | [readonly] 
**discounts_total** | **str** | The amount of value of the line that are due to discounts. | [readonly] 
**taxes_inclusive_total** | **str** | The total amount of taxes that are included in the line. | [readonly] 
**taxes_exclusive_total** | **str** | The total amount of taxes that are added on top of amount from the line. | [readonly] 
**taxes_total** | **str** | The total amount of taxes for this line. | [readonly] 
**total** | **str** | The total amount value of the line after taxes, discounts and commitments. | [readonly] 

## Example

```python
from moolabs.models.invoice_totals import InvoiceTotals

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTotals from a JSON string
invoice_totals_instance = InvoiceTotals.from_json(json)
# print the JSON string representation of the object
print(InvoiceTotals.to_json())

# convert the object into a dict
invoice_totals_dict = invoice_totals_instance.to_dict()
# create an instance of InvoiceTotals from a dict
invoice_totals_from_dict = InvoiceTotals.from_dict(invoice_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


