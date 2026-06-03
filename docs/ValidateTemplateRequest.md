# ValidateTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] [default to 'email']
**subject_template** | **str** |  | 
**body_template** | **str** |  | 
**preview_mode** | **str** |  | [optional] 
**case_id** | **str** |  | [optional] 

## Example

```python
from moolabs.models.validate_template_request import ValidateTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTemplateRequest from a JSON string
validate_template_request_instance = ValidateTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateTemplateRequest.to_json())

# convert the object into a dict
validate_template_request_dict = validate_template_request_instance.to_dict()
# create an instance of ValidateTemplateRequest from a dict
validate_template_request_from_dict = ValidateTemplateRequest.from_dict(validate_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


