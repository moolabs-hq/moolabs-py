# EntitlementBooleanV2

Entitlement template of a boolean entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**annotations** | **Dict[str, object]** | The annotations of the entitlement. | [optional] [readonly] 
**id** | **str** | Readonly unique ULID identifier. | [readonly] 
**feature_key** | **str** | The feature the subject is entitled to use. | 
**feature_id** | **str** | The feature the subject is entitled to use. | 
**current_usage_period** | [**Period**](Period.md) | The current usage period. | [optional] 
**usage_period** | [**RecurringPeriod**](RecurringPeriod.md) | The defined usage period of the entitlement | [optional] 
**customer_key** | **str** | The identifier key unique to the customer | [optional] 
**customer_id** | **str** | The identifier unique to the customer | 

## Example

```python
from moolabs.models.entitlement_boolean_v2 import EntitlementBooleanV2

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementBooleanV2 from a JSON string
entitlement_boolean_v2_instance = EntitlementBooleanV2.from_json(json)
# print the JSON string representation of the object
print(EntitlementBooleanV2.to_json())

# convert the object into a dict
entitlement_boolean_v2_dict = entitlement_boolean_v2_instance.to_dict()
# create an instance of EntitlementBooleanV2 from a dict
entitlement_boolean_v2_from_dict = EntitlementBooleanV2.from_dict(entitlement_boolean_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


