# AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** |  | 
**tenant_id** | **str** |  | 
**subscription_id** | **str** |  | 
**customer_id** | **str** |  | 
**plan_ref** | [**PlanRefPayload**](PlanRefPayload.md) |  | 
**effective_at** | **datetime** |  | [optional] 
**subscription** | **Dict[str, object]** |  | 
**commercial_overrides** | [**CommercialOverridesPayload**](CommercialOverridesPayload.md) |  | [optional] 

## Example

```python
from moolabs.models.app_api_v1_internal_subscription_sync_schemas_subscription_sync_request import AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest from a JSON string
app_api_v1_internal_subscription_sync_schemas_subscription_sync_request_instance = AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest.from_json(json)
# print the JSON string representation of the object
print(AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest.to_json())

# convert the object into a dict
app_api_v1_internal_subscription_sync_schemas_subscription_sync_request_dict = app_api_v1_internal_subscription_sync_schemas_subscription_sync_request_instance.to_dict()
# create an instance of AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest from a dict
app_api_v1_internal_subscription_sync_schemas_subscription_sync_request_from_dict = AppApiV1InternalSubscriptionSyncSchemasSubscriptionSyncRequest.from_dict(app_api_v1_internal_subscription_sync_schemas_subscription_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


