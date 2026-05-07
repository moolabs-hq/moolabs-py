# CustomerPaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Customer]**](Customer.md) | The items in the current page. | 

## Example

```python
from moolabs.models.customer_paginated_response import CustomerPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPaginatedResponse from a JSON string
customer_paginated_response_instance = CustomerPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerPaginatedResponse.to_json())

# convert the object into a dict
customer_paginated_response_dict = customer_paginated_response_instance.to_dict()
# create an instance of CustomerPaginatedResponse from a dict
customer_paginated_response_from_dict = CustomerPaginatedResponse.from_dict(customer_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


