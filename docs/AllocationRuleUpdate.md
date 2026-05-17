# AllocationRuleUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rule_type** | **str** |  | [optional] 
**source_filter** | **Dict[str, object]** |  | [optional] 
**target_type** | **str** |  | [optional] 
**allocation_keys** | [**List[AllocationKey]**](AllocationKey.md) |  | [optional] 
**amortization_months** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from moolabs.models.allocation_rule_update import AllocationRuleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationRuleUpdate from a JSON string
allocation_rule_update_instance = AllocationRuleUpdate.from_json(json)
# print the JSON string representation of the object
print(AllocationRuleUpdate.to_json())

# convert the object into a dict
allocation_rule_update_dict = allocation_rule_update_instance.to_dict()
# create an instance of AllocationRuleUpdate from a dict
allocation_rule_update_from_dict = AllocationRuleUpdate.from_dict(allocation_rule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


