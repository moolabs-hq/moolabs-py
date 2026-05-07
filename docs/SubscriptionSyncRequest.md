# SubscriptionSyncRequest

Request to sync a subscription from OpenMeter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Subscription ID from OpenMeter | 
**customer_id** | **str** |  | [optional] 
**status** | **str** | Subscription status | [optional] [default to 'active']
**billing_cadence** | **str** | Billing cadence (ISO 8601 duration) | [optional] [default to 'P1M']
**billing_anchor** | **str** | Billing anchor date | 
**plan_id** | **str** | Plan ID | 
**plan_version** | **str** | Plan version | [optional] [default to '1']
**active_from** | **str** | Active from date (ISO 8601) | 
**active_to** | **str** |  | [optional] 
**effective_at** | **str** |  | [optional] 

## Example

```python
from moolabs.models.subscription_sync_request import SubscriptionSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionSyncRequest from a JSON string
subscription_sync_request_instance = SubscriptionSyncRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionSyncRequest.to_json())

# convert the object into a dict
subscription_sync_request_dict = subscription_sync_request_instance.to_dict()
# create an instance of SubscriptionSyncRequest from a dict
subscription_sync_request_from_dict = SubscriptionSyncRequest.from_dict(subscription_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


