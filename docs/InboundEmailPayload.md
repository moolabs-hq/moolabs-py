# InboundEmailPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient** | **str** |  | 
**from_email** | **str** |  | 
**message_id** | **str** |  | 
**subject** | **str** |  | [optional] 
**attachments** | [**List[InboundEmailAttachment]**](InboundEmailAttachment.md) |  | [optional] 

## Example

```python
from moolabs.models.inbound_email_payload import InboundEmailPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InboundEmailPayload from a JSON string
inbound_email_payload_instance = InboundEmailPayload.from_json(json)
# print the JSON string representation of the object
print(InboundEmailPayload.to_json())

# convert the object into a dict
inbound_email_payload_dict = inbound_email_payload_instance.to_dict()
# create an instance of InboundEmailPayload from a dict
inbound_email_payload_from_dict = InboundEmailPayload.from_dict(inbound_email_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


