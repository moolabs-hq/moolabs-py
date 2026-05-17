# ObservationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**bom_id** | **str** |  | 
**bom_version** | **int** |  | 
**total_billing_events** | **int** |  | 
**fully_observed_count** | **int** |  | 
**partially_observed_count** | **int** |  | 
**observation_unknown_count** | **int** |  | 
**observation_coverage_pct** | **float** |  | 
**per_workflow_type** | **List[Dict[str, object]]** |  | 

## Example

```python
from moolabs.models.observation_out import ObservationOut

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationOut from a JSON string
observation_out_instance = ObservationOut.from_json(json)
# print the JSON string representation of the object
print(ObservationOut.to_json())

# convert the object into a dict
observation_out_dict = observation_out_instance.to_dict()
# create an instance of ObservationOut from a dict
observation_out_from_dict = ObservationOut.from_dict(observation_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


