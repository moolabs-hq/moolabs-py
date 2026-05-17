# NoteResponse

GET /cases/{case_id}/notes/{id} response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**case_id** | **str** |  | 
**account_id** | **str** |  | [optional] 
**content** | **str** |  | 
**author** | **str** |  | 
**note_type** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.note_response import NoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteResponse from a JSON string
note_response_instance = NoteResponse.from_json(json)
# print the JSON string representation of the object
print(NoteResponse.to_json())

# convert the object into a dict
note_response_dict = note_response_instance.to_dict()
# create an instance of NoteResponse from a dict
note_response_from_dict = NoteResponse.from_dict(note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


