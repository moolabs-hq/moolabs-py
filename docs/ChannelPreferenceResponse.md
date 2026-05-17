# ChannelPreferenceResponse

Response for a single channel preference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**contact_id** | **str** |  | 
**channel** | **str** |  | 
**consent_status** | **str** |  | 
**opt_out** | **bool** |  | 
**suppressed_until** | **datetime** |  | [optional] 
**consent_source** | **str** |  | [optional] 
**consent_captured_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.channel_preference_response import ChannelPreferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPreferenceResponse from a JSON string
channel_preference_response_instance = ChannelPreferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelPreferenceResponse.to_json())

# convert the object into a dict
channel_preference_response_dict = channel_preference_response_instance.to_dict()
# create an instance of ChannelPreferenceResponse from a dict
channel_preference_response_from_dict = ChannelPreferenceResponse.from_dict(channel_preference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


