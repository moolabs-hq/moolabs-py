# RemoveContractParticipantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**thread_id** | **str** |  | 
**side** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**status** | **str** |  | 
**added_by_actor_id** | **str** |  | 
**removed_by_actor_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.remove_contract_participant_response import RemoveContractParticipantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveContractParticipantResponse from a JSON string
remove_contract_participant_response_instance = RemoveContractParticipantResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveContractParticipantResponse.to_json())

# convert the object into a dict
remove_contract_participant_response_dict = remove_contract_participant_response_instance.to_dict()
# create an instance of RemoveContractParticipantResponse from a dict
remove_contract_participant_response_from_dict = RemoveContractParticipantResponse.from_dict(remove_contract_participant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


