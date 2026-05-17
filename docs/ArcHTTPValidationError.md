# ArcHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ArcValidationError]**](ArcValidationError.md) |  | [optional] 

## Example

```python
from moolabs.models.arc_http_validation_error import ArcHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ArcHTTPValidationError from a JSON string
arc_http_validation_error_instance = ArcHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(ArcHTTPValidationError.to_json())

# convert the object into a dict
arc_http_validation_error_dict = arc_http_validation_error_instance.to_dict()
# create an instance of ArcHTTPValidationError from a dict
arc_http_validation_error_from_dict = ArcHTTPValidationError.from_dict(arc_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


