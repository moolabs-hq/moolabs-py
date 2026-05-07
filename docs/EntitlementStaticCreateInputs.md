# EntitlementStaticCreateInputs

Create inputs for static entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**feature_id** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**usage_period** | [**RecurringPeriodCreateInput**](RecurringPeriodCreateInput.md) | The usage period associated with the entitlement. | [optional] 
**type** | **str** |  | 
**config** | **str** | The JSON parsable config of the entitlement. This value is also returned when checking entitlement access and it is useful for configuring fine-grained access settings to the feature, implemented in your own system. Has to be an object. | 

## Example

```python
from moolabs.models.entitlement_static_create_inputs import EntitlementStaticCreateInputs

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementStaticCreateInputs from a JSON string
entitlement_static_create_inputs_instance = EntitlementStaticCreateInputs.from_json(json)
# print the JSON string representation of the object
print(EntitlementStaticCreateInputs.to_json())

# convert the object into a dict
entitlement_static_create_inputs_dict = entitlement_static_create_inputs_instance.to_dict()
# create an instance of EntitlementStaticCreateInputs from a dict
entitlement_static_create_inputs_from_dict = EntitlementStaticCreateInputs.from_dict(entitlement_static_create_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


