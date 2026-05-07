# CheckoutSessionCustomTextAfterSubmitParamsSubmit

Custom text that should be displayed alongside the payment confirmation button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from moolabs.models.checkout_session_custom_text_after_submit_params_submit import CheckoutSessionCustomTextAfterSubmitParamsSubmit

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionCustomTextAfterSubmitParamsSubmit from a JSON string
checkout_session_custom_text_after_submit_params_submit_instance = CheckoutSessionCustomTextAfterSubmitParamsSubmit.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionCustomTextAfterSubmitParamsSubmit.to_json())

# convert the object into a dict
checkout_session_custom_text_after_submit_params_submit_dict = checkout_session_custom_text_after_submit_params_submit_instance.to_dict()
# create an instance of CheckoutSessionCustomTextAfterSubmitParamsSubmit from a dict
checkout_session_custom_text_after_submit_params_submit_from_dict = CheckoutSessionCustomTextAfterSubmitParamsSubmit.from_dict(checkout_session_custom_text_after_submit_params_submit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


