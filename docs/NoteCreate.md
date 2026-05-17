# NoteCreate

POST /cases/{case_id}/notes — create a note.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**author** | **str** |  | 
**note_type** | **str** | general, escalation, dispute, internal, customer_interaction | [optional] [default to 'general']
**account_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.note_create import NoteCreate

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCreate from a JSON string
note_create_instance = NoteCreate.from_json(json)
# print the JSON string representation of the object
print(NoteCreate.to_json())

# convert the object into a dict
note_create_dict = note_create_instance.to_dict()
# create an instance of NoteCreate from a dict
note_create_from_dict = NoteCreate.from_dict(note_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


