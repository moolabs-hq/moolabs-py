# NotificationEventPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[NotificationEvent]**](NotificationEvent.md) | The items in the current page. | 

## Example

```python
from moolabs.models.notification_event_paginated_response import NotificationEventPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationEventPaginatedResponse from a JSON string
notification_event_paginated_response_instance = NotificationEventPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationEventPaginatedResponse.to_json())

# convert the object into a dict
notification_event_paginated_response_dict = notification_event_paginated_response_instance.to_dict()
# create an instance of NotificationEventPaginatedResponse from a dict
notification_event_paginated_response_from_dict = NotificationEventPaginatedResponse.from_dict(notification_event_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


