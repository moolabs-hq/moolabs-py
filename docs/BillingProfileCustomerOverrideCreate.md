# BillingProfileCustomerOverrideCreate

Payload for creating a new or updating an existing customer override.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_profile_id** | **str** | The billing profile this override is associated with.  If not provided, the default billing profile is chosen if available. | [optional] 

## Example

```python
from moolabs.models.billing_profile_customer_override_create import BillingProfileCustomerOverrideCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCustomerOverrideCreate from a JSON string
billing_profile_customer_override_create_instance = BillingProfileCustomerOverrideCreate.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCustomerOverrideCreate.to_json())

# convert the object into a dict
billing_profile_customer_override_create_dict = billing_profile_customer_override_create_instance.to_dict()
# create an instance of BillingProfileCustomerOverrideCreate from a dict
billing_profile_customer_override_create_from_dict = BillingProfileCustomerOverrideCreate.from_dict(billing_profile_customer_override_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


