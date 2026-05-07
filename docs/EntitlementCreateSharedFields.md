# EntitlementCreateSharedFields

Shared fields for entitlement creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**feature_id** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**usage_period** | [**RecurringPeriodCreateInput**](RecurringPeriodCreateInput.md) | The usage period associated with the entitlement. | [optional] 

## Example

```python
from moolabs.models.entitlement_create_shared_fields import EntitlementCreateSharedFields

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementCreateSharedFields from a JSON string
entitlement_create_shared_fields_instance = EntitlementCreateSharedFields.from_json(json)
# print the JSON string representation of the object
print(EntitlementCreateSharedFields.to_json())

# convert the object into a dict
entitlement_create_shared_fields_dict = entitlement_create_shared_fields_instance.to_dict()
# create an instance of EntitlementCreateSharedFields from a dict
entitlement_create_shared_fields_from_dict = EntitlementCreateSharedFields.from_dict(entitlement_create_shared_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


