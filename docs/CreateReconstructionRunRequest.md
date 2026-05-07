# CreateReconstructionRunRequest

Request to create a reconstruction run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier | 
**pool_id** | **str** | Pool identifier | 
**root_wallet_id** | **str** | Root wallet ID | 
**from_effective_at** | **datetime** | Start of effective time window | 
**to_effective_at** | **datetime** | End of effective time window | 
**trigger_event_id** | **str** | Trigger event ID (LATE event) | 
**late_threshold_seconds** | **int** | LATE event threshold (seconds) | [optional] [default to 3600]

## Example

```python
from moolabs.models.create_reconstruction_run_request import CreateReconstructionRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReconstructionRunRequest from a JSON string
create_reconstruction_run_request_instance = CreateReconstructionRunRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReconstructionRunRequest.to_json())

# convert the object into a dict
create_reconstruction_run_request_dict = create_reconstruction_run_request_instance.to_dict()
# create an instance of CreateReconstructionRunRequest from a dict
create_reconstruction_run_request_from_dict = CreateReconstructionRunRequest.from_dict(create_reconstruction_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


