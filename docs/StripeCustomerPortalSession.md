# StripeCustomerPortalSession

Stripe customer portal session.  See: https://docs.stripe.com/api/customer_portal/sessions/object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the customer portal session.  See: https://docs.stripe.com/api/customer_portal/sessions/object#portal_session_object-id | 
**stripe_customer_id** | **str** | The ID of the stripe customer. | 
**configuration_id** | **str** | Configuration used to customize the customer portal.  See: https://docs.stripe.com/api/customer_portal/sessions/object#portal_session_object-configuration | 
**livemode** | **bool** | Livemode.  See: https://docs.stripe.com/api/customer_portal/sessions/object#portal_session_object-livemode | 
**created_at** | **datetime** | Created at.  See: https://docs.stripe.com/api/customer_portal/sessions/object#portal_session_object-created | 
**return_url** | **str** | Return URL.  See: https://docs.stripe.com/api/customer_portal/sessions/object#portal_session_object-return_url | 
**locale** | **str** | Status.   /** The IETF language tag of the locale customer portal is displayed in.  See: https://docs.stripe.com/api/customer_portal/sessions/object#portal_session_object-locale | 
**url** | **str** | /** The ID of the customer.The URL to redirect the customer to after they have completed their requested actions. | 

## Example

```python
from moolabs.models.stripe_customer_portal_session import StripeCustomerPortalSession

# TODO update the JSON string below
json = "{}"
# create an instance of StripeCustomerPortalSession from a JSON string
stripe_customer_portal_session_instance = StripeCustomerPortalSession.from_json(json)
# print the JSON string representation of the object
print(StripeCustomerPortalSession.to_json())

# convert the object into a dict
stripe_customer_portal_session_dict = stripe_customer_portal_session_instance.to_dict()
# create an instance of StripeCustomerPortalSession from a dict
stripe_customer_portal_session_from_dict = StripeCustomerPortalSession.from_dict(stripe_customer_portal_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


