# ErrorExtension

Generic ErrorExtension as part of HTTPProblem.Extensions.[StatusCode]

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The path to the field. | [readonly] 
**code** | **str** | The machine readable description of the error. | [readonly] 
**message** | **str** | The human readable description of the error. | [readonly] 

## Example

```python
from moolabs.models.error_extension import ErrorExtension

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorExtension from a JSON string
error_extension_instance = ErrorExtension.from_json(json)
# print the JSON string representation of the object
print(ErrorExtension.to_json())

# convert the object into a dict
error_extension_dict = error_extension_instance.to_dict()
# create an instance of ErrorExtension from a dict
error_extension_from_dict = ErrorExtension.from_dict(error_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


