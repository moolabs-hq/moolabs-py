# StripeAPIKeyInput

The Stripe API key input. Used to authenticate with the Stripe API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_api_key** | **str** |  | 

## Example

```python
from moolabs.models.stripe_api_key_input import StripeAPIKeyInput

# TODO update the JSON string below
json = "{}"
# create an instance of StripeAPIKeyInput from a JSON string
stripe_api_key_input_instance = StripeAPIKeyInput.from_json(json)
# print the JSON string representation of the object
print(StripeAPIKeyInput.to_json())

# convert the object into a dict
stripe_api_key_input_dict = stripe_api_key_input_instance.to_dict()
# create an instance of StripeAPIKeyInput from a dict
stripe_api_key_input_from_dict = StripeAPIKeyInput.from_dict(stripe_api_key_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


