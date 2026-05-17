# AppApiV1PortalRouterCreatePortalTokenRequest

Request to create a portal token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Subject the token is scoped to | 
**expires_in_seconds** | **int** | Token TTL (1m to 24h) | [optional] [default to 3600]
**scopes** | **List[str]** | Optional scope list | [optional] 

## Example

```python
from moolabs.models.app_api_v1_portal_router_create_portal_token_request import AppApiV1PortalRouterCreatePortalTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApiV1PortalRouterCreatePortalTokenRequest from a JSON string
app_api_v1_portal_router_create_portal_token_request_instance = AppApiV1PortalRouterCreatePortalTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AppApiV1PortalRouterCreatePortalTokenRequest.to_json())

# convert the object into a dict
app_api_v1_portal_router_create_portal_token_request_dict = app_api_v1_portal_router_create_portal_token_request_instance.to_dict()
# create an instance of AppApiV1PortalRouterCreatePortalTokenRequest from a dict
app_api_v1_portal_router_create_portal_token_request_from_dict = AppApiV1PortalRouterCreatePortalTokenRequest.from_dict(app_api_v1_portal_router_create_portal_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


