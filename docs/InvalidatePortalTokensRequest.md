# InvalidatePortalTokensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Invalidate a portal token by ID. | [optional] 
**subject** | **str** | Invalidate all portal tokens for a subject. | [optional] 

## Example

```python
from moolabs.models.invalidate_portal_tokens_request import InvalidatePortalTokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidatePortalTokensRequest from a JSON string
invalidate_portal_tokens_request_instance = InvalidatePortalTokensRequest.from_json(json)
# print the JSON string representation of the object
print(InvalidatePortalTokensRequest.to_json())

# convert the object into a dict
invalidate_portal_tokens_request_dict = invalidate_portal_tokens_request_instance.to_dict()
# create an instance of InvalidatePortalTokensRequest from a dict
invalidate_portal_tokens_request_from_dict = InvalidatePortalTokensRequest.from_dict(invalidate_portal_tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


