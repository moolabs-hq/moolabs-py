# EntitlementBooleanCreateInputs

Create inputs for boolean entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**feature_id** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**usage_period** | [**RecurringPeriodCreateInput**](RecurringPeriodCreateInput.md) | The usage period associated with the entitlement. | [optional] 
**type** | **str** |  | 

## Example

```python
from moolabs.models.entitlement_boolean_create_inputs import EntitlementBooleanCreateInputs

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementBooleanCreateInputs from a JSON string
entitlement_boolean_create_inputs_instance = EntitlementBooleanCreateInputs.from_json(json)
# print the JSON string representation of the object
print(EntitlementBooleanCreateInputs.to_json())

# convert the object into a dict
entitlement_boolean_create_inputs_dict = entitlement_boolean_create_inputs_instance.to_dict()
# create an instance of EntitlementBooleanCreateInputs from a dict
entitlement_boolean_create_inputs_from_dict = EntitlementBooleanCreateInputs.from_dict(entitlement_boolean_create_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


