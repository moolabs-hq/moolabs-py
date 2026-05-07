# StripeCustomerAppData

Stripe Customer App Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The app ID. If not provided, it will use the global default for the app type. | [optional] 
**type** | **str** | The app name. | 
**stripe_customer_id** | **str** | The Stripe customer ID. | 
**stripe_default_payment_method_id** | **str** | The Stripe default payment method ID. | [optional] 
**app** | [**StripeApp**](StripeApp.md) | The installed stripe app this data belongs to. | [optional] [readonly] 

## Example

```python
from moolabs.models.stripe_customer_app_data import StripeCustomerAppData

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerAppData from a JSON string
stripe_customer_app_data_instance = StripeCustomerAppData.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerAppData.to_json())

# convert the object into a dict
stripe_customer_app_data_dict = stripe_customer_app_data_instance.to_dict()
# create an instance of StripeCustomerAppData from a dict
stripe_customer_app_data_from_dict = StripeCustomerAppData.from_dict(stripe_customer_app_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


