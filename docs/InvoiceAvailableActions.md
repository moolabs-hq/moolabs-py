# InvoiceAvailableActions

InvoiceAvailableActions represents the actions that can be performed on the invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advance** | [**InvoiceAvailableActionDetails**](InvoiceAvailableActionDetails.md) | Advance the invoice to the next status. | [optional] [readonly] 
**approve** | [**InvoiceAvailableActionDetails**](InvoiceAvailableActionDetails.md) | Approve an invoice that requires manual approval. | [optional] [readonly] 
**delete** | [**InvoiceAvailableActionDetails**](InvoiceAvailableActionDetails.md) | Delete the invoice (only non-issued invoices can be deleted). | [optional] [readonly] 
**retry** | [**InvoiceAvailableActionDetails**](InvoiceAvailableActionDetails.md) | Retry an invoice issuing step that failed. | [optional] [readonly] 
**snapshot_quantities** | [**InvoiceAvailableActionDetails**](InvoiceAvailableActionDetails.md) | Snapshot quantities for usage based line items. | [optional] [readonly] 
**void** | [**InvoiceAvailableActionDetails**](InvoiceAvailableActionDetails.md) | Void an already issued invoice. | [optional] [readonly] 
**invoice** | **Dict[str, object]** | Invoice a gathering invoice | [optional] [readonly] 

## Example

```python
from moolabs.models.invoice_available_actions import InvoiceAvailableActions

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAvailableActions from a JSON string
invoice_available_actions_instance = InvoiceAvailableActions.from_json(json)
# print the JSON string representation of the object
print(InvoiceAvailableActions.to_json())

# convert the object into a dict
invoice_available_actions_dict = invoice_available_actions_instance.to_dict()
# create an instance of InvoiceAvailableActions from a dict
invoice_available_actions_from_dict = InvoiceAvailableActions.from_dict(invoice_available_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


