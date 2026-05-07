# ResetEntitlementUsageInput

Reset parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_at** | **datetime** | The time at which the reset takes effect, defaults to now. The reset cannot be in the future. The provided value is truncated to the minute due to how historical meter data is stored. | [optional] 
**retain_anchor** | **bool** | Determines whether the usage period anchor is retained or reset to the effectiveAt time. - If true, the usage period anchor is retained. - If false, the usage period anchor is reset to the effectiveAt time. | [optional] 
**preserve_overage** | **bool** | Determines whether the overage is preserved or forgiven, overriding the entitlement&#39;s default behavior. - If true, the overage is preserved. - If false, the overage is forgiven. | [optional] 

## Example

```python
from moolabs.models.reset_entitlement_usage_input import ResetEntitlementUsageInput

# TODO update the JSON string below
json = "{}"
# create an instance of ResetEntitlementUsageInput from a JSON string
reset_entitlement_usage_input_instance = ResetEntitlementUsageInput.from_json(json)
# print the JSON string representation of the object
print(ResetEntitlementUsageInput.to_json())

# convert the object into a dict
reset_entitlement_usage_input_dict = reset_entitlement_usage_input_instance.to_dict()
# create an instance of ResetEntitlementUsageInput from a dict
reset_entitlement_usage_input_from_dict = ResetEntitlementUsageInput.from_dict(reset_entitlement_usage_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


