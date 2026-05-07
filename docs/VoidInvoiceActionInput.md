# VoidInvoiceActionInput

Request to void an invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**VoidInvoiceActionCreate**](VoidInvoiceActionCreate.md) | The action to take on the voided line items. | 
**reason** | **str** | The reason for voiding the invoice. | 
**overrides** | [**List[VoidInvoiceActionLineOverride]**](VoidInvoiceActionLineOverride.md) | Per line item overrides for the action.  If not specified, the &#x60;action&#x60; will be applied to all line items. | [optional] 

## Example

```python
from moolabs.models.void_invoice_action_input import VoidInvoiceActionInput

# TODO update the JSON string below
json = "{}"
# create an instance of VoidInvoiceActionInput from a JSON string
void_invoice_action_input_instance = VoidInvoiceActionInput.from_json(json)
# print the JSON string representation of the object
print(VoidInvoiceActionInput.to_json())

# convert the object into a dict
void_invoice_action_input_dict = void_invoice_action_input_instance.to_dict()
# create an instance of VoidInvoiceActionInput from a dict
void_invoice_action_input_from_dict = VoidInvoiceActionInput.from_dict(void_invoice_action_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


