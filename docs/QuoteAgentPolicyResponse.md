# QuoteAgentPolicyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**agent_name** | **str** |  | 
**trust_tier** | **int** |  | 
**enabled** | **bool** |  | 
**kill_switch** | **bool** |  | 
**shadow_mode** | **bool** |  | 
**max_autonomy** | **str** |  | 
**evidence_coverage_threshold** | **int** |  | 
**rate_limit_per_minute** | **int** |  | 
**allowed_surfaces** | **List[str]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from moolabs.models.quote_agent_policy_response import QuoteAgentPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteAgentPolicyResponse from a JSON string
quote_agent_policy_response_instance = QuoteAgentPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(QuoteAgentPolicyResponse.to_json())

# convert the object into a dict
quote_agent_policy_response_dict = quote_agent_policy_response_instance.to_dict()
# create an instance of QuoteAgentPolicyResponse from a dict
quote_agent_policy_response_from_dict = QuoteAgentPolicyResponse.from_dict(quote_agent_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


