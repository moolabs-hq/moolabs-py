# InvoicePendingLinesActionFiltersInput

InvoicePendingLinesActionFiltersInput specifies which lines to include in the invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_ids** | **List[str]** | The pending line items to include in the invoice, if not provided: - all line items that have invoice_at &lt; asOf will be included - [progressive billing only] all usage based line items will be included up to asOf, new usage-based line items will be staged for the rest of the billing cycle  All lineIDs present in the list, must exists and must be invoicable as of asOf, or the action will fail. | [optional] 

## Example

```python
from moolabs.models.invoice_pending_lines_action_filters_input import InvoicePendingLinesActionFiltersInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePendingLinesActionFiltersInput from a JSON string
invoice_pending_lines_action_filters_input_instance = InvoicePendingLinesActionFiltersInput.from_json(json)
# print the JSON string representation of the object
print(InvoicePendingLinesActionFiltersInput.to_json())

# convert the object into a dict
invoice_pending_lines_action_filters_input_dict = invoice_pending_lines_action_filters_input_instance.to_dict()
# create an instance of InvoicePendingLinesActionFiltersInput from a dict
invoice_pending_lines_action_filters_input_from_dict = InvoicePendingLinesActionFiltersInput.from_dict(invoice_pending_lines_action_filters_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


