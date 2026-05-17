# SnapshotComputeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**tenant_id** | **str** |  | 
**period_type** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**status** | **str** |  | 
**snapshot** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.snapshot_compute_response import SnapshotComputeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotComputeResponse from a JSON string
snapshot_compute_response_instance = SnapshotComputeResponse.from_json(json)
# print the JSON string representation of the object
print(SnapshotComputeResponse.to_json())

# convert the object into a dict
snapshot_compute_response_dict = snapshot_compute_response_instance.to_dict()
# create an instance of SnapshotComputeResponse from a dict
snapshot_compute_response_from_dict = SnapshotComputeResponse.from_dict(snapshot_compute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


