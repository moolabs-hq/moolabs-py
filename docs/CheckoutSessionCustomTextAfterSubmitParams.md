# CheckoutSessionCustomTextAfterSubmitParams

Stripe CheckoutSession.custom_text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_submit** | [**CheckoutSessionCustomTextAfterSubmitParamsAfterSubmit**](CheckoutSessionCustomTextAfterSubmitParamsAfterSubmit.md) |  | [optional] 
**shipping_address** | [**CheckoutSessionCustomTextAfterSubmitParamsShippingAddress**](CheckoutSessionCustomTextAfterSubmitParamsShippingAddress.md) |  | [optional] 
**submit** | [**CheckoutSessionCustomTextAfterSubmitParamsSubmit**](CheckoutSessionCustomTextAfterSubmitParamsSubmit.md) |  | [optional] 
**terms_of_service_acceptance** | [**CheckoutSessionCustomTextAfterSubmitParamsTermsOfServiceAcceptance**](CheckoutSessionCustomTextAfterSubmitParamsTermsOfServiceAcceptance.md) |  | [optional] 

## Example

```python
from moolabs.models.checkout_session_custom_text_after_submit_params import CheckoutSessionCustomTextAfterSubmitParams

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionCustomTextAfterSubmitParams from a JSON string
checkout_session_custom_text_after_submit_params_instance = CheckoutSessionCustomTextAfterSubmitParams.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionCustomTextAfterSubmitParams.to_json())

# convert the object into a dict
checkout_session_custom_text_after_submit_params_dict = checkout_session_custom_text_after_submit_params_instance.to_dict()
# create an instance of CheckoutSessionCustomTextAfterSubmitParams from a dict
checkout_session_custom_text_after_submit_params_from_dict = CheckoutSessionCustomTextAfterSubmitParams.from_dict(checkout_session_custom_text_after_submit_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


