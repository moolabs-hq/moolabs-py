# TemplateVersionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TemplateVersionResponse]**](TemplateVersionResponse.md) |  | 

## Example

```python
from moolabs.models.template_version_list_response import TemplateVersionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateVersionListResponse from a JSON string
template_version_list_response_instance = TemplateVersionListResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateVersionListResponse.to_json())

# convert the object into a dict
template_version_list_response_dict = template_version_list_response_instance.to_dict()
# create an instance of TemplateVersionListResponse from a dict
template_version_list_response_from_dict = TemplateVersionListResponse.from_dict(template_version_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


