# ResourceMapCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** |  | 
**resource_id** | **str** |  | 
**resource_type** | **str** |  | [optional] 
**service_name** | **str** |  | 
**team_name** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**tags** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.resource_map_create_request import ResourceMapCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMapCreateRequest from a JSON string
resource_map_create_request_instance = ResourceMapCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceMapCreateRequest.to_json())

# convert the object into a dict
resource_map_create_request_dict = resource_map_create_request_instance.to_dict()
# create an instance of ResourceMapCreateRequest from a dict
resource_map_create_request_from_dict = ResourceMapCreateRequest.from_dict(resource_map_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


