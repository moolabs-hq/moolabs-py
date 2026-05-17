# ChannelPreferenceCreate

Body for creating/updating a channel preference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | One of: email, sms, phone, portal | 
**consent_status** | **str** | One of: unknown, granted, denied, revoked | [optional] [default to 'unknown']
**opt_out** | **bool** |  | [optional] [default to False]
**suppressed_until** | **datetime** |  | [optional] 
**consent_source** | **str** |  | [optional] 
**consent_captured_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.channel_preference_create import ChannelPreferenceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPreferenceCreate from a JSON string
channel_preference_create_instance = ChannelPreferenceCreate.from_json(json)
# print the JSON string representation of the object
print(ChannelPreferenceCreate.to_json())

# convert the object into a dict
channel_preference_create_dict = channel_preference_create_instance.to_dict()
# create an instance of ChannelPreferenceCreate from a dict
channel_preference_create_from_dict = ChannelPreferenceCreate.from_dict(channel_preference_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


