# GoogleChatQuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**cards_v2** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from moolabs.models.google_chat_quote_response import GoogleChatQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleChatQuoteResponse from a JSON string
google_chat_quote_response_instance = GoogleChatQuoteResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleChatQuoteResponse.to_json())

# convert the object into a dict
google_chat_quote_response_dict = google_chat_quote_response_instance.to_dict()
# create an instance of GoogleChatQuoteResponse from a dict
google_chat_quote_response_from_dict = GoogleChatQuoteResponse.from_dict(google_chat_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


