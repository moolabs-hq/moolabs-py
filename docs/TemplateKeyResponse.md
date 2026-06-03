# TemplateKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**canonical_template_key** | **str** |  | 
**display_name** | **str** |  | 
**channel** | **str** |  | [optional] [default to 'email']
**key_source** | **str** |  | 
**variable_policy** | **Dict[str, object]** |  | 
**allowed_variables** | **List[str]** |  | 
**required_variables** | **List[str]** |  | 
**legacy_aliases** | **List[str]** |  | [optional] 
**system_seeded** | **bool** |  | 
**selectable** | **bool** |  | 
**archived** | **bool** |  | [optional] [default to False]

## Example

```python
from moolabs.models.template_key_response import TemplateKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateKeyResponse from a JSON string
template_key_response_instance = TemplateKeyResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateKeyResponse.to_json())

# convert the object into a dict
template_key_response_dict = template_key_response_instance.to_dict()
# create an instance of TemplateKeyResponse from a dict
template_key_response_from_dict = TemplateKeyResponse.from_dict(template_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


