# StripeCustomerAppDataBase

Stripe Customer App Data Base.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stripe_customer_id** | **str** | The Stripe customer ID. | 
**stripe_default_payment_method_id** | **str** | The Stripe default payment method ID. | [optional] 

## Example

```python
from moolabs.models.stripe_customer_app_data_base import StripeCustomerAppDataBase

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerAppDataBase from a JSON string
stripe_customer_app_data_base_instance = StripeCustomerAppDataBase.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerAppDataBase.to_json())

# convert the object into a dict
stripe_customer_app_data_base_dict = stripe_customer_app_data_base_instance.to_dict()
# create an instance of StripeCustomerAppDataBase from a dict
stripe_customer_app_data_base_from_dict = StripeCustomerAppDataBase.from_dict(stripe_customer_app_data_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


