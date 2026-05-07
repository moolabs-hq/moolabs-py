# AppReplaceUpdate

App ReplaceUpdate Model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**type** | **str** | The app&#39;s type is Stripe. | 
**secret_api_key** | **str** | The Stripe API key. | [optional] 
**enable_draft_sync_hook** | **bool** | Enable draft.sync hook.  If the hook is not enabled, the invoice will be progressed to the next state automatically. | 
**enable_issuing_sync_hook** | **bool** | Enable issuing.sync hook.  If the hook is not enabled, the invoice will be progressed to the next state automatically. | 

## Example

```python
from moolabs.models.app_replace_update import AppReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AppReplaceUpdate from a JSON string
app_replace_update_instance = AppReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(AppReplaceUpdate.to_json())

# convert the object into a dict
app_replace_update_dict = app_replace_update_instance.to_dict()
# create an instance of AppReplaceUpdate from a dict
app_replace_update_from_dict = AppReplaceUpdate.from_dict(app_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


