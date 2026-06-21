# ClausePack

A versioned bundle of clause families for a given industry vertical.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack_id** | **str** |  | 
**version** | **int** |  | 
**lifecycle_state** | **str** |  | 
**industry_vertical** | **str** |  | 
**applies_to_contract_types** | **List[str]** |  | 
**provenance** | [**PackProvenance**](PackProvenance.md) |  | 
**clause_families** | [**List[ClauseFamily]**](ClauseFamily.md) |  | 

## Example

```python
from moolabs.models.clause_pack import ClausePack

# TODO update the JSON string below
json = "{}"
# create an instance of ClausePack from a JSON string
clause_pack_instance = ClausePack.from_json(json)
# print the JSON string representation of the object
print(ClausePack.to_json())

# convert the object into a dict
clause_pack_dict = clause_pack_instance.to_dict()
# create an instance of ClausePack from a dict
clause_pack_from_dict = ClausePack.from_dict(clause_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


