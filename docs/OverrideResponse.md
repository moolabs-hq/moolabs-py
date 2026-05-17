# OverrideResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steering_event_id** | **str** |  | 
**status** | **str** |  | 
**completion_kind** | **str** |  | 

## Example

```python
from moolabs.models.override_response import OverrideResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideResponse from a JSON string
override_response_instance = OverrideResponse.from_json(json)
# print the JSON string representation of the object
print(OverrideResponse.to_json())

# convert the object into a dict
override_response_dict = override_response_instance.to_dict()
# create an instance of OverrideResponse from a dict
override_response_from_dict = OverrideResponse.from_dict(override_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


