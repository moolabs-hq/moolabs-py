# SnapshotResponse

Response from creating a balance snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**pool_id** | **str** |  | 
**wallet_id** | **str** |  | 
**as_of_effective_at** | **datetime** |  | 
**as_of_recorded_at** | **datetime** |  | 
**balance_micros** | **int** |  | 
**snapshot_fingerprint** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from moolabs.models.snapshot_response import SnapshotResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotResponse from a JSON string
snapshot_response_instance = SnapshotResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotResponse.to_json())

# convert the object into a dict
snapshot_response_dict = snapshot_response_instance.to_dict()
# create an instance of SnapshotResponse from a dict
snapshot_response_from_dict = SnapshotResponse.from_dict(snapshot_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


