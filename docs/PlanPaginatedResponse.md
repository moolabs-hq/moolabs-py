# PlanPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Plan]**](Plan.md) | The items in the current page. | 

## Example

```python
from moolabs.models.plan_paginated_response import PlanPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanPaginatedResponse from a JSON string
plan_paginated_response_instance = PlanPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(PlanPaginatedResponse.to_json())

# convert the object into a dict
plan_paginated_response_dict = plan_paginated_response_instance.to_dict()
# create an instance of PlanPaginatedResponse from a dict
plan_paginated_response_from_dict = PlanPaginatedResponse.from_dict(plan_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


