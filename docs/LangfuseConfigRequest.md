# LangfuseConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | 
**secret_key** | **str** |  | 
**host** | **str** |  | [optional] [default to 'https://cloud.langfuse.com']

## Example

```python
from moolabs.models.langfuse_config_request import LangfuseConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LangfuseConfigRequest from a JSON string
langfuse_config_request_instance = LangfuseConfigRequest.from_json(json)
# print the JSON string representation of the object
print(LangfuseConfigRequest.to_json())

# convert the object into a dict
langfuse_config_request_dict = langfuse_config_request_instance.to_dict()
# create an instance of LangfuseConfigRequest from a dict
langfuse_config_request_from_dict = LangfuseConfigRequest.from_dict(langfuse_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


