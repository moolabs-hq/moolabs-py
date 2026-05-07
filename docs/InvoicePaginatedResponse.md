# InvoicePaginatedResponse

Paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[Invoice]**](Invoice.md) | The items in the current page. | 

## Example

```python
from moolabs.models.invoice_paginated_response import InvoicePaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePaginatedResponse from a JSON string
invoice_paginated_response_instance = InvoicePaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(InvoicePaginatedResponse.to_json())

# convert the object into a dict
invoice_paginated_response_dict = invoice_paginated_response_instance.to_dict()
# create an instance of InvoicePaginatedResponse from a dict
invoice_paginated_response_from_dict = InvoicePaginatedResponse.from_dict(invoice_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


