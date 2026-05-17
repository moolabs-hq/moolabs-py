# ShadowRunSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shadow_run_id** | **str** |  | 
**rows_processed** | **int** |  | 
**rows_attributed** | **int** |  | 
**coverage_pct** | **float** |  | 
**algorithms_used** | **Dict[str, int]** |  | 

## Example

```python
from moolabs.models.shadow_run_summary import ShadowRunSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ShadowRunSummary from a JSON string
shadow_run_summary_instance = ShadowRunSummary.from_json(json)
# print the JSON string representation of the object
print(ShadowRunSummary.to_json())

# convert the object into a dict
shadow_run_summary_dict = shadow_run_summary_instance.to_dict()
# create an instance of ShadowRunSummary from a dict
shadow_run_summary_from_dict = ShadowRunSummary.from_dict(shadow_run_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


