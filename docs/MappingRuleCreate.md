# MappingRuleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_name** | **str** |  | 
**description** | **str** |  | [optional] 
**priority** | **int** |  | [optional] [default to 100]
**source_type** | **str** |  | 
**source_field** | **str** |  | 
**transform_type** | **str** |  | [optional] [default to 'direct']
**transform_pattern** | **str** |  | [optional] 
**transform_map** | **Dict[str, object]** |  | [optional] 
**target_field** | **str** |  | 
**pii_check_enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from moolabs.models.mapping_rule_create import MappingRuleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MappingRuleCreate from a JSON string
mapping_rule_create_instance = MappingRuleCreate.from_json(json)
# print the JSON string representation of the object
print(MappingRuleCreate.to_json())

# convert the object into a dict
mapping_rule_create_dict = mapping_rule_create_instance.to_dict()
# create an instance of MappingRuleCreate from a dict
mapping_rule_create_from_dict = MappingRuleCreate.from_dict(mapping_rule_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


