# CostEventIngest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**idempotency_key** | **str** |  | 
**trace_id** | **str** |  | [optional] 
**root_span_id** | **str** |  | [optional] 
**span_id** | **str** |  | [optional] 
**parent_span_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**feature_id** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**workflow_version** | **str** |  | [optional] 
**provider** | **str** |  | 
**model_requested** | **str** |  | [optional] 
**model_responded** | **str** |  | [optional] 
**operation_type** | **str** |  | [optional] 
**component_type** | **str** |  | [optional] 
**observed_total_cost** | [**ObservedTotalCost**](ObservedTotalCost.md) |  | 
**currency** | **str** |  | 
**reporting_total_cost** | [**ReportingTotalCost**](ReportingTotalCost.md) |  | 
**reporting_currency** | **str** |  | [optional] [default to 'USD']
**fx_rate_to_reporting** | [**FxRateToReporting**](FxRateToReporting.md) |  | [optional] 
**latency_ms** | **int** |  | [optional] 
**cache_hit** | **bool** |  | [optional] [default to False]
**environment** | **str** |  | [optional] [default to 'production']
**usage_event_id** | **str** |  | [optional] 
**ingestion_path** | **str** |  | [optional] [default to 'sdk']
**ingestion_source** | **str** |  | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 
**provider_metadata** | **Dict[str, object]** |  | [optional] 
**otel_attributes** | **Dict[str, object]** |  | [optional] 
**event_timestamp** | **datetime** |  | 
**line_items** | [**List[LineItemCreate]**](LineItemCreate.md) |  | [optional] 

## Example

```python
from moolabs.models.cost_event_ingest import CostEventIngest

# TODO update the JSON string below
json = "{}"
# create an instance of CostEventIngest from a JSON string
cost_event_ingest_instance = CostEventIngest.from_json(json)
# print the JSON string representation of the object
print(CostEventIngest.to_json())

# convert the object into a dict
cost_event_ingest_dict = cost_event_ingest_instance.to_dict()
# create an instance of CostEventIngest from a dict
cost_event_ingest_from_dict = CostEventIngest.from_dict(cost_event_ingest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


