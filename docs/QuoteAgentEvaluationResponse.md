# QuoteAgentEvaluationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**agent_run_id** | **str** |  | 
**command_id** | **str** |  | 
**outcome** | **str** |  | 
**reviewer_actor_id** | **str** |  | 
**human_override_reason** | **str** |  | 
**evidence_coverage** | **int** |  | 
**metrics** | **Dict[str, object]** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from moolabs.models.quote_agent_evaluation_response import QuoteAgentEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAgentEvaluationResponse from a JSON string
quote_agent_evaluation_response_instance = QuoteAgentEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteAgentEvaluationResponse.to_json())

# convert the object into a dict
quote_agent_evaluation_response_dict = quote_agent_evaluation_response_instance.to_dict()
# create an instance of QuoteAgentEvaluationResponse from a dict
quote_agent_evaluation_response_from_dict = QuoteAgentEvaluationResponse.from_dict(quote_agent_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


