# SaveRedlineEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_key** | **str** |  | 
**block_id** | **int** |  | 
**op** | **str** |  | 
**before** | **str** |  | 
**after** | **str** |  | 

## Example

```python
from moolabs.models.save_redline_edit_request import SaveRedlineEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SaveRedlineEditRequest from a JSON string
save_redline_edit_request_instance = SaveRedlineEditRequest.from_json(json)
# print the JSON string representation of the object
print(SaveRedlineEditRequest.to_json())

# convert the object into a dict
save_redline_edit_request_dict = save_redline_edit_request_instance.to_dict()
# create an instance of SaveRedlineEditRequest from a dict
save_redline_edit_request_from_dict = SaveRedlineEditRequest.from_dict(save_redline_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


