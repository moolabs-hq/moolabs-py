# AppReference

App reference  Can be used as a short reference to an app if the full app object is not needed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the app. | 

## Example

```python
from moolabs.models.app_reference import AppReference

# TODO update the JSON string below
json = "{}"
# create an instance of AppReference from a JSON string
app_reference_instance = AppReference.from_json(json)
# print the JSON string representation of the object
print(AppReference.to_json())

# convert the object into a dict
app_reference_dict = app_reference_instance.to_dict()
# create an instance of AppReference from a dict
app_reference_from_dict = AppReference.from_dict(app_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


