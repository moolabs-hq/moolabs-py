# ValidationErrorProblemResponseExtensions

Validation issues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_errors** | [**List[MeterValidationError]**](MeterValidationError.md) |  | [optional] 

## Example

```python
from moolabs.models.validation_error_problem_response_extensions import ValidationErrorProblemResponseExtensions

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationErrorProblemResponseExtensions from a JSON string
validation_error_problem_response_extensions_instance = ValidationErrorProblemResponseExtensions.from_json(json)
# print the JSON string representation of the object
print(ValidationErrorProblemResponseExtensions.to_json())

# convert the object into a dict
validation_error_problem_response_extensions_dict = validation_error_problem_response_extensions_instance.to_dict()
# create an instance of ValidationErrorProblemResponseExtensions from a dict
validation_error_problem_response_extensions_from_dict = ValidationErrorProblemResponseExtensions.from_dict(validation_error_problem_response_extensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


