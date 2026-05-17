# MappingRuleUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**source_type** | **str** |  | [optional] 
**source_field** | **str** |  | [optional] 
**transform_type** | **str** |  | [optional] 
**transform_pattern** | **str** |  | [optional] 
**transform_map** | **Dict[str, object]** |  | [optional] 
**target_field** | **str** |  | [optional] 
**pii_check_enabled** | **bool** |  | [optional] 

## Example

```python
from moolabs.models.mapping_rule_update import MappingRuleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MappingRuleUpdate from a JSON string
mapping_rule_update_instance = MappingRuleUpdate.from_json(json)
# print the JSON string representation of the object
print(MappingRuleUpdate.to_json())

# convert the object into a dict
mapping_rule_update_dict = mapping_rule_update_instance.to_dict()
# create an instance of MappingRuleUpdate from a dict
mapping_rule_update_from_dict = MappingRuleUpdate.from_dict(mapping_rule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


