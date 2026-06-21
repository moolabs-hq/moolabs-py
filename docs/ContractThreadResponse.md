# ContractThreadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | [optional] 
**status** | **str** |  | 
**subject** | **str** |  | [optional] 
**reply_alias** | **str** |  | 
**created_by_actor_id** | **str** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.contract_thread_response import ContractThreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractThreadResponse from a JSON string
contract_thread_response_instance = ContractThreadResponse.from_json(json)
# print the JSON string representation of the object
print(ContractThreadResponse.to_json())

# convert the object into a dict
contract_thread_response_dict = contract_thread_response_instance.to_dict()
# create an instance of ContractThreadResponse from a dict
contract_thread_response_from_dict = ContractThreadResponse.from_dict(contract_thread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


