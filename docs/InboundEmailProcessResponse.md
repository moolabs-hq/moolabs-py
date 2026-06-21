# InboundEmailProcessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inbound_message_id** | **str** |  | 
**status** | **str** |  | 
**created** | **bool** |  | 
**version** | [**ContractVersionResponse**](ContractVersionResponse.md) |  | [optional] 

## Example

```python
from moolabs.models.inbound_email_process_response import InboundEmailProcessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundEmailProcessResponse from a JSON string
inbound_email_process_response_instance = InboundEmailProcessResponse.from_json(json)
# print the JSON string representation of the object
print(InboundEmailProcessResponse.to_json())

# convert the object into a dict
inbound_email_process_response_dict = inbound_email_process_response_instance.to_dict()
# create an instance of InboundEmailProcessResponse from a dict
inbound_email_process_response_from_dict = InboundEmailProcessResponse.from_dict(inbound_email_process_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


