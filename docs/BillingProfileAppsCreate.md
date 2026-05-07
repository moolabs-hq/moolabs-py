# BillingProfileAppsCreate

BillingProfileAppsCreate represents the input for creating a billing profile's apps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | **str** | The tax app used for this workflow | 
**invoicing** | **str** | The invoicing app used for this workflow | 
**payment** | **str** | The payment app used for this workflow | 

## Example

```python
from moolabs.models.billing_profile_apps_create import BillingProfileAppsCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileAppsCreate from a JSON string
billing_profile_apps_create_instance = BillingProfileAppsCreate.from_json(json)
# print the JSON string representation of the object
print(BillingProfileAppsCreate.to_json())

# convert the object into a dict
billing_profile_apps_create_dict = billing_profile_apps_create_instance.to_dict()
# create an instance of BillingProfileAppsCreate from a dict
billing_profile_apps_create_from_dict = BillingProfileAppsCreate.from_dict(billing_profile_apps_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


