# NotificationRuleInvoiceCreated

Notification rule with invoice.created type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**id** | **str** | Identifies the notification rule. | [readonly] 
**type** | **str** | Notification rule type. | 
**name** | **str** | The user friendly name of the notification rule. | 
**disabled** | **bool** | Whether the rule is disabled or not. | [optional] [default to False]
**channels** | [**List[NotificationChannelMeta]**](NotificationChannelMeta.md) | List of notification channels the rule applies to. | 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 

## Example

```python
from moolabs.models.notification_rule_invoice_created import NotificationRuleInvoiceCreated

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRuleInvoiceCreated from a JSON string
notification_rule_invoice_created_instance = NotificationRuleInvoiceCreated.from_json(json)
# print the JSON string representation of the object
print(NotificationRuleInvoiceCreated.to_json())

# convert the object into a dict
notification_rule_invoice_created_dict = notification_rule_invoice_created_instance.to_dict()
# create an instance of NotificationRuleInvoiceCreated from a dict
notification_rule_invoice_created_from_dict = NotificationRuleInvoiceCreated.from_dict(notification_rule_invoice_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


