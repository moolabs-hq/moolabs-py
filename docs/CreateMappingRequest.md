# CreateMappingRequest

Request to create a feature key mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meter_slug** | **str** | Meter slug from OpenMeter | 
**feature_key** | **str** | Feature key to map to | 
**effective_at** | **str** | When this mapping takes effect (ISO 8601, defaults to now) | [optional] 

## Example

```python
from moolabs.models.create_mapping_request import CreateMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMappingRequest from a JSON string
create_mapping_request_instance = CreateMappingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMappingRequest.to_json())

# convert the object into a dict
create_mapping_request_dict = create_mapping_request_instance.to_dict()
# create an instance of CreateMappingRequest from a dict
create_mapping_request_from_dict = CreateMappingRequest.from_dict(create_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


