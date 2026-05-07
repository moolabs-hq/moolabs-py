# CustomInvoicingAppReplaceUpdate

Resource update operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**type** | **str** | The app&#39;s type is CustomInvoicing. | 
**enable_draft_sync_hook** | **bool** | Enable draft.sync hook.  If the hook is not enabled, the invoice will be progressed to the next state automatically. | 
**enable_issuing_sync_hook** | **bool** | Enable issuing.sync hook.  If the hook is not enabled, the invoice will be progressed to the next state automatically. | 

## Example

```python
from moolabs.models.custom_invoicing_app_replace_update import CustomInvoicingAppReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingAppReplaceUpdate from a JSON string
custom_invoicing_app_replace_update_instance = CustomInvoicingAppReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingAppReplaceUpdate.to_json())

# convert the object into a dict
custom_invoicing_app_replace_update_dict = custom_invoicing_app_replace_update_instance.to_dict()
# create an instance of CustomInvoicingAppReplaceUpdate from a dict
custom_invoicing_app_replace_update_from_dict = CustomInvoicingAppReplaceUpdate.from_dict(custom_invoicing_app_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


