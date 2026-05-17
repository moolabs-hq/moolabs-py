# InvalidatePortalTokenRequest

Request to invalidate portal token(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Plaintext token to revoke | [optional] 
**subject** | **str** | Revoke all tokens for subject | [optional] 

## Example

```python
from moolabs.models.invalidate_portal_token_request import InvalidatePortalTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidatePortalTokenRequest from a JSON string
invalidate_portal_token_request_instance = InvalidatePortalTokenRequest.from_json(json)
# print the JSON string representation of the object
print(InvalidatePortalTokenRequest.to_json())

# convert the object into a dict
invalidate_portal_token_request_dict = invalidate_portal_token_request_instance.to_dict()
# create an instance of InvalidatePortalTokenRequest from a dict
invalidate_portal_token_request_from_dict = InvalidatePortalTokenRequest.from_dict(invalidate_portal_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


