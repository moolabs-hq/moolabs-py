# BulkReplayRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_ids** | **List[str]** |  | [optional] 
**source** | **str** |  | [optional] 
**max_count** | **int** |  | [optional] [default to 100]

## Example

```python
from moolabs.models.bulk_replay_request import BulkReplayRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkReplayRequest from a JSON string
bulk_replay_request_instance = BulkReplayRequest.from_json(json)
# print the JSON string representation of the object
print(BulkReplayRequest.to_json())

# convert the object into a dict
bulk_replay_request_dict = bulk_replay_request_instance.to_dict()
# create an instance of BulkReplayRequest from a dict
bulk_replay_request_from_dict = BulkReplayRequest.from_dict(bulk_replay_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


