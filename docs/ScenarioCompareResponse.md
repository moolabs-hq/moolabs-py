# ScenarioCompareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_scenarios** | **int** |  | 
**scenarios** | [**List[ScenarioItem]**](ScenarioItem.md) |  | 

## Example

```python
from moolabs.models.scenario_compare_response import ScenarioCompareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioCompareResponse from a JSON string
scenario_compare_response_instance = ScenarioCompareResponse.from_json(json)
# print the JSON string representation of the object
print(ScenarioCompareResponse.to_json())

# convert the object into a dict
scenario_compare_response_dict = scenario_compare_response_instance.to_dict()
# create an instance of ScenarioCompareResponse from a dict
scenario_compare_response_from_dict = ScenarioCompareResponse.from_dict(scenario_compare_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


