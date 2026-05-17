# CostAdjustmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**original_cost_event_id** | **str** |  | 
**original_cost_event_timestamp** | **datetime** |  | 
**adjustment_type** | **str** |  | 
**adjustment_amount** | **str** |  | 
**reason** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from moolabs.models.cost_adjustment_response import CostAdjustmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CostAdjustmentResponse from a JSON string
cost_adjustment_response_instance = CostAdjustmentResponse.from_json(json)
# print the JSON string representation of the object
print(CostAdjustmentResponse.to_json())

# convert the object into a dict
cost_adjustment_response_dict = cost_adjustment_response_instance.to_dict()
# create an instance of CostAdjustmentResponse from a dict
cost_adjustment_response_from_dict = CostAdjustmentResponse.from_dict(cost_adjustment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


