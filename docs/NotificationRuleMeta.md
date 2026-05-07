# NotificationRuleMeta

Metadata only fields of a notification channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the notification rule. | [readonly] 
**type** | [**NotificationEventType**](NotificationEventType.md) | Notification rule type. | [readonly] 

## Example

```python
from moolabs.models.notification_rule_meta import NotificationRuleMeta

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRuleMeta from a JSON string
notification_rule_meta_instance = NotificationRuleMeta.from_json(json)
# print the JSON string representation of the object
print(NotificationRuleMeta.to_json())

# convert the object into a dict
notification_rule_meta_dict = notification_rule_meta_instance.to_dict()
# create an instance of NotificationRuleMeta from a dict
notification_rule_meta_from_dict = NotificationRuleMeta.from_dict(notification_rule_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


