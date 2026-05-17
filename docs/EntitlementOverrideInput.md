# EntitlementOverrideInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**entitlement_type** | **str** |  | [optional] [default to 'metered']
**default_value** | **str** |  | [optional] [default to '']
**override_value** | **str** |  | 
**window** | **str** |  | [optional] [default to 'Monthly']

## Example

```python
from moolabs.models.entitlement_override_input import EntitlementOverrideInput

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementOverrideInput from a JSON string
entitlement_override_input_instance = EntitlementOverrideInput.from_json(json)
# print the JSON string representation of the object
print(EntitlementOverrideInput.to_json())

# convert the object into a dict
entitlement_override_input_dict = entitlement_override_input_instance.to_dict()
# create an instance of EntitlementOverrideInput from a dict
entitlement_override_input_from_dict = EntitlementOverrideInput.from_dict(entitlement_override_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


