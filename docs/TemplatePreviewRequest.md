# TemplatePreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_context** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.template_preview_request import TemplatePreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePreviewRequest from a JSON string
template_preview_request_instance = TemplatePreviewRequest.from_json(json)
# print the JSON string representation of the object
print(TemplatePreviewRequest.to_json())

# convert the object into a dict
template_preview_request_dict = template_preview_request_instance.to_dict()
# create an instance of TemplatePreviewRequest from a dict
template_preview_request_from_dict = TemplatePreviewRequest.from_dict(template_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


