# NotificationChannelMeta

Metadata only fields of a notification channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the notification channel. | [readonly] 
**type** | [**NotificationChannelType**](NotificationChannelType.md) | Notification channel type. | 

## Example

```python
from moolabs.models.notification_channel_meta import NotificationChannelMeta

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelMeta from a JSON string
notification_channel_meta_instance = NotificationChannelMeta.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelMeta.to_json())

# convert the object into a dict
notification_channel_meta_dict = notification_channel_meta_instance.to_dict()
# create an instance of NotificationChannelMeta from a dict
notification_channel_meta_from_dict = NotificationChannelMeta.from_dict(notification_channel_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


