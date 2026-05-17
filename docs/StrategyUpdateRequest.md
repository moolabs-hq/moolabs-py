# StrategyUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**risk_tier** | **str** |  | [optional] 
**stages** | [**List[StageSchema]**](StageSchema.md) |  | [optional] 
**channel_policy** | [**Dict[str, ChannelPolicySchema]**](ChannelPolicySchema.md) |  | [optional] 
**segment_filters** | **Dict[str, object]** |  | [optional] 
**escalation_policy** | **Dict[str, object]** |  | [optional] 
**priority** | **int** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from moolabs.models.strategy_update_request import StrategyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StrategyUpdateRequest from a JSON string
strategy_update_request_instance = StrategyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(StrategyUpdateRequest.to_json())

# convert the object into a dict
strategy_update_request_dict = strategy_update_request_instance.to_dict()
# create an instance of StrategyUpdateRequest from a dict
strategy_update_request_from_dict = StrategyUpdateRequest.from_dict(strategy_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


