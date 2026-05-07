# StripeWebhookEvent

Stripe webhook event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The event ID. | 
**type** | **str** | The event type. | 
**livemode** | **bool** | Live mode. | 
**created** | **int** | The event created timestamp. | 
**data** | [**StripeWebhookEventData**](StripeWebhookEventData.md) |  | 

## Example

```python
from moolabs.models.stripe_webhook_event import StripeWebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StripeWebhookEvent from a JSON string
stripe_webhook_event_instance = StripeWebhookEvent.from_json(json)
# print the JSON string representation of the object
print(StripeWebhookEvent.to_json())

# convert the object into a dict
stripe_webhook_event_dict = stripe_webhook_event_instance.to_dict()
# create an instance of StripeWebhookEvent from a dict
stripe_webhook_event_from_dict = StripeWebhookEvent.from_dict(stripe_webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


