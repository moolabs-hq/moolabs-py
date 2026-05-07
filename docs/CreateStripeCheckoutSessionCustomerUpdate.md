# CreateStripeCheckoutSessionCustomerUpdate

Controls what fields on Customer can be updated by the Checkout Session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CreateStripeCheckoutSessionCustomerUpdateBehavior**](CreateStripeCheckoutSessionCustomerUpdateBehavior.md) | Describes whether Checkout saves the billing address onto customer.address. To always collect a full billing address, use billing_address_collection. Defaults to never. | [optional] 
**name** | [**CreateStripeCheckoutSessionCustomerUpdateBehavior**](CreateStripeCheckoutSessionCustomerUpdateBehavior.md) | Describes whether Checkout saves the name onto customer.name. Defaults to never. | [optional] 
**shipping** | [**CreateStripeCheckoutSessionCustomerUpdateBehavior**](CreateStripeCheckoutSessionCustomerUpdateBehavior.md) | Describes whether Checkout saves shipping information onto customer.shipping. To collect shipping information, use shipping_address_collection. Defaults to never. | [optional] 

## Example

```python
from moolabs.models.create_stripe_checkout_session_customer_update import CreateStripeCheckoutSessionCustomerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionCustomerUpdate from a JSON string
create_stripe_checkout_session_customer_update_instance = CreateStripeCheckoutSessionCustomerUpdate.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionCustomerUpdate.to_json())

# convert the object into a dict
create_stripe_checkout_session_customer_update_dict = create_stripe_checkout_session_customer_update_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionCustomerUpdate from a dict
create_stripe_checkout_session_customer_update_from_dict = CreateStripeCheckoutSessionCustomerUpdate.from_dict(create_stripe_checkout_session_customer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


