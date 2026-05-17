# AllocationKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**pct** | **float** |  | [optional] 
**metric** | **str** |  | [optional] 

## Example

```python
from moolabs.models.allocation_key import AllocationKey

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationKey from a JSON string
allocation_key_instance = AllocationKey.from_json(json)
# print the JSON string representation of the object
print(AllocationKey.to_json())

# convert the object into a dict
allocation_key_dict = allocation_key_instance.to_dict()
# create an instance of AllocationKey from a dict
allocation_key_from_dict = AllocationKey.from_dict(allocation_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


