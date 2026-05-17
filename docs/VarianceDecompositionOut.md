# VarianceDecompositionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**standard_cost** | **float** |  | 
**actual_cost** | **float** |  | 
**total_variance** | **float** |  | 
**price_variance** | **float** |  | 
**usage_variance** | **float** |  | 
**volume_variance** | **float** |  | 
**mix_variance** | **float** |  | 
**attribution_tier** | **str** |  | 
**heuristic_alert** | **bool** |  | 
**bom_version** | **int** |  | 
**bom_template_id** | **str** |  | 
**computed_at** | **str** |  | 
**alert_note** | **str** |  | [optional] 

## Example

```python
from moolabs.models.variance_decomposition_out import VarianceDecompositionOut

# TODO update the JSON string below
json = "{}"
# create an instance of VarianceDecompositionOut from a JSON string
variance_decomposition_out_instance = VarianceDecompositionOut.from_json(json)
# print the JSON string representation of the object
print(VarianceDecompositionOut.to_json())

# convert the object into a dict
variance_decomposition_out_dict = variance_decomposition_out_instance.to_dict()
# create an instance of VarianceDecompositionOut from a dict
variance_decomposition_out_from_dict = VarianceDecompositionOut.from_dict(variance_decomposition_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


