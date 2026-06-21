# ContractDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**thread_id** | **str** |  | 
**quote_id** | **str** |  | 
**label** | **str** |  | 
**document_type** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.contract_document_response import ContractDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDocumentResponse from a JSON string
contract_document_response_instance = ContractDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(ContractDocumentResponse.to_json())

# convert the object into a dict
contract_document_response_dict = contract_document_response_instance.to_dict()
# create an instance of ContractDocumentResponse from a dict
contract_document_response_from_dict = ContractDocumentResponse.from_dict(contract_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


