# BulkActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action: pause, resume, escalate, assign | 
**case_ids** | **List[str]** |  | 
**params** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.bulk_action_request import BulkActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkActionRequest from a JSON string
bulk_action_request_instance = BulkActionRequest.from_json(json)
# print the JSON string representation of the object
print(BulkActionRequest.to_json())

# convert the object into a dict
bulk_action_request_dict = bulk_action_request_instance.to_dict()
# create an instance of BulkActionRequest from a dict
bulk_action_request_from_dict = BulkActionRequest.from_dict(bulk_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


