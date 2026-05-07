# FilterIDExact

A filter for a ID (ULID) field allowing only equality or inclusion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_in** | **List[str]** | The field must be in the provided list of values. | [optional] 

## Example

```python
from moolabs.models.filter_id_exact import FilterIDExact

# TODO update the JSON string below
json = "{}"
# create an instance of FilterIDExact from a JSON string
filter_id_exact_instance = FilterIDExact.from_json(json)
# print the JSON string representation of the object
print(FilterIDExact.to_json())

# convert the object into a dict
filter_id_exact_dict = filter_id_exact_instance.to_dict()
# create an instance of FilterIDExact from a dict
filter_id_exact_from_dict = FilterIDExact.from_dict(filter_id_exact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


