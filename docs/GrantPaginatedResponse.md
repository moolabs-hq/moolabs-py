# GrantPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[EntitlementGrant]**](EntitlementGrant.md) | The items in the current page. | 

## Example

```python
from moolabs.models.grant_paginated_response import GrantPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrantPaginatedResponse from a JSON string
grant_paginated_response_instance = GrantPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GrantPaginatedResponse.to_json())

# convert the object into a dict
grant_paginated_response_dict = grant_paginated_response_instance.to_dict()
# create an instance of GrantPaginatedResponse from a dict
grant_paginated_response_from_dict = GrantPaginatedResponse.from_dict(grant_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


