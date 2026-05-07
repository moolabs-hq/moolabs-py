# NotificationEventDeliveryStatus

The delivery status of the notification event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**NotificationEventDeliveryStatusState**](NotificationEventDeliveryStatusState.md) | Delivery state of the notification event to the channel. | [readonly] 
**reason** | **str** | The reason of the last deliverry state update. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the status was last updated in RFC 3339 format. | [readonly] 
**channel** | [**NotificationChannelMeta**](NotificationChannelMeta.md) | Notification channel the delivery status associated with. | [readonly] 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 
**next_attempt** | **datetime** | Timestamp of the next delivery attempt. If null it means there will be no more delivery attempts. | [optional] [readonly] 
**attempts** | [**List[NotificationEventDeliveryAttempt]**](NotificationEventDeliveryAttempt.md) | List of delivery attempts. | 

## Example

```python
from moolabs.models.notification_event_delivery_status import NotificationEventDeliveryStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventDeliveryStatus from a JSON string
notification_event_delivery_status_instance = NotificationEventDeliveryStatus.from_json(json)
# print the JSON string representation of the object
print(NotificationEventDeliveryStatus.to_json())

# convert the object into a dict
notification_event_delivery_status_dict = notification_event_delivery_status_instance.to_dict()
# create an instance of NotificationEventDeliveryStatus from a dict
notification_event_delivery_status_from_dict = NotificationEventDeliveryStatus.from_dict(notification_event_delivery_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


