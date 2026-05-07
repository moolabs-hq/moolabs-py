# EventDeliveryAttemptResponse

The response of the event delivery attempt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | Status code of the response if available. | [optional] [readonly] 
**body** | **str** | The body of the response. | [readonly] 
**duration_ms** | **int** | The duration of the response in milliseconds. | [readonly] 
**url** | **str** | URL where the event was sent in case of notification channel with webhook type. | [optional] [readonly] 

## Example

```python
from moolabs.models.event_delivery_attempt_response import EventDeliveryAttemptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventDeliveryAttemptResponse from a JSON string
event_delivery_attempt_response_instance = EventDeliveryAttemptResponse.from_json(json)
# print the JSON string representation of the object
print(EventDeliveryAttemptResponse.to_json())

# convert the object into a dict
event_delivery_attempt_response_dict = event_delivery_attempt_response_instance.to_dict()
# create an instance of EventDeliveryAttemptResponse from a dict
event_delivery_attempt_response_from_dict = EventDeliveryAttemptResponse.from_dict(event_delivery_attempt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


