# ValidateTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation** | **Dict[str, object]** |  | 
**render_context_summary** | **Dict[str, object]** |  | [optional] 

## Example

```python
from moolabs.models.validate_template_response import ValidateTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTemplateResponse from a JSON string
validate_template_response_instance = ValidateTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateTemplateResponse.to_json())

# convert the object into a dict
validate_template_response_dict = validate_template_response_instance.to_dict()
# create an instance of ValidateTemplateResponse from a dict
validate_template_response_from_dict = ValidateTemplateResponse.from_dict(validate_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


