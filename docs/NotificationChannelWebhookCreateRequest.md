# NotificationChannelWebhookCreateRequest

Request with input parameters for creating new notification channel with webhook type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Notification channel type. | 
**name** | **str** | User friendly name of the channel. | 
**disabled** | **bool** | Whether the channel is disabled or not. | [optional] [default to False]
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**url** | **str** | Webhook URL where the notification is sent. | 
**custom_headers** | **Dict[str, str]** | Custom HTTP headers sent as part of the webhook request. | [optional] 
**signing_secret** | **str** | Signing secret used for webhook request validation on the receiving end.  Format: &#x60;base64&#x60; encoded random bytes optionally prefixed with &#x60;whsec_&#x60;. Recommended size: 24 | [optional] 

## Example

```python
from moolabs.models.notification_channel_webhook_create_request import NotificationChannelWebhookCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelWebhookCreateRequest from a JSON string
notification_channel_webhook_create_request_instance = NotificationChannelWebhookCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelWebhookCreateRequest.to_json())

# convert the object into a dict
notification_channel_webhook_create_request_dict = notification_channel_webhook_create_request_instance.to_dict()
# create an instance of NotificationChannelWebhookCreateRequest from a dict
notification_channel_webhook_create_request_from_dict = NotificationChannelWebhookCreateRequest.from_dict(notification_channel_webhook_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


