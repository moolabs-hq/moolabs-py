# CreateStripeCheckoutSessionResult

Create Stripe Checkout Session response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | The OpenMeter customer ID. | 
**stripe_customer_id** | **str** | The Stripe customer ID. | 
**session_id** | **str** | The checkout session ID. | 
**setup_intent_id** | **str** | The checkout session setup intent ID. | 
**client_secret** | **str** | The client secret of the checkout session. This can be used to initialize Stripe.js for your client-side implementation. | [optional] 
**client_reference_id** | **str** | A unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the session with your internal systems. | [optional] 
**customer_email** | **str** | Customer&#39;s email address provided to Stripe. | [optional] 
**currency** | **str** | Three-letter ISO currency code, in lowercase. | [optional] 
**created_at** | **datetime** | Timestamp at which the checkout session was created. | 
**expires_at** | **datetime** | Timestamp at which the checkout session will expire. | [optional] 
**metadata** | **Dict[str, str]** | Set of key-value pairs attached to the checkout session. | [optional] 
**status** | **str** | The status of the checkout session. | [optional] 
**url** | **str** | URL to show the checkout session. | [optional] 
**mode** | [**StripeCheckoutSessionMode**](StripeCheckoutSessionMode.md) | Mode Always &#x60;setup&#x60; for now. | 
**cancel_url** | **str** | Cancel URL. | [optional] 
**success_url** | **str** | Success URL. | [optional] 
**return_url** | **str** | Return URL. | [optional] 

## Example

```python
from moolabs.models.create_stripe_checkout_session_result import CreateStripeCheckoutSessionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionResult from a JSON string
create_stripe_checkout_session_result_instance = CreateStripeCheckoutSessionResult.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionResult.to_json())

# convert the object into a dict
create_stripe_checkout_session_result_dict = create_stripe_checkout_session_result_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionResult from a dict
create_stripe_checkout_session_result_from_dict = CreateStripeCheckoutSessionResult.from_dict(create_stripe_checkout_session_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


