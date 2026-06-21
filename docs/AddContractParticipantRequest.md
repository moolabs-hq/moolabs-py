# AddContractParticipantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** |  | 
**role** | **str** |  | 
**email** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 

## Example

```python
from moolabs.models.add_contract_participant_request import AddContractParticipantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddContractParticipantRequest from a JSON string
add_contract_participant_request_instance = AddContractParticipantRequest.from_json(json)
# print the JSON string representation of the object
print(AddContractParticipantRequest.to_json())

# convert the object into a dict
add_contract_participant_request_dict = add_contract_participant_request_instance.to_dict()
# create an instance of AddContractParticipantRequest from a dict
add_contract_participant_request_from_dict = AddContractParticipantRequest.from_dict(add_contract_participant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


