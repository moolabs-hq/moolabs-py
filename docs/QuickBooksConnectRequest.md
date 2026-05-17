# QuickBooksConnectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** |  | 
**sync_direction** | **str** |  | 
**sync_frequency** | **str** |  | 
**owner** | **str** |  | [optional] 

## Example

```python
from moolabs.models.quick_books_connect_request import QuickBooksConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuickBooksConnectRequest from a JSON string
quick_books_connect_request_instance = QuickBooksConnectRequest.from_json(json)
# print the JSON string representation of the object
print(QuickBooksConnectRequest.to_json())

# convert the object into a dict
quick_books_connect_request_dict = quick_books_connect_request_instance.to_dict()
# create an instance of QuickBooksConnectRequest from a dict
quick_books_connect_request_from_dict = QuickBooksConnectRequest.from_dict(quick_books_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


