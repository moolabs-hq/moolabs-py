# ComputeVarianceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**tenant_id** | **str** |  | 
**feature_key** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**bom_template_id** | **str** |  | 
**status** | **str** |  | 
**variance** | [**VarianceDecompositionOut**](VarianceDecompositionOut.md) |  | [optional] 

## Example

```python
from moolabs.models.compute_variance_response import ComputeVarianceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeVarianceResponse from a JSON string
compute_variance_response_instance = ComputeVarianceResponse.from_json(json)
# print the JSON string representation of the object
print(ComputeVarianceResponse.to_json())

# convert the object into a dict
compute_variance_response_dict = compute_variance_response_instance.to_dict()
# create an instance of ComputeVarianceResponse from a dict
compute_variance_response_from_dict = ComputeVarianceResponse.from_dict(compute_variance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


