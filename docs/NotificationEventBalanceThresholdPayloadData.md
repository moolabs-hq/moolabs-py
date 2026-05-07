# NotificationEventBalanceThresholdPayloadData

Data of the payload for notification event with `entitlements.balance.threshold` type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement** | [**EntitlementMetered**](EntitlementMetered.md) |  | [readonly] 
**feature** | [**Feature**](Feature.md) |  | [readonly] 
**subject** | [**Subject**](Subject.md) |  | [readonly] 
**value** | [**EntitlementValue**](EntitlementValue.md) |  | [readonly] 
**customer** | [**Customer**](Customer.md) |  | [optional] [readonly] 
**threshold** | [**NotificationRuleBalanceThresholdValue**](NotificationRuleBalanceThresholdValue.md) |  | [readonly] 

## Example

```python
from moolabs.models.notification_event_balance_threshold_payload_data import NotificationEventBalanceThresholdPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventBalanceThresholdPayloadData from a JSON string
notification_event_balance_threshold_payload_data_instance = NotificationEventBalanceThresholdPayloadData.from_json(json)
# print the JSON string representation of the object
print(NotificationEventBalanceThresholdPayloadData.to_json())

# convert the object into a dict
notification_event_balance_threshold_payload_data_dict = notification_event_balance_threshold_payload_data_instance.to_dict()
# create an instance of NotificationEventBalanceThresholdPayloadData from a dict
notification_event_balance_threshold_payload_data_from_dict = NotificationEventBalanceThresholdPayloadData.from_dict(notification_event_balance_threshold_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


