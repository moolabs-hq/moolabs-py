# IDResource

IDResource is a resouce with an ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the resource. | [readonly] 

## Example

```python
from moolabs.models.id_resource import IDResource

# TODO update the JSON string below
json = "{}"
# create an instance of IDResource from a JSON string
id_resource_instance = IDResource.from_json(json)
# print the JSON string representation of the object
print(IDResource.to_json())

# convert the object into a dict
id_resource_dict = id_resource_instance.to_dict()
# create an instance of IDResource from a dict
id_resource_from_dict = IDResource.from_dict(id_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


