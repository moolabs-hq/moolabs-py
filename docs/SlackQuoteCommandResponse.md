# SlackQuoteCommandResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** |  | [optional] [default to 'ephemeral']
**text** | **str** |  | 
**command_kind** | **str** |  | 
**deep_links** | **List[Dict[str, str]]** |  | [optional] 

## Example

```python
from moolabs.models.slack_quote_command_response import SlackQuoteCommandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SlackQuoteCommandResponse from a JSON string
slack_quote_command_response_instance = SlackQuoteCommandResponse.from_json(json)
# print the JSON string representation of the object
print(SlackQuoteCommandResponse.to_json())

# convert the object into a dict
slack_quote_command_response_dict = slack_quote_command_response_instance.to_dict()
# create an instance of SlackQuoteCommandResponse from a dict
slack_quote_command_response_from_dict = SlackQuoteCommandResponse.from_dict(slack_quote_command_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


