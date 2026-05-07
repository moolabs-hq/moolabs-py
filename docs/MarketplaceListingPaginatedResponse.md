# MarketplaceListingPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[MarketplaceListing]**](MarketplaceListing.md) | The items in the current page. | 

## Example

```python
from moolabs.models.marketplace_listing_paginated_response import MarketplaceListingPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceListingPaginatedResponse from a JSON string
marketplace_listing_paginated_response_instance = MarketplaceListingPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceListingPaginatedResponse.to_json())

# convert the object into a dict
marketplace_listing_paginated_response_dict = marketplace_listing_paginated_response_instance.to_dict()
# create an instance of MarketplaceListingPaginatedResponse from a dict
marketplace_listing_paginated_response_from_dict = MarketplaceListingPaginatedResponse.from_dict(marketplace_listing_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


