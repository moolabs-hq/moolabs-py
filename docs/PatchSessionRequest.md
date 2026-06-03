# PatchSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scratchpad** | **Dict[str, object]** |  | [optional] 
**line_items** | [**List[QuoteLineItemInput]**](QuoteLineItemInput.md) |  | [optional] 
**commercial_terms** | **Dict[str, object]** |  | [optional] 
**credit_terms** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.patch_session_request import PatchSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSessionRequest from a JSON string
patch_session_request_instance = PatchSessionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSessionRequest.to_json())

# convert the object into a dict
patch_session_request_dict = patch_session_request_instance.to_dict()
# create an instance of PatchSessionRequest from a dict
patch_session_request_from_dict = PatchSessionRequest.from_dict(patch_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


