# ReallocateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 

## Example

```python
from moolabs.models.reallocate_request import ReallocateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReallocateRequest from a JSON string
reallocate_request_instance = ReallocateRequest.from_json(json)
# print the JSON string representation of the object
print(ReallocateRequest.to_json())

# convert the object into a dict
reallocate_request_dict = reallocate_request_instance.to_dict()
# create an instance of ReallocateRequest from a dict
reallocate_request_from_dict = ReallocateRequest.from_dict(reallocate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


