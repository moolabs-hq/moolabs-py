# ResourceMapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** |  | 
**cloud_provider** | **str** |  | 
**resource_id** | **str** |  | 
**resource_type** | **str** |  | 
**service_name** | **str** |  | 
**team_name** | **str** |  | 
**environment** | **str** |  | 
**tags** | **Dict[str, object]** |  | 
**is_active** | **bool** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from moolabs.models.resource_map_response import ResourceMapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMapResponse from a JSON string
resource_map_response_instance = ResourceMapResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceMapResponse.to_json())

# convert the object into a dict
resource_map_response_dict = resource_map_response_instance.to_dict()
# create an instance of ResourceMapResponse from a dict
resource_map_response_from_dict = ResourceMapResponse.from_dict(resource_map_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


