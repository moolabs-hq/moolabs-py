# ChannelPreferenceUpdate

PUT /contacts/{id}/preferences — bulk update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferences** | [**List[ChannelPreferenceCreate]**](ChannelPreferenceCreate.md) |  | 

## Example

```python
from moolabs.models.channel_preference_update import ChannelPreferenceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPreferenceUpdate from a JSON string
channel_preference_update_instance = ChannelPreferenceUpdate.from_json(json)
# print the JSON string representation of the object
print(ChannelPreferenceUpdate.to_json())

# convert the object into a dict
channel_preference_update_dict = channel_preference_update_instance.to_dict()
# create an instance of ChannelPreferenceUpdate from a dict
channel_preference_update_from_dict = ChannelPreferenceUpdate.from_dict(channel_preference_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


