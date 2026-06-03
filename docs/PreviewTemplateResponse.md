# PreviewTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** |  | 
**body** | **str** |  | 
**context_summary** | **Dict[str, object]** |  | 
**version_id** | **str** |  | 
**canonical_template_key** | **str** |  | 

## Example

```python
from moolabs.models.preview_template_response import PreviewTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTemplateResponse from a JSON string
preview_template_response_instance = PreviewTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(PreviewTemplateResponse.to_json())

# convert the object into a dict
preview_template_response_dict = preview_template_response_instance.to_dict()
# create an instance of PreviewTemplateResponse from a dict
preview_template_response_from_dict = PreviewTemplateResponse.from_dict(preview_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


