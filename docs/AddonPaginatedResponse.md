# AddonPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Addon]**](Addon.md) | The items in the current page. | 

## Example

```python
from moolabs.models.addon_paginated_response import AddonPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonPaginatedResponse from a JSON string
addon_paginated_response_instance = AddonPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AddonPaginatedResponse.to_json())

# convert the object into a dict
addon_paginated_response_dict = addon_paginated_response_instance.to_dict()
# create an instance of AddonPaginatedResponse from a dict
addon_paginated_response_from_dict = AddonPaginatedResponse.from_dict(addon_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


