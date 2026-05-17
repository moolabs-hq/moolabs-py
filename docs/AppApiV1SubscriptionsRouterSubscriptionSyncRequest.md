# AppApiV1SubscriptionsRouterSubscriptionSyncRequest

Request to sync a subscription from OpenMeter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Subscription ID from OpenMeter | 
**customer_id** | **str** | Customer ID | [optional] 
**status** | **str** | Subscription status | [optional] [default to 'active']
**billing_cadence** | **str** | Billing cadence (ISO 8601 duration) | [optional] [default to 'P1M']
**billing_anchor** | **str** | Billing anchor date | 
**plan_id** | **str** | Plan ID | 
**plan_version** | **str** | Plan version | [optional] [default to '1']
**active_from** | **str** | Active from date (ISO 8601) | 
**active_to** | **str** | Active to date (ISO 8601) | [optional] 
**effective_at** | **str** | When this change takes effect (ISO 8601) | [optional] 
**feature_overrides** | [**List[FeatureOverrideRequest]**](FeatureOverrideRequest.md) | Per-feature price overrides | [optional] 
**feature_prices** | [**List[FeaturePriceRequest]**](FeaturePriceRequest.md) | Per-feature pricing | [optional] 

## Example

```python
from moolabs.models.app_api_v1_subscriptions_router_subscription_sync_request import AppApiV1SubscriptionsRouterSubscriptionSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppApiV1SubscriptionsRouterSubscriptionSyncRequest from a JSON string
app_api_v1_subscriptions_router_subscription_sync_request_instance = AppApiV1SubscriptionsRouterSubscriptionSyncRequest.from_json(json)
# print the JSON string representation of the object
print(AppApiV1SubscriptionsRouterSubscriptionSyncRequest.to_json())

# convert the object into a dict
app_api_v1_subscriptions_router_subscription_sync_request_dict = app_api_v1_subscriptions_router_subscription_sync_request_instance.to_dict()
# create an instance of AppApiV1SubscriptionsRouterSubscriptionSyncRequest from a dict
app_api_v1_subscriptions_router_subscription_sync_request_from_dict = AppApiV1SubscriptionsRouterSubscriptionSyncRequest.from_dict(app_api_v1_subscriptions_router_subscription_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


