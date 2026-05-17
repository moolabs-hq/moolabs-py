# OverrideRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corrected_values** | **Dict[str, object]** |  | 
**completion_note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.override_request import OverrideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideRequest from a JSON string
override_request_instance = OverrideRequest.from_json(json)
# print the JSON string representation of the object
print(OverrideRequest.to_json())

# convert the object into a dict
override_request_dict = override_request_instance.to_dict()
# create an instance of OverrideRequest from a dict
override_request_from_dict = OverrideRequest.from_dict(override_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


