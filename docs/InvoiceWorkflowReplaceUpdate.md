# InvoiceWorkflowReplaceUpdate

InvoiceWorkflowReplaceUpdate represents the update model for an invoice workflow.  Fields that are immutable a re removed from the model. This is based on InvoiceWorkflowSettings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow** | [**InvoiceWorkflowSettingsReplaceUpdate**](InvoiceWorkflowSettingsReplaceUpdate.md) | The workflow used for this invoice. | 

## Example

```python
from moolabs.models.invoice_workflow_replace_update import InvoiceWorkflowReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceWorkflowReplaceUpdate from a JSON string
invoice_workflow_replace_update_instance = InvoiceWorkflowReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(InvoiceWorkflowReplaceUpdate.to_json())

# convert the object into a dict
invoice_workflow_replace_update_dict = invoice_workflow_replace_update_instance.to_dict()
# create an instance of InvoiceWorkflowReplaceUpdate from a dict
invoice_workflow_replace_update_from_dict = InvoiceWorkflowReplaceUpdate.from_dict(invoice_workflow_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


