# AppCapability

App capability.  Capabilities only exist in config so they don't extend the Resource model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AppCapabilityType**](AppCapabilityType.md) | The capability type. | 
**key** | **str** | Key | 
**name** | **str** | The capability name. | 
**description** | **str** | The capability description. | 

## Example

```python
from moolabs.models.app_capability import AppCapability

# TODO update the JSON string below
json = "{}"
# create an instance of AppCapability from a JSON string
app_capability_instance = AppCapability.from_json(json)
# print the JSON string representation of the object
print(AppCapability.to_json())

# convert the object into a dict
app_capability_dict = app_capability_instance.to_dict()
# create an instance of AppCapability from a dict
app_capability_from_dict = AppCapability.from_dict(app_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


