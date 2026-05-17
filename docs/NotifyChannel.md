# NotifyChannel

A structured notification channel.  Use type=\"email\" with an address field:   {\"type\": \"email\", \"address\": \"ops@example.com\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Channel type — currently only &#39;email&#39; is supported | 
**address** | **str** | Email address to notify | 

## Example

```python
from moolabs.models.notify_channel import NotifyChannel

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyChannel from a JSON string
notify_channel_instance = NotifyChannel.from_json(json)
# print the JSON string representation of the object
print(NotifyChannel.to_json())

# convert the object into a dict
notify_channel_dict = notify_channel_instance.to_dict()
# create an instance of NotifyChannel from a dict
notify_channel_from_dict = NotifyChannel.from_dict(notify_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


