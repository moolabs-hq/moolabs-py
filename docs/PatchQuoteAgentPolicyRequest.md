# PatchQuoteAgentPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**kill_switch** | **bool** |  | [optional] 
**shadow_mode** | **bool** |  | [optional] 
**evidence_coverage_threshold** | **int** |  | [optional] 
**rate_limit_per_minute** | **int** |  | [optional] 
**allowed_surfaces** | **List[str]** |  | [optional] 

## Example

```python
from moolabs.models.patch_quote_agent_policy_request import PatchQuoteAgentPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchQuoteAgentPolicyRequest from a JSON string
patch_quote_agent_policy_request_instance = PatchQuoteAgentPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(PatchQuoteAgentPolicyRequest.to_json())

# convert the object into a dict
patch_quote_agent_policy_request_dict = patch_quote_agent_policy_request_instance.to_dict()
# create an instance of PatchQuoteAgentPolicyRequest from a dict
patch_quote_agent_policy_request_from_dict = PatchQuoteAgentPolicyRequest.from_dict(patch_quote_agent_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


