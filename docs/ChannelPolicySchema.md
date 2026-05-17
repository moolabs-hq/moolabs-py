# ChannelPolicySchema

Per-channel rate limits and quiet hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_per_week** | **int** |  | [optional] [default to 3]
**quiet_hours_start** | **str** |  | [optional] [default to '21:00']
**quiet_hours_end** | **str** |  | [optional] [default to '08:00']

## Example

```python
from moolabs.models.channel_policy_schema import ChannelPolicySchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelPolicySchema from a JSON string
channel_policy_schema_instance = ChannelPolicySchema.from_json(json)
# print the JSON string representation of the object
print(ChannelPolicySchema.to_json())

# convert the object into a dict
channel_policy_schema_dict = channel_policy_schema_instance.to_dict()
# create an instance of ChannelPolicySchema from a dict
channel_policy_schema_from_dict = ChannelPolicySchema.from_dict(channel_policy_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


