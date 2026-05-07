# PlanAddonPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[PlanAddon]**](PlanAddon.md) | The items in the current page. | 

## Example

```python
from moolabs.models.plan_addon_paginated_response import PlanAddonPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanAddonPaginatedResponse from a JSON string
plan_addon_paginated_response_instance = PlanAddonPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PlanAddonPaginatedResponse.to_json())

# convert the object into a dict
plan_addon_paginated_response_dict = plan_addon_paginated_response_instance.to_dict()
# create an instance of PlanAddonPaginatedResponse from a dict
plan_addon_paginated_response_from_dict = PlanAddonPaginatedResponse.from_dict(plan_addon_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


