# AppBase

Abstract base model for installed apps.  Represent an app installed to the organization. This is an actual instance, with its own configuration and credentials.

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

## Example

```python
from moolabs.models.app_base import AppBase

# TODO update the JSON string below
json = "{}"
# create an instance of AppBase from a JSON string
app_base_instance = AppBase.from_json(json)
# print the JSON string representation of the object
print(AppBase.to_json())

# convert the object into a dict
app_base_dict = app_base_instance.to_dict()
# create an instance of AppBase from a dict
app_base_from_dict = AppBase.from_dict(app_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


