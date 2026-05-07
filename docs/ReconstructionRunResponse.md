# ReconstructionRunResponse

Response from creating a reconstruction run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** |  | 
**root_wallet_id** | **str** |  | 
**wallet_count** | **int** |  | 
**affected_events_count** | **int** |  | 
**correction_entries_created** | **List[str]** |  | 

## Example

```python
from moolabs.models.reconstruction_run_response import ReconstructionRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReconstructionRunResponse from a JSON string
reconstruction_run_response_instance = ReconstructionRunResponse.from_json(json)
# print the JSON string representation of the object
print(ReconstructionRunResponse.to_json())

# convert the object into a dict
reconstruction_run_response_dict = reconstruction_run_response_instance.to_dict()
# create an instance of ReconstructionRunResponse from a dict
reconstruction_run_response_from_dict = ReconstructionRunResponse.from_dict(reconstruction_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


