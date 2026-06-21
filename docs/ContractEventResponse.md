# ContractEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**thread_id** | **str** |  | 
**quote_id** | **str** |  | 
**event_type** | **str** |  | 
**actor_type** | **str** |  | 
**actor_id** | **str** |  | [optional] 
**participant_id** | **str** |  | [optional] 
**document_version_id** | **str** |  | [optional] 
**safe_metadata** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.contract_event_response import ContractEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractEventResponse from a JSON string
contract_event_response_instance = ContractEventResponse.from_json(json)
# print the JSON string representation of the object
print(ContractEventResponse.to_json())

# convert the object into a dict
contract_event_response_dict = contract_event_response_instance.to_dict()
# create an instance of ContractEventResponse from a dict
contract_event_response_from_dict = ContractEventResponse.from_dict(contract_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


