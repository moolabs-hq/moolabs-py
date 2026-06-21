# ClausePosition

A negotiating position within a clause family.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | **str** |  | 
**standard_language** | **str** |  | [optional] 
**rationale** | **str** |  | [optional] 

## Example

```python
from moolabs.models.clause_position import ClausePosition

# TODO update the JSON string below
json = "{}"
# create an instance of ClausePosition from a JSON string
clause_position_instance = ClausePosition.from_json(json)
# print the JSON string representation of the object
print(ClausePosition.to_json())

# convert the object into a dict
clause_position_dict = clause_position_instance.to_dict()
# create an instance of ClausePosition from a dict
clause_position_from_dict = ClausePosition.from_dict(clause_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


