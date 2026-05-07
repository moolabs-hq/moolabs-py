# CreatePortalTokenRequest

Request to create a portal token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject the token is scoped to | 
**expires_in_seconds** | **int** | Token TTL (1m to 24h) | [optional] [default to 3600]
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from moolabs.models.create_portal_token_request import CreatePortalTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortalTokenRequest from a JSON string
create_portal_token_request_instance = CreatePortalTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePortalTokenRequest.to_json())

# convert the object into a dict
create_portal_token_request_dict = create_portal_token_request_instance.to_dict()
# create an instance of CreatePortalTokenRequest from a dict
create_portal_token_request_from_dict = CreatePortalTokenRequest.from_dict(create_portal_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


