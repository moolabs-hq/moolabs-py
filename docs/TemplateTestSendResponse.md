# TemplateTestSendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**recipient** | **str** |  | 
**template_id** | **str** |  | 
**used_fallback** | **bool** |  | 

## Example

```python
from moolabs.models.template_test_send_response import TemplateTestSendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateTestSendResponse from a JSON string
template_test_send_response_instance = TemplateTestSendResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateTestSendResponse.to_json())

# convert the object into a dict
template_test_send_response_dict = template_test_send_response_instance.to_dict()
# create an instance of TemplateTestSendResponse from a dict
template_test_send_response_from_dict = TemplateTestSendResponse.from_dict(template_test_send_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


