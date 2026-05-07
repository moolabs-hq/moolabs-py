# EntitlementMeteredCalculatedFields

Calculated fields for metered entitlements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_reset** | **datetime** | The time the last reset happened. | [readonly] 
**current_usage_period** | [**Period**](Period.md) | The current usage period. | [readonly] 
**measure_usage_from** | **datetime** | The time from which usage is measured. If not specified on creation, defaults to entitlement creation time. | [readonly] 
**usage_period** | [**RecurringPeriod**](RecurringPeriod.md) | THe usage period of the entitlement. | [readonly] 

## Example

```python
from moolabs.models.entitlement_metered_calculated_fields import EntitlementMeteredCalculatedFields

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementMeteredCalculatedFields from a JSON string
entitlement_metered_calculated_fields_instance = EntitlementMeteredCalculatedFields.from_json(json)
# print the JSON string representation of the object
print(EntitlementMeteredCalculatedFields.to_json())

# convert the object into a dict
entitlement_metered_calculated_fields_dict = entitlement_metered_calculated_fields_instance.to_dict()
# create an instance of EntitlementMeteredCalculatedFields from a dict
entitlement_metered_calculated_fields_from_dict = EntitlementMeteredCalculatedFields.from_dict(entitlement_metered_calculated_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


