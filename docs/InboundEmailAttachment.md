# InboundEmailAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**content_type** | **str** |  | [optional] [default to 'application/octet-stream']
**content_base64** | **str** |  | 

## Example

```python
from moolabs.models.inbound_email_attachment import InboundEmailAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of InboundEmailAttachment from a JSON string
inbound_email_attachment_instance = InboundEmailAttachment.from_json(json)
# print the JSON string representation of the object
print(InboundEmailAttachment.to_json())

# convert the object into a dict
inbound_email_attachment_dict = inbound_email_attachment_instance.to_dict()
# create an instance of InboundEmailAttachment from a dict
inbound_email_attachment_from_dict = InboundEmailAttachment.from_dict(inbound_email_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


