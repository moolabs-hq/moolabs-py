# ScenarioItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario_index** | **int** |  | 
**scenario_label** | **str** |  | 
**error** | **str** |  | [optional] 
**feature_key** | **str** |  | [optional] 
**simulation_period_months** | **int** |  | [optional] 
**projected_volume** | **int** |  | [optional] 
**proposed_price_per_event** | **float** |  | [optional] 
**projected_revenue** | **float** |  | [optional] 
**projected_cost** | **float** |  | [optional] 
**projected_margin** | **float** |  | [optional] 
**projected_margin_pct** | **float** |  | [optional] 
**bom_id** | **str** |  | [optional] 
**bom_version** | **int** |  | [optional] 
**component_breakdown** | **List[Dict[str, object]]** |  | [optional] 
**risk_flags** | **List[Dict[str, object]]** |  | [optional] 
**reconciliation_basis** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.scenario_item import ScenarioItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScenarioItem from a JSON string
scenario_item_instance = ScenarioItem.from_json(json)
# print the JSON string representation of the object
print(ScenarioItem.to_json())

# convert the object into a dict
scenario_item_dict = scenario_item_instance.to_dict()
# create an instance of ScenarioItem from a dict
scenario_item_from_dict = ScenarioItem.from_dict(scenario_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


