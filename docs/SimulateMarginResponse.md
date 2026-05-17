# SimulateMarginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_key** | **str** |  | 
**simulation_period_months** | **int** |  | 
**projected_volume** | **int** |  | 
**proposed_price_per_event** | **float** |  | 
**projected_revenue** | **float** |  | 
**projected_cost** | **float** |  | 
**projected_margin** | **float** |  | 
**projected_margin_pct** | **float** |  | 
**bom_id** | **str** |  | 
**bom_version** | **int** |  | 
**component_breakdown** | **List[Dict[str, object]]** |  | 
**risk_flags** | **List[Dict[str, object]]** |  | 
**reconciliation_basis** | [**ReconciliationBasisOut**](ReconciliationBasisOut.md) |  | 

## Example

```python
from moolabs.models.simulate_margin_response import SimulateMarginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateMarginResponse from a JSON string
simulate_margin_response_instance = SimulateMarginResponse.from_json(json)
# print the JSON string representation of the object
print(SimulateMarginResponse.to_json())

# convert the object into a dict
simulate_margin_response_dict = simulate_margin_response_instance.to_dict()
# create an instance of SimulateMarginResponse from a dict
simulate_margin_response_from_dict = SimulateMarginResponse.from_dict(simulate_margin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


