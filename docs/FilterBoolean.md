# FilterBoolean

A filter for a boolean field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **bool** | The field must be equal to the provided value. | [optional] 

## Example

```python
from moolabs.models.filter_boolean import FilterBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of FilterBoolean from a JSON string
filter_boolean_instance = FilterBoolean.from_json(json)
# print the JSON string representation of the object
print(FilterBoolean.to_json())

# convert the object into a dict
filter_boolean_dict = filter_boolean_instance.to_dict()
# create an instance of FilterBoolean from a dict
filter_boolean_from_dict = FilterBoolean.from_dict(filter_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


