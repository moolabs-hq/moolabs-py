# FilterInteger

A filter for an integer field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **int** | The field must be equal to the provided value. | [optional] 
**ne** | **int** | The field must not be equal to the provided value. | [optional] 
**gt** | **int** | The field must be greater than the provided value. | [optional] 
**gte** | **int** | The field must be greater than or equal to the provided value. | [optional] 
**lt** | **int** | The field must be less than the provided value. | [optional] 
**lte** | **int** | The field must be less than or equal to the provided value. | [optional] 
**var_and** | [**List[FilterInteger]**](FilterInteger.md) | Provide a list of filters to be combined with a logical AND. | [optional] 
**var_or** | [**List[FilterInteger]**](FilterInteger.md) | Provide a list of filters to be combined with a logical OR. | [optional] 

## Example

```python
from moolabs.models.filter_integer import FilterInteger

# TODO update the JSON string below
json = "{}"
# create an instance of FilterInteger from a JSON string
filter_integer_instance = FilterInteger.from_json(json)
# print the JSON string representation of the object
print(FilterInteger.to_json())

# convert the object into a dict
filter_integer_dict = filter_integer_instance.to_dict()
# create an instance of FilterInteger from a dict
filter_integer_from_dict = FilterInteger.from_dict(filter_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


