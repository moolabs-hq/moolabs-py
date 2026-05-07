# CustomInvoicingApp

Custom Invoicing app can be used for interface with any invoicing or payment system.  This app provides ways to manipulate invoices and payments, however the integration must rely on Notifications API to get notified about invoice changes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**listing** | [**MarketplaceListing**](MarketplaceListing.md) | The marketplace listing that this installed app is based on. | [readonly] 
**status** | [**AppStatus**](AppStatus.md) | Status of the app connection. | [readonly] 
**type** | **str** | The app&#39;s type is CustomInvoicing. | 
**enable_draft_sync_hook** | **bool** | Enable draft.sync hook.  If the hook is not enabled, the invoice will be progressed to the next state automatically. | 
**enable_issuing_sync_hook** | **bool** | Enable issuing.sync hook.  If the hook is not enabled, the invoice will be progressed to the next state automatically. | 

## Example

```python
from moolabs.models.custom_invoicing_app import CustomInvoicingApp

# TODO update the JSON string below
json = "{}"
# create an instance of CustomInvoicingApp from a JSON string
custom_invoicing_app_instance = CustomInvoicingApp.from_json(json)
# print the JSON string representation of the object
print(CustomInvoicingApp.to_json())

# convert the object into a dict
custom_invoicing_app_dict = custom_invoicing_app_instance.to_dict()
# create an instance of CustomInvoicingApp from a dict
custom_invoicing_app_from_dict = CustomInvoicingApp.from_dict(custom_invoicing_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


