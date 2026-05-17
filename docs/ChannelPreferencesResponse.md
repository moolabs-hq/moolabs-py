# ChannelPreferencesResponse

GET /contacts/{id}/preferences — all preferences for a contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ChannelPreferenceResponse]**](ChannelPreferenceResponse.md) |  | 

## Example

```python
from moolabs.models.channel_preferences_response import ChannelPreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPreferencesResponse from a JSON string
channel_preferences_response_instance = ChannelPreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(ChannelPreferencesResponse.to_json())

# convert the object into a dict
channel_preferences_response_dict = channel_preferences_response_instance.to_dict()
# create an instance of ChannelPreferencesResponse from a dict
channel_preferences_response_from_dict = ChannelPreferencesResponse.from_dict(channel_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


