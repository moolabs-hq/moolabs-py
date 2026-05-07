# CreateStripeCustomerPortalSessionParams

Stripe customer portal request params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** | The ID of an existing configuration to use for this session, describing its functionality and features. If not specified, the session uses the default configuration.  See https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-configuration | [optional] 
**locale** | **str** | The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s preferred_locales or browser’s locale is used.  See: https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-locale | [optional] 
**return_url** | **str** | The URL to redirect the customer to after they have completed their requested actions.  See: https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-return_url | [optional] 

## Example

```python
from moolabs.models.create_stripe_customer_portal_session_params import CreateStripeCustomerPortalSessionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCustomerPortalSessionParams from a JSON string
create_stripe_customer_portal_session_params_instance = CreateStripeCustomerPortalSessionParams.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCustomerPortalSessionParams.to_json())

# convert the object into a dict
create_stripe_customer_portal_session_params_dict = create_stripe_customer_portal_session_params_instance.to_dict()
# create an instance of CreateStripeCustomerPortalSessionParams from a dict
create_stripe_customer_portal_session_params_from_dict = CreateStripeCustomerPortalSessionParams.from_dict(create_stripe_customer_portal_session_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


