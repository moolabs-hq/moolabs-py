# IngestedEvent

An ingested event with optional validation error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**Event**](Event.md) | The original event ingested. | 
**customer_id** | **str** | The customer ID if the event is associated with a customer. | [optional] 
**validation_error** | **str** | The validation error if the event failed validation. | [optional] 
**ingested_at** | **datetime** | The date and time the event was ingested. | 
**stored_at** | **datetime** | The date and time the event was stored. | 

## Example

```python
from moolabs.models.ingested_event import IngestedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IngestedEvent from a JSON string
ingested_event_instance = IngestedEvent.from_json(json)
# print the JSON string representation of the object
print(IngestedEvent.to_json())

# convert the object into a dict
ingested_event_dict = ingested_event_instance.to_dict()
# create an instance of IngestedEvent from a dict
ingested_event_from_dict = IngestedEvent.from_dict(ingested_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


