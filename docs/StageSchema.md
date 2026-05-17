# StageSchema

One stage in a dunning strategy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | **int** | Stage sequence number | 
**name** | **str** |  | 
**days_overdue_trigger** | **int** |  | 
**channel** | **str** |  | 
**tone** | **str** |  | [optional] [default to 'professional']
**autonomy_min** | **int** |  | [optional] [default to 1]
**template_key** | **str** |  | 

## Example

```python
from moolabs.models.stage_schema import StageSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StageSchema from a JSON string
stage_schema_instance = StageSchema.from_json(json)
# print the JSON string representation of the object
print(StageSchema.to_json())

# convert the object into a dict
stage_schema_dict = stage_schema_instance.to_dict()
# create an instance of StageSchema from a dict
stage_schema_from_dict = StageSchema.from_dict(stage_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


