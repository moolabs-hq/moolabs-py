# CreateStripeCheckoutSessionRequestCustomer

Provide a customer ID or key to use an existing OpenMeter customer. or provide a customer object to create a new customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ULID (Universally Unique Lexicographically Sortable Identifier). | 
**key** | **str** | An optional unique key of the customer. Useful to reference the customer in external systems. For example, your database ID. | 
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**usage_attribution** | [**CustomerUsageAttribution**](CustomerUsageAttribution.md) | Mapping to attribute metered usage to the customer | 
**primary_email** | **str** | The primary email address of the customer. | [optional] 
**currency** | **str** | Currency of the customer. Used for billing, tax and invoicing. | [optional] 
**billing_address** | [**Address**](Address.md) | The billing address of the customer. Used for tax and invoicing. | [optional] 

## Example

```python
from moolabs.models.create_stripe_checkout_session_request_customer import CreateStripeCheckoutSessionRequestCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionRequestCustomer from a JSON string
create_stripe_checkout_session_request_customer_instance = CreateStripeCheckoutSessionRequestCustomer.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionRequestCustomer.to_json())

# convert the object into a dict
create_stripe_checkout_session_request_customer_dict = create_stripe_checkout_session_request_customer_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionRequestCustomer from a dict
create_stripe_checkout_session_request_customer_from_dict = CreateStripeCheckoutSessionRequestCustomer.from_dict(create_stripe_checkout_session_request_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


