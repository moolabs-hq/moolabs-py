# ContractThreadSnapshotResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread** | [**ContractThreadResponse**](ContractThreadResponse.md) |  | 
**participants** | [**List[ContractParticipantResponse]**](ContractParticipantResponse.md) |  | 
**documents** | [**List[ContractDocumentResponse]**](ContractDocumentResponse.md) |  | 
**events** | [**List[ContractEventResponse]**](ContractEventResponse.md) |  | 

## Example

```python
from moolabs.models.contract_thread_snapshot_response import ContractThreadSnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractThreadSnapshotResponse from a JSON string
contract_thread_snapshot_response_instance = ContractThreadSnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(ContractThreadSnapshotResponse.to_json())

# convert the object into a dict
contract_thread_snapshot_response_dict = contract_thread_snapshot_response_instance.to_dict()
# create an instance of ContractThreadSnapshotResponse from a dict
contract_thread_snapshot_response_from_dict = ContractThreadSnapshotResponse.from_dict(contract_thread_snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


