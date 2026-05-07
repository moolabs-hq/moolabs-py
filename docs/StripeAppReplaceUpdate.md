# StripeAppReplaceUpdate

Resource update operation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for the resource. Between 1 and 256 characters. | 
**description** | **str** | Optional description of the resource. Maximum 1024 characters. | [optional] 
**metadata** | **Dict[str, str]** | Additional metadata for the resource. | [optional] 
**type** | **str** | The app&#39;s type is Stripe. | 
**secret_api_key** | **str** | The Stripe API key. | [optional] 

## Example

```python
from moolabs.models.stripe_app_replace_update import StripeAppReplaceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StripeAppReplaceUpdate from a JSON string
stripe_app_replace_update_instance = StripeAppReplaceUpdate.from_json(json)
# print the JSON string representation of the object
print(StripeAppReplaceUpdate.to_json())

# convert the object into a dict
stripe_app_replace_update_dict = stripe_app_replace_update_instance.to_dict()
# create an instance of StripeAppReplaceUpdate from a dict
stripe_app_replace_update_from_dict = StripeAppReplaceUpdate.from_dict(stripe_app_replace_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


