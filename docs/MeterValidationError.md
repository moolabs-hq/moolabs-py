# MeterValidationError

Validation errors providing detailed description of the issue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The path to the field. | [readonly] 
**code** | **str** | The machine readable description of the error. | [readonly] 
**message** | **str** | The human readable description of the error. | [readonly] 
**attributes** | **Dict[str, object]** | Additional attributes. | [optional] [readonly] 

## Example

```python
from moolabs.models.meter_validation_error import MeterValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of MeterValidationError from a JSON string
meter_validation_error_instance = MeterValidationError.from_json(json)
# print the JSON string representation of the object
print(MeterValidationError.to_json())

# convert the object into a dict
meter_validation_error_dict = meter_validation_error_instance.to_dict()
# create an instance of MeterValidationError from a dict
meter_validation_error_from_dict = MeterValidationError.from_dict(meter_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


