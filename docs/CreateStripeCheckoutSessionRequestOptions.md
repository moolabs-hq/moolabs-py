# CreateStripeCheckoutSessionRequestOptions

Create Stripe checkout session options See https://docs.stripe.com/api/checkout/sessions/create

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address_collection** | [**CreateStripeCheckoutSessionBillingAddressCollection**](CreateStripeCheckoutSessionBillingAddressCollection.md) | Specify whether Checkout should collect the customer’s billing address. Defaults to auto. | [optional] 
**cancel_url** | **str** | If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website. This parameter is not allowed if ui_mode is embedded. | [optional] 
**client_reference_id** | **str** | A unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the session with your internal systems. | [optional] 
**customer_update** | [**CreateStripeCheckoutSessionCustomerUpdate**](CreateStripeCheckoutSessionCustomerUpdate.md) | Controls what fields on Customer can be updated by the Checkout Session. | [optional] 
**consent_collection** | [**CreateStripeCheckoutSessionConsentCollection**](CreateStripeCheckoutSessionConsentCollection.md) | Configure fields for the Checkout Session to gather active consent from customers. | [optional] 
**currency** | **str** | Three-letter ISO currency code, in lowercase. | [optional] 
**custom_text** | [**CheckoutSessionCustomTextAfterSubmitParams**](CheckoutSessionCustomTextAfterSubmitParams.md) | Display additional text for your customers using custom text. | [optional] 
**expires_at** | **int** | The Epoch time in seconds at which the Checkout Session will expire. It can be anywhere from 30 minutes to 24 hours after Checkout Session creation. By default, this value is 24 hours from creation. | [optional] 
**locale** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** | Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata. | [optional] 
**return_url** | **str** | The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. This parameter is required if ui_mode is embedded and redirect-based payment methods are enabled on the session. | [optional] 
**success_url** | **str** | The URL to which Stripe should send customers when payment or setup is complete. This parameter is not allowed if ui_mode is embedded. If you’d like to use information from the successful Checkout Session on your page, read the guide on customizing your success page: https://docs.stripe.com/payments/checkout/custom-success-page | [optional] 
**ui_mode** | [**CheckoutSessionUIMode**](CheckoutSessionUIMode.md) | The UI mode of the Session. Defaults to hosted. | [optional] 
**payment_method_types** | **List[str]** | A list of the types of payment methods (e.g., card) this Checkout Session can accept. | [optional] 
**redirect_on_completion** | [**CreateStripeCheckoutSessionRedirectOnCompletion**](CreateStripeCheckoutSessionRedirectOnCompletion.md) | This parameter applies to ui_mode: embedded. Defaults to always. Learn more about the redirect behavior of embedded sessions at https://docs.stripe.com/payments/checkout/custom-success-page?payment-ui&#x3D;embedded-form | [optional] 
**tax_id_collection** | [**CreateCheckoutSessionTaxIdCollection**](CreateCheckoutSessionTaxIdCollection.md) | Controls tax ID collection during checkout. | [optional] 

## Example

```python
from moolabs.models.create_stripe_checkout_session_request_options import CreateStripeCheckoutSessionRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionRequestOptions from a JSON string
create_stripe_checkout_session_request_options_instance = CreateStripeCheckoutSessionRequestOptions.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionRequestOptions.to_json())

# convert the object into a dict
create_stripe_checkout_session_request_options_dict = create_stripe_checkout_session_request_options_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionRequestOptions from a dict
create_stripe_checkout_session_request_options_from_dict = CreateStripeCheckoutSessionRequestOptions.from_dict(create_stripe_checkout_session_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


