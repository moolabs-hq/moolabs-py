# VarianceSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**items** | [**List[VarianceDecompositionOut]**](VarianceDecompositionOut.md) |  | 
**total_items** | **int** |  | 

## Example

```python
from moolabs.models.variance_summary_response import VarianceSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VarianceSummaryResponse from a JSON string
variance_summary_response_instance = VarianceSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(VarianceSummaryResponse.to_json())

# convert the object into a dict
variance_summary_response_dict = variance_summary_response_instance.to_dict()
# create an instance of VarianceSummaryResponse from a dict
variance_summary_response_from_dict = VarianceSummaryResponse.from_dict(variance_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


