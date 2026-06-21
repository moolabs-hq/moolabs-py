# ContractInboundMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**thread_id** | **str** |  | 
**provider_message_id** | **str** |  | 
**from_email** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**status** | **str** |  | 
**quarantine_reason** | **str** |  | [optional] 
**safe_metadata** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.contract_inbound_message_response import ContractInboundMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractInboundMessageResponse from a JSON string
contract_inbound_message_response_instance = ContractInboundMessageResponse.from_json(json)
# print the JSON string representation of the object
print(ContractInboundMessageResponse.to_json())

# convert the object into a dict
contract_inbound_message_response_dict = contract_inbound_message_response_instance.to_dict()
# create an instance of ContractInboundMessageResponse from a dict
contract_inbound_message_response_from_dict = ContractInboundMessageResponse.from_dict(contract_inbound_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


