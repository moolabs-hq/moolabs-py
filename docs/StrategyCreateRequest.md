# StrategyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**risk_tier** | **str** |  | 
**stages** | [**List[StageSchema]**](StageSchema.md) |  | 
**channel_policy** | [**Dict[str, ChannelPolicySchema]**](ChannelPolicySchema.md) |  | [optional] 
**segment_filters** | **Dict[str, object]** |  | [optional] 
**escalation_policy** | **Dict[str, object]** |  | [optional] 
**priority** | **int** |  | [optional] [default to 100]
**is_default** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.strategy_create_request import StrategyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StrategyCreateRequest from a JSON string
strategy_create_request_instance = StrategyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StrategyCreateRequest.to_json())

# convert the object into a dict
strategy_create_request_dict = strategy_create_request_instance.to_dict()
# create an instance of StrategyCreateRequest from a dict
strategy_create_request_from_dict = StrategyCreateRequest.from_dict(strategy_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


