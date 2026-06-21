# CostEventDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**idempotency_key** | **str** |  | 
**request_id** | **str** |  | [optional] 
**customer_id** | **str** |  | 
**feature_id** | **str** |  | [optional] 
**provider** | **str** |  | 
**model_requested** | **str** |  | 
**model_responded** | **str** |  | 
**observed_total_cost** | **str** |  | 
**currency** | **str** |  | 
**reporting_total_cost** | **str** |  | 
**reporting_currency** | **str** |  | 
**status** | **str** |  | 
**tags** | **Dict[str, object]** |  | 
**event_timestamp** | **datetime** |  | 
**created_at** | **datetime** |  | 
**trace_id** | **str** |  | 
**span_id** | **str** |  | 
**latency_ms** | **int** |  | 
**line_items** | **List[Dict[str, object]]** |  | 
**reconciliation_status** | **str** |  | [optional] 

## Example

```python
from moolabs.models.cost_event_detail_response import CostEventDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostEventDetailResponse from a JSON string
cost_event_detail_response_instance = CostEventDetailResponse.from_json(json)
# print the JSON string representation of the object
print(CostEventDetailResponse.to_json())

# convert the object into a dict
cost_event_detail_response_dict = cost_event_detail_response_instance.to_dict()
# create an instance of CostEventDetailResponse from a dict
cost_event_detail_response_from_dict = CostEventDetailResponse.from_dict(cost_event_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


