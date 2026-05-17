# ComputeVarianceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant UUID | 
**feature_key** | **str** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**bom_template_id** | **str** | BOM template UUID | 

## Example

```python
from moolabs.models.compute_variance_request import ComputeVarianceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeVarianceRequest from a JSON string
compute_variance_request_instance = ComputeVarianceRequest.from_json(json)
# print the JSON string representation of the object
print(ComputeVarianceRequest.to_json())

# convert the object into a dict
compute_variance_request_dict = compute_variance_request_instance.to_dict()
# create an instance of ComputeVarianceRequest from a dict
compute_variance_request_from_dict = ComputeVarianceRequest.from_dict(compute_variance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


