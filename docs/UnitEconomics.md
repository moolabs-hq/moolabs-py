# UnitEconomics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**mean_cost** | **float** |  | 
**p50_cost** | **float** |  | 
**p95_cost** | **float** |  | 
**p99_cost** | **float** |  | 
**sample_count** | **int** |  | 

## Example

```python
from moolabs.models.unit_economics import UnitEconomics

# TODO update the JSON string below
json = "{}"
# create an instance of UnitEconomics from a JSON string
unit_economics_instance = UnitEconomics.from_json(json)
# print the JSON string representation of the object
print(UnitEconomics.to_json())

# convert the object into a dict
unit_economics_dict = unit_economics_instance.to_dict()
# create an instance of UnitEconomics from a dict
unit_economics_from_dict = UnitEconomics.from_dict(unit_economics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


