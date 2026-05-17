# AcuteHTTPValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[AcuteValidationError]**](AcuteValidationError.md) |  | [optional] 

## Example

```python
from moolabs.models.acute_http_validation_error import AcuteHTTPValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AcuteHTTPValidationError from a JSON string
acute_http_validation_error_instance = AcuteHTTPValidationError.from_json(json)
# print the JSON string representation of the object
print(AcuteHTTPValidationError.to_json())

# convert the object into a dict
acute_http_validation_error_dict = acute_http_validation_error_instance.to_dict()
# create an instance of AcuteHTTPValidationError from a dict
acute_http_validation_error_from_dict = AcuteHTTPValidationError.from_dict(acute_http_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


