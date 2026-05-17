# AllocationRuleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**rule_type** | **str** | &#39;proportional_usage&#39;, &#39;fixed_percentage&#39;, &#39;equal_split&#39;, &#39;amortization&#39; | 
**source_filter** | **Dict[str, object]** |  | [optional] 
**target_type** | **str** | &#39;customer&#39;, &#39;feature&#39;, or &#39;plan&#39; | 
**allocation_keys** | [**List[AllocationKey]**](AllocationKey.md) |  | [optional] 
**amortization_months** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**priority** | **int** |  | [optional] [default to 100]
**created_by** | **str** |  | [optional] 

## Example

```python
from moolabs.models.allocation_rule_create import AllocationRuleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationRuleCreate from a JSON string
allocation_rule_create_instance = AllocationRuleCreate.from_json(json)
# print the JSON string representation of the object
print(AllocationRuleCreate.to_json())

# convert the object into a dict
allocation_rule_create_dict = allocation_rule_create_instance.to_dict()
# create an instance of AllocationRuleCreate from a dict
allocation_rule_create_from_dict = AllocationRuleCreate.from_dict(allocation_rule_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


