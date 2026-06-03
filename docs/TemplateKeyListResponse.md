# TemplateKeyListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** |  | [optional] [default to 'email']
**seeded_keys** | [**List[TemplateKeyResponse]**](TemplateKeyResponse.md) |  | 
**custom_keys** | [**List[TemplateKeyResponse]**](TemplateKeyResponse.md) |  | 

## Example

```python
from moolabs.models.template_key_list_response import TemplateKeyListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateKeyListResponse from a JSON string
template_key_list_response_instance = TemplateKeyListResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateKeyListResponse.to_json())

# convert the object into a dict
template_key_list_response_dict = template_key_list_response_instance.to_dict()
# create an instance of TemplateKeyListResponse from a dict
template_key_list_response_from_dict = TemplateKeyListResponse.from_dict(template_key_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


