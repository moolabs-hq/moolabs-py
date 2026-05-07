# EntitlementMeteredCreateInputs

Create inpurs for metered entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**feature_id** | **str** | The feature the subject is entitled to use. Either featureKey or featureId is required. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the feature. | [optional] 
**type** | **str** |  | 
**is_soft_limit** | **bool** | If softLimit&#x3D;true the subject can use the feature even if the entitlement is exhausted, hasAccess will always be true. | [optional] [default to False]
**is_unlimited** | **bool** | Deprecated, ignored by the backend. Please use isSoftLimit instead; this field will be removed in the future. | [optional] [default to False]
**usage_period** | [**RecurringPeriodCreateInput**](RecurringPeriodCreateInput.md) | The usage period associated with the entitlement. | 
**measure_usage_from** | [**MeasureUsageFrom**](MeasureUsageFrom.md) | Defines the time from which usage is measured. If not specified on creation, defaults to entitlement creation time. | [optional] 
**issue_after_reset** | **float** | You can grant usage automatically alongside the entitlement, the example scenario would be creating a starting balance. If an amount is specified here, a grant will be created alongside the entitlement with the specified amount. That grant will have it&#39;s rollover settings configured in a way that after each reset operation, the balance will return the original amount specified here. Manually creating such a grant would mean having the \&quot;amount\&quot;, \&quot;minRolloverAmount\&quot;, and \&quot;maxRolloverAmount\&quot; fields all be the same. | [optional] 
**issue_after_reset_priority** | **int** | Defines the grant priority for the default grant. | [optional] [default to 1]
**preserve_overage_at_reset** | **bool** | If true, the overage is preserved at reset. If false, the usage is reset to 0. | [optional] [default to False]

## Example

```python
from moolabs.models.entitlement_metered_create_inputs import EntitlementMeteredCreateInputs

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementMeteredCreateInputs from a JSON string
entitlement_metered_create_inputs_instance = EntitlementMeteredCreateInputs.from_json(json)
# print the JSON string representation of the object
print(EntitlementMeteredCreateInputs.to_json())

# convert the object into a dict
entitlement_metered_create_inputs_dict = entitlement_metered_create_inputs_instance.to_dict()
# create an instance of EntitlementMeteredCreateInputs from a dict
entitlement_metered_create_inputs_from_dict = EntitlementMeteredCreateInputs.from_dict(entitlement_metered_create_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


