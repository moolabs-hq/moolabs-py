# SubscriptionPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Subscription]**](Subscription.md) | The items in the current page. | 

## Example

```python
from moolabs.models.subscription_paginated_response import SubscriptionPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaginatedResponse from a JSON string
subscription_paginated_response_instance = SubscriptionPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPaginatedResponse.to_json())

# convert the object into a dict
subscription_paginated_response_dict = subscription_paginated_response_instance.to_dict()
# create an instance of SubscriptionPaginatedResponse from a dict
subscription_paginated_response_from_dict = SubscriptionPaginatedResponse.from_dict(subscription_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


