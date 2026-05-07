# LifecycleEventRequest

Request for a subscription lifecycle event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Subscription ID | 
**event_type** | **str** | Event type: ACTIVATED, UPDATED, CANCELLED, PAUSED, RESUMED | 
**event_id** | **str** | Unique event ID (for idempotency) | 
**effective_at** | **str** | When the event takes effect (ISO 8601) | 
**subscription_data** | **Dict[str, object]** |  | [optional] 
**payload_json** | **str** |  | [optional] 

## Example

```python
from moolabs.models.lifecycle_event_request import LifecycleEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleEventRequest from a JSON string
lifecycle_event_request_instance = LifecycleEventRequest.from_json(json)
# print the JSON string representation of the object
print(LifecycleEventRequest.to_json())

# convert the object into a dict
lifecycle_event_request_dict = lifecycle_event_request_instance.to_dict()
# create an instance of LifecycleEventRequest from a dict
lifecycle_event_request_from_dict = LifecycleEventRequest.from_dict(lifecycle_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


