# SubscriptionExpanded

Expanded subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**annotations** | **Dict[str, object]** | Set of key-value pairs managed by the system. Cannot be modified by user. | [optional] [readonly] 
**status** | [**SubscriptionStatus**](SubscriptionStatus.md) | The status of the subscription. | [readonly] 
**customer_id** | **str** | The customer ID of the subscription. | 
**plan** | [**PlanReference**](PlanReference.md) | The plan of the subscription. | [optional] 
**currency** | **str** | The currency code of the subscription. Will be revised once we add multi currency support. | 
**billing_cadence** | **str** | The billing cadence for the subscriptions. Defines how often customers are billed using ISO8601 duration format. Examples: \&quot;P1M\&quot; (monthly), \&quot;P3M\&quot; (quarterly), \&quot;P1Y\&quot; (annually). | [readonly] 
**pro_rating_config** | [**ProRatingConfig**](ProRatingConfig.md) | The pro-rating configuration for the subscriptions. | [optional] [readonly] 
**billing_anchor** | **datetime** | The normalizedbilling anchor of the subscription. | [readonly] 
**commercial_overrides** | [**CommercialOverrides**](CommercialOverrides.md) | Commercial terms for this subscription (discounts, pool overrides, wallet policy). | [optional] [readonly] 
**alignment** | [**SubscriptionAlignment**](SubscriptionAlignment.md) | Alignment details enriched with the current billing period. | [optional] 
**phases** | [**List[SubscriptionPhaseExpanded]**](SubscriptionPhaseExpanded.md) | The phases of the subscription. | 

## Example

```python
from moolabs.models.subscription_expanded import SubscriptionExpanded

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionExpanded from a JSON string
subscription_expanded_instance = SubscriptionExpanded.from_json(json)
# print the JSON string representation of the object
print(SubscriptionExpanded.to_json())

# convert the object into a dict
subscription_expanded_dict = subscription_expanded_instance.to_dict()
# create an instance of SubscriptionExpanded from a dict
subscription_expanded_from_dict = SubscriptionExpanded.from_dict(subscription_expanded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


