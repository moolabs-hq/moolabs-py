# StripeWebhookEventData

The event data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** |  | 

## Example

```python
from moolabs.models.stripe_webhook_event_data import StripeWebhookEventData

# TODO update the JSON string below
json = "{}"
# create an instance of StripeWebhookEventData from a JSON string
stripe_webhook_event_data_instance = StripeWebhookEventData.from_json(json)
# print the JSON string representation of the object
print(StripeWebhookEventData.to_json())

# convert the object into a dict
stripe_webhook_event_data_dict = stripe_webhook_event_data_instance.to_dict()
# create an instance of StripeWebhookEventData from a dict
stripe_webhook_event_data_from_dict = StripeWebhookEventData.from_dict(stripe_webhook_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


