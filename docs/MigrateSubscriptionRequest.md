# MigrateSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timing** | [**SubscriptionTiming**](SubscriptionTiming.md) | Timing configuration for the migration, when the migration should take effect. If not supported by the subscription, 400 will be returned. | [optional] 
**target_version** | **int** | The version of the plan to migrate to. If not provided, the subscription will migrate to the latest version of the current plan. | [optional] 
**starting_phase** | **str** | The key of the phase to start the subscription in. If not provided, the subscription will start in the first phase of the plan. | [optional] 
**billing_anchor** | **datetime** | The billing anchor of the subscription. The provided date will be normalized according to the billing cadence to the nearest recurrence before start time. If not provided, the previous subscription billing anchor will be used. | [optional] 
**commercial_overrides** | [**CommercialOverrides**](CommercialOverrides.md) | Commercial terms for the migrated subscription. Omitted preserves the current subscription&#39;s overrides. | [optional] 

## Example

```python
from moolabs.models.migrate_subscription_request import MigrateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateSubscriptionRequest from a JSON string
migrate_subscription_request_instance = MigrateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(MigrateSubscriptionRequest.to_json())

# convert the object into a dict
migrate_subscription_request_dict = migrate_subscription_request_instance.to_dict()
# create an instance of MigrateSubscriptionRequest from a dict
migrate_subscription_request_from_dict = MigrateSubscriptionRequest.from_dict(migrate_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


