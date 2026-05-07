# BillingProfileCustomerOverride

Customer override values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp of when the resource was created. | [readonly] 
**updated_at** | **datetime** | Timestamp of when the resource was last updated. | [readonly] 
**billing_profile_id** | **str** | The billing profile this override is associated with.  If empty the default profile is looked up dynamically. | [optional] 
**customer_id** | **str** | The customer id this override is associated with. | 

## Example

```python
from moolabs.models.billing_profile_customer_override import BillingProfileCustomerOverride

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCustomerOverride from a JSON string
billing_profile_customer_override_instance = BillingProfileCustomerOverride.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCustomerOverride.to_json())

# convert the object into a dict
billing_profile_customer_override_dict = billing_profile_customer_override_instance.to_dict()
# create an instance of BillingProfileCustomerOverride from a dict
billing_profile_customer_override_from_dict = BillingProfileCustomerOverride.from_dict(billing_profile_customer_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


