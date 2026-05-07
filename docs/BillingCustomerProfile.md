# BillingCustomerProfile

Customer specific merged profile.  This profile is calculated from the customer override and the billing profile it references or the default.  Thus this does not have any kind of resource fields, only the calculated values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | [**BillingParty**](BillingParty.md) | The name and contact information for the supplier this billing profile represents | [readonly] 
**workflow** | [**BillingWorkflow**](BillingWorkflow.md) | The billing workflow settings for this profile | [readonly] 
**apps** | [**BillingProfileAppsOrReference**](BillingProfileAppsOrReference.md) | The applications used by this billing profile.  Expand settings govern if this includes the whole app object or just the ID references. | [readonly] 

## Example

```python
from moolabs.models.billing_customer_profile import BillingCustomerProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCustomerProfile from a JSON string
billing_customer_profile_instance = BillingCustomerProfile.from_json(json)
# print the JSON string representation of the object
print(BillingCustomerProfile.to_json())

# convert the object into a dict
billing_customer_profile_dict = billing_customer_profile_instance.to_dict()
# create an instance of BillingCustomerProfile from a dict
billing_customer_profile_from_dict = BillingCustomerProfile.from_dict(billing_customer_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


