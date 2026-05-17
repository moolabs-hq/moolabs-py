# SimulateOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bom_id** | **str** |  | 
**bom_version** | **int** |  | 
**feature_key** | **str** |  | 
**billing_event_count** | **int** |  | 
**components** | **List[Dict[str, object]]** |  | 
**total_projected_cost** | **float** |  | 
**total_standard_cost** | **float** |  | 
**vs_standard** | **Dict[str, object]** |  | 
**rate_freshness** | **str** |  | 

## Example

```python
from moolabs.models.simulate_out import SimulateOut

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateOut from a JSON string
simulate_out_instance = SimulateOut.from_json(json)
# print the JSON string representation of the object
print(SimulateOut.to_json())

# convert the object into a dict
simulate_out_dict = simulate_out_instance.to_dict()
# create an instance of SimulateOut from a dict
simulate_out_from_dict = SimulateOut.from_dict(simulate_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


