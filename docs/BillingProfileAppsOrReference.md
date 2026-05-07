# BillingProfileAppsOrReference

ProfileAppsOrReference represents the union of ProfileApps and ProfileAppReferences for a billing profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | [**AppReference**](AppReference.md) | The tax app used for this workflow | [readonly] 
**invoicing** | [**AppReference**](AppReference.md) | The invoicing app used for this workflow | [readonly] 
**payment** | [**AppReference**](AppReference.md) | The payment app used for this workflow | [readonly] 

## Example

```python
from moolabs.models.billing_profile_apps_or_reference import BillingProfileAppsOrReference

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileAppsOrReference from a JSON string
billing_profile_apps_or_reference_instance = BillingProfileAppsOrReference.from_json(json)
# print the JSON string representation of the object
print(BillingProfileAppsOrReference.to_json())

# convert the object into a dict
billing_profile_apps_or_reference_dict = billing_profile_apps_or_reference_instance.to_dict()
# create an instance of BillingProfileAppsOrReference from a dict
billing_profile_apps_or_reference_from_dict = BillingProfileAppsOrReference.from_dict(billing_profile_apps_or_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


