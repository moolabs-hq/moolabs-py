# NotificationRulePaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[NotificationRule]**](NotificationRule.md) | The items in the current page. | 

## Example

```python
from moolabs.models.notification_rule_paginated_response import NotificationRulePaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRulePaginatedResponse from a JSON string
notification_rule_paginated_response_instance = NotificationRulePaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationRulePaginatedResponse.to_json())

# convert the object into a dict
notification_rule_paginated_response_dict = notification_rule_paginated_response_instance.to_dict()
# create an instance of NotificationRulePaginatedResponse from a dict
notification_rule_paginated_response_from_dict = NotificationRulePaginatedResponse.from_dict(notification_rule_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


