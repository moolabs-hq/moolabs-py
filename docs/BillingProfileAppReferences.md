# BillingProfileAppReferences

BillingProfileAppReferences represents the references (id, type) to the apps used by a billing profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | [**AppReference**](AppReference.md) | The tax app used for this workflow | [readonly] 
**invoicing** | [**AppReference**](AppReference.md) | The invoicing app used for this workflow | [readonly] 
**payment** | [**AppReference**](AppReference.md) | The payment app used for this workflow | [readonly] 

## Example

```python
from moolabs.models.billing_profile_app_references import BillingProfileAppReferences

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileAppReferences from a JSON string
billing_profile_app_references_instance = BillingProfileAppReferences.from_json(json)
# print the JSON string representation of the object
print(BillingProfileAppReferences.to_json())

# convert the object into a dict
billing_profile_app_references_dict = billing_profile_app_references_instance.to_dict()
# create an instance of BillingProfileAppReferences from a dict
billing_profile_app_references_from_dict = BillingProfileAppReferences.from_dict(billing_profile_app_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


