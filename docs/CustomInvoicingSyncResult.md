# CustomInvoicingSyncResult

Information to synchronize the invoice.  Can be used to store external app's IDs on the invoice or lines.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** | If set the invoice&#39;s number will be set to this value. | [optional] 
**external_id** | **str** | If set the invoice&#39;s invoicing external ID will be set to this value. | [optional] 
**line_external_ids** | [**List[CustomInvoicingLineExternalIdMapping]**](CustomInvoicingLineExternalIdMapping.md) | If set the invoice&#39;s line external IDs will be set to this value.  This can be used to reference the external system&#39;s entities in the invoice. | [optional] 
**line_discount_external_ids** | [**List[CustomInvoicingLineDiscountExternalIdMapping]**](CustomInvoicingLineDiscountExternalIdMapping.md) | If set the invoice&#39;s line discount external IDs will be set to this value.  This can be used to reference the external system&#39;s entities in the invoice. | [optional] 

## Example

```python
from moolabs.models.custom_invoicing_sync_result import CustomInvoicingSyncResult

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingSyncResult from a JSON string
custom_invoicing_sync_result_instance = CustomInvoicingSyncResult.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingSyncResult.to_json())

# convert the object into a dict
custom_invoicing_sync_result_dict = custom_invoicing_sync_result_instance.to_dict()
# create an instance of CustomInvoicingSyncResult from a dict
custom_invoicing_sync_result_from_dict = CustomInvoicingSyncResult.from_dict(custom_invoicing_sync_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


