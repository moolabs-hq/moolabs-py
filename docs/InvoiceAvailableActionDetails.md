# InvoiceAvailableActionDetails

InvoiceAvailableActionInvoiceDetails represents the details of the invoice action for non-gathering invoices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resulting_state** | **str** | The state the invoice will reach if the action is activated and all intermediate steps are successful.  For example advancing a draft_created invoice will result in a draft_manual_approval_needed invoice. | [readonly] 

## Example

```python
from moolabs.models.invoice_available_action_details import InvoiceAvailableActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAvailableActionDetails from a JSON string
invoice_available_action_details_instance = InvoiceAvailableActionDetails.from_json(json)
# print the JSON string representation of the object
print(InvoiceAvailableActionDetails.to_json())

# convert the object into a dict
invoice_available_action_details_dict = invoice_available_action_details_instance.to_dict()
# create an instance of InvoiceAvailableActionDetails from a dict
invoice_available_action_details_from_dict = InvoiceAvailableActionDetails.from_dict(invoice_available_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


