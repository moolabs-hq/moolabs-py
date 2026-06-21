# ClauseFinding

The diagnostic verdict for a single clause family.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family_id** | **str** |  | 
**found_span** | **Dict[str, object]** |  | [optional] 
**verdict** | **str** |  | 
**matched_tier** | **str** |  | [optional] 
**delta** | **str** |  | [optional] 
**confidence** | **float** |  | 
**requires_context** | **bool** |  | [optional] [default to False]
**deal_context_hit** | **str** |  | [optional] 
**clarifying_question** | **str** |  | [optional] 

## Example

```python
from moolabs.models.clause_finding import ClauseFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ClauseFinding from a JSON string
clause_finding_instance = ClauseFinding.from_json(json)
# print the JSON string representation of the object
print(ClauseFinding.to_json())

# convert the object into a dict
clause_finding_dict = clause_finding_instance.to_dict()
# create an instance of ClauseFinding from a dict
clause_finding_from_dict = ClauseFinding.from_dict(clause_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


