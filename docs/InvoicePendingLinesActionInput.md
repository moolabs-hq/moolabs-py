# InvoicePendingLinesActionInput

BillingInvoiceActionInput is the input for creating an invoice.  Invoice creation is always based on already pending line items created by the billingCreateLineByCustomer operation. Empty invoices are not allowed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**InvoicePendingLinesActionFiltersInput**](InvoicePendingLinesActionFiltersInput.md) | Filters to apply when creating the invoice. | [optional] 
**as_of** | **datetime** | The time as of which the invoice is created.  If not provided, the current time is used. | [optional] 
**customer_id** | **str** | The customer ID for which to create the invoice. | 
**progressive_billing_override** | **bool** | Override the progressive billing setting of the customer.  Can be used to disable/enable progressive billing in case the business logic requires it, if not provided the billing profile&#39;s progressive billing setting will be used. | [optional] 

## Example

```python
from moolabs.models.invoice_pending_lines_action_input import InvoicePendingLinesActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePendingLinesActionInput from a JSON string
invoice_pending_lines_action_input_instance = InvoicePendingLinesActionInput.from_json(json)
# print the JSON string representation of the object
print(InvoicePendingLinesActionInput.to_json())

# convert the object into a dict
invoice_pending_lines_action_input_dict = invoice_pending_lines_action_input_instance.to_dict()
# create an instance of InvoicePendingLinesActionInput from a dict
invoice_pending_lines_action_input_from_dict = InvoicePendingLinesActionInput.from_dict(invoice_pending_lines_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


