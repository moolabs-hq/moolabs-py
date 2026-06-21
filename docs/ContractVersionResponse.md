# ContractVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**thread_id** | **str** |  | 
**document_id** | **str** |  | 
**quote_id** | **str** |  | 
**version_no** | **int** |  | 
**source** | **str** |  | 
**participant_id** | **str** |  | [optional] 
**inbound_message_id** | **str** |  | [optional] 
**filename** | **str** |  | 
**content_type** | **str** |  | 
**size_bytes** | **int** |  | 
**artifact_hash** | **str** |  | 
**scan_status** | **str** |  | 
**extracted_text** | **str** |  | 
**structure** | **Dict[str, object]** |  | 
**provider_message_id** | **str** |  | [optional] 
**email_subject** | **str** |  | [optional] 
**received_at** | **datetime** |  | [optional] 
**created_by_actor_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.contract_version_response import ContractVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractVersionResponse from a JSON string
contract_version_response_instance = ContractVersionResponse.from_json(json)
# print the JSON string representation of the object
print(ContractVersionResponse.to_json())

# convert the object into a dict
contract_version_response_dict = contract_version_response_instance.to_dict()
# create an instance of ContractVersionResponse from a dict
contract_version_response_from_dict = ContractVersionResponse.from_dict(contract_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


