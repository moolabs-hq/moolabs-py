# NotificationRuleInvoiceCreatedCreateRequest

Request with input parameters for creating new notification rule with invoice.created type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Notification rule type. | 
**name** | **str** | The user friendly name of the notification rule. | 
**disabled** | **bool** | Whether the rule is disabled or not. | [optional] [default to False]
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**channels** | **List[str]** | List of notification channels the rule is applied to. | 

## Example

```python
from moolabs.models.notification_rule_invoice_created_create_request import NotificationRuleInvoiceCreatedCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRuleInvoiceCreatedCreateRequest from a JSON string
notification_rule_invoice_created_create_request_instance = NotificationRuleInvoiceCreatedCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationRuleInvoiceCreatedCreateRequest.to_json())

# convert the object into a dict
notification_rule_invoice_created_create_request_dict = notification_rule_invoice_created_create_request_instance.to_dict()
# create an instance of NotificationRuleInvoiceCreatedCreateRequest from a dict
notification_rule_invoice_created_create_request_from_dict = NotificationRuleInvoiceCreatedCreateRequest.from_dict(notification_rule_invoice_created_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


