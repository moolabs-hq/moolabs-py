# CommunicationListResponse

GET /cases/{case_id}/communications — paginated list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CommunicationResponse]**](CommunicationResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from moolabs.models.communication_list_response import CommunicationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationListResponse from a JSON string
communication_list_response_instance = CommunicationListResponse.from_json(json)
# print the JSON string representation of the object
print(CommunicationListResponse.to_json())

# convert the object into a dict
communication_list_response_dict = communication_list_response_instance.to_dict()
# create an instance of CommunicationListResponse from a dict
communication_list_response_from_dict = CommunicationListResponse.from_dict(communication_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


