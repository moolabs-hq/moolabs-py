# ReattemptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steering_event_id** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from moolabs.models.reattempt_response import ReattemptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReattemptResponse from a JSON string
reattempt_response_instance = ReattemptResponse.from_json(json)
# print the JSON string representation of the object
print(ReattemptResponse.to_json())

# convert the object into a dict
reattempt_response_dict = reattempt_response_instance.to_dict()
# create an instance of ReattemptResponse from a dict
reattempt_response_from_dict = ReattemptResponse.from_dict(reattempt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


