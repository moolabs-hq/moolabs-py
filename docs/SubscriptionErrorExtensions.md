# SubscriptionErrorExtensions

Error extensions for the Subscription Errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_errors** | [**List[ErrorExtension]**](ErrorExtension.md) |  | 

## Example

```python
from moolabs.models.subscription_error_extensions import SubscriptionErrorExtensions

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionErrorExtensions from a JSON string
subscription_error_extensions_instance = SubscriptionErrorExtensions.from_json(json)
# print the JSON string representation of the object
print(SubscriptionErrorExtensions.to_json())

# convert the object into a dict
subscription_error_extensions_dict = subscription_error_extensions_instance.to_dict()
# create an instance of SubscriptionErrorExtensions from a dict
subscription_error_extensions_from_dict = SubscriptionErrorExtensions.from_dict(subscription_error_extensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


