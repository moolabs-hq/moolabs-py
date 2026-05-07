# NotificationRuleBalanceThresholdCreateRequest

Request with input parameters for creating new notification rule with entitlements.balance.threshold type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Notification rule type. | 
**name** | **str** | The user friendly name of the notification rule. | 
**disabled** | **bool** | Whether the rule is disabled or not. | [optional] [default to False]
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**thresholds** | [**List[NotificationRuleBalanceThresholdValue]**](NotificationRuleBalanceThresholdValue.md) | List of thresholds the rule suppose to be triggered. | 
**channels** | **List[str]** | List of notification channels the rule is applied to. | 
**features** | **List[str]** | Optional field for defining the scope of notification by feature. It may contain features by id or key. | [optional] 

## Example

```python
from moolabs.models.notification_rule_balance_threshold_create_request import NotificationRuleBalanceThresholdCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRuleBalanceThresholdCreateRequest from a JSON string
notification_rule_balance_threshold_create_request_instance = NotificationRuleBalanceThresholdCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationRuleBalanceThresholdCreateRequest.to_json())

# convert the object into a dict
notification_rule_balance_threshold_create_request_dict = notification_rule_balance_threshold_create_request_instance.to_dict()
# create an instance of NotificationRuleBalanceThresholdCreateRequest from a dict
notification_rule_balance_threshold_create_request_from_dict = NotificationRuleBalanceThresholdCreateRequest.from_dict(notification_rule_balance_threshold_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


