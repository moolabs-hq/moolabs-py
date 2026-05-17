# ChatMessageIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from moolabs.models.chat_message_in import ChatMessageIn

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageIn from a JSON string
chat_message_in_instance = ChatMessageIn.from_json(json)
# print the JSON string representation of the object
print(ChatMessageIn.to_json())

# convert the object into a dict
chat_message_in_dict = chat_message_in_instance.to_dict()
# create an instance of ChatMessageIn from a dict
chat_message_in_from_dict = ChatMessageIn.from_dict(chat_message_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


