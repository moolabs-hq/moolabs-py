# TemplateKeyCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_template_key** | **str** |  | 
**display_name** | **str** |  | 
**change_reason** | **str** |  | 

## Example

```python
from moolabs.models.template_key_create_request import TemplateKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateKeyCreateRequest from a JSON string
template_key_create_request_instance = TemplateKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TemplateKeyCreateRequest.to_json())

# convert the object into a dict
template_key_create_request_dict = template_key_create_request_instance.to_dict()
# create an instance of TemplateKeyCreateRequest from a dict
template_key_create_request_from_dict = TemplateKeyCreateRequest.from_dict(template_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


