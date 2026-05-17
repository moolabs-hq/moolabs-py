# ArcValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[ValidationErrorLocInner]**](ValidationErrorLocInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from moolabs.models.arc_validation_error import ArcValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ArcValidationError from a JSON string
arc_validation_error_instance = ArcValidationError.from_json(json)
# print the JSON string representation of the object
print(ArcValidationError.to_json())

# convert the object into a dict
arc_validation_error_dict = arc_validation_error_instance.to_dict()
# create an instance of ArcValidationError from a dict
arc_validation_error_from_dict = ArcValidationError.from_dict(arc_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


