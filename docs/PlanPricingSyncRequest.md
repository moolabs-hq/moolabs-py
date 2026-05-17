# PlanPricingSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**operation** | **str** |  | 
**plan_id** | **str** |  | 
**plan** | **Dict[str, object]** |  | [optional] 
**effective_at** | **datetime** |  | [optional] 

## Example

```python
from moolabs.models.plan_pricing_sync_request import PlanPricingSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanPricingSyncRequest from a JSON string
plan_pricing_sync_request_instance = PlanPricingSyncRequest.from_json(json)
# print the JSON string representation of the object
print(PlanPricingSyncRequest.to_json())

# convert the object into a dict
plan_pricing_sync_request_dict = plan_pricing_sync_request_instance.to_dict()
# create an instance of PlanPricingSyncRequest from a dict
plan_pricing_sync_request_from_dict = PlanPricingSyncRequest.from_dict(plan_pricing_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


