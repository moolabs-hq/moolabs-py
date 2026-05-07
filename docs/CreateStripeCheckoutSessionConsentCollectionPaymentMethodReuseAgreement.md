# CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement

Create Stripe checkout session payment method reuse agreement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | [**CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreementPosition**](CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreementPosition.md) |  | [optional] 

## Example

```python
from moolabs.models.create_stripe_checkout_session_consent_collection_payment_method_reuse_agreement import CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement from a JSON string
create_stripe_checkout_session_consent_collection_payment_method_reuse_agreement_instance = CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement.to_json())

# convert the object into a dict
create_stripe_checkout_session_consent_collection_payment_method_reuse_agreement_dict = create_stripe_checkout_session_consent_collection_payment_method_reuse_agreement_instance.to_dict()
# create an instance of CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement from a dict
create_stripe_checkout_session_consent_collection_payment_method_reuse_agreement_from_dict = CreateStripeCheckoutSessionConsentCollectionPaymentMethodReuseAgreement.from_dict(create_stripe_checkout_session_consent_collection_payment_method_reuse_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


