# NotificationChannelPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[NotificationChannelWebhook]**](NotificationChannelWebhook.md) | The items in the current page. | 

## Example

```python
from moolabs.models.notification_channel_paginated_response import NotificationChannelPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelPaginatedResponse from a JSON string
notification_channel_paginated_response_instance = NotificationChannelPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelPaginatedResponse.to_json())

# convert the object into a dict
notification_channel_paginated_response_dict = notification_channel_paginated_response_instance.to_dict()
# create an instance of NotificationChannelPaginatedResponse from a dict
notification_channel_paginated_response_from_dict = NotificationChannelPaginatedResponse.from_dict(notification_channel_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


