# TemplateMetaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**render_syntax** | **str** |  | 
**template_ids** | **List[str]** |  | 
**context_contract** | **Dict[str, object]** |  | 
**template_names** | **Dict[str, object]** |  | 

## Example

```python
from moolabs.models.template_meta_response import TemplateMetaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateMetaResponse from a JSON string
template_meta_response_instance = TemplateMetaResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateMetaResponse.to_json())

# convert the object into a dict
template_meta_response_dict = template_meta_response_instance.to_dict()
# create an instance of TemplateMetaResponse from a dict
template_meta_response_from_dict = TemplateMetaResponse.from_dict(template_meta_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


