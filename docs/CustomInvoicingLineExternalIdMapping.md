# CustomInvoicingLineExternalIdMapping

Mapping between lines and external IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_id** | **str** | The line ID. | 
**external_id** | **str** | The external ID (e.g. custom invoicing system&#39;s ID). | 

## Example

```python
from moolabs.models.custom_invoicing_line_external_id_mapping import CustomInvoicingLineExternalIdMapping

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingLineExternalIdMapping from a JSON string
custom_invoicing_line_external_id_mapping_instance = CustomInvoicingLineExternalIdMapping.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingLineExternalIdMapping.to_json())

# convert the object into a dict
custom_invoicing_line_external_id_mapping_dict = custom_invoicing_line_external_id_mapping_instance.to_dict()
# create an instance of CustomInvoicingLineExternalIdMapping from a dict
custom_invoicing_line_external_id_mapping_from_dict = CustomInvoicingLineExternalIdMapping.from_dict(custom_invoicing_line_external_id_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


