# FeaturePaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Feature]**](Feature.md) | The items in the current page. | 

## Example

```python
from moolabs.models.feature_paginated_response import FeaturePaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePaginatedResponse from a JSON string
feature_paginated_response_instance = FeaturePaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(FeaturePaginatedResponse.to_json())

# convert the object into a dict
feature_paginated_response_dict = feature_paginated_response_instance.to_dict()
# create an instance of FeaturePaginatedResponse from a dict
feature_paginated_response_from_dict = FeaturePaginatedResponse.from_dict(feature_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


