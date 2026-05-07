# NotificationEvent

Type of the notification event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier of the notification event. | [readonly] 
**type** | [**NotificationEventType**](NotificationEventType.md) | Type of the notification event. | [readonly] 
**created_at** | **datetime** | Timestamp when the notification event was created in RFC 3339 format. | [readonly] 
**rule** | [**NotificationRule**](NotificationRule.md) | The nnotification rule which generated this event. | [readonly] 
**delivery_status** | [**List[NotificationEventDeliveryStatus]**](NotificationEventDeliveryStatus.md) | The delivery status of the notification event. | 
**payload** | [**NotificationEventPayload**](NotificationEventPayload.md) | Timestamp when the notification event was created in RFC 3339 format. | [readonly] 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 

## Example

```python
from moolabs.models.notification_event import NotificationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEvent from a JSON string
notification_event_instance = NotificationEvent.from_json(json)
# print the JSON string representation of the object
print(NotificationEvent.to_json())

# convert the object into a dict
notification_event_dict = notification_event_instance.to_dict()
# create an instance of NotificationEvent from a dict
notification_event_from_dict = NotificationEvent.from_dict(notification_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


