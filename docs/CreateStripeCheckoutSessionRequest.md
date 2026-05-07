# CreateStripeCheckoutSessionRequest

Create Stripe checkout session request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | If not provided, the default Stripe app is used if any. | [optional] 
**customer** | [**CreateStripeCheckoutSessionRequestCustomer**](CreateStripeCheckoutSessionRequestCustomer.md) |  | 
**stripe_customer_id** | **str** | Stripe customer ID. If not provided OpenMeter creates a new Stripe customer or uses the OpenMeter customer&#39;s default Stripe customer ID. | [optional] 
**options** | [**CreateStripeCheckoutSessionRequestOptions**](CreateStripeCheckoutSessionRequestOptions.md) | Options passed to Stripe when creating the checkout session. | 

## Example

```python
from moolabs.models.create_stripe_checkout_session_request import CreateStripeCheckoutSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionRequest from a JSON string
create_stripe_checkout_session_request_instance = CreateStripeCheckoutSessionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionRequest.to_json())

# convert the object into a dict
create_stripe_checkout_session_request_dict = create_stripe_checkout_session_request_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionRequest from a dict
create_stripe_checkout_session_request_from_dict = CreateStripeCheckoutSessionRequest.from_dict(create_stripe_checkout_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


