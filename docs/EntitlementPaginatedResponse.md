# EntitlementPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Entitlement]**](Entitlement.md) | The items in the current page. | 

## Example

```python
from moolabs.models.entitlement_paginated_response import EntitlementPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementPaginatedResponse from a JSON string
entitlement_paginated_response_instance = EntitlementPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(EntitlementPaginatedResponse.to_json())

# convert the object into a dict
entitlement_paginated_response_dict = entitlement_paginated_response_instance.to_dict()
# create an instance of EntitlementPaginatedResponse from a dict
entitlement_paginated_response_from_dict = EntitlementPaginatedResponse.from_dict(entitlement_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


