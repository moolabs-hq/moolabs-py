# InvoiceReplaceUpdate

InvoiceReplaceUpdate represents the update model for an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**supplier** | [**BillingPartyReplaceUpdate**](BillingPartyReplaceUpdate.md) | The supplier of the lines included in the invoice. | 
**customer** | [**BillingPartyReplaceUpdate**](BillingPartyReplaceUpdate.md) | The customer the invoice is sent to. | 
**lines** | [**List[InvoiceLineReplaceUpdate]**](InvoiceLineReplaceUpdate.md) | The lines included in the invoice. | 
**workflow** | [**InvoiceWorkflowReplaceUpdate**](InvoiceWorkflowReplaceUpdate.md) | The workflow settings for the invoice. | 

## Example

```python
from moolabs.models.invoice_replace_update import InvoiceReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReplaceUpdate from a JSON string
invoice_replace_update_instance = InvoiceReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(InvoiceReplaceUpdate.to_json())

# convert the object into a dict
invoice_replace_update_dict = invoice_replace_update_instance.to_dict()
# create an instance of InvoiceReplaceUpdate from a dict
invoice_replace_update_from_dict = InvoiceReplaceUpdate.from_dict(invoice_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


