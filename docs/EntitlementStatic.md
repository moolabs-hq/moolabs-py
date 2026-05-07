# EntitlementStatic

A static entitlement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**config** | **str** | The JSON parsable config of the entitlement. This value is also returned when checking entitlement access and it is useful for configuring fine-grained access settings to the feature, implemented in your own system. Has to be an object. | 
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**annotations** | **Dict[str, object]** | The annotations of the entitlement. | [optional] [readonly] 
**id** | **str** | Readonly unique ULID identifier. | [readonly] 
**subject_key** | **str** | The identifier key unique to the subject. NOTE: Subjects are being deprecated, please use the new customer APIs. | 
**feature_key** | **str** | The feature the subject is entitled to use. | 
**feature_id** | **str** | The feature the subject is entitled to use. | 
**current_usage_period** | [**Period**](Period.md) | The current usage period. | [optional] 
**usage_period** | [**RecurringPeriod**](RecurringPeriod.md) | The defined usage period of the entitlement | [optional] 

## Example

```python
from moolabs.models.entitlement_static import EntitlementStatic

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementStatic from a JSON string
entitlement_static_instance = EntitlementStatic.from_json(json)
# print the JSON string representation of the object
print(EntitlementStatic.to_json())

# convert the object into a dict
entitlement_static_dict = entitlement_static_instance.to_dict()
# create an instance of EntitlementStatic from a dict
entitlement_static_from_dict = EntitlementStatic.from_dict(entitlement_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


