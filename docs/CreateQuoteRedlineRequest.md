# CreateQuoteRedlineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_version** | **int** |  | 
**source** | **str** |  | 
**proposed_terms** | **Dict[str, object]** |  | [optional] 
**redline_text** | **str** |  | 
**evidence_metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.create_quote_redline_request import CreateQuoteRedlineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuoteRedlineRequest from a JSON string
create_quote_redline_request_instance = CreateQuoteRedlineRequest.from_json(json)
# print the JSON string representation of the object
print(CreateQuoteRedlineRequest.to_json())

# convert the object into a dict
create_quote_redline_request_dict = create_quote_redline_request_instance.to_dict()
# create an instance of CreateQuoteRedlineRequest from a dict
create_quote_redline_request_from_dict = CreateQuoteRedlineRequest.from_dict(create_quote_redline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


