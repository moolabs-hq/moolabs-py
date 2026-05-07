# FilterFloat

A filter for a float field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **float** | The field must be equal to the provided value. | [optional] 
**ne** | **float** | The field must not be equal to the provided value. | [optional] 
**gt** | **float** | The field must be greater than the provided value. | [optional] 
**gte** | **float** | The field must be greater than or equal to the provided value. | [optional] 
**lt** | **float** | The field must be less than the provided value. | [optional] 
**lte** | **float** | The field must be less than or equal to the provided value. | [optional] 
**var_and** | [**List[FilterFloat]**](FilterFloat.md) | Provide a list of filters to be combined with a logical AND. | [optional] 
**var_or** | [**List[FilterFloat]**](FilterFloat.md) | Provide a list of filters to be combined with a logical OR. | [optional] 

## Example

```python
from moolabs.models.filter_float import FilterFloat

# TODO update the JSON string below
json = "{}"
# create an instance of FilterFloat from a JSON string
filter_float_instance = FilterFloat.from_json(json)
# print the JSON string representation of the object
print(FilterFloat.to_json())

# convert the object into a dict
filter_float_dict = filter_float_instance.to_dict()
# create an instance of FilterFloat from a dict
filter_float_from_dict = FilterFloat.from_dict(filter_float_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


