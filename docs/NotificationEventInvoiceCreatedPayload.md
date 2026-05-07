# NotificationEventInvoiceCreatedPayload

Payload for notification event with `invoice.created` type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the notification event the payload belongs to. | [readonly] 
**type** | **str** | Type of the notification event. | [readonly] 
**timestamp** | **datetime** | Timestamp when the notification event was created in RFC 3339 format. | [readonly] 
**data** | [**Invoice**](Invoice.md) | The data of the payload. | [readonly] 

## Example

```python
from moolabs.models.notification_event_invoice_created_payload import NotificationEventInvoiceCreatedPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventInvoiceCreatedPayload from a JSON string
notification_event_invoice_created_payload_instance = NotificationEventInvoiceCreatedPayload.from_json(json)
# print the JSON string representation of the object
print(NotificationEventInvoiceCreatedPayload.to_json())

# convert the object into a dict
notification_event_invoice_created_payload_dict = notification_event_invoice_created_payload_instance.to_dict()
# create an instance of NotificationEventInvoiceCreatedPayload from a dict
notification_event_invoice_created_payload_from_dict = NotificationEventInvoiceCreatedPayload.from_dict(notification_event_invoice_created_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


