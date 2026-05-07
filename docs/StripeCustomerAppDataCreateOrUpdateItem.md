# StripeCustomerAppDataCreateOrUpdateItem

Stripe Customer App Data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The app ID. If not provided, it will use the global default for the app type. | [optional] 
**type** | **str** | The app name. | 
**stripe_customer_id** | **str** | The Stripe customer ID. | 
**stripe_default_payment_method_id** | **str** | The Stripe default payment method ID. | [optional] 

## Example

```python
from moolabs.models.stripe_customer_app_data_create_or_update_item import StripeCustomerAppDataCreateOrUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerAppDataCreateOrUpdateItem from a JSON string
stripe_customer_app_data_create_or_update_item_instance = StripeCustomerAppDataCreateOrUpdateItem.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerAppDataCreateOrUpdateItem.to_json())

# convert the object into a dict
stripe_customer_app_data_create_or_update_item_dict = stripe_customer_app_data_create_or_update_item_instance.to_dict()
# create an instance of StripeCustomerAppDataCreateOrUpdateItem from a dict
stripe_customer_app_data_create_or_update_item_from_dict = StripeCustomerAppDataCreateOrUpdateItem.from_dict(stripe_customer_app_data_create_or_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


