# IngestedEventCursorPaginatedResponse

A response for cursor pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IngestedEvent]**](IngestedEvent.md) | The items in the response. | 
**next_cursor** | **str** | The cursor of the last item in the list. | [optional] 

## Example

```python
from moolabs.models.ingested_event_cursor_paginated_response import IngestedEventCursorPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IngestedEventCursorPaginatedResponse from a JSON string
ingested_event_cursor_paginated_response_instance = IngestedEventCursorPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(IngestedEventCursorPaginatedResponse.to_json())

# convert the object into a dict
ingested_event_cursor_paginated_response_dict = ingested_event_cursor_paginated_response_instance.to_dict()
# create an instance of IngestedEventCursorPaginatedResponse from a dict
ingested_event_cursor_paginated_response_from_dict = IngestedEventCursorPaginatedResponse.from_dict(ingested_event_cursor_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


