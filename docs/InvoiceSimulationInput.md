# InvoiceSimulationInput

InvoiceSimulationInput is the input for simulating an invoice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | The number of the invoice. | [optional] 
**currency** | **str** | Currency for all invoice line items.  Multi currency invoices are not supported yet. | 
**lines** | [**List[InvoiceSimulationLine]**](InvoiceSimulationLine.md) | Lines to be included in the generated invoice. | 

## Example

```python
from moolabs.models.invoice_simulation_input import InvoiceSimulationInput

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSimulationInput from a JSON string
invoice_simulation_input_instance = InvoiceSimulationInput.from_json(json)
# print the JSON string representation of the object
print(InvoiceSimulationInput.to_json())

# convert the object into a dict
invoice_simulation_input_dict = invoice_simulation_input_instance.to_dict()
# create an instance of InvoiceSimulationInput from a dict
invoice_simulation_input_from_dict = InvoiceSimulationInput.from_dict(invoice_simulation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


