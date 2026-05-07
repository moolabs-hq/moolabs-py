# FilterTime

A filter for a time field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gt** | **datetime** | The field must be greater than the provided value. | [optional] 
**gte** | **datetime** | The field must be greater than or equal to the provided value. | [optional] 
**lt** | **datetime** | The field must be less than the provided value. | [optional] 
**lte** | **datetime** | The field must be less than or equal to the provided value. | [optional] 
**var_and** | [**List[FilterTime]**](FilterTime.md) | Provide a list of filters to be combined with a logical AND. | [optional] 
**var_or** | [**List[FilterTime]**](FilterTime.md) | Provide a list of filters to be combined with a logical OR. | [optional] 

## Example

```python
from moolabs.models.filter_time import FilterTime

# TODO update the JSON string below
json = "{}"
# create an instance of FilterTime from a JSON string
filter_time_instance = FilterTime.from_json(json)
# print the JSON string representation of the object
print(FilterTime.to_json())

# convert the object into a dict
filter_time_dict = filter_time_instance.to_dict()
# create an instance of FilterTime from a dict
filter_time_from_dict = FilterTime.from_dict(filter_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


