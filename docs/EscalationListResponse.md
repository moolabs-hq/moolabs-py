# EscalationListResponse

GET /cases/{case_id}/escalations — paginated list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EscalationResponse]**](EscalationResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 

## Example

```python
from moolabs.models.escalation_list_response import EscalationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EscalationListResponse from a JSON string
escalation_list_response_instance = EscalationListResponse.from_json(json)
# print the JSON string representation of the object
print(EscalationListResponse.to_json())

# convert the object into a dict
escalation_list_response_dict = escalation_list_response_instance.to_dict()
# create an instance of EscalationListResponse from a dict
escalation_list_response_from_dict = EscalationListResponse.from_dict(escalation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


