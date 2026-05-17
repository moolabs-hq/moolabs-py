# SenderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_name** | **str** |  | 
**from_address** | **str** |  | 
**reply_to** | **str** |  | 
**support_contact** | **str** |  | 

## Example

```python
from moolabs.models.sender_response import SenderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SenderResponse from a JSON string
sender_response_instance = SenderResponse.from_json(json)
# print the JSON string representation of the object
print(SenderResponse.to_json())

# convert the object into a dict
sender_response_dict = sender_response_instance.to_dict()
# create an instance of SenderResponse from a dict
sender_response_from_dict = SenderResponse.from_dict(sender_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


