# ClauseCitations

Citation references for a clause family.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market** | **List[str]** |  | [optional] 
**tenant_kb** | **List[str]** |  | [optional] 
**tenant_corpus** | **List[str]** |  | [optional] 

## Example

```python
from moolabs.models.clause_citations import ClauseCitations

# TODO update the JSON string below
json = "{}"
# create an instance of ClauseCitations from a JSON string
clause_citations_instance = ClauseCitations.from_json(json)
# print the JSON string representation of the object
print(ClauseCitations.to_json())

# convert the object into a dict
clause_citations_dict = clause_citations_instance.to_dict()
# create an instance of ClauseCitations from a dict
clause_citations_from_dict = ClauseCitations.from_dict(clause_citations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


