# FilterString

A filter for a string field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **str** | The field must be equal to the provided value. | [optional] 
**ne** | **str** | The field must not be equal to the provided value. | [optional] 
**var_in** | **List[str]** | The field must be in the provided list of values. | [optional] 
**nin** | **List[str]** | The field must not be in the provided list of values. | [optional] 
**like** | **str** | The field must match the provided value. | [optional] 
**nlike** | **str** | The field must not match the provided value. | [optional] 
**ilike** | **str** | The field must match the provided value, ignoring case. | [optional] 
**nilike** | **str** | The field must not match the provided value, ignoring case. | [optional] 
**gt** | **str** | The field must be greater than the provided value. | [optional] 
**gte** | **str** | The field must be greater than or equal to the provided value. | [optional] 
**lt** | **str** | The field must be less than the provided value. | [optional] 
**lte** | **str** | The field must be less than or equal to the provided value. | [optional] 
**var_and** | [**List[FilterString]**](FilterString.md) | Provide a list of filters to be combined with a logical AND. | [optional] 
**var_or** | [**List[FilterString]**](FilterString.md) | Provide a list of filters to be combined with a logical OR. | [optional] 

## Example

```python
from moolabs.models.filter_string import FilterString

# TODO update the JSON string below
json = "{}"
# create an instance of FilterString from a JSON string
filter_string_instance = FilterString.from_json(json)
# print the JSON string representation of the object
print(FilterString.to_json())

# convert the object into a dict
filter_string_dict = filter_string_instance.to_dict()
# create an instance of FilterString from a dict
filter_string_from_dict = FilterString.from_dict(filter_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


