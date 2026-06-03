# PreviewTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | 
**preview_mode** | **str** |  | [optional] 
**case_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.preview_template_request import PreviewTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTemplateRequest from a JSON string
preview_template_request_instance = PreviewTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewTemplateRequest.to_json())

# convert the object into a dict
preview_template_request_dict = preview_template_request_instance.to_dict()
# create an instance of PreviewTemplateRequest from a dict
preview_template_request_from_dict = PreviewTemplateRequest.from_dict(preview_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


