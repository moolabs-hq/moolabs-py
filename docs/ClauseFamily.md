# ClauseFamily

A logical group of related clauses, each with multiple negotiating positions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family_id** | **str** |  | 
**display_name** | **str** |  | 
**owner_persona** | **str** |  | 
**required** | **bool** |  | [optional] [default to False]
**detector** | **Dict[str, object]** |  | 
**positions** | [**Dict[str, ClausePosition]**](ClausePosition.md) |  | 
**deal_context** | [**DealContext**](DealContext.md) |  | [optional] 
**citations** | [**ClauseCitations**](ClauseCitations.md) |  | [optional] 

## Example

```python
from moolabs.models.clause_family import ClauseFamily

# TODO update the JSON string below
json = "{}"
# create an instance of ClauseFamily from a JSON string
clause_family_instance = ClauseFamily.from_json(json)
# print the JSON string representation of the object
print(ClauseFamily.to_json())

# convert the object into a dict
clause_family_dict = clause_family_instance.to_dict()
# create an instance of ClauseFamily from a dict
clause_family_from_dict = ClauseFamily.from_dict(clause_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


