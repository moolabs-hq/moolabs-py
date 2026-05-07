# CustomerAppDataPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[CustomerAppData]**](CustomerAppData.md) | The items in the current page. | 

## Example

```python
from moolabs.models.customer_app_data_paginated_response import CustomerAppDataPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAppDataPaginatedResponse from a JSON string
customer_app_data_paginated_response_instance = CustomerAppDataPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerAppDataPaginatedResponse.to_json())

# convert the object into a dict
customer_app_data_paginated_response_dict = customer_app_data_paginated_response_instance.to_dict()
# create an instance of CustomerAppDataPaginatedResponse from a dict
customer_app_data_paginated_response_from_dict = CustomerAppDataPaginatedResponse.from_dict(customer_app_data_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


