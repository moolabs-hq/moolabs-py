# CustomInvoicingLineDiscountExternalIdMapping

Mapping between line discounts and external IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_discount_id** | **str** | The line discount ID. | 
**external_id** | **str** | The external ID (e.g. custom invoicing system&#39;s ID). | 

## Example

```python
from moolabs.models.custom_invoicing_line_discount_external_id_mapping import CustomInvoicingLineDiscountExternalIdMapping

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingLineDiscountExternalIdMapping from a JSON string
custom_invoicing_line_discount_external_id_mapping_instance = CustomInvoicingLineDiscountExternalIdMapping.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingLineDiscountExternalIdMapping.to_json())

# convert the object into a dict
custom_invoicing_line_discount_external_id_mapping_dict = custom_invoicing_line_discount_external_id_mapping_instance.to_dict()
# create an instance of CustomInvoicingLineDiscountExternalIdMapping from a dict
custom_invoicing_line_discount_external_id_mapping_from_dict = CustomInvoicingLineDiscountExternalIdMapping.from_dict(custom_invoicing_line_discount_external_id_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


