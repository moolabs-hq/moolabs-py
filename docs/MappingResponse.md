# MappingResponse

Response for a feature key mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**meter_slug** | **str** |  | 
**feature_key** | **str** |  | 
**effective_from** | **str** |  | 
**effective_to** | **str** |  | [optional] 

## Example

```python
from moolabs.models.mapping_response import MappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MappingResponse from a JSON string
mapping_response_instance = MappingResponse.from_json(json)
# print the JSON string representation of the object
print(MappingResponse.to_json())

# convert the object into a dict
mapping_response_dict = mapping_response_instance.to_dict()
# create an instance of MappingResponse from a dict
mapping_response_from_dict = MappingResponse.from_dict(mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


