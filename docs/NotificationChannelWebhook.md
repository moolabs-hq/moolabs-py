# NotificationChannelWebhook

Notification channel with webhook type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**id** | **str** | Identifies the notification channel. | [readonly] 
**type** | **str** | Notification channel type. | 
**name** | **str** | User friendly name of the channel. | 
**disabled** | **bool** | Whether the channel is disabled or not. | [optional] [default to False]
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**url** | **str** | Webhook URL where the notification is sent. | 
**custom_headers** | **Dict[str, str]** | Custom HTTP headers sent as part of the webhook request. | [optional] 
**signing_secret** | **str** | Signing secret used for webhook request validation on the receiving end.  Format: &#x60;base64&#x60; encoded random bytes optionally prefixed with &#x60;whsec_&#x60;. Recommended size: 24 | [optional] 

## Example

```python
from moolabs.models.notification_channel_webhook import NotificationChannelWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelWebhook from a JSON string
notification_channel_webhook_instance = NotificationChannelWebhook.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelWebhook.to_json())

# convert the object into a dict
notification_channel_webhook_dict = notification_channel_webhook_instance.to_dict()
# create an instance of NotificationChannelWebhook from a dict
notification_channel_webhook_from_dict = NotificationChannelWebhook.from_dict(notification_channel_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


