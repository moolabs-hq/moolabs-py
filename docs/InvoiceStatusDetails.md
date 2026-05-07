# InvoiceStatusDetails

InvoiceStatusDetails represents the details of the invoice status.  API users are encouraged to rely on the immutable/failed/avaliableActions fields to determine the next steps of the invoice instead of the extendedStatus field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**immutable** | **bool** | Is the invoice editable? | [readonly] 
**failed** | **bool** | Is the invoice in a failed state? | [readonly] 
**extended_status** | **str** | Extended status information for the invoice. | [readonly] 
**available_actions** | [**InvoiceAvailableActions**](InvoiceAvailableActions.md) | The actions that can be performed on the invoice. | 

## Example

```python
from moolabs.models.invoice_status_details import InvoiceStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceStatusDetails from a JSON string
invoice_status_details_instance = InvoiceStatusDetails.from_json(json)
# print the JSON string representation of the object
print(InvoiceStatusDetails.to_json())

# convert the object into a dict
invoice_status_details_dict = invoice_status_details_instance.to_dict()
# create an instance of InvoiceStatusDetails from a dict
invoice_status_details_from_dict = InvoiceStatusDetails.from_dict(invoice_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


