# NotificationEventResendRequest

A notification event that will be re-sent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** | Notification channels to which the event should be re-sent. | [optional] 

## Example

```python
from moolabs.models.notification_event_resend_request import NotificationEventResendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventResendRequest from a JSON string
notification_event_resend_request_instance = NotificationEventResendRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationEventResendRequest.to_json())

# convert the object into a dict
notification_event_resend_request_dict = notification_event_resend_request_instance.to_dict()
# create an instance of NotificationEventResendRequest from a dict
notification_event_resend_request_from_dict = NotificationEventResendRequest.from_dict(notification_event_resend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


