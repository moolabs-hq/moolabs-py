# ShadowRunMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shadow_run_id** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**wape** | **float** |  | 
**coverage_pct** | **float** |  | 
**total_import_rows** | **int** |  | 
**attributed_rows** | **int** |  | 
**algorithm_breakdown** | [**Dict[str, AlgorithmBreakdownItem]**](AlgorithmBreakdownItem.md) |  | 

## Example

```python
from moolabs.models.shadow_run_metrics import ShadowRunMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ShadowRunMetrics from a JSON string
shadow_run_metrics_instance = ShadowRunMetrics.from_json(json)
# print the JSON string representation of the object
print(ShadowRunMetrics.to_json())

# convert the object into a dict
shadow_run_metrics_dict = shadow_run_metrics_instance.to_dict()
# create an instance of ShadowRunMetrics from a dict
shadow_run_metrics_from_dict = ShadowRunMetrics.from_dict(shadow_run_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


