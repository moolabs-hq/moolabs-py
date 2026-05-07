# EntitlementValue

Entitlements are the core of OpenMeter access management. They define access to features for subjects. Entitlements can be metered, boolean, or static.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_access** | **bool** | Whether the subject has access to the feature. Shared accross all entitlement types. | [readonly] 
**balance** | **float** | Only available for metered entitlements. Metered entitlements are built around a balance calculation where feature usage is deducted from the issued grants. Balance represents the remaining balance of the entitlement, it&#39;s value never turns negative. | [optional] [readonly] 
**usage** | **float** | Only available for metered entitlements. Returns the total feature usage in the current period. | [optional] [readonly] 
**overage** | **float** | Only available for metered entitlements. Overage represents the usage that wasn&#39;t covered by grants, e.g. if the subject had a total feature usage of 100 in the period but they were only granted 80, there would be 20 overage. | [optional] [readonly] 
**total_available_grant_amount** | **float** | The summed value of all grant amounts that are active at the time of the query. | [optional] [readonly] 
**config** | **str** | Only available for static entitlements. The JSON parsable config of the entitlement. | [optional] [readonly] 

## Example

```python
from moolabs.models.entitlement_value import EntitlementValue

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementValue from a JSON string
entitlement_value_instance = EntitlementValue.from_json(json)
# print the JSON string representation of the object
print(EntitlementValue.to_json())

# convert the object into a dict
entitlement_value_dict = entitlement_value_instance.to_dict()
# create an instance of EntitlementValue from a dict
entitlement_value_from_dict = EntitlementValue.from_dict(entitlement_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


