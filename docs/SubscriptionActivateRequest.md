# SubscriptionActivateRequest

Request to activate a subscription: sync to mirror + create initial credit grants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_data** | **Dict[str, object]** | Raw OpenMeter subscription response | 
**customer_id** | **str** | Customer ID | [optional] 
**customer_key** | **str** | Customer key (for wallet binding) | [optional] 
**subject_keys** | **List[str]** | Usage attribution subject keys | [optional] 
**active_from** | **str** | Subscription start date (ISO 8601) | [optional] 
**active_to** | **str** | Subscription end date (ISO 8601) | [optional] 
**billing_cadence** | **str** | Billing cadence (ISO 8601 duration) | [optional] 
**pool_overrides** | **Dict[str, float]** | Per-pool recurring credit overrides: pool_key -&gt; amount. &#39;__global__&#39; overrides global pool. | [optional] 

## Example

```python
from moolabs.models.subscription_activate_request import SubscriptionActivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionActivateRequest from a JSON string
subscription_activate_request_instance = SubscriptionActivateRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionActivateRequest.to_json())

# convert the object into a dict
subscription_activate_request_dict = subscription_activate_request_instance.to_dict()
# create an instance of SubscriptionActivateRequest from a dict
subscription_activate_request_from_dict = SubscriptionActivateRequest.from_dict(subscription_activate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


