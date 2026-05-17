# SnapshotComputeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Deprecated. Tenant is derived from API key. If provided, must match authenticated tenant. | [optional] 
**period_type** | **str** |  | [optional] [default to 'daily']
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 

## Example

```python
from moolabs.models.snapshot_compute_request import SnapshotComputeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotComputeRequest from a JSON string
snapshot_compute_request_instance = SnapshotComputeRequest.from_json(json)
# print the JSON string representation of the object
print(SnapshotComputeRequest.to_json())

# convert the object into a dict
snapshot_compute_request_dict = snapshot_compute_request_instance.to_dict()
# create an instance of SnapshotComputeRequest from a dict
snapshot_compute_request_from_dict = SnapshotComputeRequest.from_dict(snapshot_compute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


