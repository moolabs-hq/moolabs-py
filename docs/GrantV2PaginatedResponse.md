# GrantV2PaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[EntitlementGrantV2]**](EntitlementGrantV2.md) | The items in the current page. | 

## Example

```python
from moolabs.models.grant_v2_paginated_response import GrantV2PaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrantV2PaginatedResponse from a JSON string
grant_v2_paginated_response_instance = GrantV2PaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GrantV2PaginatedResponse.to_json())

# convert the object into a dict
grant_v2_paginated_response_dict = grant_v2_paginated_response_instance.to_dict()
# create an instance of GrantV2PaginatedResponse from a dict
grant_v2_paginated_response_from_dict = GrantV2PaginatedResponse.from_dict(grant_v2_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


