# AskMooRedlineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_id** | **str** |  | 
**family_id** | **str** |  | [optional] 
**anchor_char_start** | **int** |  | 
**anchor_char_end** | **int** |  | 
**instruction** | **str** |  | 
**anchor_quote** | **str** |  | [optional] 

## Example

```python
from moolabs.models.ask_moo_redline_request import AskMooRedlineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AskMooRedlineRequest from a JSON string
ask_moo_redline_request_instance = AskMooRedlineRequest.from_json(json)
# print the JSON string representation of the object
print(AskMooRedlineRequest.to_json())

# convert the object into a dict
ask_moo_redline_request_dict = ask_moo_redline_request_instance.to_dict()
# create an instance of AskMooRedlineRequest from a dict
ask_moo_redline_request_from_dict = AskMooRedlineRequest.from_dict(ask_moo_redline_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


