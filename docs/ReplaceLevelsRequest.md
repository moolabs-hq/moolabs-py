# ReplaceLevelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**levels** | [**List[LevelIn]**](LevelIn.md) |  | 

## Example

```python
from moolabs.models.replace_levels_request import ReplaceLevelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceLevelsRequest from a JSON string
replace_levels_request_instance = ReplaceLevelsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceLevelsRequest.to_json())

# convert the object into a dict
replace_levels_request_dict = replace_levels_request_instance.to_dict()
# create an instance of ReplaceLevelsRequest from a dict
replace_levels_request_from_dict = ReplaceLevelsRequest.from_dict(replace_levels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


