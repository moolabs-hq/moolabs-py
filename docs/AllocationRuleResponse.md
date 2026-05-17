# AllocationRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**rule_type** | **str** |  | 
**source_filter** | **Dict[str, object]** |  | 
**target_type** | **str** |  | 
**allocation_keys** | **List[object]** |  | 
**amortization_months** | **int** |  | 
**is_active** | **bool** |  | 
**priority** | **int** |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from moolabs.models.allocation_rule_response import AllocationRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationRuleResponse from a JSON string
allocation_rule_response_instance = AllocationRuleResponse.from_json(json)
# print the JSON string representation of the object
print(AllocationRuleResponse.to_json())

# convert the object into a dict
allocation_rule_response_dict = allocation_rule_response_instance.to_dict()
# create an instance of AllocationRuleResponse from a dict
allocation_rule_response_from_dict = AllocationRuleResponse.from_dict(allocation_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


