# RevokePortalTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 

## Example

```python
from moolabs.models.revoke_portal_token_request import RevokePortalTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokePortalTokenRequest from a JSON string
revoke_portal_token_request_instance = RevokePortalTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RevokePortalTokenRequest.to_json())

# convert the object into a dict
revoke_portal_token_request_dict = revoke_portal_token_request_instance.to_dict()
# create an instance of RevokePortalTokenRequest from a dict
revoke_portal_token_request_from_dict = RevokePortalTokenRequest.from_dict(revoke_portal_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


