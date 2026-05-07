# NotificationEventEntitlementValuePayloadBase

Base data for any payload with entitlement entitlement value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement** | [**EntitlementMetered**](EntitlementMetered.md) |  | [readonly] 
**feature** | [**Feature**](Feature.md) |  | [readonly] 
**subject** | [**Subject**](Subject.md) |  | [readonly] 
**value** | [**EntitlementValue**](EntitlementValue.md) |  | [readonly] 
**customer** | [**Customer**](Customer.md) |  | [optional] [readonly] 

## Example

```python
from moolabs.models.notification_event_entitlement_value_payload_base import NotificationEventEntitlementValuePayloadBase

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventEntitlementValuePayloadBase from a JSON string
notification_event_entitlement_value_payload_base_instance = NotificationEventEntitlementValuePayloadBase.from_json(json)
# print the JSON string representation of the object
print(NotificationEventEntitlementValuePayloadBase.to_json())

# convert the object into a dict
notification_event_entitlement_value_payload_base_dict = notification_event_entitlement_value_payload_base_instance.to_dict()
# create an instance of NotificationEventEntitlementValuePayloadBase from a dict
notification_event_entitlement_value_payload_base_from_dict = NotificationEventEntitlementValuePayloadBase.from_dict(notification_event_entitlement_value_payload_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


