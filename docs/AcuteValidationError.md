# AcuteValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[ValidationErrorLocInner]**](ValidationErrorLocInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from moolabs.models.acute_validation_error import AcuteValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AcuteValidationError from a JSON string
acute_validation_error_instance = AcuteValidationError.from_json(json)
# print the JSON string representation of the object
print(AcuteValidationError.to_json())

# convert the object into a dict
acute_validation_error_dict = acute_validation_error_instance.to_dict()
# create an instance of AcuteValidationError from a dict
acute_validation_error_from_dict = AcuteValidationError.from_dict(acute_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


