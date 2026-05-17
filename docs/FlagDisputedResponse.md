# FlagDisputedResponse

Response for invoice flag-disputed actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_id** | **str** |  | 
**action** | **str** |  | 
**new_status** | **str** |  | 
**message** | **str** |  | 
**dispute_id** | **str** |  | 
**invoice_id** | **str** |  | 

## Example

```python
from moolabs.models.flag_disputed_response import FlagDisputedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagDisputedResponse from a JSON string
flag_disputed_response_instance = FlagDisputedResponse.from_json(json)
# print the JSON string representation of the object
print(FlagDisputedResponse.to_json())

# convert the object into a dict
flag_disputed_response_dict = flag_disputed_response_instance.to_dict()
# create an instance of FlagDisputedResponse from a dict
flag_disputed_response_from_dict = FlagDisputedResponse.from_dict(flag_disputed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


