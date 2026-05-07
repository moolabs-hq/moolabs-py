# ListGrantsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | The total number of items. | 
**page** | **int** | The page index. | 
**page_size** | **int** | The maximum number of items per page. | 
**items** | [**List[EntitlementGrant]**](EntitlementGrant.md) | The items in the current page. | 

## Example

```python
from moolabs.models.list_grants_get200_response import ListGrantsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGrantsGet200Response from a JSON string
list_grants_get200_response_instance = ListGrantsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ListGrantsGet200Response.to_json())

# convert the object into a dict
list_grants_get200_response_dict = list_grants_get200_response_instance.to_dict()
# create an instance of ListGrantsGet200Response from a dict
list_grants_get200_response_from_dict = ListGrantsGet200Response.from_dict(list_grants_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


