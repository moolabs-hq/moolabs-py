# SubscriptionAlignment

Alignment details enriched with the current billing period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billables_must_align** | **bool** | Whether all Billable items and RateCards must align. Alignment means the Price&#39;s BillingCadence must align for both duration and anchor time. | [optional] 
**current_aligned_billing_period** | [**Period**](Period.md) | The current billing period. Only has value if the subscription is aligned and active. | [optional] 

## Example

```python
from moolabs.models.subscription_alignment import SubscriptionAlignment

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAlignment from a JSON string
subscription_alignment_instance = SubscriptionAlignment.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAlignment.to_json())

# convert the object into a dict
subscription_alignment_dict = subscription_alignment_instance.to_dict()
# create an instance of SubscriptionAlignment from a dict
subscription_alignment_from_dict = SubscriptionAlignment.from_dict(subscription_alignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


