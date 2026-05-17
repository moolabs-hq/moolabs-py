# GateStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gate_status** | **str** |  | 
**wape** | **float** |  | 
**wape_pass** | **bool** |  | 
**wape_threshold** | **float** |  | 
**coverage_pct** | **float** |  | 
**coverage_pass** | **bool** |  | 
**coverage_threshold** | **float** |  | 
**shadow_run_id** | **str** |  | 
**evaluated_at** | **str** |  | 

## Example

```python
from moolabs.models.gate_status_response import GateStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GateStatusResponse from a JSON string
gate_status_response_instance = GateStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GateStatusResponse.to_json())

# convert the object into a dict
gate_status_response_dict = gate_status_response_instance.to_dict()
# create an instance of GateStatusResponse from a dict
gate_status_response_from_dict = GateStatusResponse.from_dict(gate_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


