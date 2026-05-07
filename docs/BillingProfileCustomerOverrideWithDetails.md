# BillingProfileCustomerOverrideWithDetails

Customer specific workflow overrides.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_override** | [**BillingProfileCustomerOverride**](BillingProfileCustomerOverride.md) | The customer override values.  If empty the merged values are calculated based on the default profile. | [optional] 
**base_billing_profile_id** | **str** | The billing profile the customerProfile is associated with at the time of query.  customerOverride contains the explicit mapping set in the customer override object. If that is empty, then the baseBillingProfileId is the default profile. | 
**customer_profile** | [**BillingCustomerProfile**](BillingCustomerProfile.md) | Merged billing profile with the customer specific overrides. | [optional] 
**customer** | [**Customer**](Customer.md) | The customer this override belongs to. | [optional] 

## Example

```python
from moolabs.models.billing_profile_customer_override_with_details import BillingProfileCustomerOverrideWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCustomerOverrideWithDetails from a JSON string
billing_profile_customer_override_with_details_instance = BillingProfileCustomerOverrideWithDetails.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCustomerOverrideWithDetails.to_json())

# convert the object into a dict
billing_profile_customer_override_with_details_dict = billing_profile_customer_override_with_details_instance.to_dict()
# create an instance of BillingProfileCustomerOverrideWithDetails from a dict
billing_profile_customer_override_with_details_from_dict = BillingProfileCustomerOverrideWithDetails.from_dict(billing_profile_customer_override_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


