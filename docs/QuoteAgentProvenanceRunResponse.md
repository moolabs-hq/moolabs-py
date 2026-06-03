# QuoteAgentProvenanceRunResponse


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
**rationale_summary** | **str** |  | 
**error_code** | **str** |  | 

## Example

```python
from moolabs.models.quote_agent_provenance_run_response import QuoteAgentProvenanceRunResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAgentProvenanceRunResponse from a JSON string
quote_agent_provenance_run_response_instance = QuoteAgentProvenanceRunResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteAgentProvenanceRunResponse.to_json())

# convert the object into a dict
quote_agent_provenance_run_response_dict = quote_agent_provenance_run_response_instance.to_dict()
# create an instance of QuoteAgentProvenanceRunResponse from a dict
quote_agent_provenance_run_response_from_dict = QuoteAgentProvenanceRunResponse.from_dict(quote_agent_provenance_run_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


