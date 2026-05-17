# ScenarioRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenarios** | [**List[SimulateMarginRequest]**](SimulateMarginRequest.md) | List of simulation scenarios for side-by-side comparison | 

## Example

```python
from moolabs.models.scenario_request import ScenarioRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioRequest from a JSON string
scenario_request_instance = ScenarioRequest.from_json(json)
# print the JSON string representation of the object
print(ScenarioRequest.to_json())

# convert the object into a dict
scenario_request_dict = scenario_request_instance.to_dict()
# create an instance of ScenarioRequest from a dict
scenario_request_from_dict = ScenarioRequest.from_dict(scenario_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


