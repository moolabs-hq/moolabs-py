# MappingRuleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**rule_name** | **str** |  | 
**description** | **str** |  | 
**is_enabled** | **bool** |  | 
**priority** | **int** |  | 
**source_type** | **str** |  | 
**source_field** | **str** |  | 
**transform_type** | **str** |  | 
**transform_pattern** | **str** |  | 
**transform_map** | **Dict[str, object]** |  | 
**target_field** | **str** |  | 
**pii_check_enabled** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** |  | 

## Example

```python
from moolabs.models.mapping_rule_response import MappingRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MappingRuleResponse from a JSON string
mapping_rule_response_instance = MappingRuleResponse.from_json(json)
# print the JSON string representation of the object
print(MappingRuleResponse.to_json())

# convert the object into a dict
mapping_rule_response_dict = mapping_rule_response_instance.to_dict()
# create an instance of MappingRuleResponse from a dict
mapping_rule_response_from_dict = MappingRuleResponse.from_dict(mapping_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


