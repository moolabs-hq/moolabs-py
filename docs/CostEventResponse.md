# CostEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**idempotency_key** | **str** |  | 
**request_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**feature_id** | **str** |  | [optional] 
**provider** | **str** |  | 
**model_requested** | **str** |  | [optional] 
**model_responded** | **str** |  | [optional] 
**observed_total_cost** | **str** |  | 
**currency** | **str** |  | 
**reporting_total_cost** | **str** |  | 
**reporting_currency** | **str** |  | 
**status** | **str** |  | 
**tags** | **Dict[str, object]** |  | [optional] 
**event_timestamp** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from moolabs.models.cost_event_response import CostEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostEventResponse from a JSON string
cost_event_response_instance = CostEventResponse.from_json(json)
# print the JSON string representation of the object
print(CostEventResponse.to_json())

# convert the object into a dict
cost_event_response_dict = cost_event_response_instance.to_dict()
# create an instance of CostEventResponse from a dict
cost_event_response_from_dict = CostEventResponse.from_dict(cost_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


