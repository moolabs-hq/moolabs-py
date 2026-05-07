# SandboxApp

Sandbox app can be used for testing OpenMeter features.  The app is not creating anything in external systems, thus it is safe to use for verifying OpenMeter features.

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
**type** | **str** | The app&#39;s type is Sandbox. | 

## Example

```python
from moolabs.models.sandbox_app import SandboxApp

# TODO update the JSON string below
json = "{}"
# create an instance of SandboxApp from a JSON string
sandbox_app_instance = SandboxApp.from_json(json)
# print the JSON string representation of the object
print(SandboxApp.to_json())

# convert the object into a dict
sandbox_app_dict = sandbox_app_instance.to_dict()
# create an instance of SandboxApp from a dict
sandbox_app_from_dict = SandboxApp.from_dict(sandbox_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


