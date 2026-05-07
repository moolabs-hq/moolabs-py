# CreateStripeCheckoutSessionConsentCollection

Configure fields for the Checkout Session to gather active consent from customers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_reuse_agreement** | [**CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement**](CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement.md) | Determines the position and visibility of the payment method reuse agreement in the UI. When set to auto, Stripe’s defaults will be used. When set to hidden, the payment method reuse agreement text will always be hidden in the UI. | [optional] 
**promotions** | [**CreateStripeCheckoutSessionConsentCollectionPromotions**](CreateStripeCheckoutSessionConsentCollectionPromotions.md) | If set to auto, enables the collection of customer consent for promotional communications. The Checkout Session will determine whether to display an option to opt into promotional communication from the merchant depending on the customer’s locale. Only available to US merchants. | [optional] 
**terms_of_service** | [**CreateStripeCheckoutSessionConsentCollectionTermsOfService**](CreateStripeCheckoutSessionConsentCollectionTermsOfService.md) | If set to required, it requires customers to check a terms of service checkbox before being able to pay. There must be a valid terms of service URL set in your Stripe Dashboard settings. https://dashboard.stripe.com/settings/public | [optional] 

## Example

```python
from moolabs.models.create_stripe_checkout_session_consent_collection import CreateStripeCheckoutSessionConsentCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionConsentCollection from a JSON string
create_stripe_checkout_session_consent_collection_instance = CreateStripeCheckoutSessionConsentCollection.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionConsentCollection.to_json())

# convert the object into a dict
create_stripe_checkout_session_consent_collection_dict = create_stripe_checkout_session_consent_collection_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionConsentCollection from a dict
create_stripe_checkout_session_consent_collection_from_dict = CreateStripeCheckoutSessionConsentCollection.from_dict(create_stripe_checkout_session_consent_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


