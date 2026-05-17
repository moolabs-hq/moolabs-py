# CostAdjustmentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**original_cost_event_id** | **str** |  | [optional] 
**original_cost_event_timestamp** | **datetime** |  | [optional] 
**external_adjustment_id** | **str** | Optional client-owned idempotency key for adjustments. When present, server dedups on (tenant_id, external_adjustment_id); re-POST returns the original 201 row. Backward-compatible: existing callers that omit this field get append-only behavior. | [optional] 
**adjustment_type** | **str** |  | 
**adjustment_scope** | **str** |  | [optional] [default to 'event']
**original_total** | [**OriginalTotal**](OriginalTotal.md) |  | [optional] 
**adjusted_total** | [**AdjustedTotal**](AdjustedTotal.md) |  | [optional] 
**adjustment_amount** | [**AdjustmentAmount**](AdjustmentAmount.md) |  | 
**adjustment_period_start** | **datetime** |  | [optional] 
**adjustment_period_end** | **datetime** |  | [optional] 
**provider** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**reason** | **str** |  | 
**source** | **str** |  | [optional] 
**approved_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.cost_adjustment_create import CostAdjustmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CostAdjustmentCreate from a JSON string
cost_adjustment_create_instance = CostAdjustmentCreate.from_json(json)
# print the JSON string representation of the object
print(CostAdjustmentCreate.to_json())

# convert the object into a dict
cost_adjustment_create_dict = cost_adjustment_create_instance.to_dict()
# create an instance of CostAdjustmentCreate from a dict
cost_adjustment_create_from_dict = CostAdjustmentCreate.from_dict(cost_adjustment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


