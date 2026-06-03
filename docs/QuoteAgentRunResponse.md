# QuoteAgentRunResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**quote_id** | **str** |  | 
**quote_version** | **int** |  | 
**agent_name** | **str** |  | 
**trust_tier** | **int** |  | 
**surface** | **str** |  | 
**actor_type** | **str** |  | 
**actor_id** | **str** |  | 
**status** | **str** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**input_hash** | **str** |  | 
**output_hash** | **str** |  | 
**rationale_summary** | **str** |  | 
**tool_trace** | **List[Dict[str, object]]** |  | 
**error_code** | **str** |  | 
**trace_id** | **str** |  | 

## Example

```python
from moolabs.models.quote_agent_run_response import QuoteAgentRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAgentRunResponse from a JSON string
quote_agent_run_response_instance = QuoteAgentRunResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteAgentRunResponse.to_json())

# convert the object into a dict
quote_agent_run_response_dict = quote_agent_run_response_instance.to_dict()
# create an instance of QuoteAgentRunResponse from a dict
quote_agent_run_response_from_dict = QuoteAgentRunResponse.from_dict(quote_agent_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


