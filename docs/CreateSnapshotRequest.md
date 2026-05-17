# CreateSnapshotRequest

Request to create a balance snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**wallet_id** | **str** | Wallet identifier | 
**as_of_effective_at** | **datetime** | Effective timestamp for balance calculation | 
**as_of_recorded_at** | **datetime** | Recorded timestamp (cut time) - defaults to now | [optional] 
**isolation_level** | **str** | Transaction isolation level | [optional] [default to 'REPEATABLE READ']

## Example

```python
from moolabs.models.create_snapshot_request import CreateSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotRequest from a JSON string
create_snapshot_request_instance = CreateSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSnapshotRequest.to_json())

# convert the object into a dict
create_snapshot_request_dict = create_snapshot_request_instance.to_dict()
# create an instance of CreateSnapshotRequest from a dict
create_snapshot_request_from_dict = CreateSnapshotRequest.from_dict(create_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


