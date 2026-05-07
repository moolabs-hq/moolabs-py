# NotificationRuleBalanceThresholdValue

Threshold value with multiple supported types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | Value of the threshold. | 
**type** | [**NotificationRuleBalanceThresholdValueType**](NotificationRuleBalanceThresholdValueType.md) | Type of the threshold. | 

## Example

```python
from moolabs.models.notification_rule_balance_threshold_value import NotificationRuleBalanceThresholdValue

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRuleBalanceThresholdValue from a JSON string
notification_rule_balance_threshold_value_instance = NotificationRuleBalanceThresholdValue.from_json(json)
# print the JSON string representation of the object
print(NotificationRuleBalanceThresholdValue.to_json())

# convert the object into a dict
notification_rule_balance_threshold_value_dict = notification_rule_balance_threshold_value_instance.to_dict()
# create an instance of NotificationRuleBalanceThresholdValue from a dict
notification_rule_balance_threshold_value_from_dict = NotificationRuleBalanceThresholdValue.from_dict(notification_rule_balance_threshold_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


