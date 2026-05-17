# CommunicationResponse

Communication response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | 
**account_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**direction** | **str** |  | 
**channel** | **str** |  | 
**status** | **str** |  | 
**audience** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**thread_id** | **str** |  | [optional] 
**parent_communication_id** | **str** |  | [optional] 
**dunning_stage** | **str** |  | 
**generated_by** | **str** |  | 
**approval_request_id** | **str** |  | [optional] 
**sent_at** | **datetime** |  | [optional] 
**opened_at** | **datetime** |  | [optional] 
**clicked_at** | **datetime** |  | [optional] 
**reply_detected_at** | **datetime** |  | [optional] 
**external_message_id** | **str** |  | [optional] 
**consent_snapshot** | **Dict[str, object]** |  | [optional] 
**jurisdiction_snapshot** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.communication_response import CommunicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationResponse from a JSON string
communication_response_instance = CommunicationResponse.from_json(json)
# print the JSON string representation of the object
print(CommunicationResponse.to_json())

# convert the object into a dict
communication_response_dict = communication_response_instance.to_dict()
# create an instance of CommunicationResponse from a dict
communication_response_from_dict = CommunicationResponse.from_dict(communication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


