# BomVarianceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bom_template_id** | **str** |  | 
**bom_version** | **int** |  | 
**feature_key** | **str** |  | 
**period_start** | **str** |  | 
**period_end** | **str** |  | 
**standard_total** | **float** |  | 
**actual_total** | **float** |  | 
**total_variance** | **float** |  | 
**price_variance** | **float** |  | 
**usage_variance** | **float** |  | 
**volume_variance** | **float** |  | 
**mix_variance** | **float** |  | 
**attribution_tier** | **str** |  | 
**heuristic_alert** | **bool** |  | 
**components** | **List[Dict[str, object]]** |  | 

## Example

```python
from moolabs.models.bom_variance_out import BomVarianceOut

# TODO update the JSON string below
json = "{}"
# create an instance of BomVarianceOut from a JSON string
bom_variance_out_instance = BomVarianceOut.from_json(json)
# print the JSON string representation of the object
print(BomVarianceOut.to_json())

# convert the object into a dict
bom_variance_out_dict = bom_variance_out_instance.to_dict()
# create an instance of BomVarianceOut from a dict
bom_variance_out_from_dict = BomVarianceOut.from_dict(bom_variance_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


