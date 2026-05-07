# Event

CloudEvents Specification JSON Schema  Optional properties are nullable according to the CloudEvents specification: OPTIONAL not omitted attributes MAY be represented as a null JSON value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the event. | 
**source** | **str** | Identifies the context in which an event happened. | 
**specversion** | **str** | The version of the CloudEvents specification which the event uses. | [default to '1.0']
**type** | **str** | Contains a value describing the type of event related to the originating occurrence. | 
**datacontenttype** | **str** | Content type of the CloudEvents data value. Only the value \&quot;application/json\&quot; is allowed over HTTP. | [optional] 
**dataschema** | **str** | Identifies the schema that data adheres to. | [optional] 
**subject** | **str** | Describes the subject of the event in the context of the event producer (identified by source). | 
**time** | **datetime** | Timestamp of when the occurrence happened. Must adhere to RFC 3339. | [optional] 
**data** | **Dict[str, object]** | The event payload. Optional, if present it must be a JSON object. | [optional] 

## Example

```python
from moolabs.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


