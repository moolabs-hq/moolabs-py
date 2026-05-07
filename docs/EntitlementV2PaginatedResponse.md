# EntitlementV2PaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[EntitlementV2]**](EntitlementV2.md) | The items in the current page. | 

## Example

```python
from moolabs.models.entitlement_v2_paginated_response import EntitlementV2PaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementV2PaginatedResponse from a JSON string
entitlement_v2_paginated_response_instance = EntitlementV2PaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(EntitlementV2PaginatedResponse.to_json())

# convert the object into a dict
entitlement_v2_paginated_response_dict = entitlement_v2_paginated_response_instance.to_dict()
# create an instance of EntitlementV2PaginatedResponse from a dict
entitlement_v2_paginated_response_from_dict = EntitlementV2PaginatedResponse.from_dict(entitlement_v2_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


