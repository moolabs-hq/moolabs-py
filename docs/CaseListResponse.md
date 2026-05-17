# CaseListResponse

GET /cases — paginated list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CaseListItemResponse]**](CaseListItemResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from moolabs.models.case_list_response import CaseListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CaseListResponse from a JSON string
case_list_response_instance = CaseListResponse.from_json(json)
# print the JSON string representation of the object
print(CaseListResponse.to_json())

# convert the object into a dict
case_list_response_dict = case_list_response_instance.to_dict()
# create an instance of CaseListResponse from a dict
case_list_response_from_dict = CaseListResponse.from_dict(case_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


