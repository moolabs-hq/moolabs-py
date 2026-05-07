# AppPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[App]**](App.md) | The items in the current page. | 

## Example

```python
from moolabs.models.app_paginated_response import AppPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppPaginatedResponse from a JSON string
app_paginated_response_instance = AppPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AppPaginatedResponse.to_json())

# convert the object into a dict
app_paginated_response_dict = app_paginated_response_instance.to_dict()
# create an instance of AppPaginatedResponse from a dict
app_paginated_response_from_dict = AppPaginatedResponse.from_dict(app_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


