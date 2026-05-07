# SandboxAppReplaceUpdate

Resource update operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**type** | **str** | The app&#39;s type is Sandbox. | 

## Example

```python
from moolabs.models.sandbox_app_replace_update import SandboxAppReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxAppReplaceUpdate from a JSON string
sandbox_app_replace_update_instance = SandboxAppReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(SandboxAppReplaceUpdate.to_json())

# convert the object into a dict
sandbox_app_replace_update_dict = sandbox_app_replace_update_instance.to_dict()
# create an instance of SandboxAppReplaceUpdate from a dict
sandbox_app_replace_update_from_dict = SandboxAppReplaceUpdate.from_dict(sandbox_app_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


