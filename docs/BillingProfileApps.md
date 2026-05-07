# BillingProfileApps

BillingProfileApps represents the applications used by a billing profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | [**App**](App.md) | The tax app used for this workflow | [readonly] 
**invoicing** | [**App**](App.md) | The invoicing app used for this workflow | [readonly] 
**payment** | [**App**](App.md) | The payment app used for this workflow | [readonly] 

## Example

```python
from moolabs.models.billing_profile_apps import BillingProfileApps

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileApps from a JSON string
billing_profile_apps_instance = BillingProfileApps.from_json(json)
# print the JSON string representation of the object
print(BillingProfileApps.to_json())

# convert the object into a dict
billing_profile_apps_dict = billing_profile_apps_instance.to_dict()
# create an instance of BillingProfileApps from a dict
billing_profile_apps_from_dict = BillingProfileApps.from_dict(billing_profile_apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


