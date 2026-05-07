# GrantsListResponse

Response for listing grants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GrantResponse]**](GrantResponse.md) |  | 
**total** | **int** |  | 
**total_remaining** | **float** |  | [optional] 

## Example

```python
from moolabs.models.grants_list_response import GrantsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GrantsListResponse from a JSON string
grants_list_response_instance = GrantsListResponse.from_json(json)
# print the JSON string representation of the object
print(GrantsListResponse.to_json())

# convert the object into a dict
grants_list_response_dict = grants_list_response_instance.to_dict()
# create an instance of GrantsListResponse from a dict
grants_list_response_from_dict = GrantsListResponse.from_dict(grants_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


