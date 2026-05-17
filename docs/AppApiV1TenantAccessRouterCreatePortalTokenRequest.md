# AppApiV1TenantAccessRouterCreatePortalTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 
**expires_in_seconds** | **int** |  | [optional] [default to 3600]

## Example

```python
from moolabs.models.app_api_v1_tenant_access_router_create_portal_token_request import AppApiV1TenantAccessRouterCreatePortalTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApiV1TenantAccessRouterCreatePortalTokenRequest from a JSON string
app_api_v1_tenant_access_router_create_portal_token_request_instance = AppApiV1TenantAccessRouterCreatePortalTokenRequest.from_json(json)
# print the JSON string representation of the object
print(AppApiV1TenantAccessRouterCreatePortalTokenRequest.to_json())

# convert the object into a dict
app_api_v1_tenant_access_router_create_portal_token_request_dict = app_api_v1_tenant_access_router_create_portal_token_request_instance.to_dict()
# create an instance of AppApiV1TenantAccessRouterCreatePortalTokenRequest from a dict
app_api_v1_tenant_access_router_create_portal_token_request_from_dict = AppApiV1TenantAccessRouterCreatePortalTokenRequest.from_dict(app_api_v1_tenant_access_router_create_portal_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


