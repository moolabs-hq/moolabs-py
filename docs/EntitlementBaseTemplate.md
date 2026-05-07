# EntitlementBaseTemplate

Shared fields of the entitlement templates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**deleted_at** | **datetime** | Timestamp of when the resource was permanently deleted. | [optional] [readonly] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**active_from** | **datetime** | The cadence start of the resource. | 
**active_to** | **datetime** | The cadence end of the resource. | [optional] 
**annotations** | **Dict[str, object]** | The annotations of the entitlement. | [optional] [readonly] 
**id** | **str** | Readonly unique ULID identifier. | [readonly] 
**type** | [**EntitlementType**](EntitlementType.md) | The type of the entitlement. | 
**subject_key** | **str** | The identifier key unique to the subject. NOTE: Subjects are being deprecated, please use the new customer APIs. | 
**feature_key** | **str** | The feature the subject is entitled to use. | 
**feature_id** | **str** | The feature the subject is entitled to use. | 
**current_usage_period** | [**Period**](Period.md) | The current usage period. | [optional] 
**usage_period** | [**RecurringPeriod**](RecurringPeriod.md) | The defined usage period of the entitlement | [optional] 

## Example

```python
from moolabs.models.entitlement_base_template import EntitlementBaseTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementBaseTemplate from a JSON string
entitlement_base_template_instance = EntitlementBaseTemplate.from_json(json)
# print the JSON string representation of the object
print(EntitlementBaseTemplate.to_json())

# convert the object into a dict
entitlement_base_template_dict = entitlement_base_template_instance.to_dict()
# create an instance of EntitlementBaseTemplate from a dict
entitlement_base_template_from_dict = EntitlementBaseTemplate.from_dict(entitlement_base_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


