# NotificationEventDeliveryAttempt

The delivery attempt of the notification event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**NotificationEventDeliveryStatusState**](NotificationEventDeliveryStatusState.md) | State of teh delivery attempt. | [readonly] 
**response** | [**EventDeliveryAttemptResponse**](EventDeliveryAttemptResponse.md) | Response returned by the notification event recipient. | [readonly] 
**timestamp** | **datetime** | Timestamp of the delivery attempt. | [readonly] 

## Example

```python
from moolabs.models.notification_event_delivery_attempt import NotificationEventDeliveryAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventDeliveryAttempt from a JSON string
notification_event_delivery_attempt_instance = NotificationEventDeliveryAttempt.from_json(json)
# print the JSON string representation of the object
print(NotificationEventDeliveryAttempt.to_json())

# convert the object into a dict
notification_event_delivery_attempt_dict = notification_event_delivery_attempt_instance.to_dict()
# create an instance of NotificationEventDeliveryAttempt from a dict
notification_event_delivery_attempt_from_dict = NotificationEventDeliveryAttempt.from_dict(notification_event_delivery_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


