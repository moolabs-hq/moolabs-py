# SimulateMarginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant UUID | 
**feature_key** | **str** | Feature key to simulate | 
**proposed_price_per_event** | **float** | Proposed price per billing event | 
**projected_volume** | **int** | Billing events per month | 
**proposed_model_mix** | **Dict[str, float]** | Model mix fractions — must sum to 1.0. E.g. {&#39;claude-sonnet-4.6&#39;: 0.7, &#39;claude-haiku-3.5&#39;: 0.3} | [optional] 
**simulation_period_months** | **int** | Number of months to simulate | [optional] [default to 1]
**label** | **str** | Optional label for this scenario | [optional] 

## Example

```python
from moolabs.models.simulate_margin_request import SimulateMarginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimulateMarginRequest from a JSON string
simulate_margin_request_instance = SimulateMarginRequest.from_json(json)
# print the JSON string representation of the object
print(SimulateMarginRequest.to_json())

# convert the object into a dict
simulate_margin_request_dict = simulate_margin_request_instance.to_dict()
# create an instance of SimulateMarginRequest from a dict
simulate_margin_request_from_dict = SimulateMarginRequest.from_dict(simulate_margin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


